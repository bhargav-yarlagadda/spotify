# Spotify Liked Songs Monitor

## Overview
This Python script monitors the songs you like on Spotify. It continuously checks for new liked songs and prints the updated list to the console. If a new song is liked, it immediately notifies you by printing the song's name and artist.

## Features
- Fetches and displays currently liked songs.
- Monitors for new liked songs in real-time.
- Notifies when a new song is liked.

## Requirements
- Python 3.x
- `spotipy` library
- `python-dotenv` library

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
python spotify_liked_songs_monitor.py