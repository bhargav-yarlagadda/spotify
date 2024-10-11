# Spotify Liked Songs Downloader

## Overview

Welcome to the **Spotify Liked Songs Downloader**! If you've ever found yourself grooving to a new tune on Spotify, only to realize that when it comes time to hit the download button you remember that you dont have a **premier account** , fear not! This script is here to rescue your musical memory. It automatically snags those sweet jams you’ve liked on Spotify and downloads them straight to your specified folder, so you can jam out anytime, anywhere—without needing to rely on your questionable memory!

*P.S. You don’t need a Spotify Premium account for this script to work its magic. This script is intended for educational purposes only and is not meant to infringe on artists' rights or steal their work. Always support your favorite artists!*


## Features
- **Download Like a Pro**: Automatically download songs you like on Spotify without lifting a finger—just sit back and let the magic happen!
- **Real-time Monitoring**: Continuously checks for new liked songs. If you discover a new favorite, it’ll be downloaded faster than you can say “Why did I like that?”
- **Saves You from Regret**: Never lose track of that banger you liked during a late-night scrolling session. It’s like having a personal assistant for your music library (but less judgmental).
- **Customizable Download Folder**: Choose where your musical treasures go, so you don’t accidentally download them to your “I’ll Never Look at This Again” folder.

## Features
- **Fetches and displays your currently liked songs.**
- Monitors for new liked songs in real time.
- **Automatically downloads any new liked songs to your specified folder.**

## Requirements
- Python 3.x
- `spotipy` library for interacting with the Spotify API
- `python-dotenv` library for managing environment variables
- `yt-dlp` for downloading audio from YouTube

## important steps
- make sure that you set up .env file and store the id in .env
- make sure that you set up your spotify developer account
### Update this to your actual folder path
- set your directory for storing downloaded songs 
    my directory is
**DOWNLOAD_FOLDER = r'c:\Users\bhargav\OneDrive\Desktop\spotify_downloads_with_69_others'**  


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