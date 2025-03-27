# Discord Music Bot Deployment Guide

This guide will help you deploy your Discord music bot to a server or hosting platform so that it can run 24/7 as an official bot.

## Prerequisites

1. A Discord bot account with token
2. A server/hosting platform to run the bot
3. Python 3.8+ installed
4. FFmpeg installed on the system

## Required Dependencies

```
discord.py
yt-dlp
pynacl
python-dotenv
spotdl
```

## Setup Steps

### 1. Set Up Your Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application and set up a bot
3. Enable the proper intents (at minimum MESSAGE CONTENT and SERVER MEMBERS)
4. Generate an invite link with proper permissions
5. Add the bot to your servers

### 2. Configure Environment Variables

Create a `.env` file in the root directory with:

```
DISCORD_BOT_TOKEN=your_token_here
```

For security, never commit this file to public repositories.

### 3. Deploy to a Hosting Platform

#### Option 1: VPS/Dedicated Server

1. Upload all bot files to your server
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```
3. Make sure FFmpeg is installed:
   ```
   apt-get update && apt-get install -y ffmpeg
   ```
4. Run the bot:
   ```
   python main.py
   ```
5. Use a process manager like PM2 or systemd to keep it running:
   ```
   pm2 start main.py --name discord-music-bot --interpreter python3
   ```

#### Option 2: Specialized Discord Bot Hosting

Many services offer specialized Discord bot hosting:
- [Railway](https://railway.app/)
- [Heroku](https://www.heroku.com/)
- [DigitalOcean](https://www.digitalocean.com/)
- [Replit](https://replit.com/)

Follow their platform-specific deployment guides.

### 4. Sync Slash Commands (First Time Only)

After deploying, run the command sync script once:

```
python sync_commands.py
```

This registers all slash commands with Discord. Only do this when commands change.

## Important Files

- `main.py` - The entry point that starts both the bot and web server
- `bot.py` - Core bot functionality
- `cogs/music.py` - All music commands and playback logic
- `utils/ytdl.py` - YouTube/media extraction utilities
- `sync_commands.py` - Utility to sync slash commands with Discord

## Optimizations for 24/7 Operation

1. Add error handling and automatic reconnection:
   - The bot already includes automatic error handling and recovery
   - Consider adding monitoring and automatic restarts if needed

2. Limit resource usage:
   - The audio extraction is optimized for speed and reliability
   - Consider setting queue limits for busy servers
   - Audio caching is disabled to prevent disk space issues

3. Monitor performance:
   - Add logging to a file to track issues:
     ```python
     import logging
     logging.basicConfig(filename='bot.log', level=logging.INFO)
     ```

## Scaling

For larger deployments with many servers:
1. Use sharding in `bot.py` (discord.py supports this automatically)
2. Consider deploying multiple instances
3. Add database support for persistent queues (currently uses in-memory storage)

## Troubleshooting

- If audio doesn't play, ensure FFmpeg is installed correctly
- Check if the bot has proper permissions in Discord
- Verify the Opus library is available (the bot has fallback options)
- Examine log output for specific error messages

## Need Help?

- Discord.py documentation: https://discordpy.readthedocs.io/
- YT-DLP documentation: https://github.com/yt-dlp/yt-dlp
- Discord Developer Portal: https://discord.com/developers/docs/intro