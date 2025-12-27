import copy
class User:
    # This is the User class. It is responsible for creating a user object
    # A user object has a username, password, name and a list of playlists
    username = ""
    password = ""
    name = ""
    playlists = []
    
    def __init__(self,username, password, name,playlists):
        # The constructor for the User class
        # It takes in the username, password, name and playlists of the user
        self.username = username
        self.password = password
        self.name = name
        self.playlists = playlists
        
    def create_playlist(self,name,songs,creator,total_rumtime):
        # This function creates a new playlist for the user
        # It takes in the name, songs, creator and total runtime of the playlist
        from Database import Playlist
        playlist = Playlist(name,songs,creator,total_rumtime)
        self.playlists.append(playlist)
        
    def delete_playlist(self,playlist):
        # This function deletes a playlist from the user's list of playlists
        # It takes in the playlist object to be deleted
        self.playlists.remove(playlist.name) 
        print(playlist.name,"deleted successfully")
        
    def get_playlist(self):
        # This function returns the user's playlists
        for playlist in self.playlists:
            return playlist
        
    def sort_user_plylists(self):
        # This function sorts the user's playlists in alphabetical order
        self.playlists.sort()
        for i in range(len(self.playlists)):
            print(self.playlists[i])
            
    def login(self,username,password):
        # This function logs in the user
        # It takes in the username and password of the user
        if(self.username == username and self.password == password):
            print("Login successful")
            return True
        else:
            print("Login failed")
            return False