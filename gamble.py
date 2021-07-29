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
With a twist of voting the card(s) played 😲. 
Each player has 13 cards. Turns according to tag mention.
Whoever empty the hand, wins 😎! 
2 is the boss, 3 is the servant here. Suits are relevant.
```
gb cdd @p1 @p2 @p3 @p4 -- Must and only four players
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
    cdd_rules.set_thumbnail(url = avatar)
    cdd_rules.set_footer(text = 'Any bugs or issues, dm or pm or whatever message me: Nightfury#8826 🥰')

# Doudizhu Page
    ddz_rules = discord.Embed(
title = 'No-Currency Gamble Bot Handbook 📒',
description = '''
{} is confused about ChoDaidi and DouDiZhu 😵

Chapter 4 - 🧧 DouDiZhu / 斗地主

Another legendary card game! But more advanced 😳
With a twist of voting the card(s) played. Again.
Each player has 17 cards.
3 cards remaining goes whoever called for Landlord after shown to all players.
2 players (Peasant Team) 👩🏻‍🌾 compete against the Landlord 🤴🏻
Landlord wins if hand emptied, vice versa.
CJ is the boss, 3 is the servant here. Suits are irrelevant 😎
```
gb ddz @p1 @p2 @p3 -- Must and only three players
✅ Join game ❎ Cancel game 👌 Agree 💩 Decline 
```
```
SCORETABLE 💱 Largest to Smallest
Nuke 💣 [Double Joker]
Bomb 🧨 [Four of a Kind]
Large Space Shuttle 🚀 [2 or more Four of a Kind + Pairs]
Small Space Shuttle 🚀 [2 or more Four of a Kind + Single]
Space Shuttle 🚀 [2 or more Four of a Kind]
Pairs Four 
Single Four
Large Airplane ✈️ [2 or more Trio + Pairs]
Small Airplane ✈️ [2 or more Trio + Single]
Airplane ✈️ [2 or more Trio]
Trio 
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

Chapter 5 - 🔟 Match Ten / 合十

Casual luck game.
Match a pair of cards and make a TEN.
Pair of Jack, Queen, King, respectively are TEN.
First to clear hand, wins!
```
gb mt @p1 @... @p10 - Max of 10 players
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

    
# ChoDaiDi for and only four
@bot.command(aliases = ['cdd'])
async def chodaidi(message, firstName: discord.Member, secondName: discord.Member, thirdName: discord.Member, fourthName: discord.Member):
    firstName_hand = []
    secondName_hand = []
    thirdName_hand = []
    fourthName_hand = []
    players = [firstName, secondName, thirdName, fourthName]
    playerhand = [firstName_hand, secondName_hand, thirdName_hand, fourthName_hand]

    join = '✅'
    cancel = '❎'

    accept = '👌'
    decline = '💩'

    one = '1️⃣'
    two = '2️⃣'
    three = '3️⃣'
    four = '4️⃣'
    five = '5️⃣'
    
    await message.send('''
This is ChoDaiDi / 锄大第, be prepared and understand the rules beforehand 😌 
Card(s) played is/are validated by players' votes 🤫
Have some sportsmanship or 'gambleship'? 👻
''')
    await asyncio.sleep(5)

# Join game or cancel game
    ready = await message.send('All must react for the game to start 👀\nReact accordingly to mention')
    await ready.add_reaction(join)
    await ready.add_reaction(cancel)

    for player in players:
        def checkReady(reaction, user):
            return user == player and str(reaction) in [join, cancel]
        
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 60.0, check = checkReady)
            if str(reaction) == join:
                await message.send('{} joined 🤩'.format(player.name))
            elif str(reaction) == cancel:
                await message.send('{} rejected 😠'.format(player.name))
                return
        except asyncio.TimeoutError:
            await message.send('Someone did not join. Game cancelled.')
            return

    await message.send('Be ready ✔️ ... Card shuffling 🔄 ...\nD = ♦️ Diamond 方块\nC = ♣️ Club 梅花\nH = ♥️ Heart 红心\nS = ♠️ Spade 黑桃')

# Set deck and shuffle and distribute and send to players
    deck = [
'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK', 'DA',
'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK', 'CA',
'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK', 'HA',
'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'SA'
]
    
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
# Loop while nobody hands are empty
    while win == 0:
        for player in players:
            x = players.index(player)
            getDecline = False
            while getDecline == False:
                playcard = 0
                countcard = 0
                nocard = 0
                response_list = []
                getDecline = True
                play = await message.send("{}'s turn.\nHow many cards should you play? 🤔".format(player.mention))
                for play_emoji in [one, two, three, four, five, cancel]:
                    await play.add_reaction(play_emoji)
# Prompt how many cards to play and loop
                def checkPlay(reaction, user):
                    return user == player and str(reaction) in [one, two, three, four, five, cancel]
                
                try:
                    reaction, user = await bot.wait_for('reaction_add', timeout = 120.0, check = checkPlay)
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
                    playcard = 0
                    await message.send("Time's up. {} lost a turn 😕".format(player.name))
# Loop according as reacted
                nocard = playcard
                while countcard != playcard:
                    await message.send('Play your card(s) one message at a time. {} left.'.format(nocard))
                    response = await bot.wait_for('message', timeout = 120.0, check = None)
                    if message.author != bot.user:
                        if response.author.id == player.id:
                            if response.content in playerhand[x]:
                                response_list.append(response.content)
                                countcard = countcard + 1
                                nocard = nocard - 1
                            elif response.content not in playerhand[x]:
                                await message.send('You sure the card is in your hand? 😐')
                        elif response.author.id != player.id:
                            await message.send('Not you.')
                    else:
                        pass
# Voting round to validate the cards played
                vote = await message.send("Voting Round\nDo you agree with {}'s card? 😏\n```{}``` ".format(player.name, response_list))
                for vote_emoji in [accept, decline]:
                    await vote.add_reaction(vote_emoji)

                for playervote in [firstName, secondName, thirdName, fourthName]:
                    def checkVote(reaction, user):
                        return user == playervote and str(reaction) in [accept, decline]

                    try:
                        reaction, user = await bot.wait_for('reaction_add', timeout = 20.0, check = checkVote)
                        if str(reaction) == accept:
                            await message.send('{} agreed.'.format(playervote.name))
                        elif str(reaction) == decline:
                            await message.send('{} disagreed. Replay card'.format(playervote.name))
                            getDecline = False
                    except asyncio.TimeoutError:
                        await message.send('{} did not vote so count as agreed 🤪'.format(playervote.name))
# Remove played card and check if hands empty
            if getDecline == True:
                if playerhand[x]:
                    for i in response_list:
                        playerhand[x].remove(i)
                    await player.send('This is your card in hand now.\n{}'.format(playerhand[x]))
                    await message.send('{} still have {} card(s) left.'.format(player, len(playerhand[x])))
                elif not playerhand[x]:
                    win = 1
                    await message.send('🥳 {} wins! 🥳'.format(player.mention))
                                
    await message.send('Confirming result 👾 ...')
    await asyncio.sleep(4)
    await message.send(" 💸 THE SCOREBOARD 💸\n{}\n{} card(s) left.\n{}\n{} card(s) left.\n{}\n{} card(s) left.\n{}\n{} card(s) left.".format(firstName, len(firstName_hand), secondName, len(secondName_hand), thirdName, len(thirdName_hand), fourthName, len(fourthName_hand)))
    

# DouDiZhu for and only three
@bot.command(aliases = ['ddz'])
async def doudizhu(message, firstName: discord.Member, secondName: discord.Member, thirdName: discord.Member):
    await message.send('Under dev.')


# Match Ten 
@bot.command(aliases = ['mt'])
async def matchten(message, *name: discord.Member):
    if len(name) > 10:
        await message.send('Maximum 10 players')
        return
    elif len(name) < 3:
        await message.send('Minimum 3 players.')
        return
    else:
        await message.send('Loading...')

    await asyncio.sleep(5)

    deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 69]
    pickplayeremojis = ['🥮', '🍣', '🍱', '🍙', '🍩', '🌮', '🥗', '🥘', '☕️', '🍵']
    pickcardemojis = ['🐱', '🐭', '🐹', '🐰', '🦊', '🐻', '🐼', '🐨', '🐯', '🦁', '🐮', '🐷', '🐸', '🐵', '🐔', '🐧', '🐦', '🐤', '🐣', '🐥', '🦆', '🦅', '🦉', '🐓', '🦃', '🐾', '🐉', '🐲', '🌵', '🎄', '🌲', '🌳', '🌴', '🌱', '🌿', '☘️', '🍀', '🎍', '🎋', '🍃', '🍂', '🍁', '🍄', '🐚', '🌾', '💐', '🌷', '🌹', '🥀', '🌺', '🌸', '🌼', '🌻', '🌕', '🌖', '🌗', '🌘', '🌑', '🌒', '🌓', '🌔', '🌙', '🌎', '🌍', '🌏', '🪐', '💫', '⭐️', '🌟', '✨', '⚡️', '☄️', '💥', '🔥']

    players = []
    playerhand = []
    for player in name:
        players.append(player)
        playerhand.append(list(player.name))
# Clear list to be empty lists
    for hand in playerhand:
        hand.clear()
# Shuffle card and distribute and send
    while deck:
        for hand in playerhand:
            random.shuffle(deck)
            a = random.choice(deck)
            hand.append(a)
            deck.remove(a)
    
    await asyncio.sleep(2)

    for player in players:
        x = players.index(player)
        await player.send('This is your card in hand.\n{}'.format(playerhand[x]))
    
    await message.send('Ready? Game start soon... Match cards sum up to 10 as a pair!')
    await asyncio.sleep(5)
# Loop while no hand is empty
    win = 0
    while win == 0:
        for player in players:
            x = players.index(player)
            getDecline = False
            getSkip = False
            while getDecline == False:
                getDecline = True
                await message.send("{}'s turn. Play your cards one by one.".format(player.mention))
# PLay card that add up to ten
                played = []
                playround = 0
                try:
                    while playround != 2:
                        play = await bot.wait_for('message', timeout = 120.0, check = None)
                        if message.author != bot.user:
                            if play.author.id == player.id:
                                if play.content in playerhand[x]:
                                    played.append(play.content)
                                    playround = playround + 1
                                elif play.content not in playerhand[x]:
                                    await message.send('HO! You think you can fool me. Think again.')
                            elif play.author.id != player.id:
                                await message.send("Nowadays, people are very impatient, aren't they?")
                        else:
                            pass
                except asyncio.TimeoutError:
                    await message.send("You lost your turn, {}.".format(player.mention))
                    getSkip = True
# Check card
                if getSkip == False:
                    if sum(played) == 10:
                        await message.send('TEN!')
                        for i in played:
                            playerhand[x].remove(i)
                    elif 10 in played:
                        if played[0] == 10 and played[1] == 10:
                            await message.send('PAIR TEN!')
                            for i in played:
                                playerhand[x].remove(i)
                        else:
                            await message.send('{}? WTH'.format(sum(played)))
                            getDecline = False
                    else:
                        await message.send('{}? WTH'.format(sum(played)))
                        getDecline = False
            
            await asyncio.sleep(2)
# Pick a player
            if getSkip == False:
                pickplayer = await message.send("Pick a random player, {}.".format(player.mention))
                checkplayeremoji = []
                for i in range(0, len(name)):
                    a = random.choice(pickplayeremojis)
                    checkplayeremoji.append(a)
                    pickplayer.add_reaction(a)
                
                def checkpickplayer(reaction, user):
                    return user == player and str(reaction) in checkplayeremoji
                
                try:
                    reaction, user = await bot.wait_for('reaction_add', timeout = 180.0, check = checkpickplayer)
                    if str(reaction) in checkplayeremoji:
# Pick the player card
                        y = random.choice(players)
                        z = players.index(y)
                        pickcard = await message.send("Pick a card from {}'s deck, {}.".format(y.name, player.mention))
                        checkcardemoji = []
                        for i in range(0, len(playerhand[z])):
                            b = random.choice(pickcardemojis)
                            checkcardemoji.append(b)
                            pickcard.add_reaction(b)
                        
                        def checkpickcard(reaction, user):
                            return user == player and str(reaction) in checkcardemoji

                        reaction, user = await bot.wait_for('reaction_add', timeout = None, check = checkpickcard)
                        if str(reaction) in checkcardemoji:
                            j = random.choice(playerhand[z])
                            playerhand[x].append(j)
                            playerhand[z].remove(j)
                except asyncio.TimeoutError:
                    await message.send("Time's up, next!")

            elif getSkip == True:
                await message.send('You did not play your card just now, so you are skipped. Wait for next round.')

# Finalizing and resend hand and check if empty
            if getDecline == True:
                await player.send('This is your card in hand.\n{}'.format(playerhand[x]))
                await y.send('This is your card in hand.\n{}'.format(playerhand[z]))
                await message.send('{} still have {} left.\n{} still have {} left.'.format(player, len(playerhand[x]), y, len(playerhand[z])))
                
                for i in playerhand:
                    if i:
                        pass
                    elif not i:
                        win = 1
                        winnerhand = playerhand.index(i)
                        winner = players[winnerhand]
                        await message.send('{} is the winner.'.format(winner.mention))

            await asyncio.sleep(4)
# Sending results
    await message.send('Sending in the scoreboard.')
    await asyncio.sleep(2)
    for player in players:
        hand = players.index(player)
        await message.send("{} with {} card(s) left.".format(player.name, len(playerhand[hand])))




# Execute bot 
bot.run(os.environ.get('BOT_SECRET_TOKEN'))
