import pandas as pd
import functools
import operator
from datetime import datetime

def get_current_song(current):
    if current.status_code == 201:
        print("Token has expiered!")
        return False
    if current.status_code != 200:
        print("Nothing is playing :C")
        return False
    if current.status_code == 401:
        print(data["error"]["message"])
        return False
    if current.status_code == 204:
        print("Spotify is not playing")
        return False
    if current.status_code == 200:
        data = current.json()
        timestamp = int(data["timestamp"])
        print(timestamp)
        # Formating
        time = datetime.fromtimestamp(timestamp/1e3)
        print(type(time))
        # Name of the album
        album = data["item"]["album"]["name"]
        # Name of the Artist
        artist = data["item"]["album"]["artists"][0]['name']
        # Name of the Song
        song = data["item"]["name"]
        # Popularity
        popularity = data["item"]["popularity"]
        # uri
        uri = data["item"]["uri"]
        # Link to the track:
        track_id = data["item"]["preview_url"]
        # Explicit
        explicit = data["item"]["explicit"]
        # Image
        image_id = data["item"]["album"]["images"][0]["url"]
        # Available Market count
        market_count = len(data["item"]["available_markets"])
    return [time, album,artist,song,popularity,explicit,market_count]

# Returning top artists:
# type: tracks/artists
# time_range: short_term, midium_term, long_term
# limit: int
# offset: int
def try_me(personal):
    personal = personal.json()
    print(len(personal["items"][0]["album"]["available_markets"]))
def get_personal_data(personal, personal_args):
    songs = []
    personal = personal.json()
    print(type(personal))
    for i in range(0, personal_args[2]):
        number_of_authors = len(personal["items"][i]["album"]["artists"])
        #Getting Authors
        authors = get_authors(personal, i, number_of_authors)

        dict = {
                "Name": personal["items"][i]["name"],
                "Main Author": authors[0],
                "Populartiy": personal["items"][i]["popularity"],
                "Album Type": personal["items"][i]["album"]["album_type"],
                "Available Markets": len(personal["items"][i]["album"]["available_markets"])
            }
        # Additional columns if the song has more than 1 author
        if len(authors) > 1:
            dict.update({"Secondary Author": authors[1]})
        print(dict)
        songs.append(dict)
    #print(songs)
    return songs

# Helper Functions
def get_authors(personal, song_id, number_of_authors):
    authors = []
    for x in range(0, number_of_authors):
            authors.append(personal["items"][song_id]["album"]["artists"][x]["name"])
    return authors


def get_number_of_authors(personal: str, limit: int):
    for i in range(0, limit):
        return len(personal["items"][i]["album"]["artists"])


#Building endpoint
def build_endpoint_personal(personal_args) -> str:
    return "https://api.spotify.com/v1/me/top/{}?time_range={}&limit={}&offset={}".format(*personal_args)
