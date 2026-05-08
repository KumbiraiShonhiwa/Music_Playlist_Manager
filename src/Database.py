#!/usr/bin/env python
"""
This module handles database operations for the music playlist application.
"""
import json
import sys
import getpass
from user import User
from song import Song
from playlist import Playlist


class Database:
    """
    This class manages users, songs, and playlists in the music application.
    """
    songs = [Song]
    users = [User]
    playlists = [Playlist]
    login_attempts = 0

    def __init__(self):
        """Initializes the Database object."""
        # self.songs = []
        self.users = []
        # self.playlist = []

    def load_test_data(self, file_path="test_data.json"):
        """
        Loads test data from a JSON file to populate the database.

        Args:
            file_path (str): The path to the JSON file.
        """
        with open(file_path, 'r', encoding='utf-8') as f:
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

    def authenticate(self):
        # This function is responsible for authenticating the user
        # The user will have 3 attempts to login
        # If the user fails to login after 3 attempts, the program will exit
        # If the user logs in successfully, the user object will be returned
        while self.login_attempts < 3:
            username = input("Enter username: ")
            password = getpass.getpass(prompt="Enter password: ")
            user = self.search(username)
            if user is not None:
                if user.password == password:
                    print("Login successful\n")
                    return user
                
                print("Incorrect password")
                self.login_attempts += 1
                continue
            
            print("User not found")
            return None
        print("Too many login attempts. Exiting.")

    def search(self, username):
        # Function will search for user object with the correct username
        # When the user object is found the function will return the user object
        # If the username is not found we print a message to alert this
        found_username = None
        for i in range(len(self.users)):
            if (self.users[i].username == username):
                found_username = self.users[i]
                return found_username
        if (found_username == None):
            print("User not found")
        return found_username

    def update_song(self, song):
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
        song.update_details(name, singer, genre, runtime)
        return song

    def update_playlist(self, playlist):
        # This function is responsible for updating the playlist
        # The user will be given a menu where they can change the name of the playlist, add a new song to the playlist and remove a song from the playlist
        # The user will enter the name of the song when they are adding a new song
        # The user will enter a new name when renaming the playlist
        # the user will select remove song, which triggers the playlist object's remove song function
        done = True
        for i in range(len(self.playlists)):
            if (self.playlists[i].name == playlist.name):
                name = self.playlists[i].name
                songs = self.playlists[i].songs
                creator = self.playlists[i].creator
                total_runtime = self.playlists[i].total_runtime
                while done == True:
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

    def search_playlists(self, playlist):
        # Search the global playlist array (list).
        # The passed in parameters, self (Database object) and playlist (name of the playlist)
        # If the playlist is found, return the playlist object.
        # If the playlist is not found, return None.
        found_playlist = None
        for i in range(len(self.playlists)):
            if (self.playlists[i].name == playlist):
                found_playlist = self.playlists[i]
                return found_playlist
        if (found_playlist == None):
            print("Playlist not found")
        return found_playlist

    def select_playlist(self, user):
        # This function allows users to select any playlist that they have created
        # This function will print out a list in a readable fashion
        # Users will input the number that correlates to the playlist they want.
        # Function returns a playlist object which is returned from the function search_playlists()
        print("Select a playlist: ")
        for i in range(len(user.playlists)):
            print(i+1, user.playlists[i].name)
        print(len(user.playlists)+1, "Exit")
        playlist_number = int(input())
        if playlist_number == len(user.playlists)+1:
            exit()
        playlist = user.playlists[playlist_number-1]
        return playlist

    def select_song(self, playlist):
        # This function allows users to select any song in the passed in playlist
        # This function will print out a list in a readable fashion
        # Users will input the number that correlates to the song they want.
        # Function returns a song object.
        print("Select a song: ")
        for i in range(len(playlist.songs)):
            print(i+1, playlist.songs[i].name)
        print(len(playlist.songs)+1, "Exit")
        song_number = int(input())
        if song_number == len(playlist.songs)+1:
            exit()
        song = playlist.songs[song_number-1]
        return song

    def return_playlist_by_name(self, playlist_name):
        # This function will return a playlist object
        # Searching through the entire playlist array, if a playlist object's name matches the passed in string, we return the object else we print a not found message
        for i in range(len(self.playlists)):
            if (self.playlists[i].name == playlist_name):
                return self.playlists[i]
        print("Playlist not found")
        return None

    def run_menu(self, user):
        # This function is responsible for running the main menu of the application
        # The user will be able to select from a list of options
        # The user object is passed in as a parameter
        done = True
        if (user != None):
            print("Welcome", user.name,"\n")
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
                        playlist.add_song(
                            song_name, song_singer_name, song_genre, song_runtime)

                    case "2":
                        # This case is for changing the details of a song in a playlist
                        playlist = self.select_playlist(user)
                        song = self.select_song(playlist)
                        if (song == None):
                            print("Song not found")
                            continue
                        self.update_song(song)
                    case "3":
                        # This case is for renaming a playlist
                        playlist = self.select_playlist(user)
                        if (playlist == None):
                            print("Playlist not found")
                            continue
                        playlist.rename_playlist(input("Enter new name: "))
                    case "4":
                        # This case is for removing a playlist
                        done1 = True
                        while (done1 == True):
                            playlist = self.select_playlist(user)
                            if (playlist == None):
                                print("Playlist not found")

                            else:
                                user.delete_playlist(playlist)
                                user_input = input("Are you done (y/n): ")
                                if (user_input == "y"):
                                    done1 = False
                                elif (user_input == "n"):
                                    done1 = True
                                else:
                                    print("Invalid input")
                                    done1 = False
                    case "5":
                        # This case is for removing a song from a playlist
                        playlist = self.select_playlist(user)
                        song = self.select_song(playlist)
                        if (playlist == None or song == None):
                            print("Playlist or song not found")
                            continue
                        else:
                            playlist.remove_song(song)

                    case "6":
                        # This case is for identifying duplicated songs in playlists
                        done2 = True
                        while (done2 == True):
                            user.print_duplicate_songs()
                            user_input = input("Are you done (y/n): ")
                            if (user_input == "y"):
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
                        if (playlist == None):
                            print("Playlist not found")
                            continue
                        else:
                            playlist.sort_songs()
                            print("Songs sorted successfully")
                    case "9":
                        # This case is for shuffling the songs in a playlist
                        playlist = self.select_playlist(user)
                        if (playlist == None):
                            print("Playlist not found")
                            continue
                        else:
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
                            if (user_input == "y"):
                                done3 = False
                            elif (user_input == "n"):
                                done3 = True
                            else:
                                print("Invalid input")
                                done3 = False
                    case "11":
                        # This case is for exiting the program
                        SystemExit()
                    case _:
                        # This case is for invalid input
                        print("Invalid input")
                        self.run_menu(user)