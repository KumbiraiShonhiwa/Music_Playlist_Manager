import random

class Playlist:
    from Song import Song
    name = ""
    songs = [Song]
    creator = any
    total_runtime = 0
    def __init__(self,name,creator:any,songs:any,total_runtime=0):
        self.name = name
        self.creator = creator
        self.songs = songs
        self.total_runtime = total_runtime
        
    def add_song(self,song):
        self.songs.append(song)
        print(song,"added to playlist")
        
        
    def remove_song(self):
        self.print_songs()
        song = input("Enter song name: ")
        if(song not in self.songs):
            print("Song not found")
            return False
        else:
            self.songs.remove(song)
            print(song,"removed from playlist")
            return True
        
    
    def sort_songs(self):
        for i in range(len(self.songs)):
            for j in range(len(self.songs)):
                if(self.songs[i] < self.songs[j]):
                    temp = self.songs[i]
                    self.songs[i] = self.songs[j]
                    self.songs[j] = temp
        self.print_songs()
        
    def shuffle_songs(self):
        random.shuffle(self.songs)
        self.print_songs()
    
    def find_duplicates(self,playlist):
       for i in range(len(self.songs)):
           for j in range(len(playlist.songs)):
               if(self.songs[i] == playlist.songs[j]):
                   print("Duplicate found: ",self.songs[i])
                   return True
       print("No duplicates found")
       return False
    
    def rename_playlist(self,new_name):
        self.name = new_name
        print("Playlist renamed successfully")
  
        
    def calculate_runtime(self):
        for song in self.songs:
            self.total_runtime += song.runtime
        
    def print_songs(self):
        for song in self.songs:
            print(song)
            
    def get_number_of_songs(self):
        count = 0
        for song in self.songs:
            count += 1
        return count
    
    def get_songs(self):
        return self.songs
        
    def display_playlist(self):
        print("Name of Playlist: ",self.name, "Songs: ",self.print_songs(), "Total Runtime: ",self.total_runtime)
        
    def export_to_text_file(self,filename):
        # T
        with open(filename,"a") as file:
            file.write("PlaylistName: "+self.name+"\n")
            file.write("Songs: ")
            for song in self.songs:
                file.write(song+"|")
            file.write("CreatorName: "+self.creator+"\n")
            file.write("TotalRuntime: "+self.total_runtime+"\n")
            
        
    