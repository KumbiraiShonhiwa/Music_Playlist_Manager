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
    
    def test_authenticate_functionality(self):
        assert self.user1.login("test_user", "password123") == True
        assert self.user2.login("test_user2", "password123") == True
        assert self.user1.login("test_user", "wrong_password") == False
        assert self.user2.login("wrong_user", "password123") == False
        
    
    def test_add_song_functionality(self):
        assert self.playlist1.add_song(self.song2.name) == True
        assert self.playlist1.add_song(self.song1.name) == True
    
    def test_remove_song_functionality(self):
        self.playlist1.display_playlist
        assert self.playlist1.remove_song(self.song1.name) == True
        assert self.playlist1.remove_song(self.song2.name) == True
        assert self.playlist1.remove_song(self.song3.name) == False
      
    
    def test_sort_songs_functionality(self):
        self.playlist1.sort_songs_name()     
        assert self.playlist1.songs[0].name == "Bohemian Rhapsody"
        assert self.playlist1.songs[1].name == "Stairway to Heaven"
        
    
    def test_rename_playlist_functionality(self):
        self.playlist1.rename_playlist("Fever Dream")
        assert self.playlist1.name == "Fever Dream"
        assert self.playlist1.name != "My Rock Favorites"
        
    
    
        
    
    
    
    
    
    
    