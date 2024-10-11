# Spotify Liked Songs Downloader

## Overview

Welcome to the **Spotify Liked Songs Downloader**! If you've ever found yourself grooving to a new tune on Spotify, only to realize that when it comes time to hit the download button you remember that you dont have a **premier account** , fear not! This script is here to rescue your musical memory. It automatically snags those sweet jams you’ve liked on Spotify and downloads them straight to your specified folder, so you can jam out anytime, anywhere—without needing to rely on your questionable memory!

*P.S. You don’t need a Spotify Premium account for this script to work its magic. This script is intended for educational purposes only and is not meant to infringe on artists' rights or steal their work. Always support your favorite artists!*

## Issues

Alright, so here’s the situation: I might not be a coding genius, but there’s a little snag when it comes to extracting audio. I need to have **FFmpeg** downloaded to make this work. The funny part? I don’t have it, and I’m guessing you don’t either—unless you’ve got some secret tech stash I don’t know about!

When you try to download your favorite jam, it throws an error like it’s trying to tell you, "**Preprocessor error**." But don’t worry about it! Just keep enjoying your music and showing those songs some love—your favorite song will be downloaded in the background without any issues. Who needs audio extraction when you can vibe out like there’s no tomorrow? 🎶

So, keep listening and keep liking—because life’s too short to fix these minor issues.



## Features
- **Download Like a Pro**: Automatically download songs you like on Spotify without lifting a finger—just sit back and let the magic happen!
- **Real-time Monitoring**: Continuously checks for new liked songs. If you discover a new favorite, it’ll be downloaded faster than you can say “Why did I like that?”
- **Saves You from Regret**: Never lose track of that banger you liked during a late-night scrolling session. It’s like having a personal assistant for your music library (but less judgmental).
- **Customizable Download Folder**: Choose where your musical treasures go, so you don’t accidentally download them to your “I’ll Never Look at This Again” folder.

## Requirements
- Python 3.x
- `spotipy` library for interacting with the Spotify API
- `python-dotenv` library for managing environment variables
- `yt-dlp` for downloading audio from YouTube

## Heads Up!

Before you dive in, here are some important steps to follow:

- Make sure to set up your `.env` file and store your **Spotify Client ID** in it. This will keep things neat and secure.
- Ensure your **Spotify Developer Account** is fully set up and ready to go.
- Follow the steps mentioned in the Spotify Developer documentation. You’ll need to verify your account by being redirected to a URL. Once you’re authenticated, a `.cache` file will be generated, containing the all-important **access token** (your key to the Spotify kingdom 🎶).

### Update This to Your Actual Folder Path
Don’t forget to set your directory for storing downloaded songs. For example, my directory looks like this:

```python
DOWNLOAD_FOLDER = r'c:\Users\bhargav\OneDrive\Desktop\spotify_downloads_with_69_others'
```

## Setup
1. **Clone the repository** (if applicable):
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv env
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```bash
        .\env\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source env/bin/activate
        ```

4. **Install dependencies**:
    ```bash
    pip install spotipy python-dotenv
    ```

5. **Create a `.env` file** in the project root with the following content:
    ```env
    SPOTIFY_CLIENT_ID=<your_client_id>
    SPOTIFY_CLIENT_SECRET=<your_client_secret>
    SPOTIFY_REDIRECT_URI=<your_redirect_uri>
    ```

    - You can obtain your `CLIENT_ID` and `CLIENT_SECRET` by creating an application on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
    - The `REDIRECT_URI` should be one you set in your Spotify app settings. You can use `http://localhost:8888/callback` for testing purposes.

## Usage

Run the script from the command line:

```bash
python script.py
