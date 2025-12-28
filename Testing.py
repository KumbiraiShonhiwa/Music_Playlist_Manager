from Database import *
from User import *
from Song import *
from Playlist import *
import pytest
 
import json

class Test:
    def __init__(self):
        with open('test_data.json') as f:
            data = json.load(f)

        self.users = []
        self.songs = []
        self.playlists = []

        for user_data in data:
            user_playlists = []
            for playlist_data in user_data['playlists']:
                playlist_songs = []
                for song_data in playlist_data['songs']:
                    song = Song(song_data['name'], song_data['genre'], song_data['singer'], song_data['runtime'])
                    self.songs.append(song)
                    playlist_songs.append(song)
                playlist = Playlist(playlist_data['name'], playlist_data['creator_name'], playlist_songs)
                self.playlists.append(playlist)
                user_playlists.append(playlist.name)
            
            user = User(user_data['username'], user_data['password'], user_data['name'], user_playlists)
            self.users.append(user)

        self.user1 = self.users[0]
        self.user2 = self.users[1]
        self.playlist1 = self.playlists[0]
        self.song1 = self.songs[0]
        self.song2 = self.songs[1]
        self.song3 = Song("Hotel California", "Rock", "Eagles", "6:30")


    
    def test_authenticate_functionality(self):
        # This function tests the login functionality of the User class
        assert self.user1.login("test_user", "password123") == True
        assert self.user2.login("test_user2", "password123") == True
        assert self.user1.login("test_user", "wrong_password") == False
        assert self.user2.login("wrong_user", "password123") == False
        
    
    def test_add_song_functionality(self):
        # This function tests the add_song functionality of the Playlist class
        assert self.playlist1.add_song(self.song2.name, self.song2.singer, self.song2.genre, self.song2.runtime) == True
        assert self.playlist1.add_song(self.song1.name, self.song1.singer, self.song1.genre, self.song1.runtime) == True
    
    def test_remove_song_functionality(self):
        # This function tests the remove_song functionality of the Playlist class
        self.playlist1.display_playlist
        assert self.playlist1.remove_song(self.song1.name) == True
        assert self.playlist1.remove_song(self.song2.name) == True
        assert self.playlist1.remove_song(self.song3.name) == False
      
    
    def test_sort_songs_functionality(self):
        # This function tests the sort_songs_name functionality of the Playlist class
        self.playlist1.sort_songs_name()     
        assert self.playlist1.songs[0].name == "Bohemian Rhapsody"
        assert self.playlist1.songs[1].name == "Stairway to Heaven"
        
    
    def test_rename_playlist_functionality(self):
        # This function tests the rename_playlist functionality of the Playlist class
        self.playlist1.rename_playlist("Fever Dream")
        assert self.playlist1.name == "Fever Dream"
        assert self.playlist1.name != "My Rock Favorites"
        
class TestDatabase:
    def setUp(self):
        self.db = Database()
        self.db.load_user_data("test_users.txt")
        self.db.load_song_data("test_songs.txt")
        self.db.load_playlist_data("test_playlists.txt")

    def test_load_user_data(self):
        self.setUp()
        assert len(self.db.users) == 2
        assert self.db.users[0].username == "test_user"

    def test_load_song_data(self):
        self.setUp()
        assert len(self.db.songs) == 5
        assert self.db.songs[0].name == "Bohemian Rhapsody"

    def test_load_playlist_data(self):
        self.setUp()
        assert len(self.db.playlists) == 2
        assert self.db.playlists[0].name == "My Rock Favorites"

    def test_search_user(self):
        self.setUp()
        assert self.db.search("test_user").username == "test_user"
        assert self.db.search("non_existent_user") == None

    def test_add_remove_user(self):
        self.setUp()
        new_user = User("new_user", "password", "New User", [])
        self.db.add_user(new_user)
        assert len(self.db.users) == 3
        assert self.db.search("new_user").username == "new_user"
        self.db.remove_user(new_user)
        assert len(self.db.users) == 2

    def test_add_remove_song(self):
        self.setUp()
        new_song = Song("new_song", "new_genre", "new_singer", "1:00")
        self.db.add_song(new_song)
        assert len(self.db.songs) == 6
        self.db.remove_song(new_song)
        assert len(self.db.songs) == 5

    def test_add_remove_playlist(self):
        self.setUp()
        new_playlist = Playlist("new_playlist", "test_user", [])
        self.db.add_playlist(new_playlist)
        assert len(self.db.playlist) == 1
        self.db.remove_playlist(new_playlist, self.db.users[0])
        assert len(self.db.playlist) == 0





        
    
    
        
    
    
    
    
    
    
    