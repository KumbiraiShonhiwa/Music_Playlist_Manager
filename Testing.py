from Database import *
from User import *
from Song import *
from Playlist import *
import pytest
 
class Test:
    # Create some song objects
    song1 = Song("Bohemian Rhapsody", "Rock", "Queen", "5:55")
    song2 = Song("Stairway to Heaven", "Rock", "Led Zeppelin", "8:02")
    song3 = Song("Hotel California", "Rock", "Eagles", "6:30")

    # Create a playlist and add songs to it
    playlist1 = Playlist("My Rock Favorites", "test_user", [song1, song2])
    
    # Create a user and assign the playlist to them
    user1 = User("test_user", "password123", "Test User", [playlist1.name])
    user2 = User("test_user2", "password123", "Test User2", [playlist1.name])


    # Initialize the lists with the created objects
    users = [user1]
    songs = [song1, song2, song3]
    playlists = [playlist1]
    
    def test_login_functionality(self):
        pass
    
    def test_add_song_functionality(self):
        pass
    
    def test_remove_song_functionality(self):
        pass
    
    def test_sort_songs_functionality(self):
        pass
    
    def test_shuffle_songs_functionality(self):
        pass
    
    def test_rename_playlist_functionality(self):
        pass
    
    def test_sort_playlists_by_name_functionality(self):
        pass
    
    def test_export_data_functionality(self):
        pass
    
    
    
    
    