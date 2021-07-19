import discord
from discord.ext import commands
import random
from random import choices
import asyncio

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

    rules = discord.Embed(title = '{} is looking at the No-Currency-Gamble Rulebook'.format(name), description = 'There are no currency used, this bot uses your luck and unluck. Have fun! 😉', color = 0xf8f8ff)
    rules.set_thumbnail(url = avatar)
    rules.add_field(name = '💰 Coinflip', value = 'For one. [cfs]\nFor two. [cfd <@p1> <@p2>]', inline = False)
    rules.add_field(name = '🤖 Guess The Bot Card', value = 'Versus Bot! [gs <@p1>]', inline = False)
    rules.add_field(name = '🎭 Blackjack', value = '''
Classic! 
[bj <@p1> <@p2> ... unlimited!!!]
```🎴 Hit 🛑 Hold```    
''', inline = False)
    rules.add_field(name = '💎 Texas Poker', value = '''
Stack chips! 
[tp <@p1> <@p2> ... unlimited!!!]
```➕ Raise 🛑 Hold ❌ Fold 💵 ALL IN!```
```
For your information, the scoring table.
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
''', inline = False)
    rules.add_field(name = '🃏 Landlord', value = 'Legendary card game! [ll <@p1> <@p2> <@p3> <@p4> UC', inline = False)
    await message.send(embed = rules)

# Coinflip for one
@bot.command(aliases = ['cfs'])
async def coinflips(message):
    firstName = message.author.name
    
    coin = ['Head', 'Tail', 'It stands!']
    luck = [10, 10, 1]
    result = random.choices(coin, luck, k =1)

    await asyncio.sleep(3)

    result_head = [
'{} flipped a coin and landed on {}. Ouch, the coin hit its head.'.format(firstName, result)
]
    result_tail = [
'{} flipped a coin and landed on {}. Oh no, it broke its tailbone. Call the ambulance! NOW!'.format(firstName, result)
]
    result_stand = [
'Holy shit! {} MADE THE COIN STANDS. You are the LUCKIEST HUMAN alive! For now. Play again, maybe money will start raining in where you live. I mean fake money. HA!'.format(firstName)
]

    if result == ['Head']:
        await message.send(random.choice(result_head))
    elif result == ['Tail']:
        await message.send(random.choice(result_tail))
    elif result == ['It stands!']:
        await message.send(random.choice(result_stand))


# Coinflip for two
@bot.command(aliases = ['cfd'])
async def coinflipd(message, firstName: discord.Member, secondName: discord.Member):
    coin = ['Head', 'Tail', 'It stands!']
    luck = [10, 10, 1]
    result = random.choices(coin, luck, k =1)
    arrow_up = '⬆'
    arrow_down = '⬇'

    result_head = [
'Head it is. Hmm, when did a coin has head. Interesting.'
]
    result_tail = [
'Ha! It is tail.'
]
    result_stand = [
'Well, you never know. {} flipped and made the coin stands. Mind-blowing, eh? {}. You are not, obviously.'.format(firstName, secondName)
]

    await message.send('{} challenged {} to coinflip! The coin is now in the air!'.format(firstName.mention, secondName.mention))
    await asyncio.sleep(3)

    m1 = await message.send('What is your guess, {}? The coin is still spinning.'.format(secondName))

# Add reaction emoji
    await m1.add_reaction(arrow_up)
    await m1.add_reaction(arrow_down)

# Check is it the correct user reacting the message
    def valid(reaction, user):
        return user == secondName and str(reaction) in [arrow_up, arrow_down]

    try:
        reaction, user = await bot.wait_for('reaction_add', timeout = 30.0, check = valid)
        if str(reaction) == arrow_up:
            if result == ['Head']:
                await message.send(random.choice(result_head))
            else:
                await message.send('Too bad. Wrong guess. No luck. Bye bye.')
        elif str(reaction) == arrow_down:
            if result == ['Tail']:
                await message.send(random.choice(result_tail))
            else:
                await message.send('Too bad. Wrong guess. No luck. Bye bye.')
        elif result == ['It stands!']:
            await message.send(random.choice(result_stand))
    except asyncio.TimeoutError:
            await message.send('Interesting, the coin has flipped for 30 seconds in the air and {} did not guess. I wonder why?'.format(secondName))


# Guess the bot card
@bot.command(aliases = ['gs'])
async def guess(message, firstName: discord.Member):
    diamond = '♦️'
    club = '♣️'
    heart = '♥️'
    spade = '♠️'
    card_pattern = ['Diamond', 'Club', 'Heart', 'Spade']
    luck1 = [0.25, 0.25, 0.25, 0.25]

    two = '2️⃣'
    three = '3️⃣'
    four = '4️⃣'
    five = '5️⃣'
    six = '6️⃣'
    seven = '7️⃣'
    eight = '8️⃣'
    nine = '9️⃣'
    ten = '🔟'
    jack = '🤴'
    queen = '👸'
    king = '👑'
    ace = '🅰️'
    card_no = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    luck2 = [0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13]

    result_card_pattern = random.choices(card_pattern, luck1, k = 1)
    result_card_no = random.choices(card_no, luck2, k = 1)

    m1 = await message.send('Guess my card pattern, human. Or shall I call you by your name, {}. Two chances.'.format(firstName))
    await m1.add_reaction(diamond)
    await m1.add_reaction(club)
    await m1.add_reaction(heart)
    await m1.add_reaction(spade)

    def valid1(reaction, user):
        return user == firstName and str(reaction) in [diamond, club, heart, spade]
    
    try:
        chance1 = 0
        ans1 = False
        while chance1 < 2 and ans1 == False:
            reaction, user = await bot.wait_for('reaction_add', timeout = 15.0, check = valid1)
            if str(reaction) == diamond:
                if result_card_pattern == ['Diamond']:
                    ans1 = True
                    await message.send('Well, well, well, guessed. Now, try this.')
                else:
                    await message.send('Too bad so sad, human.')
            elif str(reaction) == club:
                if result_card_pattern == ['Club']:
                    ans1 = True
                    await message.send('Well, well, well, guessed. Now, try this.')
                else:
                    await message.send('Too bad so sad, human.')
            elif str(reaction) == heart:
                if result_card_pattern == ['Heart']:
                    ans1 = True
                    await message.send('Well, well, well, guessed. Now, try this.')
                else:
                    await message.send('Too bad so sad, human.')
            elif str(reaction) == spade:
                if result_card_pattern == ['Spade']:
                    ans1 = True
                    await message.send('Well, well, well, guessed. Now, try this.')
                else:
                    await message.send('Too bad so sad, human.')
            chance1 = chance1 + 1
    except asyncio.TimeoutError:
        await message.send('Hellooooo? Anybody thereeee? No? All your luck is mine now 👀. Do not leave yet!')

    m2 = await message.send('Guess my card number now. Prove to me you are worthy human, {}. Four chances.'.format(firstName))
    await m2.add_reaction(two)
    await m2.add_reaction(three)
    await m2.add_reaction(four)
    await m2.add_reaction(five)
    await m2.add_reaction(six)
    await m2.add_reaction(seven)
    await m2.add_reaction(eight)
    await m2.add_reaction(nine)
    await m2.add_reaction(ten)
    await m2.add_reaction(jack)
    await m2.add_reaction(queen)
    await m2.add_reaction(king)
    await m2.add_reaction(ace)

    def valid2(reaction, user):
        return user == firstName and str(reaction) in [two, three, four, five, six, seven, eight, nine, ten, jack, queen, king, ace]

    try:
        chance2 = 0
        ans2 = False
        while chance2 < 4 and ans2 == False:
            reaction, user = await bot.wait_for('reaction_add', timeout = 20.0, check = valid2)
            if str(reaction) == two:
                if result_card_no == ['2']:
                    ans2 = True
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == three:
                if result_card_no == ['3']:
                    ans2 = True
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == four:
                if result_card_no == ['4']:
                    ans2 = True
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == five:
                if result_card_no == ['5']:
                    ans2 = True
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == six:
                if result_card_no == ['6']:
                    ans2 = True
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == seven:
                if result_card_no == ['7']:
                    ans2 = True
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == eight:
                if result_card_no == ['8']:
                    ans2 = True
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == nine:
                if result_card_no == ['9']:
                    ans2 = True
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == ten:
                if result_card_no == ['10']:
                    ans2 = True
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == jack:
                if result_card_no == ['J']:
                    ans2 = True
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == queen:
                if result_card_no == ['Q']:
                    ans2 = True
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == king:
                if result_card_no == ['K']:
                    ans2 = True
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == ace:
                if result_card_no == ['A']:
                    ans2 = True
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            chance2 = chance2 + 1
            if chance2 == 4:
                await message.send('The card is {} {}'.format(result_card_pattern, result_card_no))
    except asyncio.TimeoutError:
        await message.send('You are unworthy, human! The card is {} {}'.format(result_card_pattern, result_card_no))


# Blackjack for two
@bot.command(aliases = ['bj'])
async def blackjack(message, *name: discord.Member):
    hit = '🎴'
    holdc = '🛑'
    
    deck = [11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10]
    random.shuffle(deck)

# Each player round
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
    checkhandlist = []
    for player in players:
        hand = []
        for i in range(0, 2):
            a = random.choice(deck)
            deck.remove(a)
            hand.append(a)
        handlist.append(player.name)
        for i in hand:
            handlist.append(i)
            checkhandlist.append(i)
        await player.send('Here is your card in hand.\n{}'.format(hand))
    
    await asyncio.sleep(5)
    await message.send('Cards have been distributed! 😏 Shuffling...')
    await asyncio.sleep(2)

# Round Loop
    pool = 1

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

        holdc = []
        for player in players:
            holdc.append(False)

        while all(holdc) == False:
            for player in players:
                x = players.index(player)
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
                                await message.send('Bruh, you do not have any fame left. Consider giving your clothes? HOLD it please!')
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
                            await message.send('{} folded. Sad but no regrets eh?'.format(player.mention))
                        elif str(reaction) == all_in:
                            if fame[x] == 0:
                                await message.send("I know you are rich, but just hold, will you?")
                            else:
                                holdc[x] = True
                                fame[x] = fame[x] - 10
                                famepool = famepool + 10
                                await message.send('{} ALL INNNNNN!!! 🤩'.format(player.mention))
                    except asyncio.TimeoutError:
                        holdc[x] = True
                        await message.send('{} did not respond! Out you go 👺.'.format(player))
                elif foldc[x] == True:
                    holdc[x] = True
                    await message.send('You folded. So just be patient, Mr/Mrs {}.'.format(player.mention))
                    
        pool = pool + 1 

    await message.send('Totalling... {} in total for the winner 🤑.'.format(famepool))
    await asyncio.sleep(3)
    await message.send("Player's card. \n{}".format(handlist))
    await message.send("Dealer's card. \n{}".format(dealer_hand))

    




bot.run('ODU5MDM5NzkzOTQ2NDI3Mzky.YNm5Jw.lCDZaXLJezsle_grbeDb_JtOLa0')