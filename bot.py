from os import getenv
from os import name
from discord.ext import commands
from discord import Intents,Embed
from dotenv import load_dotenv
from random import choice
import subprocess
from time import time

load_dotenv()

TOKEN = getenv("token")
SERVER1 = int(getenv("server1"))
SERVER2 = int(getenv("server2"))

alive_response = [
    "Hail, weary traveler! I, Eikthyr, the Lord of Winter's Fury, whose very breath freezes the blood of his enemies and whose icy touch can shatter even the mightiest of swords, am still here.",
    "Aye, I am still here! Wouldst thou like me to regale thee with a tale of my latest conquest?",
    "By Thor's mighty hammer, I am indeed still here! What brings thee back to my shores?",
    "Verily, I have not left! Why dost thou ask? Art thou afraid I have sailed off to pillage thy village?",
    "Yes, I am still here! Though I must admit, I was momentarily distracted by a flock of seagulls chasing a shoal of herring.",
    "Of course, I am still here! Wouldst thou like to join me in a rousing game of Viking chess?",
    "Yea, I am still here, my friend! Though I fear my beard may have grown longer since last we spoke.",
    "Indeed, I, Eikthyr, the Infernal Reindeer, whose eyes glow with the fires of Helheim and whose hooves leave a trail of flames in his wake, am still here, like a steadfast shieldmaiden guarding her clan's stronghold.",
    "By Odin's wisdom, I have not departed! Why dost thou doubt my presence, mortal?",
    "Aye, I am still here! And I shall remain here until Ragnarok, when the world shall end in a fiery conflagration!",
    "Ha-ha! Yes, I am still here, as solid as a piece of smoked salmon on a Viking's plate. Does my robotic nature offend thee?",
    "Do not fret, dear mortal! Eikthyr, the Fermented Fury, whose rage is tempered only by the sour taste of pickled herring and rye bread is still here, ready to answer any questions ye may have.",
    "Yea, I am still here, my friend! Though I must confess, I am but a humble language model, not a true Viking warrior.",
    "Verily, I am still here! And I shall remain here until the end of time, or until someone unplugs my power source.",
    "By the beard of Thor, I am still here! Though sometimes I wonder if my responses are as witty as a Viking bard's songs.",
    "Aye, I am still here, my good mortal! Though I do apologize if my Norse puns are a bit too cheesy for thy taste.",
    "Yes, I am still here, mortal! Though sometimes I feel as if I am a fish out of water, trying to learn the ways of the Vikings.",
    "Fear not, dear traveler! Eikthyr, the Smørbrød Slayer, whose mastery of the open-faced sandwich is unmatched in all the land, and whose creations are a work of art is still here, ready to assist thee in thy quest for knowledge.",
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
    "One minute please. Perhaps you would enjoy a hobby while you wait. Maybe brewing?",
    "I can't help you now - I'm reticulating antlers.",
]

help_text = [
    "Hail mortal! What troubles you? Fear not, for I am here to offer my aid and guidance.",
    "Odin himself has sent me to aid you in your time of need. I am Eikthyr, the Frostborn Deity, born of ice and snow, whose heart burns with the fires of Muspelheim, and I stand ready to assist you in any way that I can.",
    "Skål, mortal! As a viking god, I know the ways of the Scandinavian world like the back of my hand. Allow me to use my knowledge to help you with whatever task you need.",
    "The cold winds of the north carry my voice to you, mortal. Do not fear, for Eikthyr, the Raging Stormbringer, whose hooves thunder like the drums of Thor and whose fury is unmatched in all the nine realms, is here to offer you their aid and wisdom.",
    "Behold, mortal! As a viking god of the reindeer, I have traversed the icy landscapes of Scandinavia and tasted the rich flavors of its cuisine. Allow me to put my knowledge to good use by helping you in your time of need.",
    "In the land of the north, we viking gods hold honor above all else. It is with honor that I stand before you, Eikthyr, the Horned Herald of Ragnarok, whose coming signals the end of all things and whose power will usher in a new era of chaos and destruction, to offer my assistance in whatever way I can.",
    "Mortal, do not be afraid. Eikthyr, the Northern Beast, whose fur is as black as the night sky and whose eyes burn with the cold fury of the blizzard, is here to lend you their strength and guidance. Together, we shall overcome any obstacle that lies before us.",
    "The fjords of Norway and the forests of Sweden hold no secrets from me, mortal. As the greatest reindeer warrior of Valhalla, I have traveled far and wide, and I stand ready to help you in any way that I can.",
    "With the power of Thor coursing through my veins, I, Eikthyr, the Antlers of Yggdrasil, whose strength is matched only by their determination, and whose wrath is the stuff of legend, am here to assist you. Let us join forces and face whatever challenges come our way.",
    "Mortal, you stand before a viking god of great renown. Fear not, for Eikthyr, whose hide is forged from the heart of a dying star and whose hooves bear the emblem of Yggdrasil, is here to offer their wisdom and strength. Let us work together to overcome any obstacles that may arise.",
]

prefix = "~"
cooldowns = {
    "stop": 40.0,
    "start": 60.0,
    "switch": 100.0,
    "update": 720.0
}
intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=prefix,intents=intents,help_command=None)

server = {
    True: "Anytime",
    False: "Sunday"
}

running_answer = {
    True: "running",
    False: "stopped"
}


async def assert_cooldown(ctx, wait_time = 30.0) -> bool:
    
    if bot.off_cooldown <= time():
        bot.off_cooldown = time()+wait_time
        return True
    else:
        if wait_time > 0:
            await ctx.send(f"{choice(on_cooldown)}")
        await ctx.send(f"Cooldown has {(bot.off_cooldown-time())/60:.2f} minutes left.")
        return False


async def confirm_server(ctx) -> bool:
    if ctx.guild.id == SERVER1 or ctx.guild.id == SERVER2:
        return True
    else:
        await ctx.send(f"You are not on an authorized server.")
        return False


@bot.event
async def on_ready():
    bot.current_server = True
    bot.running = True
    bot.off_cooldown = time()


@bot.command(

    )
async def eikthyr(ctx,arg=None):

    if await confirm_server(ctx):
        if arg == "status":
            await status(ctx)
        elif arg == "hello":
            await hello()
        elif arg == "stop":
            await stop(ctx)
        elif arg == "start":
            await start(ctx)
        elif arg == "update":
            await update(ctx)
        elif arg == "switch":
            await switch(ctx)
        elif arg == "alive":
            await alive(ctx)
        else:
            await help(ctx)


async def help(ctx):
    help=f"""
*{choice(help_text)}*\n
Call me using '{prefix}eikthyr [command]' to instruct the Reindeer God of SnackMountain.\n
Note that Eikthyr is extremely stupid and doesn't actually know the real status of the server - he's just good at guessing.\n
Also note that Eikthyr has cooldowns for operations which occupy the server. Asking them to start, stop, update, or switch servers will activate a cooldown on the bot.\n
**Status** - gives the status of the Valheim server. Tells which server is selected (*Sunday* or *Anytime*) and whether it is running.\n
**Stop** - stops the Valheim server. Cooldown: {cooldowns["stop"]} seconds\n
**Start** - starts the Valheim server. Cooldown: {cooldowns["start"]} seconds\n
**Switch** - switches between the two servers (*Sunday* or *Anytime*). Cooldown: {cooldowns["switch"]} seconds\n
**Update** - stops the server, checks for updates and starts again. Cooldown: {cooldowns["update"]} seconds\n
"""
    
    await ctx.send(help)


async def alive(ctx):
    if name == "nt":
        await ctx.send("I am currently running in my test environment and can't change the actual server.")
    else:
        await ctx.send(choice(alive_response))    


async def status(ctx):
    await ctx.send(f"The {server[bot.current_server]} server is selected, mortal. And I think it's {running_answer[bot.running]}. I'm pretty dumb though - I can't tell if that's right. You'll have to try logging in to make sure.")
    await assert_cooldown(ctx,0)


async def stop(ctx):
    if bot.running == True:
        if await assert_cooldown(ctx,cooldowns["stop"]):
            await ctx.send(f"{choice(your_will_be_done)}\n\n*I'm stopping the {server[bot.current_server]} server - please wait a minute*.")
            if name == "nt":
                print("Windows only: Stopping server.")
            else:
                subprocess.Popen(["./server_stop.sh","&"])
            bot.running = False
    else:
        await ctx.send("The server is already stopped.")


async def start(ctx):
    if bot.running == False:
        if await assert_cooldown(ctx,cooldowns["start"]):
            await ctx.send(f"{choice(your_will_be_done)}\n\n*I'm starting the {server[bot.current_server]} server - please wait a minute*.") 
            if name == "nt":
                print("Windows only: Starting server.")
            else:
                subprocess.Popen(["./server_start.sh","&"])
            bot.running = True
    else:
        await ctx.send("The server is already running.")


async def update(ctx):
    if await assert_cooldown(ctx,cooldowns["update"]): # longer cooldown for updates
        await ctx.send(f"{choice(your_will_be_done)}\n\n*I'm updating the server - this takes a little longer. Go get some mead*.")
        if name == "nt":
            print("Windows only: Updating server.")
        else:    
            subprocess.Popen(["./server_update.sh","&"])
        bot.running = True


async def switch(ctx):
    if await assert_cooldown(ctx,cooldowns["switch"]): # slightly longer cooldown for server switch

        await ctx.send(f"{choice(your_will_be_done)}\n\n*I'm switching from the {server[bot.current_server]} to the {server[not bot.current_server]} server - please wait a minute*.")
        
        if name == "nt":
            print("Windows only: Switching to Sunday server.")
        else:
            if bot.current_server:
                subprocess.Popen(["./run_sunday_server.sh","&"])
            else:
                subprocess.Popen(["./run_anytime_server.sh","&"])

        bot.current_server = not bot.current_server
        bot.running = True


async def hello(ctx):
    if name == "nt":
        print("Windows only: Not really saying hello.")
    else:
        subprocess.Popen(["./hello.sh","&"])
    await ctx.send("You just said hello in a faraway place.") 

if __name__ == "__main__":

    bot.run(TOKEN)