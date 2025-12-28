
class Song:
    # This is the Song class. It is responsible for creating a song object
    # A song object has a name, genre, singer and runtime
    name = ""
    genre = ""
    singer = any
    runtime = 0.0
    def __init__(self,name,genre,singer,runtime):
        # The constructor for the Song class
        # It takes in the name, genre, singer and runtime of the song
        self.name = name
        self.genre = genre
        self.singer = singer
        self.runtime = runtime
    
    def update_details(self,new_name,new_singer,new_genre,new_runtime):
        # This function updates the details of the song
        # It takes in the new name, singer, genre and runtime of the song
        
            self.name = new_name
            self.singer = new_singer
            self.genre = new_genre
            self.runtime = new_runtime
            
            
            
    def check_duplicates(self,other):
        # This function checks for duplicate songs
        # It takes in another song object and compares it to the current song object
        # It returns True if the songs are the same and False if they are not
        if self.name == other.name and self.singer == other.singer and self.genre == self.genre and self.runtime == other.runtime:
            return True
        else:
            return False
    
    def disiplay_song(self):
        # This function displays the details of the song
        print("Name: ",self.name,"\nSinger: ",self.singer,"\nGenre: ",self.genre,"\nRuntime: ",self.runtime)
        
