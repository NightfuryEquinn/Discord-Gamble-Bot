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
p/s: Jack, Queen, King are counted as 10, but reduced chances.
```
gb bj @p1 @... -- No limit of players
🎴 Hit 🛑 Hold
```    
'''.format(name), 
color = random.choice(colors))
    bj_rules.set_thumbnail(url = avatar)
    bj_rules.set_footer(text = 'Any bugs or issues, dm or pm or whatever message me: Nightfury#8826 🥰')

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
    tp_rules.set_footer(text = 'Any bugs or issues, dm or pm or whatever message me: Nightfury#8826 🥰')

# Chodaidi Page
    cdd_rules = discord.Embed(
title = 'No-Currency Gamble Bot Handbook 📙', 
description = '''
{} is stilllll reading ~~~ 😬

Chapter 3 - 🃏 ChoDaiDi / 锄大第

Legendary card game!
One random player will be chose to vote?
Each player has 13 cards. Turns according to tag mention.
Whoever empty the hand, wins 😎! 
2 is the boss, 3 is the servant here. Suits are relevant.
```
gb cdd @p1 @p2 @p3 @p4 -- Must and only four players
👌 Accept 💩 Decline
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
    cdd_rules.set_thumbnail(url = avatar)
    cdd_rules.set_footer(text = 'Any bugs or issues, dm or pm or whatever message me: Nightfury#8826 🥰')

# Doudizhu Page
    ddz_rules = discord.Embed(
title = 'No-Currency Gamble Bot Handbook 📒',
description = '''
{} is confused about ChoDaidi and DouDiZhu 😵

Chapter 4 - 🧧 DouDiZhu / 斗地主

Another legendary card game! But more advanced 😳
Each player has 17 cards.
3 cards remaining goes whoever called for Landlord after shown to all players.
2 players (Peasant Team) 👩🏻‍🌾 compete against the Landlord 🤴🏻
Landlord wins if hand emptied, vice versa.
CJ is the boss, 3 is the servant here. Suits are irrelevant 😎
```
gb ddz @p1 @p2 @p3 -- Must and only three players
First tag is Landlord, rest are peasant.
👌 Accept 💩 Decline
```
```
SCORETABLE 💱 Largest to Smallest
Nuke 💣 [Double Joker]
Bomb 🧨 [Four of a Kind]
Large Space Shuttle 🚀 [2 or more Four of a Kind + Pairs according to number of trio]
Small Space Shuttle 🚀 [2 or more Four of a Kind + Single according to number of trio]
Space Shuttle 🚀 [2 or more Four of a Kind]
Straight
Pairs Four 
Single Four
Large Airplane ✈️ [2 or more Trio + Pairs according to number of trio]
Small Airplane ✈️ [2 or more Trio + Single according to number of trio]
Airplane ✈️ [2 or more Trio]
Trio 
Pairs
Single
```
'''.format(name),
color = random.choice(colors))
    ddz_rules.set_thumbnail(url = avatar)
    ddz_rules.set_footer(text = 'Any bugs or issues, dm or pm or whatever message me: Nightfury#8826 🥰')

# Match Ten Page
    mt_rules = discord.Embed(
title = 'No-Currency Gamble Bot Handbook 📕',
description = '''
{} finished reading. Remember to put back the book to the shelf 🙄.

Chapter 5 - 🔟 Match Ten / 拼十

Casual luck game.
Match a pair of cards and make a TEN.
Pair of Jack, Queen, King, respectively are TEN.
First to clear hand after deck is empty, wins!
```
gb mt @p1 @... @p10 - Min of 3 players / Max of 10 players
🤹 Pick 🃏 Draw
Type skip to skip during play card
```
'''.format(name),
color = random.choice(colors))
    mt_rules.set_thumbnail(url = avatar)
    mt_rules.set_footer(text = 'Any bugs or issues, dm or pm or whatever message me: Nightfury#8826 🥰')

    page = 1
    m = await message.send(embed = bj_rules)
    await m.add_reaction(left)
    await m.add_reaction(right)

    def valid(reaction, user):
        return user == message.author and str(reaction) in [left, right]
# Reading the rule book
    while True:
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 90.0, check = valid)
            await m.remove_reaction(reaction, user)

            if str(reaction) == left:
                page = page - 1
                if page < 1:
                    page = 5
            elif str(reaction) == right:
                page = page + 1
                if page > 5:
                    page = 1

            if page == 1:
                await m.edit(embed = bj_rules)
            elif page == 2:
                await m.edit(embed = tp_rules)
            elif page == 3:
                await m.edit(embed = cdd_rules)
            elif page == 4:
                await m.edit(embed = ddz_rules)
            elif page == 5:
                await m.edit(embed = mt_rules)
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
# Draw a card
                if str(reaction) == hit:
                    card = random.choice(deck)
                    deck.remove(card)
                    hands.append(card)
                    await player.send("Here is your card in hand.\n```{}```".format(hands))
# Hold and end turn
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
# Double aces or five in a row 
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
# Getting result and send
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
# Set 10 fames for each player, fold set False for this round
    dealer_hand = []
    fame = []
    foldc = []
    for player in players:
        fame.append(10)
        foldc.append(False)
# Send ROUND according to number of loops
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
# Show dealer cards
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
# Raise fame for this round
                        if str(reaction) == add:
                            if fame[x] == 0:
                                holdc[x] = True
                                await message.send('Bruh, you do not have any fame left. Consider giving your clothes?')
                            else:
                                fame[x] = fame[x] - 1
                                famepool = famepool + 1
                                await message.send('{} raised. {} left.'.format(player.mention, fame[x]))
# Hold fame for this round
                        elif str(reaction) == hold:
                            if holdc[x] == True:
                                pass
                            else:
                                holdc[x] = True
                                await message.send('{} holded.'.format(player.mention))
# Fold game, will be skipped in second and third round
                        elif str(reaction) == fold:
                            holdc[x] = True
                            foldc[x] = True
                            fame[x] = 0
                            await message.send('{} folded. Sad but no regrets eh?'.format(player.mention))
# Throw all fame in this round, will be skipped in second and third round but not folded
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

    
# ChoDaiDi for and only four
@bot.command(aliases = ['cdd'])
async def chodaidi(message, firstName: discord.Member, secondName: discord.Member, thirdName: discord.Member, fourthName: discord.Member):
    firstName_hand = []
    secondName_hand = []
    thirdName_hand = []
    fourthName_hand = []
    players = [firstName, secondName, thirdName, fourthName]
    playerhand = [firstName_hand, secondName_hand, thirdName_hand, fourthName_hand]

    accept = '👌'
    decline = '💩'

    await message.send('Before you play, make sure you know the rules.\nBEcause there is no validation for who is bigger 😌\nNo good for you to cheat, right?')
    await asyncio.sleep(5)
    await message.send('Be ready 🚦 ... Card shuffling 🔄 ...\nD = ♦️ Diamond 方块\nC = ♣️ Club 梅花\nH = ♥️ Heart 红心\nS = ♠️ Spade 黑桃')

# Set deck and shuffle and distribute and send to players
    deck = [
'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK', 'DA',
'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK', 'CA',
'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK', 'HA',
'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'SA'
]
    'D3' < 'D4' < 'D5' < 'D6' < 'D7' < 'D8' < 'D9' < 'D10' < 'DJ' < 'DQ' < 'DK' < 'DA' < 'D2' < 'C3' < 'C4' < 'C5' < 'C6' < 'C7' < 'C8' < 'C9' < 'C10' < 'CJ' < 'CQ' < 'CK' < 'CA' < 'C2' < 'H3' < 'H4' < 'H5' < 'H6' < 'H7' < 'H8' < 'H9' < 'H10' < 'HJ' < 'HQ' < 'HK' < 'HA' < 'H2' < 'S3' < 'S4' < 'S5' < 'S6' < 'S7' < 'S8' < 'S9' < 'S10' < 'SJ' < 'SQ' < 'SK' < 'SA' < 'S2' 
    
    for i in range(0, 13):
        for hand in playerhand:
            random.shuffle(deck)
            a = random.choice(deck)
            hand.append(a)
            deck.remove(a)

    await firstName.send('Here is your card in hand.\n{}'.format(firstName_hand))
    await secondName.send('Here is your card in hand.\n{}'.format(secondName_hand))
    await thirdName.send('Here is your card in hand.\n{}'.format(thirdName_hand))
    await fourthName.send('Here is your card in hand.\n{}'.format(fourthName_hand))

    await asyncio.sleep(5)
                        
    await message.send('🎲 Game Commenced 🎲')

    win = 0
    played = []
    tempplayed = []
    passcount = 0
# Loop while no one hands are empty
    while win == 0:
        for player in players:
            x = players.index(player)
            requestPass = False
# Clear 'played' if three players passed
            if passcount == 3:
                passcount = 0
                played.clear()
            elif passcount != 3:
                pass
# Proceed player round
            await message.send("{}'s turn. Play your card one by one 🤔".format(player.mention))

            checkplaycard = False
            while checkplaycard == False:
                checkplaycard = True
                try:
                    if not played:
                        playcard = 0
                        while playcard < 5:
                            response = await bot.wait_for('message', timeout = 45.0, check = None)
                            if message.author != bot.user: 
                                if response.author != bot.user:
                                    if response.author.id == player.id:
                                        if response.content.lower() == 'pass':
                                            playcard = 5
                                            requestPass = True
                                            await message.send('{} skipped 🤚'.format(player.name))
                                        else:
                                            if response.content in playerhand[x]:
                                                playcard = playcard + 1
                                                tempplayed.append(response.content)
                                            elif response.content not in playerhand[x]:
                                                await message.send('You sure the card in your hand? 😒')
                    elif played:
                        await message.send("{}, you can only play {} card(s). OR just pass 😶".format(player.mention, len(played)))
                        playcard = 0
                        while playcard < len(played):
                            response = await bot.wait_for('message', timeout = 45.0, check = None)
                            if message.author != bot.user:
                                if response.author != bot.user:
                                    if response.author.id == player.id:
                                        if response.content.lower() == 'pass':
                                            playcard == len(played)
                                            requestPass = True
                                            passcount = passcount + 1
                                            await message.send('{} skipped 🤚'.format(player.name))
                                        else:
                                            if response.content in playerhand[x]:
                                                playcard = playcard + 1
                                                tempplayed.append(response.content)
                                            elif response.content not in playerhand[x]:
                                                await message.send('You sure the card in your hand? 😒')
                        if len(played) != len(tempplayed):
                            await message.send('{}, you did not play the card(s) required. You are skipped 😠')
                            requestPass = True
                except asyncio.TimeoutError:
                    played.clear()
                    for i in tempplayed:
                        played.append(i)
                    tempplayed.clear()
                    played.sort()
# Check card played
                await asyncio.sleep(2)

                if requestPass == False:
                    await message.send('```{}```\nCard(s) played by {} 😳'.format(tempplayed, player.mention))
                    if len(played) == 1:
                        await message.send('Just a single 🥱')
                    elif len(played) == 2:
                        if played[0][1:2] == played[1][1:2]:
                            await message.send('Double! or Pair! 😐')
                    elif len(played) == 3:
                        if played[0][1:2] == played[1][1:2] and played[1][1:2] == played[2][1:2]:
                            await message.send('THREE of a kind!!! 😮')
                    elif len(played) == 4:
                        if played[0][1:2] == played[1][1:2] and played[1][1:2] == played[2][1:2] and played[2][1:2] == played[3][1:2]:
                            await message.send('!!FOUR of a KIND!! 😲')
                    elif len(played) == 5:
                        await message.send('FIVE CARD of IDK what 😱')
                    
                    await message.send('See who will be pick as the judge 🥶')

                    judge = player
                    while judge == player:
                        judge = random.choice(players)

                    judgem = await message.send('{}, do you approve? 🤫'.format(judge.mention))
                    for judge_emoji in [accept, decline]:
                        await judgem.add_reaction(judge_emoji)
                    
                    def checkjudge(reaction, user):
                        return user == judge and str(reaction) in [accept, decline]

                    try:
                        reaction, user = await bot.wait_for('reaction_add', timeout = 30.0, check = checkjudge)
                        if str(reaction) == accept:
                            await message.send('{} accepted!'.format(judge.name))
                        elif str(reaction) == decline:
                            await message.send('{} rejected! {}, replay your card.'.format(judge.name, player.mention))
                    except asyncio.TimeoutError:
                        await message.send('The judge did not react so counted as accepted 😝')

                    for i in played:
                        playerhand[x].remove(i)
                    await player.send('This is your card in hand.\n{}'.format(playerhand[x]))

# Check for winner
        for player in players:
            x = players.index(player)
            if playerhand[x]:
                await message.send('{} still have {} card(s) left.'.format(player.name, len(playerhand[x])))
            elif not playerhand[x]:
                await message.send('{} is the winner! 🥳'.format(player.mention))
                win = 1

# Send the results
    await message.send('Confirming result 👾 ...')
    await asyncio.sleep(4)
    await message.send(" 💸 THE SCOREBOARD 💸\n{}\n{} card(s) left.\n{}\n{} card(s) left.\n{}\n{} card(s) left.\n{}\n{} card(s) left.".format(firstName, len(firstName_hand), secondName, len(secondName_hand), thirdName, len(thirdName_hand), fourthName, len(fourthName_hand)))
    

# DouDiZhu for and only three
@bot.command(aliases = ['ddz'])
async def doudizhu(message, firstName: discord.Member, secondName: discord.Member, thirdName: discord.Member):
    await message.send('{} is the landlord 😌 {} and {} are peasant.'.format(firstName, secondName, thirdName))
    await asyncio.sleep(4)

    accept = '👌'
    decline = '💩'

    landlord_hand = []
    peasant1_hand = []
    peasant2_hand = []
    
    players = [firstName, secondName, thirdName]
    playerhand = [landlord_hand, peasant1_hand, peasant2_hand]

    deck = ['1', '1', '1', '1', '2', '2', '2', '2', '3', '3', '3' , '3', '4', '4', '4', '4', '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '10', '10', '10', '10', 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K', 'BW', 'CJ']
    '3' < '4' < '5' < '6' < '7' < '8' < '9' < '10' < 'J' < 'Q' < 'K' < '1' < '2' < 'BW' < 'CJ'
# Shuffle and assign deck for players
    forLandlord = []
    for i in range(0, 3):
        random.shuffle(deck)
        a = random.choice(deck)
        forLandlord.append(a)
        deck.remove(a)
    
    for i in range(0, 17):
        for player in players:
            x = players.index(player)
            random.shuffle(deck)
            a = random.choice(deck)
            playerhand[x].append(a)
            deck.remove(a)
# Show three cards for landlord and appeend to landlord deck
    await message.send('This is the three extra cards for landlord 👀 \n{}'.format(forLandlord))
    for i in forLandlord:
        landlord_hand.append(i)
# Send card to players
    for player in players:
        x = players.index(player)
        await player.send('This is your deck.\n{}'.format(playerhand[x]))

    await message.send('Game will start soon. In 10 seconds 🕐')
    await asyncio.sleep(10)
# Loop while no one hand is empty
    win = 0
    played = []
    tempplayed = []
    passcount = 0
    while win == 0:
        for player in players:
            x = players.index(player)
            requestPass = False
            
            if passcount == 3:
                passcount = 0
                played.clear()
            elif passcount != 3:
                pass

            await message.send("{}'s turn. Play your card one by one 😶".format(player.mention))

            checkplaycard = False
            while checkplaycard == False:
                checkplaycard = True
                try:
                    if not played:
                        playcard = 0
                        while playcard < 21:
                            response = await bot.wait_for('message', timeout = 45.0, check = None)
                            if message.author != bot.user: 
                                if response.author != bot.user:
                                    if response.author.id == player.id:
                                        if response.content.lower() == 'pass':
                                            playcard = 21
                                            requestPass = True
                                            await message.send('{} skipped.'.format(player.name))
                                        else:
                                            if response.content in playerhand[x]:
                                                playcard = playcard + 1
                                                tempplayed.append(response.content)
                                            elif response.content not in playerhand[x]:
                                                await message.send('You sure the card in your hand?')
                    elif played:
                        await message.send("{}, you can only play {} card(s). OR just pass.".format(player.mention, len(played)))
                        playcard = 0
                        while playcard < len(played):
                            response = await bot.wait_for('message', timeout = 45.0, check = None)
                            if message.author != bot.user:
                                if response.author != bot.user:
                                    if response.author.id == player.id:
                                        if response.content.lower() == 'pass':
                                            playcard == len(played)
                                            requestPass = True
                                            passcount = passcount + 1
                                            await message.send('{} skipped.'.format(player.name))
                                        else:
                                            if response.content in playerhand[x]:
                                                playcard = playcard + 1
                                                tempplayed.append(response.content)
                                            elif response.content not in playerhand[x]:
                                                await message.send('You sure the card in your hand?')
                        if len(played) != len(tempplayed):
                            await message.send('{}, you did not play the card(s) required. You are skipped.')
                            requestPass = True
                except asyncio.TimeoutError:
                    played.clear()
                    for i in tempplayed:
                        played.append(i)
                    tempplayed.clear()
                    played.sort()

                await asyncio.sleep(2)
# Check card
                if requestPass == False:
                    await message.send('See who will be pick as the judge.')

                    judge = player
                    while judge == player:
                        judge = random.choice(players)

                    judgem = await message.send('{}, do you approve?'.format(judge.mention))
                    for judge_emoji in [accept, decline]:
                        await judgem.add_reaction(judge_emoji)
                    
                    def checkjudge(reaction, user):
                        return user == judge and str(reaction) in [accept, decline]

                    try:
                        reaction, user = await bot.wait_for('reaction_add', timeout = 30.0, check = checkjudge)
                        if str(reaction) == accept:
                            await message.send('{} accepted!'.format(judge.name))
                        elif str(reaction) == decline:
                            await message.send('{} rejected! {}, replay your card.'.format(judge.name, player.mention))
                    except asyncio.TimeoutError:
                        await message.send('The judge did not react so counted as accepted 😝')

                    for i in played:
                        playerhand[x].remove(i)
                    await player.send('This is your card in hand.\n{}'.format(playerhand[x]))

# Check for winner
        for player in players:
            x = players.index(player)
            if playerhand[x]:
                await message.send('{} still have {} card(s) left.'.format(player.name, len(playerhand[x])))
            elif not playerhand[x]:
                if x == 0:
                    await message.send('{} is the winner! Landlord won! 🤠'.format(player.mention))
                elif x == 1 or x == 2:
                    await message.send('{} is the winner! Peasant team won! 🤯'.format(player.mention))
                win = 1


# Match Ten 
@bot.command(aliases = ['mt'])
async def matchten(message, *name: discord.Member):
# Minimum and maximum requirements
    if len(name) > 10:
        await message.send('Maximum 10 players')
        return
    elif len(name) < 3:
        await message.send('Minimum 3 players.')
        return
    else:
        await message.send('Loading... Prepare yourself')

    await asyncio.sleep(5)

    pick = '🤹'
    draw = '🃏'
    deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 69]
    pickplayeremojis = ['🥮', '🍣', '🍱', '🍙', '🍩', '🌮', '🥗', '🥘', '🍵', '🍡']
    pickcardemojis = ['😀', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '😊', '😇', '🙂', '🙃', '😉', '😌', '😍', '🥰', '😘', '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤪', '🤨', '🤩', '🥳', '😏', '😒', '😞', '😔', '😟', '😕', '🙁', '☹️', '😣', '😖', '😫', '😩', '🥺', '😢', '😭', '😤', '😠', '😡', '🤬', '🤯', '😳', '🥵']

# Get players
    players = []
    playerhand = []
    for player in name:
        players.append(player)
        playerhand.append(list(player.name))
# Clear list to be empty lists
    for hand in playerhand:
        hand.clear()
# Shuffle card and distribute and send
    for i in range(0, 5):
        for hand in playerhand:
            random.shuffle(deck)
            a = random.choice(deck)
            hand.append(a)
            deck.remove(a)
    
    await asyncio.sleep(2)

    for player in players:
        x = players.index(player)
        await player.send('This is your card in hand.\n{}'.format(playerhand[x]))
    
    await message.send('Ready? ✅ Game start soon... Match cards sum up to 10 as a pair!')
    await asyncio.sleep(5)
# Loop while no hand is empty
    win = 0
    while win == 0:
# Notify the number of cards in deck
        await message.send('❄️ {} card(s) left in deck ❄️'.format(len(deck)))
        for player in players:
            x = players.index(player)
            requestPick = False
            requestDeck = False
            chooseTimeout = False
            pickplayerTimeout = False
            if 69 in playerhand[x]:
                await message.send('JOKER is here! HAH! 🌝')
            else:
                await message.send('Normal person 🌚')
# Choose to pick from player or pick from deck
            choose = await message.send('Pick or Draw? {}'.format(player.mention))
            for choose_emoji in [pick, draw]:
                await choose.add_reaction(choose_emoji)
            
            def checkchoose(reaction, user):
                return user == player and str(reaction) in [pick, draw]

            try:
                reaction, user = await bot.wait_for('reaction_add', timeout = 60.0, check = checkchoose)
                if str(reaction) == pick:
                    requestPick = True
                elif str(reaction) == draw:
                    requestDeck = True
            except asyncio.TimeoutError:
                await message.send('{} lost a turn 🤨'.format(player.name))
                chooseTimeout = True

            if chooseTimeout == False:
# Pick a random player
                if requestPick == True:
                    pickm = await message.send('Pick a random player, {}.'.format(player.mention))
                    for i in range(0, len(name)):
                        await pickm.add_reaction(random.choice(pickplayeremojis))
                    
                    def checkpickplayer(reaction, user):
                        return user == player and str(reaction) in pickplayeremojis

                    try:
                        reaction, user = await bot.wait_for('reaction_add', timeout = 60.0, check = checkpickplayer)
                    except asyncio.TimeoutError:
                        await message.send('Seriously? No reaction? 😟')
                        pickplayerTimeout = True
# Pick a random card from the player
                    if pickplayerTimeout == False:
                        pickplayer1 = player
                        while pickplayer1 == player:
                            pickplayer1 = random.choice(players)
                        y = players.index(pickplayer1)
                        pickplayerm = await message.send("Pick a card from {}'s deck.".format(pickplayer1.name))
                        for i in range(0, len(playerhand[y])):
                            await pickplayerm.add_reaction(random.choice(pickcardemojis))

                        def checkpickplayerm(reaction, user):
                            return user == player and str(reaction) in pickcardemojis

                        try:
                            reaction, user = await bot.wait_for('reaction_add', timeout = 60.0, check = checkpickplayerm)
                            if str(reaction) in pickcardemojis:
                                t = random.choice(playerhand[y])
                                playerhand[x].append(t)
                                playerhand[y].remove(t)
                        except asyncio.TimeoutError:
                            t = random.choice(playerhand[y])
                            playerhand[x].append(t)
                            playerhand[y].remove(t)
                            await message.send('...!@%^*&^$#$ 🤬 If there is a Joker in your hand, do not blame me.')
                    
                    await player.send('This is your card in hand.\n{}'.format(playerhand[x]))
                    await pickplayer1.send('This is your card in hand.\n{}'.format(playerhand[y]))
# Pick card from deck
                if requestDeck == True:
                    if deck:
                        await message.send('{} picked a card from deck.'.format(player.name))
                        random.shuffle(deck)
                        p = random.choice(deck)
                        playerhand[x].append(p)
                        deck.remove(p)
                        await player.send('This is your card in hand.\n{}'.format(playerhand[x]))
                    elif not deck:
                        await message.send('No card in deck already 🤗 Best I help you pick a card from other. YRW ~')
                        pickplayer2 = player
                        while pickplayer2 == player:
                            pickplayer2 = random.choice(players)
                        z = players.index(pickplayer2)
                        u = random.choice(playerhand[z])
                        playerhand[x].append(u)
                        playerhand[z].remove(u)
                        await player.send('This is your card in hand.\n'.format(playerhand[x]))
                        await pickplayer2.send('This is your card in hand.\n'.format(playerhand[z]))
# Play card that match ten
                await asyncio.sleep(4)
                await message.send("{} play pair of card to match ten 😸".format(player.mention))
                getDecline = False
                getSum = False
                while getDecline == False:
                    getDecline = True
                    played = []
                    playround = 0
                    while playround != 2:
                        try:
                            while True:
                                response = await bot.wait_for('message', timeout = 60.0, check = None)
# Ignore and reject message from bot or other players
                                if message.author != bot.user: 
                                    if response.author != bot.user:
                                        if response.author.id == player.id:
                                            if response.content.lower() == 'skip':
                                                await message.send('{} skipped.'.format(player))
                                                playround = 2
                                                getSum = True
                                                break
                                            else:
                                                if int(response.content) in playerhand[x]:
                                                    played.append(int(response.content))
                                                    playround = playround + 1
                                                    break
                                                elif int(response.content) not in playerhand[x]:
                                                    await message.send('HA! You think you can fool me? Think thrice 💩')
                                                    continue
                                                else:
                                                    await message.send('I beg your pardon? Type skip to skip or play your card.')
                                                    continue
                                        elif response.author.id != player.id:
                                            await message.send("Nowadays, people are very impatient, aren't they? 🙄")
                                            continue
                        except asyncio.TimeoutError:
                            await message.send('Next... why am I doing this? Suffering from no repsonse 😵')
                            playround = 2
                            getSum = True
# Check whether the cards played are ten
                    if getSum == False:
                        for i in played:
                            int(i)
                        if sum(played) == 10:
                            await message.send('Yes, a 10!')
                        elif played[0] == 10 and played[1] == 10:
                            await message.send('DOUBLE TEN!!! TENTEN...😲')
                        elif sum(played) != 10:
                            await message.send('WTH? {}? 💩 REplay 💩'.format(sum(played)))
                            getDecline = False
# Finalizing and resend card in hand
                    if played:
                        for i in played:
                            playerhand[x].remove(i)
                        await player.send('This is your card in hand.\n{}'.format(playerhand[x]))
# Check for winner
        for winner in players:
            x = players.index(winner)
            if playerhand[x]:
                await message.send('{} still have {} card(s).'.format(winner.name, len(playerhand[x])))
            elif not playerhand[x]:
                await message.send('{} is the winner! 😎'.format(winner.mention))
                win = 1
                    

# Function to stop the bot
@bot.command()
async def stop(message):
    await message.send('Initializing shutdown sequence...')
    await asyncio.sleep(1)
    await message.send('Clearing all commands...')
    await asyncio.sleep(1)
    await message.send('Terminating quantum core...')
    await asyncio.sleep(1)
    await message.send('Quantum core is stable state... Shutting down...')
    await asyncio.sleep(1)
    await message.send('Shutdown sequence completed...')
    await bot.close()
    await bot.run(os.environ.get('BOT_SECRET_TOKEN'))





# Execute bot run
bot.run(os.environ.get('BOT_SECRET_TOKEN'))