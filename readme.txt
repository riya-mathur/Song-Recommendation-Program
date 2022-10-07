This is a backend python program which utilizes Shazam’s public APIs to search and recommend songs to the user.


Search endpoint:
The user enters a title which is put through a query string in order to get a response containing the key for the song. This response is accessed using the loads() method in order to parse a JSON string and convert it into a Python dictionary. From this dictionary, the key is extracted. 


Recommend endpoint:
The key for the song is converted into a string in order to pass it through the query string, which produces a response containing a large list of recommended songs. From here, I converted the JSON string into a Python dictionary and chose to extract a list of 6 recommended songs.
