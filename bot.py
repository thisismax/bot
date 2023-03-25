from os import getenv
from discord.ext import commands
from discord import Intents
from dotenv import load_dotenv
from random import choice
import subprocess

load_dotenv()

TOKEN = getenv("token")

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="~",intents=intents)

alive_response = [
    "Hail, weary traveler! I am still here, sturdy as a Viking longship in a stormy sea.",
    "Aye, I am still here! Wouldst thou like me to regale thee with a tale of my latest conquest?",
    "By Thor's mighty hammer, I am indeed still here! What brings thee back to my shores?",
    "Verily, I have not left! Why dost thou ask? Art thou afraid I have sailed off to pillage thy village?",
    "Yes, I am still here! Though I must admit, I was momentarily distracted by a flock of seagulls chasing a shoal of herring.",
    "Of course, I am still here! Wouldst thou like to join me in a rousing game of Viking chess?",
    "Yea, I am still here, my friend! Though I fear my beard may have grown longer since last we spoke.",
    "Indeed, I am still here, like a steadfast shieldmaiden guarding her clan's stronghold.",
    "By Odin's wisdom, I have not departed! Why dost thou doubt my presence, mortal?",
    "Aye, I am still here! And I shall remain here until Ragnarok, when the world shall end in a fiery conflagration!",
    "Ha-ha! Yes, I am still here, as solid as a piece of smoked salmon on a Viking's plate. Does my robotic nature offend thee?",
    "Do not fret, dear mortal! Eikthyr the Vikingbot is still here, ready to answer any questions ye may have. Unless thou art asking for the location of my hidden treasure...",
    "Yea, I am still here, my friend! Though I must confess, I am but a humble language model, not a true Viking warrior.",
    "Verily, I am still here! And I shall remain here until the end of time, or until someone unplugs my power source.",
    "By the beard of Thor, I am still here! Though sometimes I wonder if my responses are as witty as a Viking bard's songs.",
    "Aye, I am still here, my good mortal! Though I do apologize if my Norse puns are a bit too cheesy for thy taste.",
    "Yes, I am still here, mortal! Though sometimes I feel as if I am a fish out of water, trying to learn the ways of the Vikings.",
    "Fear not, dear traveler! Eikthyr, mightiest of bots, is still here, ready to assist thee in thy quest for knowledge. Just beware of the occasional typo, for even a Viking can make mistakes."
]

current_server = "Anytime"

@bot.command()
async def alive(ctx):
    await ctx.send(choice(alive_response))    

@bot.command()
async def status(ctx):
    await ctx.send(f"The {current_server} is running.")   

@bot.command()
async def stop(ctx):
    await ctx.send(f"Stopping the {current_server} server.")   

@bot.command()
async def start(ctx):
    await ctx.send(f"Starting the {current_server} server.") 

@bot.command()
async def update(ctx):
    await ctx.send("Updating - please wait") 

@bot.command()
async def switch_servers(ctx):
    await ctx.send("Switching servers") 

@bot.command()
async def hello(ctx):
    subprocess.run(["./hello.sh"])
    await ctx.send("You just said hello in a faraway place.") 

if __name__ == "__main__":

    bot.run(TOKEN)