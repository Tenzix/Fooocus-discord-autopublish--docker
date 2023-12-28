import os
import asyncio
import discord
from discord.ext import commands
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from discord.ext import commands, tasks
from datetime import datetime

TOKEN = os.getenv('DISCORD_TOKEN')  # Lire le token depuis la variable d'environnement
if not TOKEN:
    raise ValueError("Le token Discord n'est pas défini dans la variable d'environnement DISCORD_TOKEN")


CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')
if not CHANNEL_ID:
    raise ValueError("Le CHANNEL_ID Discord n'est pas défini dans la variable d'environnement DISCORD_CHANNEL_ID")
else:
    CHANNEL_ID = int(CHANNEL_ID)  # Convertir en entier

BASE_DIRECTORY = "/Fooocus/outputs/"

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Initialiser l'ensemble des fichiers déjà présents
existing_files = set()

def get_directory_to_watch():
    # Obtenir la date du jour et construire le chemin du dossier
    today_date = datetime.now().strftime("%Y-%m-%d")
    return os.path.join(BASE_DIRECTORY, today_date)

async def send_new_files():
    directory_to_watch = get_directory_to_watch()
    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        print(f"Canal non trouvé: {CHANNEL_ID}")
        return

    try:
        # Liste des fichiers dans le dossier
        current_files = set(os.listdir(directory_to_watch))
        new_files = current_files - existing_files
        for file_name in new_files:
            if file_name.endswith((".png", ".jpg", ".jpeg")):
                file_path = os.path.join(directory_to_watch, file_name)
                await channel.send(file=discord.File(file_path))
                print(f"Fichier envoyé: {file_path}")
                existing_files.add(file_name)
    except Exception as e:
        print(f"Erreur: {e}")

@tasks.loop(seconds=30)  # Vérifie le dossier toutes les 30 secondes
async def check_new_files():
    await send_new_files()

@bot.event
async def on_ready():
    global existing_files
    print(f'{bot.user.name} est connecté au serveur.')

    # Charger l'ensemble initial des fichiers déjà présents
    directory_to_watch = get_directory_to_watch()
    if os.path.exists(directory_to_watch):
        existing_files = set(os.listdir(directory_to_watch))
    else:
        os.makedirs(directory_to_watch)
        existing_files = set()

    # Démarrer la tâche de fond
    check_new_files.start()

bot.run(TOKEN)
