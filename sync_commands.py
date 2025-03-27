"""
One-time command to sync slash commands to Discord.

This utility script is meant to be run directly to register slash commands
with Discord. Run this after making changes to commands or when initially
setting up the bot. There's no need to run this on every bot restart.

Usage:
    python sync_commands.py

This avoids rate limiting issues that can occur when syncing commands
too frequently.
"""

import asyncio
import logging
import os
from bot import MusicBot

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('CommandSync')

async def sync_commands():
    """Sync all slash commands to Discord."""
    logger.info("Starting command sync process")
    
    # Get bot token from environment variables
    token = os.environ.get('DISCORD_BOT_TOKEN')
    if not token:
        logger.error("No Discord bot token found. Set the DISCORD_BOT_TOKEN environment variable.")
        return
    
    # Initialize the bot
    bot = MusicBot()
    
    # Override on_ready to sync commands once
    original_on_ready = bot.on_ready
    
    async def sync_on_ready():
        """Custom on_ready that syncs commands and then exits."""
        logger.info(f"Logged in as {bot.user} (ID: {bot.user.id})")
        
        try:
            logger.info("Syncing commands globally...")
            synced_commands = await bot.tree.sync()
            logger.info(f"Successfully synced {len(synced_commands)} command(s)")
            
            # Log all synced commands
            for cmd in synced_commands:
                logger.info(f"Synced command: {cmd.name}")
                
        except Exception as e:
            logger.error(f"Error syncing commands: {e}", exc_info=True)
        
        logger.info("Command sync complete. Shutting down bot.")
        await bot.close()
    
    # Replace the on_ready event
    bot.on_ready = sync_on_ready
    
    try:
        # Start the bot
        await bot.start(token)
    except KeyboardInterrupt:
        logger.info("Received keyboard interrupt")
    except Exception as e:
        logger.error(f"Error during bot operation: {e}", exc_info=True)
    finally:
        # Make sure the bot is closed
        if not bot.is_closed():
            await bot.close()
        logger.info("Bot shutdown complete")

if __name__ == "__main__":
    try:
        asyncio.run(sync_commands())
    except KeyboardInterrupt:
        print("Program interrupted by user")
    except Exception as e:
        print(f"Unexpected error: {e}")