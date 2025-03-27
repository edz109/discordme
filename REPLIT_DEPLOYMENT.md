# Deploying Your Discord Bot on Replit (24/7)

Follow these steps to make your Discord Music Bot run continuously on Replit:

## 1. Enable "Always On"

Replit's "Always On" feature keeps your bot running even when you're not actively using the Replit IDE:

1. Click on the ⚙️ icon (Tools/Settings) in the left sidebar
2. Find and select "Always On"
3. Toggle the switch to enable it
4. Your bot will now continue running even when you close the browser

Note: "Always On" is a feature available to Replit Pro/Hacker Plan users. It keeps your bot running 24/7.

## 2. Configure Environment Variables

Make sure your bot token is set as an environment variable:

1. Click on the 🔒 Secrets tab in the sidebar
2. Add your Discord bot token as `DISCORD_BOT_TOKEN`
3. This securely stores your token and makes it available to your bot

## 3. Update Your Run Configuration

Your project should already be configured to run with the command:
```
gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
```

This runs both the Discord bot and a simple web server to keep your bot active.

## 4. Health Checks (Keeping the Bot Alive)

Replit has an automatic pinging system that helps keep your bot alive:

1. The simple Flask web server in the project already serves a basic page at the root
2. Replit's systems will automatically ping this endpoint regularly
3. These pings help keep your bot active and prevent it from sleeping

## 5. Monitor Your Bot

You can monitor your bot's activity:

1. Check the "Console" tab to see bot logs and activity
2. Use the "Shell" tab to run commands for debugging

## 6. Handling Restarts

Occasionally, Replit may restart your bot:

1. The bot has built-in reconnection logic to handle disconnections
2. It will automatically rejoin voice channels if disrupted
3. The queue system will be reset if a restart occurs (this is normal behavior)

## 7. First-Time Setup (One Time Only)

Before deploying permanently, make sure you've run:
```
python sync_commands.py
```

This syncs all your slash commands with Discord's API.

## 8. Troubleshooting

If your bot stops working:

1. Check if your "Always On" setting is still enabled
2. Verify your bot token is still valid in the Secrets tab
3. Check the Console for any error messages
4. Try manually restarting by clicking the "Run" button

With these settings, your Discord Music Bot should run continuously on Replit!