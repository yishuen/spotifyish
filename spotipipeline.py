import config
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(config.client_id, config.client_secret))

# getting track IDs from playlist IDs
def playlist_track_ids(playlist_id):
    results = sp.playlist_tracks(playlist_id)['items']
    return [results[i]['track']['id'] for i in range(len(results))]

# getting playlist names and track IDs from user ID
def playlist_pipeline(user):
    playlists = sp.user_playlists(user)['items']
    playlist_ids = [p['id'] for p in playlists]

    return {sp.playlist(p)['name']: playlist_track_ids(p) for p in playlist_ids}
