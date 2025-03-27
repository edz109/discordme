# Discord Music Bot

A Discord bot that can play music from various platforms including YouTube, Spotify, SoundCloud, and more in voice channels with playback controls. This bot uses slash commands for all interactions.

## Features

- Play music from YouTube, Spotify, SoundCloud, Deezer, and Apple Music
- Dedicated search command for direct YouTube searches
- Improved search reliability with specialized algorithms
- Automatic URL detection and handling for different music platforms
- Enhanced Spotify URL processing with fallback mechanisms
- Robust error handling with automatic fallbacks
- Queue management system for adding multiple songs
- Basic playback controls (pause, resume, skip, stop)
- Enhanced volume control with boosted audio output
- Professional audio processing with advanced filters for clarity
- Optimized audio playback with reduced lag and stuttering
- Consistent playback speed and pitch stability with sample rate normalization
- Display currently playing song and queue information
- Auto-disconnect when left alone in a voice channel
- "Radio mode" for environments where direct audio playback isn't possible

## Commands

All commands use Discord's slash command system. After adding the bot to your server, you can use the following commands:

- `/join` - Joins your current voice channel
- `/search [query]` - Searches YouTube directly and plays the first result (new!)
- `/play [query]` - Plays a song from various platforms (URL or search query)
  - Supports YouTube, Spotify, SoundCloud, Deezer, Apple Music links
  - Automatically searches YouTube if no valid URL is provided
  - Enhanced search capabilities with improved reliability
- `/pause` - Pauses the currently playing song
- `/resume` - Resumes a paused song
- `/skip` - Skips the currently playing song
- `/stop` - Stops playback and clears the queue
- `/queue` - Shows the current song queue
- `/nowplaying` - Shows information about the currently playing song
- `/leave` - Leaves the voice channel
- `/volume [1-100]` - Changes the playback volume with enhanced boost (see VOLUME_SETTINGS.md)

## Setup

1. Create a Discord bot in the [Discord Developer Portal](https://discord.com/developers/applications)
2. Enable the following "Privileged Gateway Intents":
   - Server Members Intent (optional)
   - Message Content Intent (optional)
3. Add the bot to your server with the proper permissions (requires `Connect` and `Speak` permissions for voice channels)
4. Set the `DISCORD_BOT_TOKEN` environment variable with your bot token

## First-Time Setup

When changes are made to slash commands, you need to sync them with Discord. This is a one-time operation that should be done after adding or modifying commands:

```bash
python sync_commands.py
```

## Running the Bot

```bash
python main.py
```

This will start both the Discord bot and a simple web server.

## Requirements

- Python 3.8+
- discord.py
- yt-dlp
- FFmpeg (must be installed on the system)
- PyNaCl for voice support

## Notes

- The bot automatically leaves voice channels when left alone
- YouTube search is limited to one result to avoid overloading the queue
- The `/search` command provides a more direct way to search YouTube for music
- Enhanced search reliability with specialized YouTube search algorithms
- Commands that fail will provide error messages explaining what went wrong
- Radio mode activates automatically when Opus library cannot be loaded, providing YouTube links instead of direct playback
- Spotify, SoundCloud, Deezer and Apple Music links are converted to YouTube equivalents automatically
- Improved Spotify URL handling with fallback mechanisms for better reliability
- All non-URL inputs are treated as YouTube search queries
- Audio playback features enhanced volume controls for better sound quality and loudness
- Advanced audio filters provide clearer, more stable playback with reduced lag
- Audio processing includes frequency filtering, dynamic normalization, and sample rate correction
- Enhanced buffering and network handling prevent stuttering and speed fluctuations
- Default audio levels are properly balanced for optimal clarity and volume

## Volume Control

The bot features an enhanced volume system with multiple boost layers to ensure optimal audio quality in Discord voice channels. See [VOLUME_SETTINGS.md](VOLUME_SETTINGS.md) for detailed information.