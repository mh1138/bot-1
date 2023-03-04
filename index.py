import discord
import stockx
import datetime
import restocks
import csv
import alias



db = '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
#client und dessen intents werden definiert
intents = discord.Intents().all()
client = discord.Client(intents=intents)
#bot-command channel 

channel_id = 1052329706965446666


queryend = ''
aPrice = ''


mesCha = ''
a = 0


g = False
morInf = False


footer_text = ''
item_id = ''
prof_size_restocks_price = {}
keys = []
footer_text = ''
size_price_chart_sorted = {}
mesAut = ''
user_lan = ''
mesCon = ''
size_char_usM_EU = {'35.5': '3.5', '36.0': '4', '36.5': '4.5', '37.5': '5', '38.0': '5.5', '38.5': '6', '39.0': '6.5', '40.0': '7', '40.5': '7.5', '41.0': '8','42.0': '8.5', '42.5': '9', '43.0': '9.5', '44.0': '10', '44.5': '10.5', '45.0': '11','45.5': '11.5', '46.0': '12', '47.0': '12.5', '47.5': '13', '48.5': '14', '49.5': '15'}
size_char_usW_EU = {'35.5': '5', '36.0': '5.5', '36.5': '6', '37.5': '6.5', '38.0': '7', '39.5': '7.5', '39.0': '8', '40.0': '8.5', '40.5': '9', '41.0': '9.5', '42.0': '10', '42.5': '10.5', '43.0': '11', '44.0': '11.5', '44.5': '12'}

async def update_string(string, setting):
    filename = "data.csv"
    temp_data = []
    id_exists = False
    if setting == 'v':
        if user_lan == 'en':
            await mesCha.send('**VAT Updated!**')
        elif user_lan == 'de':
            await mesCha.send('**Vorsteuer-abzug Aktualisiert!**')
    elif setting == 'l':
        if string == 'en':
            await mesCha.send('**Language Updated!**')
        elif string == 'de':
            await mesCha.send('**Sprache aktualisiert!**')
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            temp_data.append(row)
            if row['user_id'] == str(mesAut):
                id_exists = True
                if setting == 'v':
                    row['vor_ab'] = string
                elif setting == 'l':
                    row['language'] = string
    if not id_exists:
        if setting == 'v':
            temp_data.append({'user_id': str(mesAut), 'vor_ab': string})
        if setting == 'l':
            temp_data.append({'user_id': str(mesAut),  'language': string})
    
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['user_id', 'vor_ab', 'language']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(temp_data)
        


async def mainn(dif, queryend, aPrice, g, morInf):
    global item_id
    global footer_text
    global prof_size_restocks_price
    global keys
    global footer_text
    global size_price_chart_sorted
    
    #Variables
    #Gets stockx api of sneaker name in a dictionary
    print('----------------------------------------------------------------------------------------------------------')
    rouNum = 0
    keys = []
    prof_size_restocks_price = {}
    size_price_chart_sorted = {}
    footer_text ='**Restock Buy Prices:**                          Last Alias Sales:\n'

    item = stockx.search(queryend, a) 
    #Calculates Price after taxes
    realPrice = round(((float(item['market']['lastSale'])*0.9)*0.97)-5, 1)
    #Calculates profit of last Sale
    profit = round(realPrice - item['retailPrice'] if g == False else realPrice - item['retailPrice']/1.19, 1)
 
    
    #Functions

    #Function for Checking if sneaker is profitalbe with retail price
    def check_profit(rP, rT):
        if rP > item['retailPrice'] if g == False else item['retailPrice']/1.19:
            return 'Yes' + ': ' + str(profit) + '€' 
        else:
            return 'No'
    #Function for checking if sneaker is profitable with individual price
    def cop(price):
        price = float(price)/1.19 if g == True else price
        if float(price) < realPrice:
            if float(price)/realPrice < 0.8:
                if round(realPrice - float(price), 1) > 100:
                    return 'CCOOPP!!!'
                return 'COP' + ' | Profit: ' + str(round(realPrice - float(price), 1)) + '€'
            else:
                return '<20% Profit: ' + str(round(realPrice - float(price), 1)) + '€ / ' + str(round(1-(float(price)/realPrice), 2) * 100) + '%'
        else:
            return 'Drop'
    #Function for Console Log
    def comLog():
        #Prints Author of message and message in the console
        print(message.author.name + ": " + message.content)
        print('     EMBED: ')
        print('     Title: ' + item['title'])
        print('     URL: ' + 'https://stockx.com/de-de/' + item['urlKey'])
        print('     Color: ' + str(0xff0000))
        print('     URL Thumbnail: ' + item['media']['imageUrl'])
        for key in item_dict:
            print('     ' + key + ': ' + str(item_dict[key]))
        print('     SizeChart: ' + usedURL)
        print('     GivenPrive: ' + aPrice)
        print('     Time: ' +  str(datetime.datetime.now()))
    
    
    #Embed

    #Embed Header

    item_dict = {
            'Colorway' : 'N/A' if item['colorway'] == '' else item['colorway'],
            'Style ID' : 'N/A' if item['styleId'] == '' else item['styleId'],
            'RetailProfit' : str(check_profit(realPrice, item['retailPrice'])),
            'Last Sale' : str(item['market']['lastSale']) + '/' + str(realPrice) + '€' if item['market']['lastSaleSize'] == '' else 'Sz: ' + item['market']['lastSaleSize'] + ' | ' + str(item['market']['lastSale']) + '/' + str(realPrice) + '€',
            'LowestAsk' : str(item['market']['lowestAsk']) + '€' if item['market']['lastSaleSize'] == '' else 'Sz: ' + item['market']['lowestAskSize'] + ' | ' + str(item['market']['lowestAsk']) + '€',
            'HighestBid' : str(item['market']['highestBid']) + '€' if item['market']['lastSaleSize'] == '' else 'Sz: ' + str(item['market']['highestBidSize']) + ' | ' + str(item['market']['highestBid']) + '€',
            'Sales72H' : str(item['market']['salesLast72Hours']),
            'Retail' : 'N/A' if item['retailPrice'] == 0 else str(item['retailPrice']) + '€' if g == False else str(item['retailPrice']) + '€ / ' + str(round(item['retailPrice']/1.19, 1)) + '€',
            'Gender': item['gender'],
            'iD' : item['id'],
            'uuiD' : item['uuid'],
            'category' : item['category'],
            'Condition' : item['condition'],
            'Manu Country' : item['countryOfManufacture'],
            'Datatype' : item['dataType'],
            'Product Category' : item['productCategory'],
            'Release Date' : item['releaseDate'],
            'Ticker Symbol' : item['tickerSymbol'],
            'Year' : item['year'],
            'URL key' : item['urlKey'],
            'Object iD' : item['objectID']
        }
    embed = discord.Embed(
        title = item['title'],
        url = 'https://stockx.com/de-de/' + item['urlKey'],
        color=0xff0000,
    )
    embed.set_thumbnail(
        url=item['media']['imageUrl']
    )  
    if morInf == True:
        description = item['description'].replace('<br>', '').replace('<a href="', '').replace('</a>', '')
        embed.description = description
    #Embed fields
    for key in item_dict:
        rouNum += 1
        if morInf == False and rouNum > 9:
            break
        embed.add_field (
            name = key,
            value = item_dict[key],
            inline = True if morInf == False else False if rouNum > 9 else True          
        )
    if aPrice != '-':
        embed.add_field(
            name = 'COP?',
            value = cop(aPrice)
        )

    #text= for i in size_price_chart
    #+ "\n MADE BY 1138 | " + fooTime)
    item_id = item['styleId']

    if item_id == 'N/A':
        item_id = item['title']

    if "/" in item_id:
        item_id = item_id.split("/")[1]

    url = 'https://restocks.net/de/shop/search?q={}&page=1'.format(item_id)
    size_price_chart = restocks.search(url)
    print(url)

    alias_list = alias.search(item_id)
    alias_size_price_last = alias_list[0]
    print(alias_size_price_last)

    for i in size_price_chart:
        if str(size_price_chart[i]) != 'N/A':
            size_price_chart_sorted[i] = int(str(size_price_chart[i])[:-2].replace('.', ''))
        else:
            size_price_chart_sorted[i] = 0
    size_price_chart_sorted = {k: v for k, v in sorted(size_price_chart_sorted.items(), key=lambda item: item[1])}
    size_price_chart_sorted = dict(reversed(list(size_price_chart_sorted.items())))
    list(size_price_chart_sorted.keys())
    print(size_price_chart)
    aa = 0
    alias_size_price_last_edited = {}
    alias_size_price_last_edited_sorted = {}

    for i in size_price_chart:
        if i == '48.0':
            continue
        if item['gender'] == 'men':
            if float(i) < 36:
                continue
            size = size_char_usM_EU[i]
            
        if item['gender'] == 'women':
            if float(i) > 46:
                continue
            
        if size in alias_size_price_last.keys():
            alias_size_price_last_edited[size] = str(alias_size_price_last[size])
            alias_size_price_last_edited_sorted[size] = alias_size_price_last[size]
        else:
            alias_size_price_last_edited[size] = '0'
            alias_size_price_last_edited_sorted[size] = 0

    print(alias_size_price_last_edited)
    alias_size_price_last_edited_sorted = {k: v for k, v in sorted(alias_size_price_last_edited_sorted.items(), key=lambda item: item[1])}
    alias_size_price_last_edited_sorted = dict(reversed(list(alias_size_price_last_edited_sorted.items())))
    print(alias_size_price_last_edited_sorted)
    aa = 0
    for i in size_price_chart:
        if i == '48.0':
            continue
        if item['gender'] == 'men':
            if float(i) < 36:
                continue
            size = size_char_usM_EU[i]
            
        if item['gender'] == 'women':
            if float(i) > 46:
                continue
        size = size_char_usM_EU[i]
        sort = str(size_price_chart_sorted[str(list(size_price_chart_sorted.keys())[aa])])
        alias_sort = str(alias_size_price_last_edited_sorted[str(list(alias_size_price_last_edited_sorted.keys())[aa])])
        dist = str(i) + ':     ' + str(size_price_chart[i])
        footer_text = footer_text + dist + '      ' + str(list(size_price_chart_sorted.keys())[aa]) + ': ' + sort + ' / ' + str(round(float(sort)*0.8, 2)) + '€       ' + str(size) + ':  ' + alias_size_price_last_edited[size] +'€             ' + str(list(alias_size_price_last_edited_sorted.keys())[aa]) + ':  ' + alias_sort + '€\n'
        
        aa += 1

    footer_text = footer_text + "MADE BY 1138 | " + str(datetime.datetime.now().strftime("%H:%M")) + '  ' + str(datetime.datetime.now().strftime("%d-%m-%Y"))



    #for i in size_price_chart_sorted:
    #    footer_text = footer_text + str(i) + ': ' + str(size_price_chart_sorted[i]) + '\n'

    





    fooTime = str(datetime.datetime.now().strftime("%H:%M %d.%m.%Y"))
    embed.set_footer(text = footer_text)
    if a == 0:
        author = 'Top Product ' + '\nRequest "'+ queryend + '" by: ' + str(mesAutName) 
    else:
        author = str(a+1) + '. Product/' + str(stockx.numKey) + '\nRequest "'+ queryend + '" by: ' + str(mesAutName) 

    embed.set_author(name = author) 
    #Embed pictures
    if item['gender'] == 'men':
        embed.set_image(url = "https://mephistostore.de/media/image/40/4b/f1/herren.jpg")
        usedURL = "https://mephistostore.de/media/image/40/4b/f1/herren.jpg"
    elif item['gender'] == 'women':
        embed.set_image(url = "https://mephistostore.de/media/image/a4/05/06/damen.jpg")
        usedURL = "https://mephistostore.de/media/image/a4/05/06/damen.jpg"
    elif item['gender'] == 'child' or  item['gender'] == 'preschool' or item['gender'] == 'toddler':
        #gs --> 6yo+
        #ps -->3-5yo
        #td --> 1-3yo
        embed.set_image(url = "https://i.ibb.co/9pTkd3d/image-98-1024x597.png") 
        usedURL = "https://i.ibb.co/9pTkd3d/image-98-1024x597.png"
        #print(db)
    else:
        usedURL = ''
    #Send Embed
    message = await mesCha.send(embed=embed)
    if a > 3:
        await message.add_reaction('1️⃣')
    if a > 0:
        await message.add_reaction('⬅️')
    if a < stockx.numKey - 1:
        await message.add_reaction('➡️')
    await message.add_reaction('ℹ️')
    #comLog()



async def settings(query):

    print('Settings!')
    query = query.lower()

    if query.startswith('help'):
        print('help')
        if user_lan == 'de':
            embed=discord.Embed(title="Einstellungs Hilfe", description="Wähle individuelle nutzer Einstellungen")
            embed.add_field(name="!settings l DE/EN", value="Wähle deine Sprache", inline=False)
            embed.add_field(name="!settings v Ja/Nein/J/N", value="Kannst du Vorsteuer abziehen?", inline=False)
            embed.add_field(name="!1138", value="Liste aller Kommands", inline=False)
            embed.set_footer(text="Made by 1138")
            await mesCha.send(embed=embed)
            print('de')
        else:
            embed=discord.Embed(title="Settings Help", description="Choose individual user settings")
            embed.add_field(name="!settings l DE/EN", value="Choose your Language", inline=False)
            embed.add_field(name="!settings v yes/nos", value="Do you VAT flip?", inline=False)
            embed.add_field(name="!1138", value="List of every Command", inline=False)
            embed.set_footer(text="Made by 1138")
            await mesCha.send(embed=embed)
            print('en')
    elif query.startswith('v'):
        
        option = query.replace('v ', '')
        if option == '':
            await mesCha.send('**Input is needed!**')
            return

        if user_lan == 'en':
            if option != 'yes' and option != 'no' and option != 'y' and option != 'n':
                if user_lan == 'en':
                    await mesCha.send('**Invalid Input! Expected: Yes/No/Y/N**')
                    return
        elif user_lan == 'de':
            if option != 'yes' and option != 'no' and option != 'y' and option != 'n':
                await mesCha.send('**Kein gültiges Argument! Möglichkeiten: Yes/No/Y/N**')
                return
        
        if option == 'n':
            option = 'no'
        elif option == 'y':
            option = 'yes'
       

        await update_string(option, 'v')

    elif query.startswith('l'):
        option = query.replace('l ', '')
        if option == '':
            await mesCha.send('**Input is needed!**')
            return

        if option != 'de' and option != 'en':
            await mesCha.send('**Invalid Input! Expected: DE/EN**')
            return

        await update_string(option, 'l')

        
async def command_list():
    global command
    command = True
    embed=discord.Embed(title="Command List", description="Possible Commands")
    embed.add_field(name="!price '...'", value="Shows you details about a certain shoe", inline=False)
    embed.add_field(name="!settings help", value="Shows you possible settings", inline=False)
    embed.set_footer(text="Made by 1138")
    message = await mesCha.send(embed=embed)
    await message.add_reaction('🇸')





@client.event
async def on_ready():
    #Nachricht in der Konsole, sobald der bot bereit ist.
    print("Der Bot ist online")

@client.event
async def on_message(message):
    global queryend
    global aPrice
    global a
    global mesCha
    global g
    global mesAut
    global user_lan
    global user_vat
    global mesCon
    global mesAutName
    global command
    a = 0
    g = False
    #Checking
    #Checks if the message author was the bot himself
    if message.author == client.user and message.content.split(' ')[0] != 'Next' and message.content.split(' ')[0] != 'Previous':
        return
    #Checks if message command was send in the bot command channel
    if message.channel.id != channel_id:
        print('wr ch')
        return
    command = False
    mesCon = message.content
    mesCha = message.channel
    mesAut = message.author.id
    mesAutName = message.author.name
    await message.delete()


    
    with open('data.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['user_id'] == str(mesAut):
                    user_vat = row['vor_ab']
                    user_lan = row['language']

    if message.content.split(' ')[0] == '!price':
        query = message.content.replace('!price ', '')
        if message.content[-1] == 'g' or user_vat == 'yes':
            query = query.replace('g', '')
            g = True
        if '-' in query:
            aPrice = query.split('-')[1]
            queryend = query.replace('-' + aPrice, '')
        else:
            aPrice = '-'
            queryend = query
        await mainn('onMes', queryend, aPrice, g, morInf)        
                       
    elif message.content.split(' ')[0] == '!settings':
        query = message.content.replace('!settings ', '')
        if query == '!settings':
            await mesCha.send("No such Command, **!settings help** for Command list!")
        await settings(query)

    elif message.content.startswith('!se'):
        await mesCha.send("Invalid Command,  **'" + mesCon + "'**  did you mean **!settings ...'** ")

    elif message.content.startswith('!1138'):
        await command_list()

    else:
        if user_lan == 'en':
            await mesCha.send("**Invalid command '!1138' for Command list**")
        elif user_lan == 'de':
            await mesCha.send("**Ungültiger Kommand '!1138' für Kommandliste**")

    


@client.event
async def on_reaction_add(reaction, user):
    global a
    global morInf
    mai = False
    if command == False:
        if user == client.user:
            return
        if reaction.emoji == '➡️' and a < stockx.numKey - 1:
            a += 1
            mai = True
        elif reaction.emoji == '⬅️' and a > 0:
            a -= 1
            mai = True
        elif reaction.emoji == '1️⃣' and a > 3:
            a = 0
            mai = True
        elif reaction.emoji == 'ℹ️':
            morInf = False if morInf else True
            mai = True

        if mai:
            channel = reaction.message.channel
            await reaction.message.delete()
            await mainn('onRea', queryend, aPrice, g, morInf)
    else:
        if user == client.user:
            return
        if reaction.emoji == '🇸':
            await reaction.message.delete()
            await settings('help')

















































        







#Startet bot mit Token
client.run('')
