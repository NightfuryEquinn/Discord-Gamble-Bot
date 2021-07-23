import discord
from discord.ext import commands
import random
from random import choices
import asyncio
import os

bot = commands.Bot(command_prefix = 'gb ')

@bot.event
async def on_ready():
    print('Connected to 4th dimension.')

# Display random bot status
async def change_status():
    await bot.wait_until_ready()

    status_list = [
'From Vegas to Macau Series', 'God of Gamblers', 'you lose', 
'you win', 'you clothesless', 'you sweating', 'you getting cheated on', 'you be the God',
'you have JA', 'how to play Mahjong', 'how to play Landlord', 'how to throw cards', 'you cry in toilet'
]

    while not bot.is_closed():
        status = random.choice(status_list)
        activity = discord.Activity(name = status, type = discord.ActivityType.watching)
        await bot.change_presence(activity = activity)
        await asyncio.sleep(3600)

bot.loop.create_task(change_status())

# Rulebook
@bot.command()
async def rules(message):
    name = message.author.name
    avatar = message.author.avatar_url

    left = '◀️'
    right = '▶️'
    colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]

# Blackjack Page
    bj_rules = discord.Embed(
title = 'No-Currency Gamble Bot Handbook 📗', 
description = '''
{} is reading ~ 🤫.

Chapter 1 - 🎭 Blackjack / 21点

Classic! 
Get 21 to win and don't explode yourself 💣
Card given one at a time 😇. No hurries.
```
gb bj @p1 @... -- No limit of players
🎴 Hit 🛑 Hold
```    
'''.format(name), 
color = random.choice(colors))
    bj_rules.set_thumbnail(url = avatar)

# Texas Poker Page
    tp_rules = discord.Embed(
title = 'No-Currency Gamble Bot Handbook 📘',
description = '''
{} nearly finished reading, but not yet 😴

Chapter 2 - 💎 Texas Poker / 德州扑克

Stack chips! 
Only all players holded will proceed second round.
Each player have 10 fames as chips 😌. 
ACES is the boss, 2 is the servant here.
```
gb tp @p1 @... -- No limit of players
➕ Raise 🛑 Hold ❌ Fold 💵 ALL IN!
```
```
SCORETABLE 💱 Largest to Smallest
Dragon 🐉 [♦️ 6 ♣️ 6 ♥️ 6 ♠️ 6 | ♦️ 4 ♣️ 4 ♥️ 4 etc.] Any combinations that occupied all seven cards
Royal Flush 👑 [♠️ 10 ♠️ J ♠️ Q ♠️ K ♠️ A]
Straight Flush ⏩ [♦️ 5 ♦️ 6 ♦️ 7 ♦️ 8 ♦️ 9]
Straight ➡️ [♣️ 6 ♦️ 7 ♠️ 8 ♦️ 9 ♥️ 10]
Flush 🔁 [♦️ 5 ♦️ 3 ♦️ 8 ♦️ J ♦️ Q]
Fours 4️⃣ [♦️ 6 ♣️ 6 ♥️ 6 ♠️ 6]
Three of a Kind 3️⃣ [♦️ 4 ♣️ 4 ♥️ 4]
Double Pair 2️⃣ [♦️ A ♣️ A | ♦️ 2 ♥️ 2]
Single Pair 1️⃣ [♦️ A ♣️ A]
```
'''.format(name), 
color = random.choice(colors))
    tp_rules.set_thumbnail(url = avatar)

# LandLord Page
    ll_rules = discord.Embed(
title = 'No-Currency Gamble Bot Handbook 📙', 
description = '''
{} finished reading. Remember to put back the book to the shelf 🙄.

Chapter 3 - 🃏 ChoDaiDi / 锄大第

Legendary card game!
With a twist of voting the card(s) played 😲. 
Each player has 13 cards. Turns according to tag mention.
Whoever empty the hand, wins 😎! 
2 is the boss, 3 is the servant here.
```
gb ll @p1 @p2 @p3 @p4 -- Must and only four players
✅ Join game ❎ Cancel game 👌 Agree 💩 Decline 
1️⃣ Single 2️⃣ Double 3️⃣ Triple 4️⃣ Four 5️⃣ FIVE
```
```
SCORETABLE 💱 Largest to Smallest
Five Combos
- Straight Flush ⏩ [♦️ 5 ♦️ 6 ♦️ 7 ♦️ 8 ♦️ 9]
- Four + Single 4️⃣1️⃣ [♦️ 6 ♣️ 6 ♥️ 6 ♠️ 6 | ♣️ A]
- Three of a Kind + Pairs 3️⃣2️⃣ [♦️ 4 ♣️ 4 ♥️ 4 | ♦️ A ♣️ A] Compare using Pairs if want to suppress.
- Straight ➡️ [♣️ 6 ♦️ 7 ♠️ 8 ♦️ 9 ♥️ 10]
- Flush 🔁 [♦️ 5 ♦️ 3 ♦️ 8 ♦️ J ♦️ Q]
Three of a Kind
Pairs
Single
```
'''.format(name), 
color = random.choice(colors))
    ll_rules.set_thumbnail(url = avatar)
    ll_rules.set_footer(text = 'Any bugs or issues, dm or pm or whatever message me: Nightfury#8826 🥰')

    page = 1
    m = await message.send(embed = bj_rules)
    await m.add_reaction(left)
    await m.add_reaction(right)

    def valid(reaction, user):
        return user == message.author and str(reaction) in [left, right]

    while True:
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 90.0, check = valid)
            await m.remove_reaction(reaction, user)

            if str(reaction) == left:
                page = page - 1
                if page < 1:
                    page = 3
            elif str(reaction) == right:
                page = page + 1
                if page > 3:
                    page = 1

            if page == 1:
                await m.edit(embed = bj_rules)
            elif page == 2:
                await m.edit(embed = tp_rules)
            elif page == 3:
                await m.edit(embed = ll_rules)
        except asyncio.TimeoutError:
            await message.send('{} put the book back already. Take it out again if you want to read 😊.'.format(name))
            break


# Blackjack for two
@bot.command(aliases = ['bj'])
async def blackjack(message, *name: discord.Member):
    hit = '🎴'
    holdc = '🛑'
    
    deck = [11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10]
    random.shuffle(deck)

# One player at a time, send card, sum up card, sending result
    result = []
    for player in name:
        hands = []
        for i in range(0, 2):
            a = random.choice(deck)
            deck.remove(a)
            hands.append(a)
        await player.send('Here is your card in hand.\n```{}```'.format(hands))
    
        await asyncio.sleep(3)
        await message.send('Look around. Although you cannot see 😶. Be prepared. One at a time.')
        await asyncio.sleep(2)

        hold = False
        while hold == False:
            m = await message.send("{}'s turn.".format(player.mention))
            await m.add_reaction(hit)
            await m.add_reaction(holdc)

            def valid(reaction, user):
                return user == player and str(reaction) in [hit, holdc]

            try:
                reaction, user = await bot.wait_for('reaction_add', timeout = 45.0, check = valid)
                if str(reaction) == hit:
                    card = random.choice(deck)
                    deck.remove(card)
                    hands.append(card)
                    await player.send("Here is your card in hand.\n```{}```".format(hands))
                elif str(reaction) == holdc:
                    hold = True
# Change 11 to 1 if sum of card bigger than 21
                    if 11 in hands:
                        if sum(hands) > 21:
                            for n, i in enumerate(hands):
                                if i == 11:
                                    hands[n] = 1
                                    x = sum(hands)
                        elif sum(hands) <= 21:
                            x = sum(hands)
                    elif 11 not in hands:
                        x = sum(hands)

                    if hands[0] == 11 and hands[1] == 11:
                        result.append('```{} got DOUBLE ACES with total of {} 😳.\n```'.format(player, x))

                    if len(hands) == 5 and sum(hands) > 21:
                        result.append('```{} tried to get five but exploded 🤯.\n```'.format(player))
                        if sum(hands) <= 21:
                            result.append('```{} got FIVE IN A ROW!!! with total of {} 🙀.\n```'.format(player, x))
                    
                    result.append('```{} got a total of {} 🥶.\n```'.format(player, x))
            except asyncio.TimeoutError:
                hold = True
                result.append('```{} is forfeited. USELESSSS.\n```'.format(player))
                await message.send("Why da heck you are not reacting 🤬?!")

    await message.send('Finalizing result... 🤓')
    await asyncio.sleep(5)
    for i in result:
        await message.send(i)


# Texas Poker
@bot.command(aliases = ['tp'])
async def texaspoker(message, *name: discord.Member):
    add = '➕'
    hold = '🛑'
    fold = '❌'
    all_in = '💵'

    famepool = len(name)

    deck = [
'♦️ A', '♦️ 2', '♦️ 3', '♦️ 4', '♦️ 5', '♦️ 6', '♦️ 7', '♦️ 8', '♦️ 9', '♦️ 10', '♦️ J', '♦️ Q', '♦️ K', 
'♣️ A', '♣️ 2', '♣️ 3', '♣️ 4', '♣️ 5', '♣️ 6', '♣️ 7', '♣️ 8', '♣️ 9', '♣️ 10', '♣️ J', '♣️ Q', '♣️ K', 
'♥️ A', '♥️ 2', '♥️ 3', '♥️ 4', '♥️ 5', '♥️ 6', '♥️ 7', '♥️ 8', '♥️ 9', '♥️ 10', '♥️ J', '♥️ Q', '♥️ K', 
'♠️ A', '♠️ 2', '♠️ 3', '♠️ 4', '♠️ 5', '♠️ 6', '♠️ 7', '♠️ 8', '♠️ 9', '♠️ 10', '♠️ J', '♠️ Q', '♠️ K'
]
    random.shuffle(deck)

# Get all the players
    players = []
   
    for player in name:
        players.append(player)

# Send card to players
    handlist = []
    for player in players:
        hand = []
        for i in range(0, 2):
            a = random.choice(deck)
            deck.remove(a)
            hand.append(a)
        handlist.append(player.name)
        for i in hand:
            handlist.append(i)
        await player.send('Here is your card in hand.\n{}'.format(hand))
    
    await asyncio.sleep(5)
    await message.send('Cards have been distributed! 😏 Shuffling...')
    await asyncio.sleep(2)

# Round Loop
    pool = 1

# Set 10 fames for each player, fold set False for this game
    dealer_hand = []
    fame = []
    foldc = []
    for player in players:
        fame.append(10)
        foldc.append(False)

    while pool < 4:
        if pool == 1:
            await message.send("ROUND ONE 1️⃣")
            
            for i in range(1, 7):
                if i % 2 == 1:
                    dealer = random.choice(deck)
                    deck.remove(dealer)
                    dealer_hand.append(dealer)
                elif i % 2 == 0:
                    dealer = random.choice(deck)
                    deck.remove(dealer)
        elif pool == 2 or pool == 3:
            if pool == 2:
                await message.send("ROUND TWO 2️⃣")
            elif pool == 3:
                await message.send("ROUND THREE 3️⃣")

            for i in range(1, 3):
                if i % 2 == 1:
                    dealer = random.choice(deck)
                    deck.remove(dealer)
                    dealer_hand.append(dealer)
                elif i % 2 == 0:
                    dealer = random.choice(deck)
                    deck.remove(dealer)

        await message.send('Cards on Table 😎\n{}'.format(dealer_hand))
        await asyncio.sleep(2)

# Hold set False for each round start
        holdc = []
        for player in players:
            holdc.append(False)

        while all(holdc) == False:
            for player in players:
                x = players.index(player)
# Ignore the player if folded in previous round
                if foldc[x] == False:
                    m = await message.send("{}'s turn. What's your move? 🤠".format(player.mention))
                    await m.add_reaction(add)
                    await m.add_reaction(hold)
                    await m.add_reaction(fold)
                    await m.add_reaction(all_in)

                    def valid(reaction, user):
                        return user == player and str(reaction) in [add, hold, fold, all_in]
                    
                    try:
                        reaction, user = await bot.wait_for('reaction_add', timeout = 30.0, check = valid)
                        
                        if str(reaction) == add:
                            if fame[x] == 0:
                                holdc[x] = True
                                await message.send('Bruh, you do not have any fame left. Consider giving your clothes?')
                            else:
                                fame[x] = fame[x] - 1
                                famepool = famepool + 1
                                await message.send('{} raised. {} left.'.format(player.mention, fame[x]))
                        elif str(reaction) == hold:
                            if holdc[x] == True:
                                pass
                            else:
                                holdc[x] = True
                                await message.send('{} holded.'.format(player.mention))
                        elif str(reaction) == fold:
                            holdc[x] = True
                            foldc[x] = True
                            fame[x] = 0
                            await message.send('{} folded. Sad but no regrets eh?'.format(player.mention))
                        elif str(reaction) == all_in:
                            if fame[x] == 0:
                                holdc[x] = True
                                await message.send("I know you are rich, but I will just hold you.")
                            else:
                                holdc[x] = True
                                famepool = famepool + fame[x]
                                fame[x] = 0
                                await message.send('{} ALL INNNNNN!!! 🤩'.format(player.mention))
                    except asyncio.TimeoutError:
                        foldc[x] = True
                        holdc[x] = True
                        await message.send('{} did not respond! Out you go 👺.'.format(player))
                elif foldc[x] == True:
                    holdc[x] = True
                    await message.send('You folded. So just be patient, Mr/Mrs {}.'.format(player.mention))
                await asyncio.sleep(2)
# Loop for twice for three rounds
        pool = pool + 1 

    await message.send('Totalling... {} in total for the winner 🤑.'.format(famepool))
    await asyncio.sleep(3)
    await message.send("Player's card. \n{}".format(handlist))
    await message.send("Dealer's card. \n{}".format(dealer_hand))
    await asyncio.sleep(2)
    await message.send("See for yourself the result. Dealer has ran away 🤡.")

    
# Landlord for and only four
@bot.command(aliases = ['ll'])
async def landlord(message, firstName: discord.Member, secondName: discord.Member, thirdName: discord.Member, fourthName: discord.Member):
    await message.send('This is a complicated game, so be prepared and understand the rules beforehand.')
    await asyncio.sleep(5)

    players = [firstName, secondName, thirdName, fourthName]

    join = '✅'
    cancel = '❎'

    accept = '👌'
    decline = '💩'

    one = '1️⃣'
    two = '2️⃣'
    three = '3️⃣'
    four = '4️⃣'
    five = '5️⃣'

# Room to join game or cancel game
    readym = await message.send('React accordingly to tag to start the game ⌛️.')
    for ready_emoji in [join, cancel]:
        await readym.add_reaction(ready_emoji)

    for player in players:
        def valid1(reaction, user):
            return user == player and str(reaction) in [join, cancel]
        
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 30.0, check = valid1)
            if str(reaction) == join:
                await message.send('{} joined'.format(player.name))
            elif str(reaction) == cancel:
                await message.send('{} rejected'.format(player.name))
                return
        except asyncio.TimeoutError:
            await message.send('Someone did not join.')
            return

    await asyncio.sleep(2)
    await message.send('Game will start soon!')
    await message.send('D = ♦️ Diamond, C = ♣️ Club, H = ♥️ Heart, S = ♠️ Spade')
    await asyncio.sleep(10)
    
    deck = [
'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK', 'DA', 'D2',
'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK', 'CA', 'C2',
'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK', 'HA', 'H2',
'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'SA', 'S2'
]

    firstName_hand = []
    secondName_hand = []
    thirdName_hand = []
    fourthName_hand = []
    playerhand = [firstName_hand, secondName_hand, thirdName_hand, fourthName_hand]

# Send 13 cards to each players
    for i in range (0, 13):
        for playerhand in [firstName_hand, secondName_hand, thirdName_hand, fourthName_hand]:
            random.shuffle(deck)
            card = random.choice(deck)
            playerhand.append(card)
            deck.remove(card)

    await message.send('Shuffling card and distributing ...')
    await firstName.send('This is your card deck.\n{}'.format(firstName_hand))
    await secondName.send('This is your card deck.\n{}'.format(secondName_hand))
    await thirdName.send('This is your card deck.\n{}'.format(thirdName_hand))
    await fourthName.send('This is your card deck.\n{}'.format(fourthName_hand))
    await asyncio.sleep(10)

    await message.send('🎲 GAME COMMENCED 🎲')

    win = 0 
    getDecline1 = False
    getDecline2 = False
    getDecline3 = False
    getDecline4 = False
# Loop while no one hand is empty
    while win == 0:
        while getDecline1 == False:
            getDecline1 = True
            response_list = []
            await message.send("{}'s turn.".format(firstName.mention))

            optionm = await message.send("How many cards you want to show?")
            for option_emoji in [one, two, three, four, five, cancel]:
                await optionm.add_reaction(option_emoji)

            def optionValid(reaction, user):
                return user == firstName and str(reaction) in [one, two, three, four, five, cancel]
    # How many card wanted to play
            playcard = 0
            try:
                reaction, user = await bot.wait_for('reaction_add', timeout = 120.0, check = optionValid)
                if str(reaction) == one:
                    playcard = 1
                elif str(reaction) == two:
                    playcard = 2
                elif str(reaction) == three:
                    playcard = 3
                elif str(reaction) == four:
                    playcard = 4
                elif str(reaction) == five:
                    playcard = 5
                elif str(reaction) == cancel:
                    playcard = 0
            except asyncio.TimeoutError:
                await message.send("OK! You don't react. Skip 😑.")
                playcard = 0
    # Loop according to the playcard
            countcard = 0
            while countcard != playcard:
                await message.send('Play your card one by one 😇.')
                response = await bot.wait_for('message', timeout = 120.0, check = None)
                if message.author.id == firstName.id:
                    if response.content in firstName_hand:
                        response_list.append(response.content)
                        countcard = countcard + 1
                    elif response.content not in firstName_hand:
                        await message.send('Card not in your deck 😐.')

            if playcard != 0:
                await message.send('```{}```'.format(response_list))
                agreem = await message.send("All agree to {}'s card? 🤔".format(firstName.name))
                for agree_emoji in [accept, decline]:
                    await agreem.add_reaction(agree_emoji)

                for player in players:
                    def valid(reaction, user):
                        return user == player and str(reaction) in [accept, decline]
            
                    try:
                        reaction, user = await bot.wait_for('reaction_add', timeout = 120.0, check = valid)
                        await message.send('{} agree or decline?'.format(player))
                        if str(reaction) == accept:
                            await message.send("{} agreed.".format(player.name))
                        elif str(reaction) == decline:
                            await message.send("{} declined.".format(player.name))
                            await message.send("YOU! Replay your card.")
                            getDecline1 = True
                    except asyncio.TimeoutError:
                        await message.send("Someone did not agree so all agreed yeah 😛.")
    # Finalizing
        for i in response_list:
            firstName_hand.remove(i)
        if not firstName_hand:
            win = 1
            await message.send("{} is the winner.".format(firstName.mention))
            break
        elif firstName_hand:
            await firstName.send('This is your deck in hand.\n{}'.format(firstName_hand))

        while getDecline2 == False:
            getDecline2 = True
            response_list = []
            await message.send("{}'s turn.".format(secondName.mention))

            optionm = await message.send("How many cards you want to show?")
            for option_emoji in [one, two, three, four, five, cancel]:
                await optionm.add_reaction(option_emoji)

            def optionValid(reaction, user):
                return user == secondName and str(reaction) in [one, two, three, four, five, cancel]
    # How many card wanted to play
            playcard = 0
            try:
                reaction, user = await bot.wait_for('reaction_add', timeout = 120.0, check = optionValid)
                if str(reaction) == one:
                    playcard = 1
                elif str(reaction) == two:
                    playcard = 2
                elif str(reaction) == three:
                    playcard = 3
                elif str(reaction) == four:
                    playcard = 4
                elif str(reaction) == five:
                    playcard = 5
                elif str(reaction) == cancel:
                    playcard = 0
            except asyncio.TimeoutError:
                await message.send("OK! You don't react. Skip 😑.")
                playcard = 0
    # Loop according to the playcard
            countcard = 0
            while countcard != playcard:
                await message.send('Play your card one by one 😇.')
                response = await bot.wait_for('message', timeout = 120.0, check = None)
                if message.author.id == secondName.id:
                    if response.content in secondName_hand:
                        response_list.append(response.content)
                        countcard = countcard + 1
                    elif response.content not in secondName_hand:
                        await message.send('Card not in your deck 😐.')

            if playcard != 0:
                await message.send('```{}```'.format(response_list))
                agreem = await message.send("All agree to {}'s card? 🤔".format(secondName.name))
                for agree_emoji in [accept, decline]:
                    await agreem.add_reaction(agree_emoji)

                for player in players:
                    def valid(reaction, user):
                        return user == player and str(reaction) in [accept, decline]
            
                    try:
                        reaction, user = await bot.wait_for('reaction_add', timeout = 120.0, check = valid)
                        await message.send('{} agree or decline?'.format(player))
                        if str(reaction) == accept:
                            await message.send("{} agreed.".format(player.name))
                        elif str(reaction) == decline:
                            await message.send("{} declined.".format(player.name))
                            await message.send("YOU! Replay your card.")
                            getDecline2 = True
                    except asyncio.TimeoutError:
                        await message.send("Someone did not agree so all agreed yeah 😛.")
    # Finalizing
        for i in response_list:
            secondName_hand.remove(i)
        if not secondName_hand:
            win = 1
            await message.send("{} is the winner.".format(secondName.mention))
            break
        elif secondName_hand:
            await secondName.send('This is your deck in hand.\n{}'.format(secondName_hand))

        while getDecline3 == False:
            getDecline3 = True
            response_list = []
            await message.send("{}'s turn.".format(thirdName.mention))

            optionm = await message.send("How many cards you want to show?")
            for option_emoji in [one, two, three, four, five, cancel]:
                await optionm.add_reaction(option_emoji)

            def optionValid(reaction, user):
                return user == thirdName and str(reaction) in [one, two, three, four, five, cancel]
    # How many card wanted to play
            playcard = 0
            try:
                reaction, user = await bot.wait_for('reaction_add', timeout = 120.0, check = optionValid)
                if str(reaction) == one:
                    playcard = 1
                elif str(reaction) == two:
                    playcard = 2
                elif str(reaction) == three:
                    playcard = 3
                elif str(reaction) == four:
                    playcard = 4
                elif str(reaction) == five:
                    playcard = 5
                elif str(reaction) == cancel:
                    playcard = 0
            except asyncio.TimeoutError:
                await message.send("OK! You don't react. Skip 😑.")
                playcard = 0
    # Loop according to the playcard
            countcard = 0
            while countcard != playcard:
                await message.send('Play your card one by one 😇.')
                response = await bot.wait_for('message', timeout = 120.0, check = None)
                if message.author.id == thirdName.id:
                    if response.content in thirdName_hand:
                        response_list.append(response.content)
                        countcard = countcard + 1
                    elif response.content not in thirdName_hand:
                        await message.send('Card not in your deck 😐.')

            if playcard != 0:
                await message.send('```{}```'.format(response_list))
                agreem = await message.send("All agree to {}'s card? 🤔".format(thirdName.name))
                for agree_emoji in [accept, decline]:
                    await agreem.add_reaction(agree_emoji)

                for player in players:
                    def valid(reaction, user):
                        return user == player and str(reaction) in [accept, decline]
            
                    try:
                        reaction, user = await bot.wait_for('reaction_add', timeout = 120.0, check = valid)
                        await message.send('{} agree or decline?'.format(player))
                        if str(reaction) == accept:
                            await message.send("{} agreed.".format(player.name))
                        elif str(reaction) == decline:
                            await message.send("{} declined.".format(player.name))
                            await message.send("YOU! Replay your card.")
                            getDecline3 = True
                    except asyncio.TimeoutError:
                        await message.send("Someone did not agree so all agreed yeah 😛.")
    # Finalizing
        for i in response_list:
            thirdName_hand.remove(i)
        if not thirdName_hand:
            win = 1
            await message.send("{} is the winner.".format(thirdName.mention))
            break
        elif thirdName_hand:
            await thirdName.send('This is your deck in hand.\n{}'.format(thirdName_hand))

        while getDecline4 == False:
            getDecline4 = True
            response_list = []
            await message.send("{}'s turn.".format(fourthName.mention))

            optionm = await message.send("How many cards you want to show?")
            for option_emoji in [one, two, three, four, five, cancel]:
                await optionm.add_reaction(option_emoji)

            def optionValid(reaction, user):
                return user == fourthName and str(reaction) in [one, two, three, four, five, cancel]
    # How many card wanted to play
            playcard = 0
            try:
                reaction, user = await bot.wait_for('reaction_add', timeout = 120.0, check = optionValid)
                if str(reaction) == one:
                    playcard = 1
                elif str(reaction) == two:
                    playcard = 2
                elif str(reaction) == three:
                    playcard = 3
                elif str(reaction) == four:
                    playcard = 4
                elif str(reaction) == five:
                    playcard = 5
                elif str(reaction) == cancel:
                    playcard = 0
            except asyncio.TimeoutError:
                await message.send("OK! You don't react. Skip 😑.")
                playcard = 0
    # Loop according to the playcard
            countcard = 0
            while countcard != playcard:
                await message.send('Play your card one by one 😇.')
                response = await bot.wait_for('message', timeout = 120.0, check = None)
                if message.author.id == fourthName.id:
                    if response.content in fourthName_hand:
                        response_list.append(response.content)
                        countcard = countcard + 1
                    elif response.content not in fourthName_hand:
                        await message.send('Card not in your deck 😐.')

            if playcard != 0:
                await message.send('```{}```'.format(response_list))
                agreem = await message.send("All agree to {}'s card? 🤔".format(fourthName.name))
                for agree_emoji in [accept, decline]:
                    await agreem.add_reaction(agree_emoji)

                for player in players:
                    def valid(reaction, user):
                        return user == player and str(reaction) in [accept, decline]
            
                    try:
                        reaction, user = await bot.wait_for('reaction_add', timeout = 120.0, check = valid)
                        await message.send('{} agree or decline?'.format(player))
                        if str(reaction) == accept:
                            await message.send("{} agreed.".format(player.name))
                        elif str(reaction) == decline:
                            await message.send("{} declined.".format(player.name))
                            await message.send("YOU! Replay your card.")
                            getDecline4 = True
                    except asyncio.TimeoutError:
                        await message.send("Someone did not agree so all agreed yeah 😛.")
    # Finalizing
        for i in response_list:
            fourthName_hand.remove(i)
        if not fourthName_hand:
            win = 1
            await message.send("{} is the winner.".format(fourthName.mention))
            break
        elif fourthName_hand:
            await fourthName.send('This is your deck in hand.\n{}'.format(fourthName_hand))
                        
    await asyncio.sleep(4)
    await message.send("THE SCOREBOARD\n{}\n{} card(s) left.\n{}\n{} card(s) left.\n{}\n{} card(s) left.\n{}\n{} card(s) left.".format(firstName, len(firstName_hand), secondName, len(secondName_hand), thirdName, len(thirdName_hand), fourthName, len(fourthName_hand)))
    
bot.run(os.environ.get('BOT_SECRET_TOKEN'))