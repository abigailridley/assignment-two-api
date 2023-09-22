# Spotify API console app for Music Recommendation

# Gather Data from user - favourite artist
# Search for songs - up to 5
# Print songs to console
# Loop through input until 'exit'
# On exit - create playlist.txt with all recommended songs 
# Output random song from playlist 

# Access to Spotify API

# Access to spotipy module
import spotipy  # 1 additional module imported
from spotipy.oauth2 import SpotifyOAuth
import random  # 2nd additional module imported


# Set up authentication
def setup_spotify():
    sp_oauth = SpotifyOAuth(
        client_id='213ba2fc193249c8be9f423ac813347d',
        client_secret='53ff341a417740b6b4500e415da2c492',
        redirect_uri='http://localhost:8888/callback', #requires uri for callback - use localhost as generic
        scope='user-library-read user-read-playback-state user-modify-playback-state'
    )
    sp = spotipy.Spotify(auth_manager=sp_oauth)
    return sp


# Get user's input for favourite artist
def get_user_input():
    artist_name = input("Enter your favourite artist: ")
    return artist_name.capitalize()


#  Recommend song function - uses inputted artist_name and spotify client, with a limit of 10 songs
def recommend_songs(artist_name, sp):
    results = sp.search(q=f'artist:{artist_name}', type='track', limit=5) #Dictionary to store song and artist data from API

    if results['tracks']['items']: #
        print(f"\nHere are some recommended songs by {artist_name}\n")
        recommended_songs = []

        for track in results['tracks']['items']:
            print(f"{track['name']}")
            recommended_songs.append(track['name'])  # add song to list

        return recommended_songs
    else:
        print(f"No songs found by {artist_name}.")
        return []


def create_playlist(songs):
    with open("your_playlist.txt", "a") as file:
        file.write("My Playlist\n")
        for song in songs:
            formatted_song = song.split(" - ")[0][
                             :50]  # split using delimiter '-' and uses the index [0] to show first part and then limit of [50] characters
            file.write(f"{formatted_song}\n")
    print("Tracks list has been saved to 'your_playlist.txt'")


if __name__ == "__main__":
    sp = setup_spotify()
    all_recommended_songs = []  # empty list to store all songs for playlist
# while loop to check spotify setup has been successful 
    while True:
        user_artist = get_user_input()
        if user_artist.lower() == 'exit':
            break
        playlist_songs = recommend_songs(user_artist, sp)
        all_recommended_songs.extend(playlist_songs)  # adds songs to [list]
        print("\n" + 'Type "exit" to close and create playlist')

    if all_recommended_songs:
        create_playlist(all_recommended_songs)

    # Random module
    random_song = random.choice(all_recommended_songs)
    print(f"\nRecommended random song from your playlist: {random_song}")

# function - add up multiple songs/albums in a loop and then 'exit' the application
# on exit, the songs are outputted into a file with open("albums.txt", "w") as file:
#         for album in albums:
#             # concatenates with new line after each album
#             file.write(album + "\n")
#     # alert the user of the file
#     print("Albums list saved to file 'albums.txt'")
