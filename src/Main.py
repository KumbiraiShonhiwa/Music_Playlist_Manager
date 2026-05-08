from Database import Database
from Song import Song
from Singer import Singer
from User import User
from Playlist import Playlist

def main():
    print("==========================================")
    print("       MUSIC SYSTEM FUNCTIONALITY TEST    ")
    print("==========================================")

    # 1. Initialize the Database
    # Note: In your code, Database acts mostly as a static container, 
    # but we instantiate it to access methods like authenticate.
    db = Database()
    print("\n[+] Database initialized.")

    # 2. Create Singers
    singer_1 = Singer("The Weeknd", "R&B")
    singer_2 = Singer("Daft Punk", "Electronic")
    print(f"[+] Singers Created: {singer_1.name}, {singer_2.name}")

    # 3. Create Songs
    print("\n[+] Creating Songs...")
    # Parameters: name, genre, singer, runtime
    song_1 = Song("Starboy", "Pop", singer_1, 3.50)
    song_2 = Song("I Feel It Coming", "Pop", singer_1, 4.29)
    song_3 = Song("One More Time", "Electronic", singer_2, 5.20)
    song_4 = Song("Harder, Better, Faster", "Electronic", singer_2, 3.45)
    
    # Display a song to test display_song()
    print("    > Testing display_song() for Song 1:")
    song_1.disiplay_song()

    # 4. Create User
    print("\n[+] Creating User...")
    # Parameters: username, password, name, playlists
    user_1 = User("music_fan_99", "securePass123", "John Doe", [])
    
    # Manually add user to db instance list for the authentication test later
    # (Since your User class uses a static Database import which might reference a different scope)
    db.users.append(user_1) 
    print(f"    User '{user_1.username}' created.")

    # 5. User Creates a Playlist
    print("\n[+] User creating a Playlist...")
    # Parameters: name, songs (empty list), creator, total_runtime
    user_1.create_playlist("Gym Vibes", [], user_1, 0.0)
    
    # Retrieve the playlist (Logic based on your User.get_playlist method)
    # Note: User.get_playlist in your code returns immediately on the first item.
    my_playlist = user_1.playlists[0] 
    print(f"    Playlist '{my_playlist.name}' created.")

    # 6. Add Songs to Playlist
    print("\n[+] Adding songs to Playlist...")
    my_playlist.add_song(song_3)
    my_playlist.add_song(song_4)
    my_playlist.add_song(song_1)
    print(f"    Current song count: {my_playlist.get_number_of_songs()}")

    # 7. Test Runtime Calculation
    print("\n[+] Calculating Runtime...")
    my_playlist.calculate_runtime()
    print(f"    Total Runtime: {my_playlist.total_runtime} mins")

    # 8. Test Duplicate Detection
    print("\n[+] Testing Duplicate Detection...")
    # Add a duplicate song (song_3) to trigger detection
    my_playlist.add_song(song_3) 
    print("    Added a duplicate song intentionally.")
    
    # Note: There is a small logic error in your Playlist.find_duplicates method signature call,
    # assuming it is fixed, this runs:
    has_duplicates = my_playlist.find_duplicates()
    if has_duplicates:
        print("    > SUCCESS: Duplicates detected.")
    else:
        print("    > FAIL: Duplicates not detected (or list checked against itself incorrectly).")

    # 9. Test Shuffling
    print("\n[+] Testing Shuffle...")
    print("    Order before shuffle:")
    my_playlist.sort_songs()
        
    my_playlist.shuffle_songs()
    
    print("    Order after shuffle:")
    for s in my_playlist.get_songs():
        print(f"    - {s.name}")

    # 10. Database Authentication Test
    print("\n[+] Testing Database Authentication...")
    
    # Test Correct Login
    print("    Attempting correct login...")
    is_auth = db.authenticate("music_fan_99", "securePass123")
    if is_auth:
        print("    > Login Successful.")
    else:
        print("    > Login Failed.")

    # Test Incorrect Login
    print("    Attempting incorrect password...")
    db.authenticate("music_fan_99", "wrongpass")

    print("\n==========================================")
    print("             TEST COMPLETED               ")
    print("==========================================")

if __name__ == "__main__":
    main()