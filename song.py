import requests
import json

def fetch_song_recommendations(title):
    # Shazam API endpoint for searching songs
    search_url = "https://shazam.p.rapidapi.com/search"

    # Parameters for the search query
    querystring = {"term": title, "locale": "en-US", "offset": "0", "limit": "5"}

    # Headers containing API key and host
    headers = {
        "X-RapidAPI-Key": "fd97387355msha67efe3f50346b4p1dd11fjsnfa6947d62730",
        "X-RapidAPI-Host": "shazam.p.rapidapi.com"
    }

    # Send a GET request to the search endpoint
    response = requests.get(search_url, headers=headers, params=querystring)

    # Parse the JSON response
    converted_response = json.loads(response.text)

    # Extract the key of the first track from the search results
    key = converted_response['tracks']['hits'][0]['track']['key']

    # Shazam API endpoint for getting song recommendations
    recommendations_url = "https://shazam.p.rapidapi.com/songs/list-recommendations"

    # Parameters for the recommendation query using the extracted key
    querystring = {"key": str(key), "locale": "en-US"}

    # Send a GET request to the recommendation endpoint
    response = requests.get(recommendations_url, headers=headers, params=querystring)

    # Parse the JSON response
    converted_response = json.loads(response.text)

    # Store unique song recommendations in a set
    unique_recommendations = set()
    for track in converted_response['tracks']:
        unique_recommendations.add(track['share']['subject'])

    return unique_recommendations

def display_recommendations(recommendations):
    # Display the song recommendations
    print("\nHere are some songs you may like:\n")
    for i, track in enumerate(recommendations):
        print(track)

# Main program
if __name__ == "__main__":
    # Get user input for the song title
    title = input("Please enter a song title: ")

    # Fetch song recommendations based on the title
    recommendations = fetch_song_recommendations(title)

    # Display the recommendations
    display_recommendations(recommendations)
