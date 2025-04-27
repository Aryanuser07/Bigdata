# Bigdata
This project fetches popular movie data from TMDB (The Movie Database) using their API and stores it into a local MongoDB database.

🚀 Features
Fetch multiple pages of popular movies from TMDB.

Store movie details (like title, overview, rating, etc.) into MongoDB.

Clean and beginner-friendly Python code.

Easy to expand into a full Movie Recommendation System later.

🛠️ Setup Instructions
1. Install MongoDB
bash
Copy
Edit
sudo apt update
sudo apt install -y mongodb
sudo systemctl start mongodb
sudo systemctl enable mongodb
2. Install Python Libraries
bash
Copy
Edit
pip install -r requirements.txt
3. Add Your TMDB API Key
Open tmdb_to_mongo.py.

Replace this line:

python
Copy
Edit
API_KEY = "YOUR_API_KEY_HERE"
with your actual TMDB API Key.

4. Run the Script
bash
Copy
Edit
python tmdb_to_mongo.py

📂 Project Structure
bash
Copy
Edit

tmdb-mongo-project/
│
├── README.md          # Project information
├── requirements.txt   # Python libraries needed
└── tmdb_to_mongo.py   # Main Python script
📚 Requirements
Python 3.x

MongoDB installed locally

TMDB account with an API Key

✨ Future Ideas
Build a web app to show movies using Flask or React.

Add user ratings and build a recommendation engine using Apache Spark.

Host MongoDB and your app on cloud platforms like AWS, Azure, or GCP.

🌟 Credits
TMDB API

Built with ❤️ by Aryan Rawat
