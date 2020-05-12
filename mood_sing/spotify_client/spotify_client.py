import requests, datetime
from urllib.error import HTTPError
from typing import List
from flask import request

import constants
from mood_sing.response_objects import RecentlyPlayedResponse, AudioFeaturesResponse

class SpotifyClient:
    def __init__(self):
        self.api_url = constants.SPOTIFY_API_URL
        self.__set_headers()

    def __set_headers(self):
        try:
            self.headers = {
                'Authorization': request.headers["Authorization"],
                'Content-Type': 'application/json'
            }
        except (KeyError):
            raise Unauthorized("No authentication token provided")

    def __make_get_request(self, endpoint: str, params: str):
        for tries in range(3):
            try:
                response = requests.get(self.api_url + endpoint, headers=self.headers, params=params)
                response.raise_for_status()
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
            except Exception as err:
                print(f'Other error occurred: {err}')
            else:
                print('Success!')
                return response.json()

    def get_recently_played(self):
        endpoint = '/me/player/recently-played'
        params = f'limit=50&after={datetime.date.today() - datetime.timedelta(1)}'
        
        return RecentlyPlayedResponse(self.__make_get_request(endpoint, params))

    def get_audio_features(self, tracks: List[str]):
        endpoint = '/audio-features'
        params = 'ids=' + ','.join(tracks)

        return AudioFeaturesResponse(self.__make_get_request(endpoint, params))
