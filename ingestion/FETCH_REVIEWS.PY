from google_play_scraper import reviews
import pandas as pd
import os

def fetch_reviews(app_id = "com.spotify.music", count = 300):
    os.makedirs("data",exist_ok = True)
    
    result, _ = reviews(
        app_id,
        lang = "en",
        country = "us",
        count = count
    )
    
    df = pd.DataFrame(result)[["content", "score", "at"]]
    df.columns = ["review", "rating", "date"]
    
    df.to_csv("review.csv", index = False)
    print("Reviews saved.")
    
if __name__ == "__main__" :
    fetch_reviews()