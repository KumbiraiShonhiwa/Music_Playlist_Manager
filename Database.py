from User import *
from Song import *
from Playlist import *

class Database:
    
    songs = [Song]
    users = [User]
    playlists = [Playlist]
    login_attempts = 0
    
    def __init__(self):
        self.songs = []
        self.users = []
        self.playlist = []

    def load_user_data(self):
        with open("Assignment_2/Users.txt","r") as file:
            lines = file.readlines()
            
            for line in lines[1:]:
                data = line.strip().split(",")
                username = data[0]
                password = data[1]
                name = data[2]
                
                playlist_string = data[3]
                
                if playlist_string:
                    playlist_data = playlist_string.split("|")
                else:
                    playlist_data = []
                
                user = User(username,password,name,playlist_data)
                self.users.append(user)
                
                
    
    def load_song_data(self):
        with open("Assignment_2/Songs.txt","r") as file:
            lines = file.readlines()
            
            for line in lines[1:]:
                data = line.strip().split(",")
                name = data[0]
                genre = data[1]
                singer = data[2]
                runtime = data[3]
                
                song = Song(name,genre,singer,runtime)
                self.songs.append(song)
                
    
    def load_playlist_data(self):
        with open("Assignment_2/Playlists.txt","r") as file:
            lines = file.readlines()
            for line in lines[1:]:
                data = line.strip().split(",")
                name = data[0]
                songs = data[1].split("|")
                creator = data[2]
                total_runtime = data[3]
                
                playlist = Playlist(name,songs=songs,creator=creator,total_runtime=total_runtime)
                self.playlists.append(playlist) 
    
    
    def authenticate(self):
        while self.login_attempts < 3:
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = self.search(username)
            if user != None:
                if user.password == password:
                    print("Login successful\n")
                    return user
                else:
                    print("Incorrect password")
                    self.login_attempts += 1
                    continue
            else:
                print("User not found")
                return False
        print("Too many login attempts. Exiting.")
        exit()

                    
    def export_data(self,filename):
        pass
    
    def search(self,username):
        found_username = None
        for i in range(len(self.users)):
            if(self.users[i].username == username):
                found_username = self.users[i]
                return found_username
        if(found_username == None):
            print("User not found")
        return found_username
    
    def add_user(self,user):
        self.users.append(user)
    
    def add_song(self,song):
        self.songs.append(song)
    
    def add_playlist(self,playlist):
        self.playlist.append(playlist)
    
    def remove_user(self,user):
        self.users.remove(user)
        
    def remove_song(self,song):
        self.songs.remove(song)
    
    def remove_playlist(self,playlist,user):
        user.delete_playlist(playlist)
        self.playlists.remove(playlist)

    def update_user(self,user):
        for i in range(len(self.users)):
            if(self.users[i].username == user.username):
                self.users[i] = user
                return True
            else:
                print("User not found")
                return False
    
    def update_song(self,song):
        done = True
        for i in range(len(self.songs)):
            if(self.songs[i].name == song):
                name = self.songs[i].name
                singer = self.songs[i].singer
                genre = self.songs[i].genre
                runtime = self.songs[i].runtime
                while done != False:
                    print("Update song details: ")
                    print("1. Name")
                    print("2. Singer")
                    print("3. Genre")
                    print("4. Runtime")
                    print("5. Exit")
                    match input():
                        case "1":
                            name = input("Enter new name: ")
                        case "2":
                            singer = input("Enter new singer: ")
                        case "3":
                            genre = input("Enter new genre: ")
                        case "4":
                            runtime = input("Enter new runtime: ")
                        case "5":
                            done = False
                        case _:
                            print("Invalid input")
                self.songs[i].update_details(name,singer,genre,runtime)
                return self.songs[i]
        print("Song not found")
        return None
    
    def update_playlist(self,playlist):
        done = True
        for i in range(len(self.playlists)):
            if(self.playlists[i].name == playlist.name):
                name = self.playlists[i].name
                songs = self.playlists[i].songs
                creator = self.playlists[i].creator
                total_runtime = self.playlists[i].total_runtime
                while done != False:
                    print("Update playlist details: ")
                    print("1. Rename Playlist")
                    print("2. Add new song to playlist")
                    print("3. Remove song")
                    print("4. Exit")
                    match input():
                        case "1":
                            name = input("Enter new name: ")
                            self.playlists[i].rename_playlist(name)
                        case "2":
                            song = input("Enter new song name: ")
                            self.playlists[i].add_song(song)
                        case "3":
                            self.playlists[i].remove_song()
                        case "4":
                            done = False
                        case _:
                            print("Invalid input")
                return self.playlists[i]
        print("Playlist not found")
        return None
        
            
        
    
    def add_song_to_playlist(self,playlist,song):
        # Adds a song to the global playlist array (list)
        # The passed in parameters, self (Database object), playlist object and the name of the song    
        # Call the playlist objects add_song() to add the song name to the list of songs in the playlist
        playlist = self.search_playlists(playlist.name)
        playlist.add_song(song)
        
    
    def search_playlists(self,playlist):
        # Search the global playlist array (list).
        # The passed in parameters, self (Database object) and playlist (name of the playlist)
        # If the playlist is found, return the playlist object.
        # If the playlist is not found, return None.
        found_playlist = None
        for i in range(len(self.playlists)):
            if(self.playlists[i].name == playlist):
                found_playlist = self.playlists[i]
                return found_playlist
        if(found_playlist == None):
            print("Playlist not found")
        return found_playlist
    
    def search_playlist_song(self,song):
        song = None
        for i in range(len(self.songs)):
            if(self.songs[i].name == song):
                found_song= self.songs[i]
                return found_song
        if song == None:
            print("Song not found")
            return False
        
                    
    def remove_song_from_playlist(self,playlist,song):
        for i in range(len(self.users)):
            if(self.users[i].username == playlist.creator):
                for j in range(len(self.users[i].playlists)):
                    if(self.users[i].playlists[j].name == playlist.name):
                        self.users[i].playlists[j].songs.remove(song)
                        return True 
    
    def identify_global_duplicates(self,user):
        # Fucntion will check for the duplicated songs in the passed in playlist object
        # Prints out the name of the playlist with duplicated songs
        
        user_playlists = [Playlist]
        for i in range(len(user.playlists)):
            playlist = self.return_playlist_by_name(user.playlists[i])
            user_playlists.append(playlist)
        
        for i in range(len(user_playlists)):
            for j in range(len(user_playlists)-1):
                user_playlists[i].find_duplicates(user_playlists[j+1])
            
    
    
    def sort_playlists_by_name(self):
        pass
    
    def select_playlist(self,user):
        print("Select a playlist: ")
        for i in range(len(user.playlists)):
            print(i+1,user.playlists[i])
        playlist_number = int(input())
        playlist = user.playlists[playlist_number-1]
        return self.search_playlists(playlist)
    
    def select_song(self,playlist):
        print("Select a song: ")
        for i in range(len(playlist.songs)):
            print(i+1,playlist.songs[i])
        song_number = int(input())
        song = playlist.songs[song_number-1]
        return song
    
    def return_playlist_by_name(self,playlist_name):
        for i in range(len(self.playlists)):
            if(self.playlists[i].name == playlist_name):
                return self.playlists[i]
        print("Playlist not found")
        return None
    
    def run_menu(self,user):
        if(user != None):
            print("Welcome",user.name)
            print("Select an option: \n")
            print("1. Add a song to a playlist.")
            print("2. Change song details for a playlist.")
            print("3. Rename a playlist.")
            print("4. Remove a playlist.")
            print("5. Remove a song from a playlist.")
            print("6. Identify duplicated songs in playlists.")
            print("7. Sort playlists by name.")
            print("8. Sort songs in each playlist by name.")
            print("9. Shuffle songs in each playlist.")
            print("10. Export playlists to a text file.")
            print("11. Exit")
            match input():
                case "1":
                    playlist = self.select_playlist(user)
                    song_name = input("Enter song name: ")
                    self.add_song_to_playlist(playlist,song_name)
                    print(song_name,"added to",playlist.name,"successfully")
                case "2":
                    playlist = self.select_playlist(user)
                    song = self.select_song(playlist)
                    updated_song = self.update_song(song)
                    print(updated_song.disiplay_song(),"Updated Successfully")
                case "3":
                    playlist = self.select_playlist(user)
                    self.update_playlist(playlist)
                case "4":
                    done = True
                    while(done == True):
                        playlist = self.select_playlist(user)
                        self.remove_playlist(playlist,user)
                        user_input = input("Are you done (y/n): ")
                        if(user_input == "y"):
                            done = False
                        elif(user_input == "n"):
                            done = True
                        else:
                            print("Invalid input")
                            done = False
                case "5":
                    playlist = self.select_playlist(user)
                    self.update_playlist(playlist)
                       
                case "6":
                    self.identify_global_duplicates(user)
                    user_input = input("Are you done (y/n): ")
                        
                case "7":
                    user.sort_user_plylists()
                    print("Playlists sorted successfully")
                case "8":
                    playlist = self.select_playlist(self,user)
                    playlist.sort_songs()
                    print("Songs sorted successfully")
                case "9":
                    playlist = self.select_playlist(self,user)
                    playlist.shuffle_songs()
                    print("Songs shuffled successfully")
                case "10":
                    done = True
                    while done:
                        playlist = self.select_playlist(self,user)
                        filename = "Assignment_2/Demo_Playlist.txt"
                        playlist.export_to_text_file(filename)
                        print("Playlist exported successfully")
                        user_input = input("Are you done (y/n): ")
                        if(user_input == "y"):
                            done = False
                        elif(user_input == "n"):
                            done = True
                        else:
                            print("Invalid input")
                            done = False
                case "11":
                    exit()
                case _:
                    print("Invalid input")
                    self.run_menu()