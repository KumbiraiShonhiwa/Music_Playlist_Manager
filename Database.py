from User import *
from Song import *
from Playlist import *

class Database:
    
    songs = [Song]
    users = [User]
    playlists = [Playlist]
    login_attempts = 0
    
    def __init__(self):
        # self.songs = []
        self.users = []
        # self.playlist = []

    def load_test_data(self, file_path="test_data.json"):
        import json

        with open(file_path, 'r') as f:
            data = json.load(f)

        for user_data in data:
            playlists = []

            for playlist_data in user_data.get("playlists", []):
                songs = []

                for song_data in playlist_data.get("songs", []):
                    song = Song(
                        song_data["name"],
                        song_data["genre"],
                        song_data["singer"],
                        song_data["runtime"]
                    )
                    songs.append(song)

                playlist = Playlist(
                    playlist_data["name"],
                    playlist_data["creator_name"],
                    songs
                )
                playlists.append(playlist)

            user = User(
                user_data["username"],
                user_data["password"],
                user_data["name"],
                playlists
            )

            self.users.append(user)

    # def load_user_data(self, file_path="Users.txt"):
    #     # This function is responsible for loading all the user data from the Users.txt file
    #     # This function will create a new user object and append it to the users array
    #     with open(file_path,"r") as file:
    #         lines = file.readlines()
            
    #         for line in lines[1:]:
    #             data = line.strip().split(",")
    #             username = data[0]
    #             password = data[1]
    #             name = data[2]
                
    #             playlist_string = data[3]
                
    #             if playlist_string:
    #                 playlist_data = playlist_string.split("|")
    #             else:
    #                 playlist_data = []
                
    #             user = User(username,password,name,playlist_data)
    #             self.users.append(user)
                
                
    
    # def load_song_data(self, file_path="Songs.txt"):
    #     # This function is responsible for loading all the song data from the Songs.txt file
    #     # This function will create a new song object and append it to the songs array
    #     with open(file_path,"r") as file:
    #         lines = file.readlines()
            
    #         for line in lines[1:]:
    #             data = line.strip().split(",")
    #             name = data[0]
    #             genre = data[1]
    #             singer = data[2]
    #             runtime = data[3]
                
    #             song = Song(name,genre,singer,runtime)
    #             self.songs.append(song)
                
    
    # def load_playlist_data(self, file_path="Playlists.txt"):
    #     # This function is responsible for loading all the playlist data from the Playlists.txt file
    #     # This function will create a new playlist object and append it to the playlists array
    #     with open(file_path,"r") as file:
    #         lines = file.readlines()
    #         for line in lines[1:]:
    #             data = line.strip().split(",")
    #             name = data[0]
    #             songs = data[1].split("|")
    #             creator = data[2]
    #             total_runtime = data[3]
                
    #             playlist = Playlist(name,songs=songs,creator=creator,total_runtime=total_runtime)
    #             self.playlists.append(playlist) 
    
    
    def authenticate(self):
        # This function is responsible for authenticating the user
        # The user will have 3 attempts to login
        # If the user fails to login after 3 attempts, the program will exit
        # If the user logs in successfully, the user object will be returned
        import maskpass
        while self.login_attempts < 3:
            username = input("Enter username: ")
            password = maskpass.askpass(mask="*")
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
                return None
        print("Too many login attempts. Exiting.")
        
    def login(self,username,password):
        # This function is responsible for logging in the user
        pass
        

                    
    def export_data(self,filename):
        pass
    
    def search(self,username):
        # Function will search for user object with the correct username
        # When the user object is found the function will return the user object
        # If the username is not found we print a message to alert this
        found_username = None
        for i in range(len(self.users)):
            if(self.users[i].username == username):
                found_username = self.users[i]
                return found_username
        if(found_username == None):
            print("User not found")
        return found_username
    
    def add_user(self,user):
        # Functions adds a user to the user array
        self.users.append(user)
    
    def add_song(self,song):
        # Functions adds a song to the song array
        self.songs.append(song)
    
    def add_playlist(self,playlist):
        # Functions adds a playlist to the playlist array
        self.playlist.append(playlist)
    
    def remove_user(self,user):
        # Functions removes a user from the user array
        self.users.remove(user)
        
    def remove_song(self,song):
        # Functions removes a song from the song array
        self.songs.remove(song)
    
    def remove_playlist(self,playlist,user):
        # Functions removes a playlist from the playlist array
        user.delete_playlist(playlist)
        self.playlists.remove(playlist)

    # def update_user(self,user):
    #     for i in range(len(self.users)):
    #         if(self.users[i].username == user.username):
    #             self.users[i] = user
    #             return True
    #         else:
    #             print("User not found")
    #             return False
    
    def update_song(self,song):
        # This function is provides the menu for updating a song
        # The user can update the name, singer, genre, runtime and allows a user to exit the menu.
        # The user will enter the new name for any of the options that they chose.
        # The function wil call update_details function on the song object and return the song object
        name = song.name
        singer = song.singer
        genre = song.genre
        runtime = song.runtime
        done = True
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
        song.update_details(name,singer,genre,runtime)      
        return song
    
    def update_playlist(self,playlist):
        # This function is responsible for updating the playlist
        # The user will be given a menu where they can change the name of the playlist, add a new song to the playlist and remove a song from the playlist
        # The user will enter the name of the song when they are adding a new song
        # The user will enter a new name when renaming the playlist
        # the user will select remove song, which triggers the playlist object's remove song function
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
                            self.playlists[i].print_songs()
                            song = input("Enter song name: ")
                            self.playlists[i].remove_song(song)
                        case "4":
                            done = False
                        case _:
                            print("Invalid input")
                return self.playlists[i]
        print("Playlist not found")
        return None
        
            
        
    
    def add_song_to_playlist(self,playlist,song,singer,genre,runtime):
        # Adds a song to the global playlist array (list)
        # The passed in parameters, self (Database object), playlist object and the name of the song    
        # Call the playlist objects add_song() to add the song name to the list of songs in the playlist
        playlist.add_song(song,singer,genre,runtime)
        
    
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
    
    # def search_playlist_song(self,song):
    #     song = None
    #     for i in range(len(self.songs)):
    #         if(self.songs[i].name == song):
    #             found_song= self.songs[i]
    #             return found_song
    #     if song == None:
    #         print("Song not found")
    #         return False
        
                    
    # def remove_song_from_playlist(self,playlist,song):
    #     for i in range(len(self.users)):
    #         if(self.users[i].username == playlist.creator):
    #             for j in range(len(self.users[i].playlists)):
    #                 if(self.users[i].playlists[j].name == playlist.name):
    #                     self.users[i].playlists[j].songs.remove(song)
    #                     return True 
    
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
                
    # def search_for_song_in_playlist(self,playlist,song_name):
    #     # This function will search for a song in the passed in playlist object
    #     # The passed in song_name is a string for the song name that is being looked for
    #     # The function returns playlist.songs[i] where i is the index of the song name that matches the passed in parameter
    #     for i in range(len(playlist.songs)):
    #         if(playlist.songs[i] == song_name):
    #             return playlist.songs[i]
    #     print("Song not found")
    #     return None
    
    # def update_song_name_in_playlist(self,playlist,song_name,new_name):
    #     # This function will update the name of a song in the passed in playlist object
    #     playlist_song_name = self.search_for_song_in_playlist(playlist,song_name)
    #     playlist_song_name = new_name
    #     return playlist_song_name
    
    def select_playlist(self,user):
        # This function allows users to select any playlist that they have created
        # This function will print out a list in a readable fashion
        # Users will input the number that correlates to the playlist they want.
        # Function returns a playlist object which is returned from the function search_playlists()
        print("Select a playlist: ")
        for i in range(len(user.playlists)):
            print(i+1,user.playlists[i].name)
        print(len(user.playlists)+1,"Exit")
        playlist_number = int(input())
        if playlist_number == len(user.playlists)+1:
            exit()
        playlist = user.playlists[playlist_number-1]
        return playlist
    
    def select_song(self,playlist):
        # This function allows users to select any song in the passed in playlist 
        # This function will print out a list in a readable fashion
        # Users will input the number that correlates to the song they want.
        # Function returns a song object.
        print("Select a song: ")
        for i in range(len(playlist.songs)):
            print(i+1,playlist.songs[i].name)
        print(len(playlist.songs)+1,"Exit")
        song_number = int(input())
        if song_number == len(playlist.songs)+1:
            exit()
        song = playlist.songs[song_number-1]
        return song
    
    def return_playlist_by_name(self,playlist_name):
        # This function will return a playlist object
        # Searching through the entire playlist array, if a playlist object's name matches the passed in string, we return the object else we print a not found message
        for i in range(len(self.playlists)):
            if(self.playlists[i].name == playlist_name):
                return self.playlists[i]
        print("Playlist not found")
        return None
    
    def run_menu(self,user):
        # This function is responsible for running the main menu of the application
        # The user will be able to select from a list of options
        # The user object is passed in as a parameter
        done = True
        if(user != None):
            print("Welcome",user.name)
            while done == True:
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
                        # This case is for adding a song to a playlist
                        playlist = self.select_playlist(user)
                        song_name = input("Enter song name: ")
                        song_singer_name = input("Enter song singer name: ")
                        song_genre = input("Enter song genre: ")
                        song_runtime = input("Enter song runtime: ")
                        playlist.add_song(song_name,song_singer_name,song_genre,song_runtime)
                        # self.add_song_to_playlist(playlist,song_name,song_singer_name,song_genre,song_runtime)
                        
                    case "2":
                        # This case is for changing the details of a song in a playlist
                        playlist = self.select_playlist(user)
                        song = self.select_song(playlist)
                        if(song == None):
                            print("Song not found")
                            continue
                        self.update_song(song)
                    case "3":
                        # This case is for renaming a playlist
                        playlist = self.select_playlist(user)
                        if(playlist == None):
                            print("Playlist not found")
                            continue
                        playlist.rename_playlist(input("Enter new name: "))
                    case "4":
                        # This case is for removing a playlist
                        done1 = True
                        while(done1 == True):
                            playlist = self.select_playlist(user)
                            if(playlist == None):
                                print("Playlist not found")
                                continue
                            user.delete_playlist(playlist)
                            user_input = input("Are you done (y/n): ")
                            if(user_input == "y"):
                                done1 = False
                            elif(user_input == "n"):
                                done1 = True
                            else:
                                print("Invalid input")
                                done1 = False
                    case "5":
                        # This case is for removing a song from a playlist
                        playlist = self.select_playlist(user)
                        song = self.select_song(playlist)
                        if(playlist == None or song == None):
                            print("Playlist or song not found")
                            continue
                        playlist.remove_song(song)
                        
                    case "6":
                        # This case is for identifying duplicated songs in playlists
                        done2 = True
                        while(done2 == True):
                            user.print_duplicate_songs()
                            user_input = input("Are you done (y/n): ")
                            if(user_input == "y"):
                                done2 = False
                            else:
                                done2 = True
                            
                    case "7":
                        # This case is for sorting the user's playlists by name
                        user.sort_user_plylists()
                        print("Playlists sorted successfully")
                    case "8":
                        # This case is for sorting the songs in a playlist by name
                        playlist = self.select_playlist(user)
                        if(playlist == None):
                            print("Playlist not found")
                            continue
                        playlist.sort_songs()
                        print("Songs sorted successfully")
                    case "9":
                        # This case is for shuffling the songs in a playlist
                        playlist = self.select_playlist(user)
                        if(playlist == None):
                            print("Playlist not found")
                            continue
                        playlist.shuffle_songs()
                        print("Songs shuffled successfully")
                    case "10":
                        # This case is for exporting a playlist to a text file
                        done3 = True
                        while done3:
                            playlist = self.select_playlist(user)
                            filename = "Demo_Playlist.txt"
                            playlist.export_to_text_file(filename)
                            print("Playlist exported successfully")
                            user_input = input("Are you done (y/n): ")
                            if(user_input == "y"):
                                done3 = False
                            elif(user_input == "n"):
                                done3 = True
                            else:
                                print("Invalid input")
                                done3 = False
                    case "11":
                        # This case is for exiting the program
                        exit()
                    case _:
                        # This case is for invalid input
                        print("Invalid input")
                        self.run_menu(user)