from flask import Flask, render_template, request, jsonify, session, redirect, url_for, send_file
from werkzeug.security import generate_password_hash, check_password_hash
import json
import os
from datetime import timedelta
import random
from io import StringIO

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)

# In-memory storage (in production, use a database)
users_db = {}
playlists_db = {}


def load_test_data():
    """Load test data from test_data.json"""
    try:
        with open('test_data.json', 'r') as f:
            data = json.load(f)

        for user_data in data:
            username = user_data['username']
            users_db[username] = {
                'username': username,
                'password': user_data['password'],  # In production, hash this
                'name': user_data['name']
            }

            playlists_db[username] = []
            for playlist_data in user_data.get('playlists', []):
                playlist = {
                    'id': f"{username}_{len(playlists_db[username])}",
                    'name': playlist_data['name'],
                    'creator': playlist_data['creator_name'],
                    'songs': playlist_data['songs']
                }
                playlists_db[username].append(playlist)
    except FileNotFoundError:
        # Create default admin user if no test data
        users_db['admin'] = {
            'username': 'admin',
            'password': 'admin',
            'name': 'Administrator'
        }
        playlists_db['admin'] = []


# Load data on startup
load_test_data()


@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    print(data)
    username = data.get('username')
    password = data.get('password')
    print(users_db[username]['password'])

    if username in users_db and users_db[username]['password'] == password:
        session['username'] = username
        session['name'] = users_db[username]['name']
        return jsonify({'success': True, 'message': 'Login successful'})

    return jsonify({'success': False, 'message': 'Invalid credentials'}), 401


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('index'))
    return render_template('dashboard.html', name=session.get('name'))


@app.route('/api/playlists', methods=['GET'])
def get_playlists():
    if 'username' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    username = session['username']
    return jsonify(playlists_db.get(username, []))


@app.route('/api/playlists', methods=['POST'])
def create_playlist():
    if 'username' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.json
    username = session['username']

    if username not in playlists_db:
        playlists_db[username] = []

    playlist = {
        'id': f"{username}_{len(playlists_db[username])}",
        'name': data.get('name', 'New Playlist'),
        'creator': username,
        'songs': []
    }

    playlists_db[username].append(playlist)
    return jsonify(playlist)


@app.route('/api/playlists/<playlist_id>', methods=['PUT'])
def update_playlist(playlist_id):
    if 'username' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    username = session['username']
    data = request.json

    for playlist in playlists_db.get(username, []):
        if playlist['id'] == playlist_id:
            if 'name' in data:
                playlist['name'] = data['name']
            if 'songs' in data:
                playlist['songs'] = data['songs']
            return jsonify(playlist)

    return jsonify({'error': 'Playlist not found'}), 404


@app.route('/api/playlists/<playlist_id>', methods=['DELETE'])
def delete_playlist(playlist_id):
    if 'username' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    username = session['username']

    playlists = playlists_db.get(username, [])
    playlists_db[username] = [p for p in playlists if p['id'] != playlist_id]

    return jsonify({'success': True})


@app.route('/api/playlists/<playlist_id>/songs', methods=['POST'])
def add_song(playlist_id):
    if 'username' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    username = session['username']
    data = request.json

    for playlist in playlists_db.get(username, []):
        if playlist['id'] == playlist_id:
            song = {
                'name': data.get('name'),
                'singer': data.get('singer'),
                'genre': data.get('genre'),
                'runtime': data.get('runtime', '0:00')
            }
            playlist['songs'].append(song)
            return jsonify(song)

    return jsonify({'error': 'Playlist not found'}), 404


@app.route('/api/playlists/<playlist_id>/songs/<int:song_index>', methods=['PUT'])
def update_song(playlist_id, song_index):
    if 'username' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    username = session['username']
    data = request.json

    for playlist in playlists_db.get(username, []):
        if playlist['id'] == playlist_id:
            if 0 <= song_index < len(playlist['songs']):
                playlist['songs'][song_index].update(data)
                return jsonify(playlist['songs'][song_index])

    return jsonify({'error': 'Song not found'}), 404


@app.route('/api/playlists/<playlist_id>/songs/<int:song_index>', methods=['DELETE'])
def delete_song(playlist_id, song_index):
    if 'username' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    username = session['username']

    for playlist in playlists_db.get(username, []):
        if playlist['id'] == playlist_id:
            if 0 <= song_index < len(playlist['songs']):
                playlist['songs'].pop(song_index)
                return jsonify({'success': True})

    return jsonify({'error': 'Song not found'}), 404


@app.route('/api/playlists/<playlist_id>/sort', methods=['POST'])
def sort_playlist_songs(playlist_id):
    if 'username' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    username = session['username']

    for playlist in playlists_db.get(username, []):
        if playlist['id'] == playlist_id:
            playlist['songs'].sort(key=lambda s: s['name'].lower())
            return jsonify(playlist)

    return jsonify({'error': 'Playlist not found'}), 404


@app.route('/api/playlists/<playlist_id>/shuffle', methods=['POST'])
def shuffle_playlist_songs(playlist_id):
    if 'username' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    username = session['username']

    for playlist in playlists_db.get(username, []):
        if playlist['id'] == playlist_id:
            random.shuffle(playlist['songs'])
            return jsonify(playlist)

    return jsonify({'error': 'Playlist not found'}), 404


@app.route('/api/playlists/sort', methods=['POST'])
def sort_all_playlists():
    if 'username' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    username = session['username']
    playlists_db[username].sort(key=lambda p: p['name'].lower())

    return jsonify(playlists_db[username])


@app.route('/api/duplicates', methods=['GET'])
def find_duplicates():
    if 'username' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    username = session['username']
    playlists = playlists_db.get(username, [])

    # Find duplicate songs across playlists
    song_locations = {}

    for playlist in playlists:
        for song in playlist['songs']:
            key = f"{song['name']}|{song['singer']}"
            if key not in song_locations:
                song_locations[key] = {
                    'song': song,
                    'playlists': []
                }
            song_locations[key]['playlists'].append(playlist['name'])

    # Filter only duplicates (appearing in more than one playlist)
    duplicates = [
        {
            'song': data['song'],
            'playlists': data['playlists']
        }
        for data in song_locations.values()
        if len(data['playlists']) > 1
    ]

    return jsonify(duplicates)


@app.route('/api/export', methods=['GET'])
def export_playlists():
    if 'username' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    username = session['username']
    playlists = playlists_db.get(username, [])

    output = StringIO()

    for playlist in playlists:
        output.write(f"PlaylistName: {playlist['name']}\n")
        output.write(f"Creator: {playlist['creator']}\n")
        output.write("Songs:\n")

        for song in playlist['songs']:
            output.write(
                f"  - {song['name']} by {song['singer']} ({song['genre']}) - {song.get('runtime', 'N/A')}\n")

        output.write("\n" + "="*50 + "\n\n")

    content = output.getvalue()
    output.close()

    return jsonify({'content': content})


@app.route('/api/import', methods=['POST'])
def import_playlists():
    if 'username' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    try:
        data = request.json
        username = session['username']
        imported_playlists = data.get('playlists', [])

        if username not in playlists_db:
            playlists_db[username] = []

        for playlist_data in imported_playlists:
            playlist = {
                'id': f"{username}_{len(playlists_db[username])}",
                'name': playlist_data.get('name', 'Imported Playlist'),
                'creator': username,
                'songs': playlist_data.get('songs', [])
            }
            playlists_db[username].append(playlist)

        return jsonify({'success': True, 'count': len(imported_playlists)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
