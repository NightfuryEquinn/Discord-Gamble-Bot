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
    rules.add_field(name = '🤨 Liar Guess', value = '''
Mind game! 
For three. [lg <@p1> <@p2> <@p3>]
```➕ Raise 🛑 Hold ❌ Fold 💵 ALL IN!```
''', inline = False)
    rules.add_field(name = '🎭 Blackjack', value = '''
Classic! 
For two. [bj2 <@p1> <@p2>]
For three. [bj3 <@p1> <@p2> <@p3>]
```🎴 Hit 🛑 Hold```    
    ''', inline = False)
    rules.add_field(name = '💎 Texas Poker', value = 'Stack chips! [tp <@p1> <@p2> <@p3>] UC', inline = False)
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


# Liar Guess for three
@bot.command(aliases = ['lg'])
async def lguess(message, firstName: discord.Member, secondName: discord.Member, thirdName: discord.Member):
    add = '➕'
    hold = '🛑'
    fold = '❌'
    all_in = '💵'

    famepool = 3
    fame1 = 10
    fame2 = 10
    fame3 = 10

    fold1 = False
    fold2 = False
    fold3 = False

    hold1 = False
    hold2 = False
    hold3 = False
    
    card_pattern = ['Diamond', 'Club', 'Heart', 'Spade']
    luck1 = [0.25, 0.25, 0.25, 0.25]

    card_no = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    luck2 = [0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.07, 0.07, 0.07, 0.07]

    result_card_pattern1 = random.choices(card_pattern, luck1, k = 1)
    result_card_no1 = random.choices(card_no, luck2, k = 1)
    result_card_pattern2 = random.choices(card_pattern, luck1, k = 1)
    result_card_no2 = random.choices(card_no, luck2, k = 1)
    result_card_pattern3 = random.choices(card_pattern, luck1, k = 1)
    result_card_no3 = random.choices(card_no, luck2, k = 1)

    await message.send('Prepare for mind game between {}, {} and {}. Who is sus 👻?'.format(firstName.mention, secondName.mention, thirdName.mention))
    await asyncio.sleep(2)

    await firstName.send('{} card is {} {}.\n{} card is {} {}.'.format(secondName, result_card_pattern2, result_card_no2, thirdName, result_card_pattern3, result_card_no3))
    await secondName.send('{} card is {} {}.\n{} card is {} {}.'.format(firstName, result_card_pattern1, result_card_no1, thirdName, result_card_pattern3, result_card_no3))
    await thirdName.send('{} card is {} {}.\n{} card is {} {}.'.format(firstName, result_card_pattern1, result_card_no1, secondName, result_card_pattern2, result_card_no2))
    
    await asyncio.sleep(2)
    await message.send('''
Cards have been sent. Now, who has the largest number plus pattern 🤔?
Each person has 10 fame.
''')

    while hold1 == False or hold2 == False or hold3 == False:
# First player
        if fold1 == False:
            m = await message.send("{}'s turn. {} fame left.".format(firstName.mention, fame1))
            await m.add_reaction(add)
            await m.add_reaction(hold)
            await m.add_reaction(fold)
            await m.add_reaction(all_in)

            def valid1(reaction, user):
                return user == firstName and str(reaction) in [add, hold, fold, all_in]

            try:
                reaction, user = await bot.wait_for('reaction_add', timeout = 60.0, check = valid1)
                if str(reaction) == add:
                    if fame1 == 0:
                        hold1 = True
                        fold1 = True
                    else:
                        famepool = famepool + 1
                        fame1 = fame1 - 1
                        await message.send('{} added 1 fame to the fame pool 😬!'.format(firstName))
                elif str(reaction) == hold:
                    hold1 = True
                    fold1 = True
                    await message.send('{} holded 🥺!'.format(firstName))
                elif str(reaction) == fold:
                    hold1 = True
                    fold1 = True
                    await message.send('{} is scared and gave up 💩.'.format(firstName))
                elif str(reaction) == all_in:
                    hold1 = True
                    fold1 = True
                    famepool = famepool + fame1
                    await message.send('OOOOOHHH! {} made a bald move! I mean bold 😲.'.format(firstName))
            except asyncio.TimeoutError:
                hold1 = True
                fold1 = True
                await message.send('{} did not answer. Forfeited 😤!'.format(firstName))

# Second player
        if fold2 == False:
            m = await message.send("{}'s turn. {} fame left.".format(secondName.mention, fame2))
            await m.add_reaction(add)
            await m.add_reaction(hold)
            await m.add_reaction(fold)
            await m.add_reaction(all_in)

            def valid2(reaction, user):
                return user == secondName and str(reaction) in [add, hold, fold, all_in]

            try:
                reaction, user = await bot.wait_for('reaction_add', timeout = 60.0, check = valid2)
                if str(reaction) == add:
                    if fame2 == 0:
                        hold2 = True
                        fold2 = True
                    else:
                        famepool = famepool + 1
                        fame2 = fame2 - 1
                        await message.send('{} added 1 fame to the fame pool 😬!'.format(secondName))
                elif str(reaction) == hold:
                    hold2 = True
                    fold2 = True
                    await message.send('{} holded 🥺!'.format(secondName))
                elif str(reaction) == fold:
                    hold2 = True
                    fold2 = True
                    await message.send('{} is scared and gave up 💩.'.format(secondName))
                elif str(reaction) == all_in:
                    hold2 = True
                    fold2 = True
                    famepool = famepool + fame2
                    await message.send('OOOOOHHH! {} made a bald move! I mean bold 😲.'.format(secondName))
            except asyncio.TimeoutError:
                hold2 = True
                fold2 = True
                await message.send('{} did not answer. Forfeited 😤!'.format(secondName))

# Third player
        if fold3 == False:
            m = await message.send("{}'s turn. {} fame left.".format(thirdName.mention, fame3))
            await m.add_reaction(add)
            await m.add_reaction(hold)
            await m.add_reaction(fold)
            await m.add_reaction(all_in)

            def valid3(reaction, user):
                return user == thirdName and str(reaction) in [add, hold, fold, all_in]

            try:
                reaction, user = await bot.wait_for('reaction_add', timeout = 60.0, check = valid3)
                if str(reaction) == add:
                    if fame3 == 0:
                        hold3 = True
                        fold3 = True
                    else:
                        famepool = famepool + 1
                        fame3 = fame3 - 1
                        await message.send('{} added 1 fame to the fame pool 😬!'.format(thirdName))
                elif str(reaction) == hold:
                    hold3 = True
                    fold3 = True
                    await message.send('{} holded 🥺!'.format(thirdName))
                elif str(reaction) == fold:
                    hold3 = True
                    fold3 = True
                    await message.send('{} is scared and gave up 💩.'.format(thirdName))
                elif str(reaction) == all_in:
                    hold3 = True
                    fold3 = True
                    famepool = famepool + fame3
                    await message.send('OOOOOHHH! {} made a bald move! I mean bold 😲.'.format(thirdName))
            except asyncio.TimeoutError:
                hold3 = True
                fold3 = True
                await message.send('{} did not answer. Forfeited 😤!'.format(thirdName))

    await message.send('Getting result... Please standby... 🤓')
    await asyncio.sleep(2)
    await message.send("{}'s card is {} {}.\n{}'s card is {} {}.\n{}'s card is {} {}.".format(firstName.mention, result_card_pattern1, result_card_no1, secondName.mention, result_card_pattern2, result_card_no2, thirdName.mention, result_card_pattern3, result_card_no3))
    await asyncio.sleep(2)
    await message.send('So, the winner who have {} fame is ...🥁'.format(famepool))
    await asyncio.sleep(4)

# Result Logic
    'Diamond 2' < 'Diamond 3' < 'Diamond 4' < 'Diamond 5' < 'Diamond 6' < 'Diamond 7' < 'Diamond 8' < 'Diamond 9' < 'Diamond 10' < 'Diamond J' < 'Diamond Q' < 'Diamond K' < 'Diamond A' < 'Club 2' < 'Club 3' < 'Club 4' < 'Club 5' < 'Club 6' < 'Club 7' < 'Club 8' < 'Club 9' < 'Club 10' < 'Club J' < 'Club Q' < 'Club K' < 'Club A' < 'Heart 2' < 'Heart 3' < 'Heart 4' < 'Heart 5' < 'Heart 6' < 'Heart 7' < 'Heart 8' < 'Heart 9' < 'Heart 10' < 'Heart J' < 'Heart Q' < 'Heart K' < 'Heart A' < 'Spade 2' < 'Spade 3' < 'Spade 4' < 'Spade 5' < 'Spade 6' < 'Spade 7' < 'Spade 8' < 'Spade 9' < 'Spade 10' < 'Spade J' < 'Spade Q' < 'Spade K' < 'Spade A'
    a = (result_card_pattern1[0] + ' ' + (result_card_no1[0]))
    b = (result_card_pattern2[0] + ' ' + (result_card_no2[0]))
    c = (result_card_pattern3[0] + ' ' + (result_card_no3[0]))
    if a < b < c:
        await message.send('{} 🤯!'.format(thirdName.mention))
    elif b < a < c:
        await message.send('{} 🤯!'.format(thirdName.mention))
    elif a < c < b:
        await message.send('{} 🤗!'.format(secondName.mention))
    elif c < a < b:
        await message.send('{} 🤗!'.format(secondName.mention))
    elif b < c < a:
        await message.send('{} 😱!'.format(firstName.mention))
    elif c < b < a:
        await message.send('{} 😱!'.format(firstName.mention))
    else:
        await message.send('Hmm, seems that there is duplication. Well, nobody cares 😴!')


# Blackjack for two
@bot.command(aliases = ['bj2'])
async def blackjack2(message, firstName: discord.Member, secondName: discord.Member):
    hit = '🎴'
    hold = '🛑'

    hold1 = False
    hold2 = False
    
    deck = [11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    random.shuffle(deck)

# Starting round
    hand1 = []
    hand2 = []

    all_hand = [hand1, hand2]
    for i in range(0, 2):
        for hands in all_hand:
            a = random.choice(deck)
            deck.remove(a)
            hands.append(a)
        
    await firstName.send('Here is your card in hand.\n```{}```'.format(hand1))
    await secondName.send('Here is your card in hand.\n```{}```'.format(hand2))
    await asyncio.sleep(3)
    await message.send('Look around. Although you cannot see 😶. Be prepared.')
    await asyncio.sleep(2)

# First player
    while hold1 == False:
        m = await message.send("{}'s turn.".format(firstName.mention))
        await m.add_reaction(hit)
        await m.add_reaction(hold)

        def valid1(reaction, user):
            return user == firstName and str(reaction) in [hit, hold]

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 45.0, check = valid1)
            if str(reaction) == hit:
                card = random.choice(deck)
                deck.remove(card)
                hand1.append(card)
                await firstName.send("Here is your card in hand.\n```{}```".format(hand1))
            elif str(reaction) == hold:
                hold1 = True
                await message.send('{} holded for dear life 🥶!'.format(firstName))
        except asyncio.TimeoutError:
            await message.send("Why da heck you are not reacting 🤬?!")

# Second player
    while hold2 == False:
        m = await message.send("{}'s turn.".format(secondName.mention))
        await m.add_reaction(hit)
        await m.add_reaction(hold)

        def valid2(reaction, user):
            return user == secondName and str(reaction) in [hit, hold]

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 45.0, check = valid2)
            if str(reaction) == hit:
                card = random.choice(deck)
                deck.remove(card)
                hand2.append(card)
                await secondName.send("Here is your card in hand.\n```{}```".format(hand2))
            elif str(reaction) == hold:
                hold2 = True
                await message.send('{} holded for dear life 🥶!'.format(secondName))
        except asyncio.TimeoutError:
            await message.send("Why da heck you are not reacting 🤬?!")

# Result first player
    if 11 in hand1:
        if sum(hand1) < 21:
            for n, i in enumerate(hand1):
                if i == 11:
                    hand1[n] = 1
                    x = sum(hand1)
        elif sum(hand1) >= 21:
            x = sum(hand1)
    elif 11 not in hand1:
        x = sum(hand1)
    await message.send("{}'s card total is {}.".format(firstName.mention, x))

    if hand1[0] == 11 and hand1[1] == 11:
        await message.send("{} got DOUBLE ACES!!! 😳".format(firstName.mention))

    if len(hand1) == 5:
        if sum(hand1) <= 21:
            await message.send("{} managed to get FIVE IN A ROW!!! 🙀".format(firstName.mention))

# Result second player
    if 11 in hand2:
        if sum(hand2) < 21:
            for n, i in enumerate(hand2):
                if i == 11:
                    hand2[n] = 1
                    x = sum(hand2)
        elif sum(hand2) >= 21:
            x = sum(hand2)
    elif 11 not in hand2:
        x = sum(hand2)
    await message.send("{}'s card total is {}.".format(secondName.mention, x))

    if hand2[0] == 11 and hand2[1] == 11:
        await message.send("{} got DOUBLE ACES!!! 😳".format(secondName.mention))

    if len(hand2) == 5:
        if sum(hand2) <= 21:
            await message.send("{} managed to get FIVE IN A ROW!!! 🙀".format(secondName.mention))


# Blackjack for three
@bot.command(aliases = ['bj3'])
async def blackjack3(message, firstName: discord.Member, secondName: discord.Member, thirdName: discord.Member):
    hit = '🎴'
    hold = '🛑'

    hold1 = False
    hold2 = False
    hold3 = False
    
    deck = [11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    random.shuffle(deck)

# Starting round
    hand1 = []
    hand2 = []
    hand3 = []

    all_hand = [hand1, hand2, hand3]
    for i in range(0, 2):
        for hands in all_hand:
            a = random.choice(deck)
            deck.remove(a)
            hands.append(a)
        
    await firstName.send('Here is your card in hand.\n```{}```'.format(hand1))
    await secondName.send('Here is your card in hand.\n```{}```'.format(hand2))
    await thirdName.send('Here is your card in hand.\n```{}```'.format(hand3))
    await asyncio.sleep(3)
    await message.send('Look around. Although you cannot see 😶. Be prepared.')
    await asyncio.sleep(2)

# First player
    while hold1 == False:
        m = await message.send("{}'s turn.".format(firstName.mention))
        await m.add_reaction(hit)
        await m.add_reaction(hold)

        def valid1(reaction, user):
            return user == firstName and str(reaction) in [hit, hold]

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 45.0, check = valid1)
            if str(reaction) == hit:
                card = random.choice(deck)
                deck.remove(card)
                hand1.append(card)
                await firstName.send("Here is your card in hand.\n```{}```".format(hand1))
            elif str(reaction) == hold:
                hold1 = True
                await message.send('{} holded for dear life 🥶!'.format(firstName))
        except asyncio.TimeoutError:
            await message.send("Why da heck you are not reacting 🤬?!")

# Second player
    while hold2 == False:
        m = await message.send("{}'s turn.".format(secondName.mention))
        await m.add_reaction(hit)
        await m.add_reaction(hold)

        def valid2(reaction, user):
            return user == secondName and str(reaction) in [hit, hold]

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 45.0, check = valid2)
            if str(reaction) == hit:
                card = random.choice(deck)
                deck.remove(card)
                hand2.append(card)
                await secondName.send("Here is your card in hand.\n```{}```".format(hand2))
            elif str(reaction) == hold:
                hold2 = True
                await message.send('{} holded for dear life 🥶!'.format(secondName))
        except asyncio.TimeoutError:
            await message.send("Why da heck you are not reacting 🤬?!")

# Third player
    while hold3 == False:
        m = await message.send("{}'s turn.".format(thirdName.mention))
        await m.add_reaction(hit)
        await m.add_reaction(hold)

        def valid3(reaction, user):
            return user == thirdName and str(reaction) in [hit, hold]

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 45.0, check = valid3)
            if str(reaction) == hit:
                card = random.choice(deck)
                deck.remove(card)
                hand3.append(card)
                await thirdName.send("Here is your card in hand.\n```{}```".format(hand3))
            elif str(reaction) == hold:
                hold3 = True
                await message.send('{} holded for dear life 🥶!'.format(thirdName))
        except asyncio.TimeoutError:
            await message.send("Why da heck you are not reacting 🤬?!")

# Result first player
    if 11 in hand1:
        if sum(hand1) < 21:
            for n, i in enumerate(hand1):
                if i == 11:
                    hand1[n] = 1
                    x = sum(hand1)
        elif sum(hand1) >= 21:
            x = sum(hand1)
    elif 11 not in hand1:
        x = sum(hand1)
    await message.send("{}'s card total is {}.".format(firstName.mention, x))

    if hand1[0] == 11 and hand1[1] == 11:
        await message.send("{} got DOUBLE ACES!!! 😳".format(firstName.mention))

    if len(hand1) == 5:
        if sum(hand1) <= 21:
            await message.send("{} managed to get FIVE IN A ROW!!! 🙀".format(firstName.mention))

# Result second player
    if 11 in hand2:
        if sum(hand2) < 21:
            for n, i in enumerate(hand2):
                if i == 11:
                    hand2[n] = 1
                    x = sum(hand2)
        elif sum(hand2) >= 21:
            x = sum(hand2)
    elif 11 not in hand2:
        x = sum(hand2)
    await message.send("{}'s card total is {}.".format(secondName.mention, x))

    if hand2[0] == 11 and hand2[1] == 11:
        await message.send("{} got DOUBLE ACES!!! 😳".format(secondName.mention))

    if len(hand2) == 5:
        if sum(hand2) <= 21:
            await message.send("{} managed to get FIVE IN A ROW!!! 🙀".format(secondName.mention))

# Result third player
    if 11 in hand3:
        if sum(hand3) < 21:
            for n, i in enumerate(hand3):
                if i == 11:
                    hand3[n] = 1
                    x = sum(hand3)
        elif sum(hand3) >= 21:
            x = sum(hand3)
    elif 11 not in hand3:
        x = sum(hand3)
    await message.send("{}'s card total is {}.".format(thirdName.mention, x))

    if hand3[0] == 11 and hand3[1] == 11:
        await message.send("{} got DOUBLE ACES!!! 😳".format(thirdName.mention))

    if len(hand3) == 5:
        if sum(hand3) <= 21:
            await message.send("{} managed to get FIVE IN A ROW!!! 🙀".format(thirdName.mention))





bot.run('ODU5MDM5NzkzOTQ2NDI3Mzky.YNm5Jw.lCDZaXLJezsle_grbeDb_JtOLa0')