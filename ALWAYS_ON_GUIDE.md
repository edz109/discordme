# Making Your Discord Bot Run 24/7 Non-Stop

Follow these steps to ensure your Discord Music Bot runs continuously, even when you turn off your laptop:

## 1. Enable "Always On" (Most Important Step)

1. Click on the ⚙️ **Tools** button in the left sidebar of Replit
2. Select **"Always On"** from the menu
3. Toggle the switch to **ON**
4. You'll see a confirmation that Always On is activated

This feature is available to Replit Pro/Hacker Plan users and keeps your bot running permanently, even when you:
- Close the Replit tab
- Turn off your computer
- Disconnect from the internet

## 2. Verify Your Environment Secrets

1. Click on the 🔒 **Secrets** tab in the left sidebar
2. Make sure your `DISCORD_BOT_TOKEN` is properly set
3. If not, add it with your actual Discord bot token

## 3. Test Non-Stop Operation

To verify your bot will continue running:
1. Use the Discord bot in a server
2. Close your Replit tab completely
3. Wait a few minutes
4. Return to your Discord server and try using commands again

The bot should respond as normal, confirming it's running independently of your browser.

## 4. Set Up Deployment (Optional)

Your bot is already configured for deployment with these settings in the `.replit` file:
```
[deployment]
deploymentTarget = "autoscale"
run = ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
```

If you want to use Replit's official deployment:
1. Click the **Deploy** button in the top-right corner
2. Follow the prompts to deploy your application

## 5. Understanding Continuous Operation

The bot will remain running because:
1. The **"Always On"** feature keeps your Repl active 24/7
2. The Flask web server creates an HTTP endpoint that Replit pings regularly
3. The bot is designed to reconnect automatically if disconnected
4. Both components (web server and Discord bot) run in parallel

## 6. Troubleshooting Non-Stop Operation

If your bot stops running:
1. Check if "Always On" is still enabled
2. Verify your Replit account subscription is active
3. Check the Console for any error messages
4. Restart the Repl manually if needed

## 7. Maximum Uptime Tips

To ensure the highest possible uptime:
1. Never modify the `.replit` file or workflows
2. Keep your Discord bot token valid and up-to-date
3. Consider setting up a third-party monitoring service
4. Check on your bot periodically to ensure it's working correctly

With these settings, your Discord Music Bot will run continuously 24/7, regardless of your personal computer's status!