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
    rules.add_field(name = '🤨 Liar Guess', value = 'Mind game with one! [lg <@p1> <@p2>]', inline = False)
    rules.add_field(name = '🎭 Blackjack', value = 'Classic! [bj <@p1> <@p2>]', inline = False)
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
        while chance1 < 2:
            reaction, user = await bot.wait_for('reaction_add', timeout = 15.0, check = valid1)
            if str(reaction) == diamond:
                if result_card_pattern == ['Diamond']:
                    await message.send('Well, well, well, guessed. Now, try this.')
                else:
                    await message.send('Too bad so sad, human.')
            elif str(reaction) == club:
                if result_card_pattern == ['Club']:
                    await message.send('Well, well, well, guessed. Now, try this.')
                else:
                    await message.send('Too bad so sad, human.')
            elif str(reaction) == heart:
                if result_card_pattern == ['Heart']:
                    await message.send('Well, well, well, guessed. Now, try this.')
                else:
                    await message.send('Too bad so sad, human.')
            elif str(reaction) == spade:
                if result_card_pattern == ['Spade']:
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
        while chance2 < 4:
            reaction, user = await bot.wait_for('reaction_add', timeout = 20.0, check = valid2)
            if str(reaction) == two:
                if result_card_no == ['2']:
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == three:
                if result_card_no == ['3']:
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == four:
                if result_card_no == ['4']:
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == five:
                if result_card_no == ['5']:
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == six:
                if result_card_no == ['6']:
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == seven:
                if result_card_no == ['7']:
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == eight:
                if result_card_no == ['8']:
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == nine:
                if result_card_no == ['9']:
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == ten:
                if result_card_no == ['10']:
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == jack:
                if result_card_no == ['J']:
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == queen:
                if result_card_no == ['Q']:
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == king:
                if result_card_no == ['K']:
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            elif str(reaction) == ace:
                if result_card_no == ['A']:
                    await message.send('MY MANNN, {}!! YOU HAVE MY RESPECT!!'.format(firstName))
                else:
                    await message.send('Try again, when you feel you are worthy enough to challenge me.')
            chance2 = chance2 + 1
            if chance2 == 4:
                await message.send('The card is {} {}'.format(result_card_pattern, result_card_no))
            else:
                pass
    except asyncio.TimeoutError:
        await message.send('You are unworthy, human! The card is {} {}'.format(result_card_pattern, result_card_no))


# Liar Guess for three
@bot.command(aliases = ['lg'])
async def lguess(message, firstName: discord.Member, secondName: discord.Member, thirdName: discord.Member):
    add = '➕'
    hold = '🛑'
    fold = '❌'
    all_in = '💲'

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
    luck2 = [0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13]

    result_card_pattern1 = random.choices(card_pattern, luck1, k = 1)
    result_card_no1 = random.choices(card_no, luck2, k = 1)
    result_card_pattern2 = random.choices(card_pattern, luck1, k = 1)
    result_card_no2 = random.choices(card_no, luck2, k = 1)
    result_card_pattern3 = random.choices(card_pattern, luck1, k = 1)
    result_card_no3 = random.choices(card_no, luck2, k = 1)

    await message.send('Prepare for mind game between {} and {}. Who is sus 👻?'.format(firstName.mention, secondName.mention))
    await asyncio.sleep(2)

    await firstName.send('{} card is {} {}.\n{} card is {} {}.'.format(secondName, result_card_pattern2, result_card_no2, thirdName, result_card_pattern3, result_card_no3))
    await secondName.send('{} card is {} {}.\n{} card is {} {}.'.format(firstName, result_card_pattern1, result_card_no1, thirdName, result_card_pattern3, result_card_no3))
    await thirdName.send('{} card is {} {}.\n{} card is {} {}.'.format(firstName, result_card_pattern1, result_card_no1, secondName, result_card_pattern2, result_card_no2))
    
    await asyncio.sleep(2)
    await message.send('''
Cards have been sent. Now, who has the largest number plus pattern 🤔?
Each person has 10 fame.
''')

# Validation
    def valid1(user, reaction):
            return user == firstName and str(reaction) in [add, hold, fold, all_in]
    
    def valid2(user, reaction):
            return user == secondName and str(reaction) in [add, hold, fold, all_in]

    def valid3(user, reaction):
            return user == thirdName and str(reaction) in [add, hold, fold, all_in]
    
    while hold1 == False and hold2 == False and hold3 == False:
# First player
        if fold1 != True:
            m = await message.send("{}'s turn. {} fame left.".format(firstName, fame1))
            await m.add_reaction(add)
            await m.add_reaction(hold)
            await m.add_reaction(fold)
            await m.add_reaction(all_in)

            try:
                reaction, user = await bot.wait_for('reaction_add', timeout = 30.0, check = valid1)
                if str(reaction) == add:
                    famepool = famepool + 1
                    fame1 = fame1 - 1
                    await message.send('{} added 1 fame to the fame pool 😬!'.format(firstName))
                elif str(reaction) == hold:
                    hold1 = True
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
        if fold2 != True:
            m = await message.send("{}'s turn".format(secondName))
            await m.add_reaction(add)
            await m.add_reaction(hold)
            await m.add_reaction(fold)
            await m.add_reaction(all_in)

            try:
                reaction, user = await bot.wait_for('reaction_add', timeout = 30.0, check = valid2)
                if str(reaction) == add:
                    famepool = famepool + 1
                    fame2 = fame2 - 1
                    await message.send('{} added 1 fame to the fame pool 😬!'.format(secondName))
                elif str(reaction) == hold:
                    hold2 = True
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
        if fold3 != True:
            m = await message.send("{}'s turn".format(thirdName))
            await m.add_reaction(add)
            await m.add_reaction(hold)
            await m.add_reaction(fold)
            await m.add_reaction(all_in)

            try:
                reaction, user = await bot.wait_for('reaction_add', timeout = 30.0, check = valid3)
                if str(reaction) == add:
                    famepool = famepool + 1
                    fame3 = fame3 - 1
                    await message.send('{} added 1 fame to the fame pool 😬!'.format(thirdName))
                elif str(reaction) == hold:
                    hold3 = True
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
    await message.send("{}'s card is {} {}.\n{}'s card is {} {}.\n{}'s card is {} {}.".format(firstName, result_card_pattern1, result_card_no1, secondName, result_card_pattern2, result_card_no2, thirdName, result_card_pattern3, result_card_no3))
    await asyncio.sleep(2)
    await message.send('So, the winner is ...🥁')
    await asyncio.sleep(2)
    await message.send('You see it yourself 🤪.')





bot.run('ODU5MDM5NzkzOTQ2NDI3Mzky.YNm5Jw.lCDZaXLJezsle_grbeDb_JtOLa0')