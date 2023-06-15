import requests
import json

def fetch_song_recommendations(title):
    search_url = "https://shazam.p.rapidapi.com/search"
    querystring = {"term": title, "locale": "en-US", "offset": "0", "limit": "5"}
    headers = {
        "X-RapidAPI-Key": "fd97387355msha67efe3f50346b4p1dd11fjsnfa6947d62730",
        "X-RapidAPI-Host": "shazam.p.rapidapi.com"
    }
    response = requests.get(search_url, headers=headers, params=querystring)
    converted_response = json.loads(response.text)
    key = converted_response['tracks']['hits'][0]['track']['key']
    
    recommendations_url = "https://shazam.p.rapidapi.com/songs/list-recommendations"
    querystring = {"key": str(key), "locale": "en-US"}
    response = requests.get(recommendations_url, headers=headers, params=querystring)
    converted_response = json.loads(response.text)
    
    unique_recommendations = set()
    for track in converted_response['tracks']:
        unique_recommendations.add(track['share']['subject'])
    
    return unique_recommendations

def display_recommendations(recommendations):
    print("\nHere are some songs you may like:\n")
    for i, track in enumerate(recommendations):
        print(track)

# Main program
if __name__ == "__main__":
    title = input("Please enter a song title: ")
    recommendations = fetch_song_recommendations(title)
    display_recommendations(recommendations)
