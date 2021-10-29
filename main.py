import discord
import os
from maze import init_maze, generate_maze, message_maze, debug_print_maze

client = discord.Client()
info = 'Olá, eu sou o xadu_bot e tenho vários comandos a seu dispor:\n\n - &velha @pessoa1 @pessoa2: inicio um desafio de jogo da velha entre a @pessoa1 e a @pessoa2'


@client.event
async def on_ready():
    print('[LISTENING] Logado e escutando como {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$maze'):
        maze = generate_maze()
        gen_message = message_maze(maze)
        gen_message += '3 ❤️'
        debug_print_maze(maze)
        await message.channel.send(gen_message)

print('[START] Iniciando xadu_bot...')

#Runs the bot
client.run(os.environ['TOKEN'])