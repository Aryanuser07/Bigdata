import requests
from pymongo import MongoClient
import time

# --- Config ---
API_KEY = "YOUR_API_KEY_HERE"  # <-- Replace with your TMDB API Key
TOTAL_PAGES = 5  # Number of pages to fetch

# --- MongoDB Setup ---
client = MongoClient("mongodb://localhost:27017/")
db = client["tmdb_db"]
collection = db["popular_movies"]

# Optional: Clear old data
collection.delete_many({})

# --- Fetch and Store ---
for page in range(1, TOTAL_PAGES + 1):
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page={page}"
    response = requests.get(url)
    data = response.json()

    if "results" in data:
        collection.insert_many(data["results"])
        print(f"Inserted Page {page} with {len(data['results'])} movies.")
    else:
        print(f"Failed at Page {page}")
    
    time.sleep(0.25)  # To avoid hitting rate limits

print("All done!")
