# Fooocus-discord-autopublish-docker
#### Description
This Python script uses the `discord.py` library to create a Discord bot that monitors a specific folder and automatically sends new files (images) to a specified Discord channel. It employs `watchdog` for file monitoring and `asyncio` for asynchronous operations.

#### Features
- Automatically monitors a specific folder for new image files.
- Automatically sends new image files to a specified Discord channel.
- Handles errors and validates the presence of necessary environment variables.

#### Prerequisites
- Python 3.6 or higher.
- `discord.py` and `watchdog` libraries installed.
- A Discord bot token and channel ID, set as environment variables.

#### Configuration
1. Set the environment variables for docker or else `DISCORD_TOKEN` and `DISCORD_CHANNEL_ID` with your Discord bot token and the ID of the channel where images will be sent.
2. Modify `BASE_DIRECTORY` to point to the folder you want to monitor.

#### Usage
1. Run the script. The bot will connect to Discord and start monitoring the specified folder.
2. Place image files in the folder. The bot will detect new files and send them to the specified Discord channel.

#### Operation
- The bot checks the specified folder every 30 seconds for new files.
- New image files are automatically sent to the Discord channel.
- The script handles errors related to Discord connectivity or file monitoring.

#### Notes
- Ensure the bot has the necessary permissions on the Discord server to send messages and files.
- The script is designed to work with images but can be modified to support other file types.
