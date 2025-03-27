import discord
from discord.ext import commands
from discord import app_commands
import logging
import os
import sys

class MusicBot(commands.Bot):
    def __init__(self):
        # Set intents with required permissions for music functionality
        intents = discord.Intents.default()
        intents.voice_states = True  # Needed for voice channel functionality
        intents.message_content = True  # For command content (requires verification in Discord Developer Portal)
        
        # Set command prefix (! by default) - will only be used for help command
        command_prefix = os.environ.get("COMMAND_PREFIX", "!")
        
        super().__init__(
            command_prefix=command_prefix,
            intents=intents,
            description="Discord Music Bot",
            reconnect=True,
            case_insensitive=True
        )
        
        # Set up logger
        self.logger = logging.getLogger("MusicBot")
        self.logger.setLevel(logging.DEBUG)
        
        # Enable audio playback mode
        self.radio_mode = False
        self.logger.info("Running in audio playback mode")
        
        # Print all intents for debugging
        self.logger.info("Bot initialized with the following intents:")
        for intent, enabled in intents:
            self.logger.info(f"Intent {intent}: {'ENABLED' if enabled else 'DISABLED'}")
        
        # Add manual sync slash command
        @self.command(name="sync", hidden=True)
        @commands.is_owner()
        async def sync_command(ctx):
            """Manually sync slash commands"""
            self.logger.info("Manual sync command received")
            await ctx.send("Syncing slash commands...")
            
            try:
                synced = await self.tree.sync()
                await ctx.send(f"Synced {len(synced)} commands globally")
                self.logger.info(f"Manually synced {len(synced)} slash commands")
            except Exception as e:
                self.logger.error(f"Error syncing commands: {e}", exc_info=e)
                await ctx.send(f"Error syncing commands: {e}")
        
    async def setup_hook(self):
        """Setup hook that runs when the bot is ready"""
        # Load music cog
        await self.load_extension("cogs.music")
        self.logger.info("Music cog loaded")
        
    async def on_ready(self):
        """Event called when the bot is ready"""
        self.logger.info(f"Logged in as {self.user} (ID: {self.user.id})")
        self.logger.info(f"Connected to {len(self.guilds)} guilds")
        
        # No automatic command syncing to avoid rate limiting
        # Use sync_commands.py to sync commands manually
        self.logger.info("Command syncing disabled on startup - use sync_commands.py to sync manually")
        
        # Set bot status
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening, 
                name="/play"
            )
        )
    
    async def on_command_error(self, ctx, error):
        """Global error handler"""
        if isinstance(error, commands.CommandNotFound):
            return
        
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Missing required argument: {error.param.name}")
            return
            
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"Bad argument: {error}")
            return
            
        # Log unexpected errors
        self.logger.error(f"Command error: {error}", exc_info=error)
        await ctx.send(f"An error occurred: {error}")
