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

    rules = discord.Embed(title = '{} is looking at the No-Currency-Gamble Rulebook'.format(name), description = 'There are no currency used, this bot uses your luck and cowardness. Have fun! 😉', color = 0xf8f8ff)
    rules.set_thumbnail(url = avatar)
    rules.add_field(name = 'Coinflip', value = 'You dont know what is coinflip? Out you go, you are not eligible to gamble. Syntax: Coinflips for one; Coinflipd for two', inline = False)
    rules.add_field(name = 'Guess', value = 'Pick a card, big or small or forfeit or fool them.', inline = False)
    rules.add_field(name = 'Blackjack', value = 'Blackjack. What? A stray dog also knows blackjack, you dont know? Ask him.', inline = False)
    rules.add_field(name = 'Texas Poker', value = 'Ask someone in your discord server. Long description.', inline = False)
    rules.add_field(name = 'Landlord', value = 'The ultimate gamble. China version by the way.', inline = False)
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
        
bot.run('ODU5MDM5NzkzOTQ2NDI3Mzky.YNm5Jw.lCDZaXLJezsle_grbeDb_JtOLa0')