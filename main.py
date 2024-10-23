from inspect import _void
import disnake as discord
from disnake.ext import commands, tasks
from disnake import TextInputStyle
import json
import requests
import time
import os
import psutil
import asyncio
import traceback

client = discord.Client()

bot = commands.Bot(command_prefix = '!',
                   case_insensitive = True,
                   intents = discord.Intents().all(),
                   help_command = None,
                   strip_after_prefix = True,
                   )

chan=bot.get_channel("CHANNELID")


@bot.event
async def on_ready():
    print(CGREENBG2 + f'Connected as {str(bot.user)}' + CEND)
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="stats and bans"))

global ign
global gamemode
global delay

CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'

CGREYBG    = '\33[100m'
CREDBG2    = '\33[101m'
CGREENBG2  = '\33[102m'
CYELLOWBG2 = '\33[103m'
CBLUEBG2   = '\33[104m'
CVIOLETBG2 = '\33[105m'
CBEIGEBG2  = '\33[106m'
CWHITEBG2  = '\33[107m'

#BOT LAUNCH
    
@bot.slash_command(name="tracker") 
async def tracker(inter, delay : int, gamemode : str, ign : str):
         await inter.response.send_message("⠀")
         chan=bot.get_channel("CHANNELID")
         os.system('cls')

         print("\n████████╗██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░")
         print("╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗")
         print("░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝")
         print("░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗")
         print("░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║")
         print("░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝")
         print("                                             made by ui<3\n")

         loop = 1    
         winstreak = 0
        
         valuewlr = 0
         valuewlr1 = 0
         value1a = 0
         value2a = 0

         delay = int(delay)
         apikey = "APIEKY"
         gamemodebig = gamemode.capitalize()

         try:
                resp = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{ign}")
                uuidplayer = resp.json()["id"]
         except KeyError:
                embed = discord.Embed
                embed = discord.Embed(title="tracker ⛤", description="```This player doesn't exist!```", color=discord.Colour.blue())
                embed.set_thumbnail(url="https://mc-heads.net/body/1ca05403f5a24b74840d6f4eba6e3c27/50")
                embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://images-ext-1.discordapp.net/external/g1FieBBXQwG4GdgupVLaJoMN7ZtO5-GVgWnI_O9YJaI/https/i.pinimg.com/originals/61/1b/69/611b693be05344bcab472607f356787f.gif?width=900&height=1131")
                await inter.channel.send(embed=embed)

                print("\n" + CYELLOWBG2 + "Sent an Embed! (KeyError)" + CEND)


         print("\n------------------------------------------------------")     

         embed = discord.Embed
         embed = discord.Embed(title="tracker ⛤", description="tracker launched successfully", color=discord.Colour.green())
         embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://images-ext-1.discordapp.net/external/g1FieBBXQwG4GdgupVLaJoMN7ZtO5-GVgWnI_O9YJaI/https/i.pinimg.com/originals/61/1b/69/611b693be05344bcab472607f356787f.gif?width=900&height=1131")

         components=[
                 discord.ui.Button(label="Disconnect", style=discord.ButtonStyle.danger, custom_id="disconnect"),
                 ]

         await inter.channel.send(embed=embed, components=components)

         print("\n" + CGREENBG2 + "Sent an Embed! (Launched)" + CEND)


         @bot.listen("on_button_click")
         async def help_listener(inter: discord.MessageInteraction):
             PROCNAME = "javaw.exe"
             for proc in psutil.process_iter():
                 if proc.name() == PROCNAME:
                     proc.kill()
             await inter.response.send_message("Disconnected!")
        
         while loop == 1:
            url = "https://api.hypixel.net/player?key=" + apikey + "&uuid=" + uuidplayer #example API endpoint for todo list app 
            response = requests.get(url)  #fetching contents from api end point  
            data_dict= {}   #creating empty dictionary object  
            if (response):   
                data_list=[]   
            try :    
                data_dict = response.json()      
                print(CGREENBG2 + "JSON Data fetched successfully" + CEND)
    
            except ValueError as e: 
                raise Exception('Invalid JSON format',e )
    
            else: 
                print ("Error fetching JSON (Ignore if it still works)!")
        
            #print("\nData Dictionary:\n",json.dumps(data_dict))

            value1a = data_dict["player"]["stats"]["Duels"][gamemode + "_duel_wins"]

            valuewlr1 = data_dict["player"]["stats"]["Duels"][gamemode + "_duel_losses"]

            print(gamemode + "Duel Wins:", data_dict["player"]["stats"]["Duels"][gamemode + "_duel_wins"])

            difference = value1a
        
            difference = value1a - value2a

            winstreak = winstreak + difference

            if valuewlr1 != valuewlr:
                 winstreak = 0

            if winstreak > 5000:
                winstreak = winstreak - value1a

            wlr = value1a / valuewlr1
            wlr_round = round(wlr, 2)

            value1a = str(value1a)
            value2a = str(value2a)
            difference = str(difference)
            wlr_round = str(wlr_round)
            winstreak = str(winstreak)

            embed = discord.Embed
            embed = discord.Embed(title="tracker ⛤", description="```" + gamemodebig +" wins for " + ign + ": "+ value1a + " (+" + difference + ") \n" + "WLR: " + wlr_round + "\nEstimated Winstreak: " + winstreak + "```", color=discord.Colour.blue())
            embed.set_thumbnail(url="https://mc-heads.net/body/" + uuidplayer + "/50")
            embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://images-ext-1.discordapp.net/external/g1FieBBXQwG4GdgupVLaJoMN7ZtO5-GVgWnI_O9YJaI/https/i.pinimg.com/originals/61/1b/69/611b693be05344bcab472607f356787f.gif?width=900&height=1131")
            components=[
                discord.ui.Button(label="Disconnect", style=discord.ButtonStyle.danger, custom_id="disconnect"),
                ]

            await inter.channel.send(embed=embed, components=components)

            print("\n" + CGREENBG2 + "Sent an Embed! (Tracker Message 1)" + CEND)


            @bot.listen("on_button_click")
            async def help_listener(inter: discord.MessageInteraction):
                    PROCNAME = "javaw.exe"
                    for proc in psutil.process_iter():
                        if proc.name() == PROCNAME:
                            proc.kill()
                    await inter.response.send_message("Disconnected!")

            

            value1a = int(value1a)
            value2a = int(value2a)
            difference = int(difference)
            winstreak = int(winstreak)

            await asyncio.sleep(delay)
        
            url = "https://api.hypixel.net/player?key=" + apikey + "&uuid=" + uuidplayer #example API endpoint for todo list app 
            response = requests.get(url)  #fetching contents from api end point  
            data_dict= {}   #creating empty dictionary object  
            if (response):   
                data_list=[]     
            try :    
                data_dict = response.json()      
                print(CGREENBG2 + "JSON Data fetched successfully" + CEND)
    
            except ValueError as e: 
                raise Exception('Invalid JSON format',e )
    
            print ("Error fetching JSON (Ignore if it still works)!")
        
            #print("\nData Dictionary:\n",json.dumps(data_dict))
            print(gamemode + "Duel Wins:", data_dict["player"]["stats"]["Duels"][gamemode + "_duel_wins"])
            value2a = data_dict["player"]["stats"]["Duels"][gamemode + "_duel_wins"]
            valuewlr = data_dict["player"]["stats"]["Duels"][gamemode + "_duel_losses"]

            wlr = value2a / valuewlr
            wlr_round = round(wlr, 2)
            difference = value2a - value1a    
            winstreak = winstreak + difference

            if winstreak > 5000:
                winstreak = winstreak - value1a

            if  valuewlr != valuewlr1:
                 winstreak = 0

            value1a = str(value1a)
            value2a = str(value2a)
            difference = str(difference)
            wlr_round = str(wlr_round)
            winstreak = str(winstreak)

            embed = discord.Embed
            embed = discord.Embed(title="tracker ⛤", description="```" + gamemodebig +" wins for " + ign + ": "+ value2a + " (+" + difference + ") \n" + "WLR: " + wlr_round + "\nEstimated Winstreak: " + winstreak + "```", color=discord.Colour.blue())
            embed.set_thumbnail(url="https://mc-heads.net/body/" + uuidplayer + "/50")
            embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://images-ext-1.discordapp.net/external/g1FieBBXQwG4GdgupVLaJoMN7ZtO5-GVgWnI_O9YJaI/https/i.pinimg.com/originals/61/1b/69/611b693be05344bcab472607f356787f.gif?width=900&height=1131")
            components=[
                discord.ui.Button(label="Disconnect", style=discord.ButtonStyle.danger, custom_id="disconnect"),
                ]

            await inter.channel.send(embed=embed, components=components)

            print("\n" + CGREENBG2 + "Sent an Embed! (Tracker Message 2)" + CEND)


            @bot.listen("on_button_click")
            async def help_listener(inter: discord.MessageInteraction):
                    PROCNAME = "javaw.exe"
                    for proc in psutil.process_iter():
                        if proc.name() == PROCNAME:
                            proc.kill()
                    await inter.response.send_message("Disconnected!")

           
    
            value1a = int(value1a)
            value2a = int(value2a)
            difference = int(difference)
            winstreak = int(winstreak)

            await asyncio.sleep(delay)   

@bot.slash_command(name="modewins")
async def wins(inter, gamemode : str, ign : str):
            await inter.response.send_message("⠀")
            apikey = "APIKEY"

            try:
                resp = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{ign}")
                uuidplayer = resp.json()["id"]
            except KeyError:
                embed = discord.Embed
                embed = discord.Embed(title="tracker ⛤", description="```This player doesn't exist!```", color=discord.Colour.blue())
                embed.set_thumbnail(url="https://mc-heads.net/body/1ca05403f5a24b74840d6f4eba6e3c27/50")
                embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://images-ext-1.discordapp.net/external/g1FieBBXQwG4GdgupVLaJoMN7ZtO5-GVgWnI_O9YJaI/https/i.pinimg.com/originals/61/1b/69/611b693be05344bcab472607f356787f.gif?width=900&height=1131")
                await inter.channel.send(embed=embed)
                print("\n" + CYELLOWBG2 + "Sent an Embed! (KeyError)" + CEND)

            chan=bot.get_channel(1139507742042763274)
            url = "https://api.hypixel.net/player?key=" + apikey + "&uuid=" + uuidplayer #example API endpoint for todo list app 
            response = requests.get(url) #fetching contents from api end point  
            data_dict_wins= {}   #creating empty dictionary object  
            if (response):   
                data_list=[]     
            try :    
                data_dict = response.json()      
                print("JSON Data fetched successfully")
    
            except ValueError as e: 
                raise Exception('Invalid JSON format',e )
    
            print ("Error fetching JSON (Ignore if it still works)!")
        
            #print("\nData Dictionary:\n",json.dumps(data_dict_wins))

            
            try:
                print(gamemode + "Duel Wins:", data_dict["player"]["stats"]["Duels"][gamemode + "_duel_wins"])
                value_wins = data_dict["player"]["stats"]["Duels"][gamemode + "_duel_wins"]
                value_losses = data_dict["player"]["stats"]["Duels"][gamemode + "_duel_losses"]

                
                wlr = value_wins / value_losses
                wlr = round(wlr, 2)

                value_wins = str(value_wins)
                wlr = str(wlr)
                gamemodebig = gamemode.capitalize()

                embed = discord.Embed
                embed = discord.Embed(title="tracker ⛤", description="```" + gamemodebig +" wins for " + ign + ": "+ value_wins + "\n" + "WLR: " + wlr + "```", color=discord.Colour.blue())
                embed.set_thumbnail(url="https://mc-heads.net/body/" + uuidplayer + "/50")
                embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://images-ext-1.discordapp.net/external/g1FieBBXQwG4GdgupVLaJoMN7ZtO5-GVgWnI_O9YJaI/https/i.pinimg.com/originals/61/1b/69/611b693be05344bcab472607f356787f.gif?width=900&height=1131")
                components=[
                    discord.ui.Button(label="Disconnect", style=discord.ButtonStyle.danger, custom_id="disconnect"),
                    ]

                await inter.channel.send(embed=embed, components=components)

                print("\n" + CGREENBG2 + "Sent an Embed! (ModeWins)" + CEND)

            except KeyError:
                embed = discord.Embed
                embed = discord.Embed(title="tracker ⛤", description="```The player either has never played this gamemode! (Or you stated a unsupported Gamemode)```", color=discord.Colour.blue())
                embed.set_thumbnail(url="https://mc-heads.net/body/" + uuidplayer + "/50")
                embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://images-ext-1.discordapp.net/external/g1FieBBXQwG4GdgupVLaJoMN7ZtO5-GVgWnI_O9YJaI/https/i.pinimg.com/originals/61/1b/69/611b693be05344bcab472607f356787f.gif?width=900&height=1131")
                await inter.channel.send(embed=embed)

                print("\n" + CYELLOWBG2 + "Sent an Embed! (KeyError)" + CEND)


            @bot.listen("on_button_click")
            async def help_listener(inter: discord.MessageInteraction):
                    PROCNAME = "javaw.exe"
                    for proc in psutil.process_iter():
                        if proc.name() == PROCNAME:
                            proc.kill()
                    await inter.response.send_message("Disconnected!")
            
           

@bot.slash_command(name="wins")
async def wins(inter, ign : str):
            await inter.response.send_message("⠀")
            apikey = "APIKEY"

            try:
                resp = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{ign}")
                uuidplayer = resp.json()["id"]
            except KeyError:
                embed = discord.Embed
                embed = discord.Embed(title="tracker ⛤", description="```This player doesn't exist!```", color=discord.Colour.blue())
                embed.set_thumbnail(url="https://mc-heads.net/body/1ca05403f5a24b74840d6f4eba6e3c27/50")
                embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://images-ext-1.discordapp.net/external/g1FieBBXQwG4GdgupVLaJoMN7ZtO5-GVgWnI_O9YJaI/https/i.pinimg.com/originals/61/1b/69/611b693be05344bcab472607f356787f.gif?width=900&height=1131")
                await inter.channel.send(embed=embed)
                print("\n" + CYELLOWBG2 + "Sent an Embed! (KeyError)" + CEND)

            chan=bot.get_channel(1139507742042763274)
            url = "https://api.hypixel.net/player?key=" + apikey + "&uuid=" + uuidplayer #example API endpoint for todo list app 
            response = requests.get(url) #fetching contents from api end point  
            data_dict_wins= {}   #creating empty dictionary object  
            if (response):   
                data_list=[]     
            try :    
                data_dict = response.json()      
                print(CGREENBG2 + "JSON Data fetched successfully" + CEND)
    
            except ValueError as e: 
                raise Exception('Invalid JSON format',e )
    
            print ("Error fetching JSON (Ignore if it still works)!")
        
            #print("\nData Dictionary:\n",json.dumps(data_dict_wins))

            
            try:
                print("Duel Wins:", data_dict["player"]["stats"]["Duels"]["wins"])
                value_wins = data_dict["player"]["stats"]["Duels"]["wins"]
                value_losses = data_dict["player"]["stats"]["Duels"]["losses"]

                
                wlr = value_wins / value_losses
                wlr = round(wlr, 2)

                value_wins = str(value_wins)
                wlr = str(wlr)

                embed = discord.Embed
                embed = discord.Embed(title="tracker ⛤", description="```Duels wins for " + ign + ": "+ value_wins + "\n" + "WLR: " + wlr + "```", color=discord.Colour.blue())
                embed.set_thumbnail(url="https://mc-heads.net/body/" + uuidplayer + "/50")
                embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://images-ext-1.discordapp.net/external/g1FieBBXQwG4GdgupVLaJoMN7ZtO5-GVgWnI_O9YJaI/https/i.pinimg.com/originals/61/1b/69/611b693be05344bcab472607f356787f.gif?width=900&height=1131")
                components=[
                    discord.ui.Button(label="Disconnect", style=discord.ButtonStyle.danger, custom_id="disconnect"),
                    ]

                await inter.channel.send(embed=embed, components=components)

                print("\n" + CGREENBG2 + "Sent an Embed! (Wins)" + CEND)

            except TypeError:
                embed = discord.Embed
                embed = discord.Embed(title="tracker ⛤", description="```The player has never played Duels!```", color=discord.Colour.blue())
                embed.set_thumbnail(url="https://mc-heads.net/body/" + uuidplayer + "/50")
                embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://images-ext-1.discordapp.net/external/g1FieBBXQwG4GdgupVLaJoMN7ZtO5-GVgWnI_O9YJaI/https/i.pinimg.com/originals/61/1b/69/611b693be05344bcab472607f356787f.gif?width=900&height=1131")
                await inter.channel.send(embed=embed)

                print("\n" + CYELLOWBG2 + "Sent an Embed! (KeyError)" + CEND)


            @bot.listen("on_button_click")
            async def help_listener(inter: discord.MessageInteraction):
                    PROCNAME = "javaw.exe"
                    for proc in psutil.process_iter():
                        if proc.name() == PROCNAME:
                            proc.kill()
                    await inter.response.send_message("Disconnected!")
            
            

@bot.slash_command(name="status")
async def wins(inter, ign : str):
            await inter.response.send_message("⠀")
            apikey = "APIKEY"

            try:
                resp = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{ign}")
                uuidplayer = resp.json()["id"]
            except KeyError:
                embed = discord.Embed
                embed = discord.Embed(title="tracker ⛤", description="```This player doesn't exist!```", color=discord.Colour.blue())
                embed.set_thumbnail(url="https://mc-heads.net/body/1ca05403f5a24b74840d6f4eba6e3c27/50")
                embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://images-ext-1.discordapp.net/external/g1FieBBXQwG4GdgupVLaJoMN7ZtO5-GVgWnI_O9YJaI/https/i.pinimg.com/originals/61/1b/69/611b693be05344bcab472607f356787f.gif?width=900&height=1131")
                await inter.channel.send(embed=embed)

                print("\n" + CYELLOWBG2 + "Sent an Embed! (KeyError)" + CEND)
    
            chan=bot.get_channel(1139507742042763274)
            url = "https://api.hypixel.net/status?key=" + apikey + "&uuid=" + uuidplayer #example API endpoint for todo list app 
            response = requests.get(url)  #fetching contents from api end point  
            data_dict_wins= {}   #creating empty dictionary object  
            if (response):   
                data_list=[]     
            try :    
                data_dict_wins = response.json()      
                print(CGREENBG2 + "JSON Data fetched successfully" + CEND)
    
            except ValueError as e: 
                raise Exception('Invalid JSON format',e )
    
            print ("Error fetching JSON (Ignore if it still works)!")
        
            #print("\nData Dictionary:\n",json.dumps(data_dict_wins))

            status = "N/A"
            location_gamemode = "N/A"
            location_map = "N/A"
            location_submode = "N/A"

            status = data_dict_wins["session"]["online"]
            
            if status == True:
                if "map" in data_dict_wins["session"]:
                    location_map = data_dict_wins["session"]["map"]

                if "mode" in data_dict_wins["session"]:
                    location_submode = data_dict_wins["session"]["mode"]
                
                location_gamemode = data_dict_wins["session"]["gameType"]
                embed = discord.Embed
                embed = discord.Embed(title="tracker ⛤", description="```" + ign + " is currently playing " + location_gamemode + ", " + location_submode + " on " + location_map + ".```", color=discord.Colour.blue())
                embed.set_thumbnail(url="https://mc-heads.net/body/" + uuidplayer + "/50")
                embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://images-ext-1.discordapp.net/external/g1FieBBXQwG4GdgupVLaJoMN7ZtO5-GVgWnI_O9YJaI/https/i.pinimg.com/originals/61/1b/69/611b693be05344bcab472607f356787f.gif?width=900&height=1131")
                await inter.channel.send(embed=embed)

                print("\n" + CGREENBG2 + "Sent an Embed! (Player online)" + CEND)

            
            else :
                embed = discord.Embed
                embed = discord.Embed(title="tracker ⛤", description="```" + ign + " is offline or hiding their status.```", color=discord.Colour.blue())
                embed.set_thumbnail(url="https://mc-heads.net/body/" + uuidplayer + "/50")
                embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://images-ext-1.discordapp.net/external/g1FieBBXQwG4GdgupVLaJoMN7ZtO5-GVgWnI_O9YJaI/https/i.pinimg.com/originals/61/1b/69/611b693be05344bcab472607f356787f.gif?width=900&height=1131")
                await inter.channel.send(embed=embed)

                print("\n" + CGREENBG2 + "Sent an Embed! (Player offline)" + CEND)

            
@bot.slash_command(name="staffbans")
async def wins(inter, delay : int):
            await inter.response.send_message("⠀")
            
            loop = 1

            bans1 = 0
            bans2 = 0
            bans1_calc = 0
            bans2_calc = 0
            apikey = "APIKEY"

            while loop == 1:
            
                chan=bot.get_channel(1139507742042763274)
                url = "https://api.hypixel.net/v2/punishmentstats?key=" + apikey  #example API endpoint for todo list app 
                response = requests.get(url)  #fetching contents from api end point  
                data_dict_wins= {}   #creating empty dictionary object  
                if (response):   
                    data_list=[]     
                try :    
                    data_dict_wins = response.json()      
                    print(CGREENBG2 + "JSON Data fetched successfully" + CEND)
    
                except ValueError as e: 
                    raise Exception('Invalid JSON format',e )
    
                print ("Error fetching JSON (Ignore if it still works)!")
                bans1 = data_dict_wins["staff_rollingDaily"]
            
                bans1_calc = bans2 - bans1
                print(bans1_calc)

                bans1_calc = str(bans1_calc)
                delay = str(delay)
                #SEND EMBED
                embed = discord.Embed
                embed = discord.Embed(title="tracker ⛤", description="```Staff have banned " + bans1_calc + " Player(s) in the last " + delay + "s```", color=discord.Colour.blue())
                embed.set_thumbnail(url="https://mc-heads.net/avatar/ec07182556b444d38e9af48bf74bde82/50/")
                embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://images-ext-1.discordapp.net/external/g1FieBBXQwG4GdgupVLaJoMN7ZtO5-GVgWnI_O9YJaI/https/i.pinimg.com/originals/61/1b/69/611b693be05344bcab472607f356787f.gif?width=900&height=1131")
                await inter.channel.send(embed=embed)

                delay = int(delay)
                bans1_calc = int(bans1_calc)

                await asyncio.sleep(delay)

                url = "https://api.hypixel.net/v2/punishmentstats?key=" + apikey  #example API endpoint for todo list app 
                response = requests.get(url)  #fetching contents from api end point  
                data_dict_wins= {}   #creating empty dictionary object  
                if (response):   
                    data_list=[]     
                try :    
                    data_dict_wins = response.json()      
                    print(CGREENBG2 + "JSON Data fetched successfully" + CEND)
    
                except ValueError as e: 
                    raise Exception('Invalid JSON format',e )
    
                print ("Error fetching JSON (Ignore if it still works)!")

                bans2 = data_dict_wins["staff_rollingDaily"]

                bans2_calc = bans1 - bans2
                print(bans2_calc)

                bans2_calc = str(bans2_calc)
                delay = str(delay)

                #SEND EMBED
                embed = discord.Embed
                embed = discord.Embed(title="tracker ⛤", description="```Staff have banned " + bans2_calc + " Player(s) in the last " + delay + "s```", color=discord.Colour.blue())
                embed.set_thumbnail(url="https://mc-heads.net/avatar/ec07182556b444d38e9af48bf74bde82/50/")
                embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://images-ext-1.discordapp.net/external/g1FieBBXQwG4GdgupVLaJoMN7ZtO5-GVgWnI_O9YJaI/https/i.pinimg.com/originals/61/1b/69/611b693be05344bcab472607f356787f.gif?width=900&height=1131")
                await inter.channel.send(embed=embed)

                delay = int(delay)
                bans2_calc = int(bans2_calc)

                await asyncio.sleep(delay)

@bot.slash_command(name="session")
async def wins(inter, ign : str, delay : int):
            await inter.response.send_message("⠀")
            apikey = "APIKEY"

            try:
                resp = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{ign}")
                uuidplayer = resp.json()["id"]
            except KeyError:
                embed = discord.Embed
                embed = discord.Embed(title="tracker ⛤", description="```This player doesn't exist!```", color=discord.Colour.blue())
                embed.set_thumbnail(url="https://mc-heads.net/body/1ca05403f5a24b74840d6f4eba6e3c27/50")
                embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://images-ext-1.discordapp.net/external/g1FieBBXQwG4GdgupVLaJoMN7ZtO5-GVgWnI_O9YJaI/https/i.pinimg.com/originals/61/1b/69/611b693be05344bcab472607f356787f.gif?width=900&height=1131")
                await inter.channel.send(embed=embed)
                print("\n" + CYELLOWBG2 + "Sent an Embed! (KeyError)" + CEND)

            chan=bot.get_channel(1139507742042763274)
            url = "https://api.hypixel.net/player?key=" + apikey + "&uuid=" + uuidplayer #example API endpoint for todo list app 
            response = requests.get(url) #fetching contents from api end point  
            data_dict_wins= {}   #creating empty dictionary object  
            if (response):   
                data_list=[]     
            try :    
                data_dict = response.json()      
                print(CGREENBG2 + "JSON Data fetched successfully" + CEND)
    
            except ValueError as e: 
                raise Exception('Invalid JSON format',e )
    
            print ("Error fetching JSON (Ignore if it still works)!")
        
            #print("\nData Dictionary:\n",json.dumps(data_dict_wins))

            
            try:
                print("Duel Wins:", data_dict["player"]["stats"]["Duels"]["wins"])
                value_wins_start = data_dict["player"]["stats"]["Duels"]["wins"]
                value_losses = data_dict["player"]["stats"]["Duels"]["losses"]

                
                wlr = value_wins_start / value_losses
                wlr = round(wlr, 2)
                delay_intern = delay*60

                delay = str(delay)
                value_wins_start_print = str(value_wins_start)
                wlr_print = str(wlr)                

                embed = discord.Embed
                embed = discord.Embed(title="tracker ⛤", description="```Duels wins at the start for " + ign + ": "+ value_wins_start_print + "\n" + "WLR: " + wlr_print + "\nWe will track your wins for " + delay + " minutes." +"```", color=discord.Colour.blue())
                embed.set_thumbnail(url="https://mc-heads.net/body/" + uuidplayer + "/50")
                embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://images-ext-1.discordapp.net/external/g1FieBBXQwG4GdgupVLaJoMN7ZtO5-GVgWnI_O9YJaI/https/i.pinimg.com/originals/61/1b/69/611b693be05344bcab472607f356787f.gif?width=900&height=1131")
                components=[
                    discord.ui.Button(label="Disconnect", style=discord.ButtonStyle.danger, custom_id="disconnect"),
                    ]

                await inter.channel.send(embed=embed, components=components)

                print("\n" + CGREENBG2 + "Sent an Embed! (Tracking Wins Start)" + CEND)
                
                await asyncio.sleep(delay_intern)

                url = "https://api.hypixel.net/player?key=" + apikey + "&uuid=" + uuidplayer #example API endpoint for todo list app 
                response = requests.get(url) #fetching contents from api end point  
                data_dict_wins= {}   #creating empty dictionary object  
                if (response):   
                    data_list=[]     
                try :    
                    data_dict = response.json()      
                    print(CGREENBG2 + "JSON Data fetched successfully" + CEND)
    
                except ValueError as e: 
                    raise Exception('Invalid JSON format',e )
    
                print ("Error fetching JSON (Ignore if it still works)!")

                print("Duel Wins:", data_dict["player"]["stats"]["Duels"]["wins"])
                value_wins_end = data_dict["player"]["stats"]["Duels"]["wins"]
                value_losses = data_dict["player"]["stats"]["Duels"]["losses"]
                
                wlr_end = value_wins_end / value_losses
                wlr_end = round(wlr, 2)

                difference_wins = value_wins_end - value_wins_start
                difference_wlr = wlr_end - wlr

                delay = str(delay)
                value_wins_end = str(value_wins_end)
                wlr_end = str(wlr_end)
                difference_wlr = (format(difference_wlr, '+'))
                difference_wins = str(difference_wins)

                embed = discord.Embed
                embed = discord.Embed(title="tracker ⛤", description="```Duels wins for " + ign + " after " + delay + " minutes: "+ value_wins_end + " (+" + difference_wins + ") \n" + "WLR: " + wlr_end + " (" + difference_wlr + ")```", color=discord.Colour.blue())
                embed.set_thumbnail(url="https://mc-heads.net/body/" + uuidplayer + "/50")
                embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://images-ext-1.discordapp.net/external/g1FieBBXQwG4GdgupVLaJoMN7ZtO5-GVgWnI_O9YJaI/https/i.pinimg.com/originals/61/1b/69/611b693be05344bcab472607f356787f.gif?width=900&height=1131")
                components=[
                    discord.ui.Button(label="Disconnect", style=discord.ButtonStyle.danger, custom_id="disconnect"),
                    ]

                await inter.channel.send(embed=embed, components=components)

                print("\n" + CGREENBG2 + "Sent an Embed! (Tracking Wins End)" + CEND)

            except KeyError:
                embed = discord.Embed
                embed = discord.Embed(title="tracker ⛤", description="```The player has never played Duels!```", color=discord.Colour.blue())
                embed.set_thumbnail(url="https://mc-heads.net/body/" + uuidplayer + "/50")
                embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://images-ext-1.discordapp.net/external/g1FieBBXQwG4GdgupVLaJoMN7ZtO5-GVgWnI_O9YJaI/https/i.pinimg.com/originals/61/1b/69/611b693be05344bcab472607f356787f.gif?width=900&height=1131")
                await inter.channel.send(embed=embed)

                print(CYELLOW2 + "\nSent an Embed! (TypeError)" + CEND)


            @bot.listen("on_button_click")
            async def help_listener(inter: discord.MessageInteraction):
                    PROCNAME = "javaw.exe"
                    for proc in psutil.process_iter():
                        if proc.name() == PROCNAME:
                            proc.kill()
                    await inter.response.send_message("Disconnected!")

@bot.slash_command(name="dev", description="help command")
async def help(inter):
        await inter.response.defer(ephemeral=True, with_message=False)
        chan=bot.get_channel(1139507742042763274)
        embed = discord.Embed
        embed = discord.Embed(title="tracker ⛤", description="developed by ui (l77l) and a friend :smirk_cat:", color=discord.Colour.blue())
        embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://images-ext-1.discordapp.net/external/g1FieBBXQwG4GdgupVLaJoMN7ZtO5-GVgWnI_O9YJaI/https/i.pinimg.com/originals/61/1b/69/611b693be05344bcab472607f356787f.gif?width=900&height=1131")
        await inter.channel.send(embed=embed)

        print("\n" + CGREENBG2 + "Sent an Embed! (DEV)" + CEND)

bot.run('BOTKEY')
