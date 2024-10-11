import os
import time
import yt_dlp  # Import yt-dlp for downloading
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env file
load_dotenv()

# Retrieve Spotify API credentials from environment variables
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')

# Specify the download folder directly
DOWNLOAD_FOLDER = r'c:\Users\bhargav\OneDrive\Desktop\spotify_downloads'  # Update this to your actual folder path

# Set up Spotify API authentication using OAuth
spotify_instance = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope='user-library-read'))  # Scope for reading user's liked songs

# Fetch all liked songs from the user's library
def get_liked_songs(spotify_instance):
    """
    Retrieve all songs liked by the user from their Spotify library.

    Args:
        spotify_instance: An instance of the Spotipy Spotify client.

    Returns:
        liked_songs: A list of dictionaries, each containing song name, artist, and ID.
    """
    liked_songs = []  # List to hold liked songs
    offset = 0  # Starting point for pagination
    limit = 50  # Number of songs to fetch in each request

    while True:
        # Fetch liked songs with pagination
        results = spotify_instance.current_user_saved_tracks(limit=limit, offset=offset)
        if not results['items']:
            break  # Exit loop if no more songs are returned
        for item in results['items']:
            track = item['track']
            # Append song details to the liked_songs list
            liked_songs.append({'name': track['name'], 'artist': track['artists'][0]['name'], 'id': track['id']})
        offset += limit  # Move to the next set of results

    return liked_songs  # Return the complete list of liked songs

def download_song(song_name, artist):
    """
    Download a song using yt-dlp if it does not already exist in the specified download folder.

    Args:
        song_name: The name of the song to download.
        artist: The artist of the song.
    """
    # Construct the filename
    filename = f"{song_name} - {artist}.mp3"
    file_path = os.path.join(DOWNLOAD_FOLDER, filename)

    # Check if the file already exists
    if os.path.exists(file_path):
        print(f"'{filename}' already exists in the download folder. Skipping download.")
        return

    # Use yt-dlp to download the song
    ydl_opts = {
        'format': 'bestaudio/best',  # Download the best available audio format
        'outtmpl': file_path,  # Output template for the filename
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Use FFmpeg to extract audio
            'preferredcodec': 'mp3',  # Convert to mp3
            'preferredquality': '192',  # Quality of the audio
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Search for the song on YouTube
            search_query = f"{song_name} {artist}"
            ydl.download([f"ytsearch:{search_query}"])
            print(f"Downloaded: {filename}")
    except Exception:
        # Suppress the error message
        pass

def main():
    """
    Main function to monitor the user's liked songs on Spotify.
    It continuously checks for new liked songs and downloads them if not already present.
    """
    # Initial fetch of liked songs
    previous_liked_songs = set()  # Set for quick lookup of previously liked songs
    liked_songs = get_liked_songs(spotify_instance)  # Get current liked songs

    # Add currently liked songs to the set
    for song in liked_songs:
        previous_liked_songs.add(song['id'])

    # Print currently liked songs
    print("\n\nCurrently Liked Songs:\n")
    for song in liked_songs:
        print(f"{song['name']} by {song['artist']}")

    print("\n\nMonitoring for new liked songs...")  # Indicate monitoring start

    try:
        while True:
            time.sleep(30)  # Wait for 30 seconds before checking again
            current_liked_songs = get_liked_songs(spotify_instance)  # Fetch current liked songs

            # Print currently liked songs
            print("\nCurrently Liked Songs:")
            for song in current_liked_songs:
                print(f"{song['name']} by {song['artist']}")

            # Check for new liked songs
            for song in current_liked_songs:
                if song['id'] not in previous_liked_songs:
                    print(f"New liked song: {song['name']} by {song['artist']}")  # Print new liked song
                    download_song(song['name'], song['artist'])  # Download the new song
                    previous_liked_songs.add(song['id'])  # Add new song ID to the set

    except KeyboardInterrupt:
        print("Monitoring stopped.")  # Message when monitoring is stopped

if __name__ == "__main__":
    main()  # Execute main function when the script is run
