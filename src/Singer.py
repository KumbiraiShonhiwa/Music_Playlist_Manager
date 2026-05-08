from database import Song
class Singer:

    name = ""
    genre = ""
    Songs = []

    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.Songs = []

    def display_singer(self):
        print("Singer Name:", Singer.name)

    def add_song(self, song: Song):
        Singer.Songs.append(song)

    def remove_song(self, song: Song):
        Singer.Songs.remove(song)

    def get_discography(self):
        for song in self.Songs:
            song.disiplay_song()
