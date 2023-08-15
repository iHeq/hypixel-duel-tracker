import disnake as discord
from disnake.ext import commands, tasks
from disnake import TextInputStyle
import json
import requests
import time
import os
import psutil
import asyncio

client = discord.Client()

bot = commands.Bot(command_prefix = '!',
                   case_insensitive = True,
                   intents = discord.Intents().all(),
                   help_command = None,
                   strip_after_prefix = True,
                   status = discord.Status.online)

chan=bot.get_channel(1139507742042763274)

@bot.event
async def on_ready():
    print(f'{str(bot.user)} Connected')

global ign
global gamemode
global delay

#BOT LAUNCH
    
@bot.slash_command(name="tracker") 
async def tracker(inter, delay : int, gamemode : str, ign : str):
         await inter.response.defer(ephemeral=True, with_message=False)
         chan=bot.get_channel(1139507742042763274)
         os.system('cls')

         print("\n████████╗██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░")
         print("╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗")
         print("░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝")
         print("░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗")
         print("░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║")
         print("░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝")
         print("                                             made by ui<3\n")

         difference = 0
         loop = 1    

         value1a = 0
         value2a = 0

         delay = int(delay)
         apikey = "hypixel-api-key"

         resp = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{ign}")
         uuidplayer = resp.json()["id"]

         print("\n------------------------------------------------------")     

         embed = discord.Embed
         embed = discord.Embed(title="tracker ⛤", description="tracker launched successfully", color=discord.Colour.green())
         embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://cdn.discordapp.com/avatars/347327358019305474/55733aaa64c43ec2ea636bada745f1fe.webp?size=240")

         components=[
                 discord.ui.Button(label="Disconnect", style=discord.ButtonStyle.danger, custom_id="disconnect"),
                 ]

         await inter.channel.send(embed=embed, components=components)

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
                print("JSON Data fetched successfully")
    
            except ValueError as e: 
                raise Exception('Invalid JSON format',e )
    
            else: 
                print ("Error fetching JSON (Ignore if it still works)!")
        
            #print("\nData Dictionary:\n",json.dumps(data_dict))
            print("Boxing Duel Wins:", data_dict["player"]["stats"]["Duels"][gamemode + "_duel_wins"])
            value1a = data_dict["player"]["stats"]["Duels"][gamemode + "_duel_wins"]
        
            difference = value1a - value2a

            value1a = str(value1a)
            value2a = str(value2a)
            difference = str(difference)
            
            embed = discord.Embed
            embed = discord.Embed(title="tracker ⛤", description="```" + gamemode + " wins for " + ign + ": "+ value1a + " (+" + difference + ")" + "```", color=discord.Colour.blue())
            embed.set_thumbnail(url="https://mc-heads.net/avatar/" + uuidplayer + "/50")
            embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://cdn.discordapp.com/avatars/347327358019305474/55733aaa64c43ec2ea636bada745f1fe.webp?size=240")
            components=[
                discord.ui.Button(label="Disconnect", style=discord.ButtonStyle.danger, custom_id="disconnect"),
                ]

            await inter.channel.send(embed=embed, components=components)

            @bot.listen("on_button_click")
            async def help_listener(inter: discord.MessageInteraction):
                    PROCNAME = "javaw.exe"
                    for proc in psutil.process_iter():
                        if proc.name() == PROCNAME:
                            proc.kill()
                    await inter.response.send_message("Disconnected!")

            print("Success! Message sent.\n------------------------------------------------------")

            value1a = int(value1a)
            value2a = int(value2a)
            difference = int(difference)
        
            await asyncio.sleep(delay)
        
            url = "https://api.hypixel.net/player?key=" + apikey + "&uuid=" + uuidplayer #example API endpoint for todo list app 
            response = requests.get(url)  #fetching contents from api end point  
            data_dict= {}   #creating empty dictionary object  
            if (response):   
                data_list=[]     
            try :    
                data_dict = response.json()      
                print("JSON Data fetched successfully")
    
            except ValueError as e: 
                raise Exception('Invalid JSON format',e )
    
            print ("Error fetching JSON (Ignore if it still works)!")
        
            #print("\nData Dictionary:\n",json.dumps(data_dict))
            print("Boxing Duel Wins:", data_dict["player"]["stats"]["Duels"][gamemode + "_duel_wins"])
            value2a = data_dict["player"]["stats"]["Duels"][gamemode + "_duel_wins"]

            difference = value2a - value1a

            value1a = str(value1a)
            value2a = str(value2a)
            difference = str(difference)
        
            embed = discord.Embed
            embed = discord.Embed(title="tracker ⛤", description="```" + gamemode +" wins for " + ign + ": "+ value2a + " (+" + difference + ")" + "```", color=discord.Colour.blue())
            embed.set_thumbnail(url="https://mc-heads.net/avatar/" + uuidplayer + "/50")
            embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://cdn.discordapp.com/avatars/347327358019305474/55733aaa64c43ec2ea636bada745f1fe.webp?size=240")
            components=[
                discord.ui.Button(label="Disconnect", style=discord.ButtonStyle.danger, custom_id="disconnect"),
                ]

            await inter.channel.send(embed=embed, components=components)

            @bot.listen("on_button_click")
            async def help_listener(inter: discord.MessageInteraction):
                    PROCNAME = "javaw.exe"
                    for proc in psutil.process_iter():
                        if proc.name() == PROCNAME:
                            proc.kill()
                    await inter.response.send_message("Disconnected!")

            print("Success! Message sent.\n------------------------------------------------------")
    
            value1a = int(value1a)
            value2a = int(value2a)
            difference = int(difference)

            await asyncio.sleep(delay)   

@bot.slash_command(name="wins")
async def wins(inter, gamemode : str, ign : str):
            await inter.response.defer(ephemeral=True, with_message=False)
            apikey = "hypixel-api-key"

            resp = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{ign}")
            uuidplayer = resp.json()["id"]
    
            chan=bot.get_channel(1139507742042763274)
            url = "https://api.hypixel.net/player?key=" + apikey + "&uuid=" + uuidplayer #example API endpoint for todo list app 
            response = requests.get(url)  #fetching contents from api end point  
            data_dict_wins= {}   #creating empty dictionary object  
            if (response):   
                data_list=[]     
            try :    
                data_dict_wins = response.json()      
                print("JSON Data fetched successfully")
    
            except ValueError as e: 
                raise Exception('Invalid JSON format',e )
    
            print ("Error fetching JSON (Ignore if it still works)!")
        
            #print("\nData Dictionary:\n",json.dumps(data_dict_wins))
            print("Boxing Duel Wins:", data_dict_wins["player"]["stats"]["Duels"][gamemode + "_duel_wins"])
            value_wins = data_dict_wins["player"]["stats"]["Duels"][gamemode + "_duel_wins"]
            
            value_wins = str(value_wins)
        
            embed = discord.Embed
            embed = discord.Embed(title="tracker ⛤", description="```" + gamemode + " wins for " + ign + ": "+ value_wins + "```", color=discord.Colour.blue())
            embed.set_thumbnail(url="https://mc-heads.net/avatar/" + uuidplayer + "/50")
            embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://cdn.discordapp.com/avatars/347327358019305474/55733aaa64c43ec2ea636bada745f1fe.webp?size=240")
            components=[
                discord.ui.Button(label="Disconnect", style=discord.ButtonStyle.danger, custom_id="disconnect"),
                ]

            await inter.channel.send(embed=embed, components=components)

            @bot.listen("on_button_click")
            async def help_listener(inter: discord.MessageInteraction):
                    PROCNAME = "javaw.exe"
                    for proc in psutil.process_iter():
                        if proc.name() == PROCNAME:
                            proc.kill()
                    await inter.response.send_message("Disconnected!")
            
            print("Success! Message sent.\n------------------------------------------------------")
            
@bot.slash_command(name="dev", description="help command")
async def help(inter):
        await inter.response.defer(ephemeral=True, with_message=False)
        chan=bot.get_channel(1139507742042763274)
        embed = discord.Embed
        embed = discord.Embed(title="tracker ⛤", description="developed by ui (l77l) and a friend :smirk_cat:", color=discord.Colour.blue())
        embed.set_footer(text="made with ♡ by ui (l77l)", icon_url="https://cdn.discordapp.com/avatars/347327358019305474/55733aaa64c43ec2ea636bada745f1fe.webp?size=240")
        await inter.channel.send(embed=embed)

            
bot.run('discord-bot-token')
