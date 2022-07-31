import requests
import json
import sys


url = "https://shazam.p.rapidapi.com/search"

title = input('Please enter a song title: ')
querystring = {"term":title,"locale":"en-US","offset":"0","limit":"5"}

headers = {
	"X-RapidAPI-Key": "fd97387355msha67efe3f50346b4p1dd11fjsnfa6947d62730",
	"X-RapidAPI-Host": "shazam.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

converted_response = json.loads(response.text)
key = converted_response['tracks']['hits'][0]['track']['key']

# Now we use the key from the search endpoint to plug into the recommendation endpoint

url = "https://shazam.p.rapidapi.com/songs/list-recommendations"

new_key = str(key)
querystring = {"key":new_key,"locale":"en-US"}

headers = {
	"X-RapidAPI-Key": "fd97387355msha67efe3f50346b4p1dd11fjsnfa6947d62730",
	"X-RapidAPI-Host": "shazam.p.rapidapi.com"
}

response2 = requests.request("GET", url, headers=headers, params=querystring)

converted_response2 = json.loads(response2.text)

for i in range(6):
	print(converted_response2['tracks'][i]['share']['subject'])
