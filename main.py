import os
import logging
import sys
from flask import Flask, render_template_string
from threading import Thread
from bot import MusicBot

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Create a Flask app for keeping the bot alive
app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Discord Music Bot</title>
        <link href="https://cdn.replit.com/agent/bootstrap-agent-dark-theme.min.css" rel="stylesheet">
        <style>
            body {
                padding: 30px;
            }
            .command-table {
                width: 100%;
                margin-top: 20px;
            }
            .bot-title {
                margin-bottom: 30px;
            }
        </style>
    </head>
    <body data-bs-theme="dark">
        <div class="container">
            <div class="row">
                <div class="col-md-8 offset-md-2">
                    <div class="text-center">
                        <h1 class="bot-title">Discord Music Bot</h1>
                        <div class="alert alert-success">
                            Bot is running and ready!
                        </div>
                    </div>
                    
                    <div class="card mt-4">
                        <div class="card-header">
                            <h3>Available Commands</h3>
                        </div>
                        <div class="card-body">
                            <table class="table command-table">
                                <thead>
                                    <tr>
                                        <th>Command</th>
                                        <th>Description</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td><code>/join</code></td>
                                        <td>Join your voice channel</td>
                                    </tr>
                                    <tr>
                                        <td><code>/search [query]</code></td>
                                        <td>Searches YouTube directly and plays the first result</td>
                                    </tr>
                                    <tr>
                                        <td><code>/play [query]</code></td>
                                        <td>Play music from various platforms (URL or search query)</td>
                                    </tr>
                                    <tr>
                                        <td><code>/pause</code></td>
                                        <td>Pause current song</td>
                                    </tr>
                                    <tr>
                                        <td><code>/resume</code></td>
                                        <td>Resume paused song</td>
                                    </tr>
                                    <tr>
                                        <td><code>/skip</code></td>
                                        <td>Skip current song</td>
                                    </tr>
                                    <tr>
                                        <td><code>/stop</code></td>
                                        <td>Stop playback and clear queue</td>
                                    </tr>
                                    <tr>
                                        <td><code>/queue</code></td>
                                        <td>Show current song queue</td>
                                    </tr>
                                    <tr>
                                        <td><code>/nowplaying</code></td>
                                        <td>Show current song info</td>
                                    </tr>
                                    <tr>
                                        <td><code>/leave</code></td>
                                        <td>Leave voice channel</td>
                                    </tr>
                                    <tr>
                                        <td><code>/volume [1-100]</code></td>
                                        <td>Change playback volume</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    
                    <div class="card mt-4">
                        <div class="card-header">
                            <h3>Supported Music Platforms</h3>
                        </div>
                        <div class="card-body">
                            <p>This bot supports music from various platforms:</p>
                            <ul class="list-group">
                                <li class="list-group-item">YouTube</li>
                                <li class="list-group-item">Spotify</li>
                                <li class="list-group-item">SoundCloud</li>
                                <li class="list-group-item">Deezer</li>
                                <li class="list-group-item">Apple Music</li>
                            </ul>
                            <p class="mt-3">Just paste a link from any of these platforms, or type a search query to find music on YouTube.</p>
                        </div>
                    </div>
                    
                    <div class="card mt-4">
                        <div class="card-header">
                            <h3>Radio Mode</h3>
                        </div>
                        <div class="card-body">
                            <p>If the bot can't play audio directly (due to Opus library limitations), it will automatically switch to "radio mode" where it provides direct links to songs instead.</p>
                            <div class="alert alert-info">
                                <strong>Note:</strong> This is a fallback mechanism to ensure the bot works in all environments.
                            </div>
                        </div>
                    </div>
                    
                    <div class="card mt-4">
                        <div class="card-header">
                            <h3>Setup</h3>
                        </div>
                        <div class="card-body">
                            <p>After making changes to slash commands, run this to sync them with Discord:</p>
                            <pre class="bg-dark text-light p-3"><code>python sync_commands.py</code></pre>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

def run_bot():
    # Get bot token from environment variable
    token = os.environ.get("DISCORD_BOT_TOKEN")
    if not token:
        logging.error("No Discord bot token found. Please set the DISCORD_BOT_TOKEN environment variable.")
        return
    
    # Validate token format to avoid obvious errors
    if not token.strip():
        logging.error("Discord bot token is empty")
        return
        
    # Basic token format check - Discord tokens are at least 50 chars long
    if len(token) < 50:
        logging.error(f"Discord bot token seems too short ({len(token)} chars), it might be invalid")
        
    # Log that we're starting, but don't log the token
    logging.info(f"Starting Discord bot with token (length: {len(token)})...")
    try:
        # Create and run the bot
        bot = MusicBot()
        bot.run(token)
    except Exception as e:
        logging.error(f"Error starting the Discord bot: {e}", exc_info=True)
        logging.error("Please check if your Discord bot token is valid")
        # Try to log a masked version of the token for debugging
        if token:
            masked_token = token[:5] + "..." + token[-5:] if len(token) > 10 else "***"
            logging.error(f"Token format check (masked): {masked_token}")

# Start the bot in a separate thread when the app is initialized
# This will run regardless of how the app is started (direct or gunicorn)
bot_thread = Thread(target=run_bot)
bot_thread.daemon = True
bot_thread.start()
logging.info("Started bot thread")

if __name__ == "__main__":
    # When run directly, we start the Flask app (the bot is already running in a thread)
    app.run(host="0.0.0.0", port=5000, debug=True)
