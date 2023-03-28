from os import getenv
from os import name
from discord.ext import commands
from discord import Intents
from dotenv import load_dotenv
from random import choice
import subprocess
from time import time

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

your_will_be_done = [
    "Fear not, mortal! Thine will shall be accomplished soon, by the might of Mjölnir!",
    "Rest assured! The task shall be completed with the swiftness of Sleipnir!",
    "As sure as the runes are written, your request shall be fulfilled with the strength of Thor!",
    "By the power of my antlers, the deed shall be done with the ferocity of a berserker!",
    "The Norns have spoken, and your desire shall be achieved with the wisdom of Odin!",
    "The winds of fate are blowing in your favor, and your request shall be granted with the speed of the Skíðblaðnir!",
    "Your wish is my command, and it shall be done before the cock crows at dawn!",
    "Worry not, for the task shall be completed with the deftness of a Viking ship's crew!",
    "Time is fleeting, but your request shall be fulfilled before the sun sets on the fjords!",
    "Take heart, for the deed shall be done ere long, with the bravery of a Viking warrior in battle! Skál!",
    "Have no fear, for your wish shall be accomplished soon with the strength of Yggdrasil!",
    "Rest easy, for the task shall be completed with the skill of a master blacksmith!",
    "The wheels of destiny turn in your favor, and your request shall be fulfilled with the cunning of Loki!",
    "By the power of my hooves, the deed shall be done with the endurance of a longship's rowing crew!",
    "The Valkyries have spoken, and your desire shall be achieved with the wisdom of Freya!",
    "The fates have woven their threads, and your request shall be granted with the dexterity of a skilled weaver!",
    "Your command shall be fulfilled with the speed of a galloping stallion across the tundra!",
    "Worry not, for the task shall be completed with the precision of a skilled archer!",
    "Time waits for no one, but your request shall be fulfilled before the next full moon!",
    "Take courage, for the deed shall be done ere long, with the power of a raging storm at sea! Hail!",
]

ready = [
    "Proceed with haste, mortal, for the path is open before you!",
    "Go forth, for the way has been cleared with the might of Mjölnir!",
    "The gates are open, and you may continue on your journey with the strength of Thor!",
    "The path ahead is clear, and you may forge ahead with the endurance of a reindeer!",
    "Your way is now unobstructed, for the skill of the gods has removed all barriers!",
    "The road lies open before you, and you may continue on your quest with the wisdom of Odin!",
    "You may proceed now, for the winds of fate blow in your favor, and the Norns have cleared your path!",
    "Fear not, for the way is clear, and you may forge ahead with the bravery of a Viking warrior!",
    "The way ahead is now free of danger, and you may continue on your journey with the cunning of Loki!",
    "You may proceed now, for the light of the sun shines upon your path, and the powers of the gods are with you! Skál!",
    "The way ahead is clear, mortal. You may continue on your quest with the strength of Yggdrasil!",
    "The road ahead is open, and you may proceed with the skill of a master craftsman!",
    "The Norns have spun their threads in your favor, and you may now continue on your journey with the wisdom of the ages!",
    "The way has been cleared with the power of my hooves, and you may continue with the endurance of a Viking raider!",
    "Your path lies unobstructed, for the Valkyries have cleared the way with the might of their swords!",
    "You may proceed now, for the fates have smiled upon you, and the gods have granted their favor!",
    "The way ahead is now open, and you may forge ahead with the cunning of a skilled strategist!",
    "The road lies clear before you, mortal. You may continue with the precision of a Viking archer!",
    "You may proceed now, for the light of the moon guides your way, and the stars shine upon your path!",
    "The way ahead is now unobstructed, and you may continue on your quest with the power of the gods at your side! Hail!",
]

on_cooldown = [
    "By the gods, you are impatient. Give me a minute.",
    "I can't help you now - I'm reticulating splines.",
    "I'm on cooldown. Go spam another bot, will you?",
    "You only need to ask once. It takes a minute to move things through the tubes.",
    "One moment please. I am having a staring contest with Odin.",
    "Please wait. I'm a bot, not a god.",
    "I am working on your previous request. Maybe you should go enjoy some ABBA.",
    "One minute please. Perhaps you would enjoy a hobby while you wait. Maybe brewing?"
]

server = {
    True: "Anytime",
    False: "Sunday"
}

running_answer = {
    True: "running",
    False: "stopped"
}

sleep_time = 30.0 # seconds

def assert_cooldown():
    #print(bot.last_execution+sleep_time, time())
    if bot.last_execution+sleep_time <= time():
        bot.last_execution = time()
        return True
    else:
        return False

@bot.event
async def on_ready():
    if name == "nt":
        print("Windows only: Running anytime server on ready.")
    else:
        pass
        #subprocess.Popen(["./run_anytime_server.sh","&"])
    bot.current_server = True
    bot.running = True
    bot.last_execution = time()-sleep_time

@bot.command()
async def alive(ctx):
    await ctx.send(choice(alive_response))    

@bot.command()
async def status(ctx):
    await ctx.send(f"The {server[bot.current_server]} server is selected, mortal. And I think it's {running_answer[bot.running]}. I'm pretty dumb though - I can't tell if that's right for sure. You'll have to try logging in to make sure.")

@bot.command()
async def stop(ctx):
    if assert_cooldown():
        await ctx.send(f"{choice(your_will_be_done)}\n\n*I'm stopping the {server[bot.current_server]} server - please wait a minute*.")
        if name == "nt":
            print("Windows only: Stopping server.")
        else:
            subprocess.Popen(["./server_stop.sh","&"])
            bot.running = False
    else:
        await ctx.send(choice(on_cooldown))


@bot.command()
async def start(ctx):
    if assert_cooldown():
        await ctx.send(f"{choice(your_will_be_done)}\n\n*I'm starting the {server[bot.current_server]} server - please wait a minute*.") 
        if name == "nt":
            print("Windows only: Starting server.")
        else:
            subprocess.Popen(["./server_start.sh","&"])
            bot.running = True
    else:
        await ctx.send(choice(on_cooldown))

@bot.command()
async def update(ctx):
    if assert_cooldown():
        await ctx.send(f"{choice(your_will_be_done)}\n\n*I'm updating the server - this takes a little longer. Go get some mead*.")
        if name == "nt":
            print("Windows only: Updating server.")
        else:    
            subprocess.Popen(["./server_update.sh","&"])
            bot.running = True
    else:
        await ctx.send(choice(on_cooldown))

@bot.command()
async def switch(ctx):
    if assert_cooldown():
        await ctx.send(f"{choice(your_will_be_done)}\n\n*I'm switching from the {server[bot.current_server]} to the {server[not bot.current_server]} server - please wait a minute*.")
        
        if bot.current_server:
            if name == "nt":
                print("Windows only: Switching to Sunday server.")
            else:
                subprocess.Popen(["./run_sunday_server.sh","&"])
        else:
            if name == "nt":
                print("Windows only: Switching to Anytime server.")
            else:
                subprocess.Popen(["./run_anytime_server.sh","&"])
        bot.current_server = not bot.current_server
        bot.running = True
    else:
        await ctx.send(choice(on_cooldown))

@bot.command()
async def hello(ctx):
    if name == "nt":
        print("Windows only: Not really saying hello.")
    else:
        subprocess.Popen(["./hello.sh","&"])
    await ctx.send("You just said hello in a faraway place.") 

if __name__ == "__main__":

    bot.run(TOKEN)