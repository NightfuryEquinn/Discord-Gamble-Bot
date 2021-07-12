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
    rules.add_field(name = '💰 Coinflip', value = 'coinflips [cfs] for one\ncoinflipd [cfd <@p1> <@p2>] for two', inline = False)
    rules.add_field(name = '🤨 Guess', value = 'guesss [us <@p1>] for one\nguessd [ud <@p1> <@p2>] for two', inline = False)
    rules.add_field(name = '🎭 Blackjack', value = 'blackjack [bj <@p1> <@p2>]', inline = False)
    rules.add_field(name = '💎 Texas Poker', value = 'Under construction', inline = False)
    rules.add_field(name = '🃏 Landlord', value = 'Under construction', inline = False)
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


# Guess the card for one
@bot.command(aliases = ['us'])
async def guesss(message, firstName: discord.Member):
    diamond = '♦️'
    club = '♣️'
    heart = '♥️'
    spade = '♠️'
    card_pattern = ['Diamond', 'Club', 'Heart', 'Spade']
    luck1 = [1, 1, 1, 1]

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
    luck2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

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


# Guess the card for two
@bot.command(aliases = ['ud'])
async def guessd(message, firstName: discord.Member, secondName: discord.Member):
    diamond = '♦️'
    club = '♣️'
    heart = '♥️'
    spade = '♠️'
    card_pattern = ['Diamond', 'Club', 'Heart', 'Spade']
    luck1 = [1, 1, 1, 1]

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
    luck2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    result_card_pattern1 = random.choices(card_pattern, luck1, k = 1)
    result_card_no1 = random.choices(card_no, luck2, k = 1)
    result_card_pattern2 = random.choices(card_pattern, luck1, k = 1)
    result_card_no2 = random.choices(card_no, luck2, k = 1)

    temp1 = False
    temp2 = False
    temp3 = False
    temp4 = False

    await message.send('Prepare for mind battle between {} and {}. Guess. The. Card.'.format(firstName.mention, secondName.mention))
    await asyncio.sleep(2)
    await firstName.send('Your card is {} {}.'.format(result_card_pattern1, result_card_no1))
    await secondName.send('Your card is {} {}.'.format(result_card_pattern2, result_card_no2))
    await asyncio.sleep(5)

    def valid1_1(user, reaction):
        return user == firstName and str(reaction) in [diamond, club, heart, spade]
    
    def valid2_1(user, reaction):
        return user == secondName and str(reaction) in [diamond, club, heart, spade]

    def valid1_2(reaction, user):
        return user == firstName and str(reaction) in [two, three, four, five, six, seven, eight, nine, ten, jack, queen, king, ace]

    def valid2_2(reaction, user):
        return user == secondName and str(reaction) in [two, three, four, five, six, seven, eight, nine, ten, jack, queen, king, ace]

# First name guess card pattern
    m1 = await message.send('Round One: Guess the pattern. Two chances! {} first.'.format(firstName.mention))
    await m1.add_reaction(diamond)
    await m1.add_reaction(club)
    await m1.add_reaction(heart)
    await m1.add_reaction(spade)

    try:
        chance1 = 0
        while chance1 < 2:
            reaction, user = await bot.wait_for('reaction_add', timeout = 15.0, check = valid1_1)
            if str(reaction) == diamond:
                if result_card_pattern2 == ['Diamond']:
                    temp1 = True
            elif str(reaction) == club:
                if result_card_pattern2 == ['Club']:
                    temp1 = True
            elif str(reaction) == heart:
                if result_card_pattern2 == ['Heart']:
                    temp1 = True
            elif str(reaction) == spade:
                if result_card_pattern2 == ['Spade']:
                    temp1 = True
            chance1 = chance1 + 1
    except asyncio.TimeoutError:
        await message.send('Hmm, someone is afraid 😏.')

# Second name guess card pattern
    m2 = await message.send('Your turn, {}.'.format(secondName.mention))
    await m2.add_reaction(diamond)
    await m2.add_reaction(club)
    await m2.add_reaction(heart)
    await m2.add_reaction(spade)

    try:
        chance2 = 0
        while chance2 < 2:
            reaction, user = await bot.wait_for('reaction_add', timeout = 15.0, check = valid2_1)
            if str(reaction) == diamond:
                if result_card_pattern1 == ['Diamond']:
                    temp2 = True
            elif str(reaction) == club:
                if result_card_pattern1 == ['Club']:
                    temp2 = True
            elif str(reaction) == heart:
                if result_card_pattern1 == ['Heart']:
                    temp2 = True
            elif str(reaction) == spade:
                if result_card_pattern1 == ['Spade']:
                    temp2 = True
            chance2 = chance2 + 1
    except asyncio.TimeoutError:
        await message.send('Hmm, someone is afraid also 😏.')

# First name guess card number
    m3 = await message.send('Round Two! Guess the card number. Four! Chances. {} first.'.format(firstName.mention))
    await m3.add_reaction(two)
    await m3.add_reaction(three)
    await m3.add_reaction(four)
    await m3.add_reaction(five)
    await m3.add_reaction(six)
    await m3.add_reaction(seven)
    await m3.add_reaction(eight)
    await m3.add_reaction(nine)
    await m3.add_reaction(ten)
    await m3.add_reaction(jack)
    await m3.add_reaction(queen)
    await m3.add_reaction(king)
    await m3.add_reaction(ace)

    try:
        chance3 = 0
        while chance3 < 4:
            reaction, user = await bot.wait_for('reaction_add', timeout = 20.0, check = valid1_2)
            if str(reaction) == two:
                if result_card_no2 == ['2']:
                    temp3 = True
            elif str(reaction) == three:
                if result_card_no2 == ['3']:
                    temp3 = True
            elif str(reaction) == four:
                if result_card_no2 == ['4']:
                    temp3 = True
            elif str(reaction) == five:
                if result_card_no2 == ['5']:
                    temp3 = True
            elif str(reaction) == six:
                if result_card_no2 == ['6']:
                    temp3 = True
            elif str(reaction) == seven:
                if result_card_no2 == ['7']:
                    temp3 = True
            elif str(reaction) == eight:
                if result_card_no2 == ['8']:
                    temp3 = True
            elif str(reaction) == nine:
                if result_card_no2 == ['9']:
                    temp3 = True
            elif str(reaction) == ten:
                if result_card_no2 == ['10']:
                    temp3 = True
            elif str(reaction) == jack:
                if result_card_no2 == ['J']:
                    temp3 = True
            elif str(reaction) == queen:
                if result_card_no2 == ['Q']:
                    temp3 = True
            elif str(reaction) == king:
                if result_card_no2 == ['K']:
                    temp3 = True
            elif str(reaction) == ace:
                if result_card_no2 == ['A']:
                    temp3 = True
            chance3 = chance3 + 1
    except asyncio.TimeoutError:
        await message.send('Are you playing or not? 🙄')

# Second name guess card number
    m4 = await message.send('{}, now is your turn.'.format(secondName.mention))
    await m4.add_reaction(two)
    await m4.add_reaction(three)
    await m4.add_reaction(four)
    await m4.add_reaction(five)
    await m4.add_reaction(six)
    await m4.add_reaction(seven)
    await m4.add_reaction(eight)
    await m4.add_reaction(nine)
    await m4.add_reaction(ten)
    await m4.add_reaction(jack)
    await m4.add_reaction(queen)
    await m4.add_reaction(king)
    await m4.add_reaction(ace)

    try:
        chance4 = 0
        while chance4 < 4:
            reaction, user = await bot.wait_for('reaction_add', timeout = 20.0, check = valid2_2)
            if str(reaction) == two:
                if result_card_no1 == ['2']:
                    temp4 = True
            elif str(reaction) == three:
                if result_card_no1 == ['3']:
                    temp4 = True
            elif str(reaction) == four:
                if result_card_no1 == ['4']:
                    temp4 = True
            elif str(reaction) == five:
                if result_card_no1 == ['5']:
                    temp4 = True
            elif str(reaction) == six:
                if result_card_no1 == ['6']:
                    temp4 = True
            elif str(reaction) == seven:
                if result_card_no1 == ['7']:
                    temp4 = True
            elif str(reaction) == eight:
                if result_card_no1 == ['8']:
                    temp4 = True
            elif str(reaction) == nine:
                if result_card_no1 == ['9']:
                    temp4 = True
            elif str(reaction) == ten:
                if result_card_no1 == ['10']:
                    temp4 = True
            elif str(reaction) == jack:
                if result_card_no1 == ['J']:
                    temp4 = True
            elif str(reaction) == queen:
                if result_card_no1 == ['Q']:
                    temp4 = True
            elif str(reaction) == king:
                if result_card_no1 == ['K']:
                    temp4 = True
            elif str(reaction) == ace:
                if result_card_no1 == ['A']:
                    temp4 = True
            chance4 = chance4 + 1
    except asyncio.TimeoutError:
        await message.send('This person is ghosting too? 🙄')

# Getting result
    await asyncio.sleep(2)
    await message.send('Getting result... Please standby... 🤓')
    await asyncio.sleep(2)

    if temp1 == True and temp3 == True:
        await message.send('Congrats! {} won this round BY LUCK 🥳.'.format(firstName.mention))
    else:
        pass

    if temp2 == True and temp4 == True:
        await message.send('Congrats! {} won this round BY LUCK 🤩.'.format(secondName.mention))
    else:
        pass

    if temp1 == True or temp3 == True:
        await message.send('{} guessed half correct! 🥳'.format(firstName.mention))
    else:
        pass

    if temp1 == True or temp3 == True:
        await message.send('{} guessed half correct! 🤩'.format(secondName.mention))

    if temp1 != True and temp3 != True:
        if temp2 != True and temp4 != True:
            await message.send('Sad. Nobody won 🥴.')





    
    await message.send('The answer is simple, humans. {}s card is {} {}; {}s card is {} {}. See? EZ 🙃.'.format(firstName, result_card_pattern1, result_card_no1, secondName, result_card_pattern2, result_card_no2))





bot.run('ODU5MDM5NzkzOTQ2NDI3Mzky.YNm5Jw.lCDZaXLJezsle_grbeDb_JtOLa0')