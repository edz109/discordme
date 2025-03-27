import os
import subprocess
import sys
import threading
import time

def run_discord_bot():
    print("Starting Discord bot...")
    bot_process = subprocess.Popen(['python', 'main.py'])
    
    return bot_process

def run_web_server():
    print("Starting web server...")
    web_process = subprocess.Popen(['python', 'web_server.py'])
    
    return web_process

if __name__ == "__main__":
    bot_process = run_discord_bot()
    web_process = run_web_server()
    
    try:
        # Keep the main thread running to handle KeyboardInterrupt
        while True:
            time.sleep(1)
            
            # Check if processes are still alive
            if bot_process.poll() is not None:
                print("Discord bot process exited, restarting...")
                bot_process = run_discord_bot()
                
            if web_process.poll() is not None:
                print("Web server process exited, restarting...")
                web_process = run_web_server()
                
    except KeyboardInterrupt:
        print("Shutting down...")
        
        # Terminate processes
        if bot_process:
            bot_process.terminate()
            
        if web_process:
            web_process.terminate()
            
        sys.exit(0)