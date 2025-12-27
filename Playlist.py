import random

class Playlist:
    # This is the Playlist class. It is responsible for creating a playlist object
    # A playlist object has a name, a creator, a list of songs and a total runtime
    name = ""
    songs = []
    creator = any
    total_runtime = 0
    def __init__(self,name,creator:any,songs:any,total_runtime=0):
        # The constructor for the Playlist class
        # It takes in the name, creator, songs and total runtime of the playlist
        self.name = name
        self.creator = creator
        self.songs = songs
        self.total_runtime = total_runtime
        
    def add_song(self,song):
        # This function adds a song to the playlist
        # It takes in the name of the song to be added
        self.songs.append(song)
        print(song,"added to ",self.name,"successfully")
        return True
        
        
    def remove_song(self,song):
        # This function removes a song from the playlist
        # It asks the user for the name of the song to be removed
        # If the song is found, it is removed and the function returns True
        # If the song is not found, an error message is displayed and the function returns False
        if(song not in self.songs):
            print("Song not found")
            return False
        else:
            self.songs.remove(song)
            print(song,"removed from",self.name,"successfully")
            return True
        
    
    def sort_songs(self):
        # This function sorts the songs in the playlist in alphabetical order
        for i in range(len(self.songs)):
            for j in range(len(self.songs)):
                if(self.songs[i] < self.songs[j]):
                    temp = self.songs[i]
                    self.songs[i] = self.songs[j]
                    self.songs[j] = temp
        self.print_songs()
        
    def sort_songs_name(self):
        # This function sorts the songs in the playlist in alphabetical order
        for i in range(len(self.songs)):
            for j in range(len(self.songs)):
                if(self.songs[i].name < self.songs[j].name):
                    temp = self.songs[i]
                    self.songs[i] = self.songs[j]
                    self.songs[j] = temp
        self.print_songs()
        
        
    def shuffle_songs(self):
        # This function shuffles the songs in the playlist
        random.shuffle(self.songs)
        self.print_songs()
    
    def find_duplicates(self,playlist):
        # This function checks for duplicate songs between two playlists
        # It takes in another playlist object and compares the songs in the two playlists
        # It returns True if a duplicate is found and False if not
       for i in range(len(self.songs)):
           for j in range(len(playlist.songs)):
               if(self.songs[i] == playlist.songs[j]):
                   print("Duplicate found: ",self.songs[i],"in",self.name,"and",playlist.name)
                   return True
       print("No duplicates found")
       return False
    
    def rename_playlist(self,new_name):
        # This function renames the playlist
        # It takes in the new name for the playlist
        self.name = new_name
        print("Playlist renamed to",self.name,"successfully")
        
  
        
    def calculate_runtime(self):
        # This function calculates the total runtime of the playlist
        self.total_runtime = 0
        for song in self.songs:
            self.total_runtime += song.runtime
        
    def print_songs(self):
        # This function prints the songs in the playlist
        for song in self.songs:
            print(song)
            
    def get_number_of_songs(self):
        # This function returns the number of songs in the playlist
        count = 0
        for song in self.songs:
            count += 1
        return count
    
    def get_songs(self):
        # This function returns the list of songs in the playlist
        return self.songs
        
    def display_playlist(self):
        # This function displays the details of the playlist
        print("Name of Playlist: ",self.name, "Songs: ",self.print_songs(), "Total Runtime: ",self.total_runtime)
        
    def export_to_text_file(self,filename):
        # This function exports the playlist to a text file
        # It takes in the name of the file to be created
        with open(filename,"a") as file:
            file.write("PlaylistName: "+self.name+"\n")
            file.write("Songs: ")
            for song in self.songs:
                file.write(song+"|")
            file.write("CreatorName: "+self.creator+"\n")
            file.write("TotalRuntime: "+self.total_runtime+"\n")
            
        
    