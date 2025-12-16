import copy
class User:
    username = ""
    password = ""
    name = ""
    playlists = []
    
    def __init__(self,username, password, name,playlists):
        self.username = username
        self.password = password
        self.name = name
        self.playlists = playlists
        
    def create_playlist(self,name,songs,creator,total_rumtime):
        from Database import Playlist
        playlist = Playlist(name,songs,creator,total_rumtime)
        self.playlists.append(playlist)
        
    def delete_playlist(self,playlist):
        self.playlists.remove(playlist.name) 
        print(playlist.name,"deleted successfully")
        
    def get_playlist(self):
        for playlist in self.playlists:
            return playlist
        
    def sort_user_plylists(self):
        self.playlists.sort()
        for i in range(len(self.playlists)):
            print(self.playlists[i])