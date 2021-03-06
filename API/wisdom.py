#!/usr/bin/python3
import random as r


def pick_random(value):
    return value[r.randint(0, len(value)-1)]

abbreviation = ["TCP", "HTTP", "SDD", "RAM", "GB",
            "CSS", "SSL", "AGP", "SQL", "FTP",
            "PCI", "AI", "ADP", "RSS", "XML",
            "EXE", "COM", "HDD", "THX", "SMTP",
            "SMS", "USB", "PNG", "XSS", "SFTP",
            "MITM"]

adjective = ["auxiliary", "primary", "back-end", "digital",
         "open-source", "virtual", "cross-platform",
         "redundant", "online", "haptic","multi-byte",
         "bluetooth", "wireless", "1080p", "neural",
         "optical", "solid state", "mobile"]

noun = ["driver", "protocol", "bandwidth", "panel", "microchip",
    "program", "port", "card", "array", "interface", "system",
    "sensor", "firewall", "hard drive", "pixel", "alarm",
    "feed", "monitor", "application", "transmitter", "bus",
    "circuit", "capacitor", "matrix", "socket", "database"]

verb = ["back up", "bypass", "hack", "override", "compress", "copy",
    "navigate", "index", "connect", "generate", "quantify",
    "calculate", "synthesize", "input", "transmit", "program",
    "reboot", "parse", "analyze"]

ingverb = ["backing up", "bypassing", "hacking", "overriding",
       "compressing", "copying", "navigating", "indexing",
       "connecting", "generating", "quantifying", "calculating",
       "synthesizing", "transmitting", "programming", "parsing",
       "DDoSing", "scamming", "pwning", "rooting", "pigning",
       "lurking"]

sentences = [
"If we {} the {}, we can get to the {} {} throught the {} {} {}!"
.format(
    pick_random(verb),
    pick_random(noun),
    pick_random(abbreviation),
    pick_random(noun),
    pick_random(adjective),
    pick_random(abbreviation),
    pick_random(noun)
),

"We need to {} the {} {} {}!"
.format(
    pick_random(verb),
    pick_random(adjective),
    pick_random(abbreviation),
    pick_random(noun),
),

"Try to {} the {} {}, maybe it will {} the {} {}!"
.format(
    pick_random(verb),
    pick_random(abbreviation),
    pick_random(noun),
    pick_random(verb),
    pick_random(adjective),
    pick_random(noun),
),

"You can't {} the {} without {} the {} {} {}!"
.format(
    pick_random(verb),
    pick_random(noun),
    pick_random(ingverb),
    pick_random(adjective),
    pick_random(abbreviation),
    pick_random(noun),
)]


wise_sentences = [
"Practice makes perect!",
"Rome was not built in a day!",
"Shoot for the moon! Even if you miss, you'll land amongst the stars!",
"There is no such thing as a hacker that never made a mistake - Anon",
"Learning to code is like growing a tree, takes time - Anon",
"If you work for Microsoft or Apple, get a life - Anon",
"It is easier to build good habits than break bad ones - Forgotton",
"Education makes man unfit for a slave - Frederick Douglas",
"Life as a script kiddie is not a life worth living - Anon",
"A person who never made a mistake, never tried anything new - Einstein",
"If you're not willing to learn code, you don't deserve to know how  to code - v1",
"Well being worth a god damn comes with an ability to not be a complete and total retard all the time ~ mickers"
]

urls = [
"https://www.youtube.com/watch?v=ZzfHjytDceU - Topics of Interest: Asyncio",
"https://www.youtube.com/watch?v=lyDLAutA88s - David Beazley: Builtin Superheros!",
"https://www.youtube.com/watch?v=E-1Y4kSsAFc - Fear and awaiting in Async",
"https://www.youtube.com/watch?v=OSGv2VnC0go - Idiomatic, Pythonic code",
"https://www.youtube.com/watch?v=N4mEzFDjqtA - Python in one video : Derek Banas",
"https://www.youtube.com/watch?v=XXmzYY03t64 - Basic SysAdmin's Guide to Python",
"https://www.youtube.com/watch?v=s1SkCYMnfbY - MulitProcessing with Python",
"https://www.youtube.com/watch?v=l_HBRhcgeuQ - Global Interpreter Lock",
"https://www.youtube.com/watch?v=ciNHn38EyRc - SQL Injections with exmaples",
"https://www.youtube.com/watch?v=GMGbOkKfZRo - Beginner SysAdmin with Python",
"https://www.youtube.com/watch?v=yHO8hdqzKw8 - Basic Python for the OS",
"https://www.youtube.com/watch?v=Thd8yoBou7k - SQL for Python Developers",
"https://www.youtube.com/watch?v=T1QEs3mdJoc - Cookie Grabbing Basics",
"https://www.youtube.com/watch?v=Pi9NpxAvYSs - Python Epiphanies"
]


courses = [
"AI! - https://www.youtube.com/watch?v=OGxgnH8y2NM&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v"
]

topics = [

]

sciences = [
"https://www.youtube.com/watch?v=9Cd36WJ79z4 : Poetry of Reality",
"https://www.youtube.com/watch?v=1PT90dAA49Q : Wave of Reason",
"https://www.youtube.com/watch?v=zSgiXGELjbc : Glorious Dawn - Carl Sagan",
"https://www.youtube.com/watch?v=vioZf4TjoUI : The Cosmic Perspective",
"https://www.youtube.com/watch?v=hOLAGYmUQV0 : The Unbroken Thread"
]

music = [
"https://www.youtube.com/watch?v=X6t3CVafuec : YTCracker - Bazaar",
"https://www.youtube.com/watch?v=ieDBrlKnaAM : YTCracker - Starship",
"https://www.youtube.com/watch?v=2tRKH_BSsk0 : YTCracker - Social Engineering",
"https://www.youtube.com/watch?v=lIuEuJvKos4 : Astrix - Jungle Walk",
"https://www.youtube.com/watch?v=FoUWHfh733Y : Dual Core - All the things",
"https://www.youtube.com/watch?v=zeIjmvZZ_SQ : Zearle - Hackers and Crackers",
"https://www.youtube.com/watch?v=v1BXfMNfjFo : Deep Space House 061",
"https://www.youtube.com/watch?v=scPU1tTIg7Y : VOICIANS - Stranger",
"https://www.youtube.com/watch?v=8fIjqPqJYhA : VOICIANS - Wolves",
"https://www.youtube.com/watch?v=8EQzx-OzQmU : Wavve - 9 is God",
"https://www.youtube.com/watch?v=2GLGZQ4Y8SM : YTCracker - Crack",
"https://www.youtube.com/watch?v=YEP7rhDuWVE : YTCracker - Untouchable",
"https://www.youtube.com/watch?v=Sr8ILq1a_yw : Dual Core - 0x0A Commandments",
"https://www.youtube.com/watch?v=yc7_NHx6oHw : YTCracker - Packets",
"https://www.youtube.com/watch?v=YrRa6dEkzmk : Beat Hackers - Experience",
"https://www.youtube.com/watch?v=f04pC0_U5-I : Talamasca - Psychedelic Trance"
]


noob_quotes = [
"So if I want to write a maleware i must use a github? ~ EniGmis7",
"Windows wouldn't be popular if microsoft didn't know what they were doing ~ leaxyz",
"how hax facebook? ~ Virtually every noob ever.",
"I'm a hacker. Can someone help me reverse an md5? ~ MoHD"
]

def noob():
  data = noob_quotes[r.randint(0, len(noob_quotes))]
  return data

def troll():
    troll = sentences[r.randint(0, len(sentences)-1)]
    return troll

def science(): return sciences[r.randint(0, len(sciences))]  

def science_song(number): data = sciences[number] ; return data  
    
def wisdom(): return wise_sentences[r.randint(0, len(wise_sentences))]

def urlpls(): return urls[r.randint(0, len(urls))]

def url(num): data = urls[num] ; return data

def song(number): data = music[number] ; return data

def quote(number): data = wise_sentences[number] ; return data

def songpls(): return music[r.randint(0, len(music))]

def randomtopic(): return topics[r.randint(0, len(topics))]

def randomcourse(): return courses[r.randint(0,len(courses))] 
