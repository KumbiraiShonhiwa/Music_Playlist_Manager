
class Song:
    
    name = ""
    genre = ""
    singer = any
    runtime = 0.0
    def __init__(self,name,genre,singer,runtime):
        self.name = name
        self.genre = genre
        self.singer = singer
        self.runtime = runtime
    
    def update_details(self,new_name,new_singer,new_genre,new_runtime):
            self.name = new_name
            self.singer = new_singer
            self.genre = new_genre
            self.runtime = new_runtime
            
            
            
    def check_duplicates(self,other):
        if self.name == other.name and self.singer == other.singer and self.genre == self.genre and self.runtime == other.runtime:
            return True
        else:
            return False
    
    def disiplay_song(self):
        print("Name: ",self.name,"Singer: ",self.singer,"Genre: ",self.genre,"Runtime: ",self.runtime)
        
