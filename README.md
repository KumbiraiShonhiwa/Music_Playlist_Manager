# 🎵 Music Playlist Manager

A Python-based music playlist manager that allows users to create, organize, and manage playlists efficiently. The application supports song and user management, playlist editing, and basic persistence using file storage, with an optional web interface for interactive use.

## 🚀 Features

* Create, view, edit, and delete playlists
* Add, remove, and search songs
* User account management
* File-based data persistence
* Optional web interface
* Includes demo data and testing scripts

## 📁 Project Structure

```text
.
├── Application.py
├── Database.py
├── Main.py
├── Playlist.py
├── Singer.py
├── Song.py
├── User.py
├── Web_App/                 # Web interface (if enabled)
├── test_data.json
├── Demo_Playlist.txt
├── Playlists.txt
├── Songs.txt
├── Users.txt
├── Testing.py
└── README.md
```

## 🧠 Getting Started

### 🛠 Prerequisites

* Python **3.8 or higher**

Check your Python version:

```bash
python --version
```

(Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

## 📦 Installation

If a `requirements.txt` file is present:

```bash
pip install -r requirements.txt
```

Otherwise, install any required dependencies manually (e.g., Flask for the web app):

```bash
pip install flask
```

## ▶️ Running the Application

### Command-Line Interface

Run the main program:

```bash
python Main.py
```

Follow the prompts to manage users, songs, and playlists.

### Web Interface (Optional)

If the web app is included:

```bash
cd Web_App
python app.py
```

Then open your browser at:

```text
http://localhost:5000
```

## 🧪 Testing

Run the test script to validate functionality:

```bash
pytest Testing.py
```

## 🗂 Demo Data

Sample files such as `Demo_Playlist.txt`, `Songs.txt`, and `Users.txt` are included to help you explore the application without manual data entry.

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes
4. Push to the branch
5. Open a pull request

## 📄 License

This project is licensed under the **MIT License**.

---
