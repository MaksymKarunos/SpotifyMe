import requests
import time
import config
import pandas as pd
from functions import *
def main():
    personal_args = ["tracks","short_term",50,0]
    endpoint_current = "https://api.spotify.com/v1/me/player/currently-playing"
    endpoint_personal = build_endpoint_personal(personal_args)
    current = requests.get(url=endpoint_current, headers=config.headers_current)
    personal = requests.get(url=endpoint_personal, headers=config.headers_personal)

    best_tracks = get_personal_data(personal, personal_args)
    song = get_current_song(current)

    print(song)

if __name__ == "__main__":
    # execute only if run as a script
    main()
