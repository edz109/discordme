import os
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Discord Music Bot</title>
        <link href="https://cdn.replit.com/agent/bootstrap-agent-dark-theme.min.css" rel="stylesheet">
        <style>
            body {
                padding: 40px 0;
            }
            .bot-icon {
                max-width: 150px;
                margin-bottom: 20px;
            }
            .footer {
                margin-top: 40px;
                font-size: 0.9rem;
                color: var(--bs-secondary);
            }
        </style>
    </head>
    <body data-bs-theme="dark">
        <div class="container text-center">
            <img src="/static/bot-icon.svg" alt="Music Bot Icon" class="bot-icon rounded-circle">
            <h1 class="display-4">Discord Music Bot</h1>
            <p class="lead">Your Discord bot is running in the background!</p>
            
            <div class="card mt-4">
                <div class="card-header">
                    <h5 class="mb-0">Bot Commands</h5>
                </div>
                <div class="card-body">
                    <div class="table-responsive">
                        <table class="table table-striped">
                            <thead>
                                <tr>
                                    <th>Command</th>
                                    <th>Description</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><code>!join</code></td>
                                    <td>Joins your voice channel</td>
                                </tr>
                                <tr>
                                    <td><code>!play &lt;url or search query&gt;</code></td>
                                    <td>Plays a song from YouTube</td>
                                </tr>
                                <tr>
                                    <td><code>!pause</code></td>
                                    <td>Pauses the currently playing song</td>
                                </tr>
                                <tr>
                                    <td><code>!resume</code></td>
                                    <td>Resumes the currently paused song</td>
                                </tr>
                                <tr>
                                    <td><code>!skip</code></td>
                                    <td>Skips the currently playing song</td>
                                </tr>
                                <tr>
                                    <td><code>!stop</code></td>
                                    <td>Stops playing music and clears the queue</td>
                                </tr>
                                <tr>
                                    <td><code>!queue</code></td>
                                    <td>Shows the current song queue</td>
                                </tr>
                                <tr>
                                    <td><code>!nowplaying</code> or <code>!np</code></td>
                                    <td>Shows information about the currently playing song</td>
                                </tr>
                                <tr>
                                    <td><code>!leave</code></td>
                                    <td>Leaves the voice channel</td>
                                </tr>
                                <tr>
                                    <td><code>!volume &lt;1-100&gt;</code></td>
                                    <td>Changes the player volume</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            
            <div class="alert alert-info mt-4">
                <h5>Setup Instructions</h5>
                <ol class="text-start">
                    <li>Invite your bot to your Discord server</li>
                    <li>Join a voice channel</li>
                    <li>Use <code>!join</code> to make the bot join your channel</li>
                    <li>Use <code>!play [song name or URL]</code> to start playing music</li>
                </ol>
            </div>
            
            <div class="footer">
                <p>This page is just a dashboard. The Discord bot is running in the background.</p>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)