import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import random


client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Hilltop Gang"))           #the status of the bot
    print("bot is ready")




@client.event
async def on_member_join(member):				#report on cmd who joined
	print(f"{member} has Joined!")
	#await bot.send_message(member, "boop")



@client.event							#report on cmd who left
async def on_member_remove(member):
	print(f"{member} has left a server")
 
 
 
############### COMMAND SECTION ###################
@client.command()						#responding to command
async def ping(ctx):
    await ctx.send('pong!')


@client.command(aliases=["8ball", "ball"])			#magic 8ball commands
async def _8ball(ctx, *, question):
    responses = [
        'It is certain.',
        'It is decidedly so.',
        'Without a doubt.',
        'Yes - definitely.',
        'You may rely on it.',
        'As I see it, yes.',
        'Most likely.',
        'Outlook good.',
        'Yes.',
        'Signs point to yes.',
        'Reply hazy, try again.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Dont count on it.',
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good',
        'Very doubtful.']
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")


@client.command()						#checks if user has admin and removes x ammount of messages (default is 1)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)

    
client.run('TOKEN GOES HERE')
