import discord
import stockx
import datetime



#client und dessen intents werden definiert
intents = discord.Intents().all()
client = discord.Client(intents=intents)
#bot-command channel 
channel_id = 1052329706965446666
db = '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
queryend = ''
aPrice = ''
mesCha = ''
a = 0
g = False
morInf = False


async def mainn(dif, queryend, aPrice, g, morInf):
    #Variables
    #Gets stockx api of sneaker name in a dictionary
    rouNum = 0
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
        color=0xff0000
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
    fooTime = str(datetime.datetime.now().strftime("%H:%M %d.%m.%Y"))
    embed.set_footer(text="MADE BY 1138 | " + fooTime)
    embed.set_author(name = 'Top Product' if a == 0 else str(a+1) + '. Product/' + str(stockx.numKey))
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
    comLog()


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
    mesCha = message.channel
    #Checking
    #Checks if the message author was the bot himself
    if message.author == client.user and message.content.split(' ')[0] != 'Next' and message.content.split(' ')[0] != 'Previous':
        return
    #Checks if message command was send in the bot command channel
    if message.channel.id != channel_id:
        print('wr ch')
        return
    #Prints Author of message and message in the console
    a = 0

    #Splitting

    #Saves Sneaker name and , if given, individual price in variables
    if message.content.split(' ')[0] == '!stx':
        query = message.content.replace('!stx ', '')
        if message.content[-1] == 'g':
            query = query.replace('g', '')
            g = True
        if '-' in query:
            aPrice = query.split('-')[1]
            queryend = query.replace('-' + aPrice, '')
        else:
            aPrice = '-'
            queryend = query
            
            
    elif message.content.split(' ')[0] == 'Next':
        query = message.content.replace('Next Product: ', '')
        if message.content[-1] == 'g':
            query = query.replace('g', '')
            g = True
        if '-' in query:
            aPrice = query.split('-')[1]
            queryend = query.replace('-' + aPrice, '')
        else:
            aPrice = '-'
            queryend = query
    elif message.content.split(' ')[0] == 'Previous':
        query = message.content.replace('Previous Product: ', '')
        if '-' in query:
            aPrice = query.split('-')[1]
            queryend = query.replace('-' + aPrice, '')
        else:
            aPrice = '-'
            queryend = query
    else:
        queryend = ''
        aPrice = '-'
        return
    if queryend == '!stx':
        return

    await mainn('onMes', queryend, aPrice, g, morInf)
    


@client.event
async def on_reaction_add(reaction, user):
    global a
    global morInf
    mai = False
    if user == client.user:
        return
    if reaction.emoji == '➡️' and a < stockx.numKey - 1:
        a += 1
        mai = True
    if reaction.emoji == '⬅️' and a > 0:
        a -= 1
        mai = True
    if reaction.emoji == '1️⃣' and a > 3:
        a = 0
        mai = True
    if reaction.emoji == 'ℹ️':
        morInf = False if morInf else True
        mai = True

    if mai:
        channel = reaction.message.channel
        await reaction.message.delete()
        await mainn('onRea', queryend, aPrice, g, morInf)


        







#Startet bot mit Token
client.run('MTA1MTUxODE1NDMxODI5MTAwNg.Gz5Wjs.uui7DfTc4YC__4iDXBN4eKah9zOE8h_RteCSOw')
