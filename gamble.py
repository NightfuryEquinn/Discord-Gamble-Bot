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
        await asyncio.sleep(60)

bot.loop.create_task(change_status())

# Rulebook
@bot.command()
async def rules(message):
    name = message.author.name
    avatar = message.author.avatar_url

    rules = discord.Embed(title = '{} is looking at the No-Currency-Gamble Rulebook'.format(name), description = 'There are no currency used, this bot uses your luck and cowardness. Have fun! 😉', color = 0xf8f8ff)
    rules.set_thumbnail(url = avatar)
    rules.add_field(name = 'Coinflip', value = 'You dont know what is coinflip? Out you go, you are not eligible to gamble.', inline = False)
    rules.add_field(name = 'Guess', value = 'Pick a card, big or small or forfeit or fool them.', inline = False)
    rules.add_field(name = 'Blackjack', value = 'Blackjack. What? A stray dog also knows blackjack, you dont know? Ask him.', inline = False)
    rules.add_field(name = 'Texas Poker', value = 'Ask someone in your discord server. Long description.', inline = False)
    rules.add_field(name = 'Landlord', value = 'The ultimate gamble. China version by the way.', inline = False)
    await message.send(embed = rules)

# Coinflip
@bot.command(aliases = ['cf'])
async def coinflip(message):
    name = message.author.name

    coin = ['Head', 'Tail', 'It stands!']
    luck = [10, 10, 0.5]
    result = random.choices(coin, luck, k = 1)
    await asyncio.sleep(5)
    
    if result == ['Head']:
        await message.send('{} flipped a coin and landed on {}. Ouch, the coin hit its head.'.format(name, result))
    elif result == ['Tail']:
        await message.send('{} flipped a coin and landed on {}. Oh no, it broke its tailbone. Call the ambulance! NOW!'.format(name, result))
    elif result == ['It stands!']:
        await message.send('Holy ****! {} MADE THE COIN STANDS. You are the LUCKIEST HUMAN alive! For now. Play again, maybe money will start raining in where you live. I mean fake money. HA!'.format(name))

bot.run('ODU5MDM5NzkzOTQ2NDI3Mzky.YNm5Jw.lCDZaXLJezsle_grbeDb_JtOLa0')