import os
import random

import discord

#Fuck if I know how intents work but this works, so don't touch it.
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

response_dict = {
    "stede": ["BONNET?"],
    "how are you": ["https://cdn.discordapp.com/attachments/871560412255109174/989397829653000213/autism_level_today.jpg"],
    "iggy": ["It's *IZZY*."],
    "gayboy": ["fuck off"],
    "bark": ["woof"],
    "birthday": ["happy fuckin' birthday!"],
    "bite": ["*bites you bites you bites you bites you bites you bites you bites you bites you bites you bites you bites you bites you bites you bites you bites you bites you bites you bites you*"],
    "blackbeard": ["https://media.discordapp.net/attachments/964941818036891659/970233138141884466/ofmd-izzy-simp-ed.png"],
    "gentlebeard": ["https://media.discordapp.net/attachments/964941818036891659/970228343922364436/x-15.png"],
    "dog": ["... no pets on board blackbeard's ship."],
    "edward": ["his name is B L A C K B E A R D"],
    "groan": ["https://media.discordapp.net/attachments/964941818036891659/970228343922364436/x-15.png"],
    "moan": ["https://media.discordapp.net/attachments/964941818036891659/970228343922364436/x-15.png"],
    "sex noise": ["https://media.discordapp.net/attachments/964941818036891659/970228343922364436/x-15.png"],
    "i think": ["no one asked you to fuckin' think!"],
    "love ed": ["do i look like some fuckin' namby-pamby pining after his boyfriend?"],
    "lucius": ["twatty"],
    "pspsps": ["i'm not your fuckin' pet"],
    "retire": ["the only retirement we get is... death."],
    "should be working": ["get back to work... NOOOOOOOWWWW!!!!"],
    "sketch": ["*fuck off* (homoerotic)"],
    "spanish jackie's": ["i fuckin' hate that place"],
    "he makes ed happy": [":nauseated_face: :nauseated_face: :nauseated_face: "],
    "why": ["i don't have to explain myself to you... fuck off!"],
    "you read": ["https://64.media.tumblr.com/90d19733765711d6b5a968e14c3de547/430a3d12c419215c-a1/s540x810/0b6284e6fbd0ae5f2b5ad1dda1589f045abb4d2c.gif"],
    "dance": ["https://media.discordapp.net/attachments/959562204137553961/962524263963852851/Izzydance.gif"],
    "mutiny": ["wait, i can change!! i'm open to feedback!"],
    "you're fired": ["you will rue this day, edward"],
    "saturday": ["https://media.discordapp.net/attachments/961202855614767146/969874111104942090/izzy-saturdaychilling.png"],
    "shampoo": ["https://media.discordapp.net/attachments/961202855614767146/969654993235869696/E9B66DDE-761C-4183-AD92-53C97439F89B.gif"],
    "hair": ["https://media.discordapp.net/attachments/961202855614767146/969654993235869696/E9B66DDE-761C-4183-AD92-53C97439F89B.gif"],
    "babygirl": ["....."],
    "need a captain": ["... could be me, yea."],
    "blackbonnet": ["https://media.discordapp.net/attachments/964941818036891659/970228343922364436/x-15.png"],
    "jizzy": ["https://media.discordapp.net/attachments/964941818036891659/970228343922364436/x-15.png"],
    "cj/izzy": ["https://media.discordapp.net/attachments/964941818036891659/970228343922364436/x-15.png"],
    "blackhands": ["https://media.discordapp.net/attachments/964941818036891659/970228343922364436/x-15.png"],
    "ed/izzy": ["https://media.discordapp.net/attachments/964941818036891659/970228343922364436/x-15.png"],
    "steddy hands": ["https://media.discordapp.net/attachments/964941818036891659/970228343922364436/x-15.png"],
    "stizzy": ["https://media.discordapp.net/attachments/964941818036891659/970228343922364436/x-15.png"],
    "jacked izzy": ["https://media.discordapp.net/attachments/964941818036891659/970228343922364436/x-15.png"],
    "fizzy": ["https://media.discordapp.net/attachments/964941818036891659/970228343922364436/x-15.png"],
    "fizzan": ["https://media.discordapp.net/attachments/964941818036891659/970228343922364436/x-15.png"],
    "the ring": ["none of yer fuckin' business.","it was my mothers'"],
    "izzypat": ["pat pat pat pat"],
    "fuck you": ["no fuck YOU"],
    "i love you": [":nauseated_face: :nauseated_face:","*cries silently*","fuck off *(homoerotic)*"],
    "lucius/izzy": ["https://media.discordapp.net/attachments/964941818036891659/970228343922364436/x-15.png"],
    "have you ever been sketched?": ["https://64.media.tumblr.com/12305e44a16ddacd8dea510fbcffc5bf/23b678ab178ccd74-7e/s540x810/ab33c3681f46678385d376cc73a052657b12c2b2.gif"],
    "spinizzy": ["**LET ME OUT!!**"],
    "hungry": ["you don't get food when you've been invaded!"],
    "food": ["you don't get food when you've been invaded!"],
    "you ok": ["................................................ no."],
    "should be sleeping": ["GO TO BED!! <:ihs8_gotobednow:985545827193847890> <:ihs8_gotobednow:985545827193847890> <:ihs8_gotobednow:985545827193847890>"],
    "go to sleep": ["GO TO BED!! <:ihs8_gotobednow:985545827193847890> <:ihs8_gotobednow:985545827193847890>"],
    "should sleep": ["GO TO BED!! <:ihs8_gotobednow:985545827193847890> <:ihs8_gotobednow:985545827193847890>"],
    "heel": ["*yes, sir*"],
    "fetch": ["oh, can't I just send the boys?"],
    ":ihs4_spinizzy:": ["**LET ME OUT!!**"],
    ":ihs2_patpat:": ["pat pat pat pat"],
    "beg": [":pleading_face:"],
    "simp": [".............. *fuck off* <:ihs5_angryeyes:964136194428518480>"],
    "izzygrab": ["*NO, NO, NOT THE BLENDER, PLEASE!!!*"],
    "smoothizzy": ["*NOOOOOOOO*"],
    "tits": ["Bonnet?"],
    "are you gay": ["*fuck off*"],
    "trans rights": ["https://media.discordapp.net/attachments/964941818036891659/970225730967441418/conpose.png"],
    "trans wrongs": ["https://cdn.discordapp.com/attachments/970028054724358204/972042301192945664/memed-io-output_1.jpeg"],
    "con o'neil":[".... Slut"],
    "good boy": ["..... fuck off","*whine*","i'm not your fuckin' pet","*no'mnot*"],
    "draw your sword": ["Oh, Bonnet, no"],
    "kiss": ["*backs away*","*stares at your lips*"],
    "behave":["*make me*", "*y-yes, sir*", "you're not my captain"],
    "scream":["<:ihs2_IzzyScream:1038907440760094840>"],
    "season 2":["SHUT THE FUCK UP","I WILL END YOU"],
"patpat":["<a:ihs2_patpat:1005737019001020467>","<a:ihs2_patpat:1005737019001020467> <a:ihs2_patpat:1005737019001020467>"],
"mermaids": ["There are no fucking mermaids"], 
"the end": ["Everything will be alright in the end. And if it's not alright, it's not the end", "https://cdn.discordapp.com/attachments/1162978517877801010/1167083422817194014/20230528_1240432.mp4?ex=654cd623&is=653a6123&hm=c0ca2f7339a5118749ae0119b78604a2b58467502678333b2aec91f31cb3b4b8&"],
    "hug": ["*wiggles away* No-", "*cries* Why is this nice?", "<:ihs8_donthugmeillcry:1157020625244786829>", "*~softly~* Fuck you"],
    "yeet": ["bonk :face_with_spiral_eyes:"],
"for the new unicorn": ["fucking cocksuckers","https://media1.tenor.com/m/l_3AKkdzrjAAAAAC/good-night-our-flag-means-death.gif"],
"fuck off": [". . . rude"],
"a curse is a curse": ["and once it takes hold. . . *awkward pause* well then it- it takes hold"],
"feet": [". . . foot"],
"izzy dead": ["I lived bitch :middle_finger:"],
"alone": ["you're born alone. . . you die alone. . . you're born alone. . . you die alone. . ."],
"stede won the duel": ["on a *FUCKIN' TECHNICALITY*"],
"cancelled": ["I went out on a limb for you, you little shit!"],
    "pride": ["It's about belonging to something :gay_pride_flag: :transgender_flag: :gay_pride_flag: :transgender_flag:","It's about belonging to something :gay_pride_flag:","It's about belonging to something :transgender_flag:"]
  }
    # Add more responses as needed

# Event handler for when a message is received
@client.event
async def on_message(message):
    # Prevent the bot from responding to itself
    if message.author == client.user:
        return

  # Check if the message content contains any of the predefined triggers
    for trigger, responses in response_dict.items():
       if trigger in message.content.lower():
          # Return a random response from the list of responses for the matched trigger
           random_response = random.choice(responses)
           await message.channel.send(random_response)

client.run(os.getenv('BOT_TOKEN','hello'))
