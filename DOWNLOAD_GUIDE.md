# How to Download Your Discord Music Bot

This guide will help you download all the necessary files from this Replit project to deploy your Discord music bot officially.

## Method 1: Download as ZIP (Recommended)

1. In Replit, click on the three dots (⋮) in the file explorer
2. Select "Download as ZIP"
3. This will download all project files to your computer

## Method 2: Use Git

If you prefer using Git, you can clone the repository:

1. Open a terminal on your computer
2. Run: `git clone https://replit.com/@username/project-name.git`
   (Replace with your actual Replit repository URL)

## Important Files to Keep

Make sure these essential files are included in your download:

- `main.py` - Main entry point
- `bot.py` - Core bot functionality
- `cogs/music.py` - Music commands and playback logic
- `utils/ytdl.py` - YouTube/media extraction utilities
- `sync_commands.py` - Slash command syncing utility
- `run.py` - Alternative entry point
- `DEPLOYMENT_GUIDE.md` - How to deploy your bot
- `VOLUME_SETTINGS.md` - Audio configuration options
- `README.md` - Documentation

## Creating a requirements.txt

For easier dependency installation, create a `requirements.txt` file containing:

```
discord.py
yt-dlp
pynacl
python-dotenv
flask
gunicorn
spotdl
```

## Next Steps

After downloading:

1. Follow the instructions in `DEPLOYMENT_GUIDE.md` to deploy your bot
2. Set up your environment variables with your Discord bot token
3. Run the sync_commands.py script once to register slash commands
4. Start your bot with `python main.py`

## Deploying as an Official Bot

To make your bot "official" on Discord:

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Select your application
3. In "General Information," you can add:
   - An app icon (use the included bot-icon.svg or generated-icon.png)
   - A description
   - Tags relevant to your bot
4. In the "Bot" section, you can configure:
   - Profile picture
   - Username
   - Whether it's public or private
5. For public bots, verify all intents and permissions are correctly set
6. Generate an OAuth2 URL to share your bot with others

For detailed deployment information, see `DEPLOYMENT_GUIDE.md`