class RecentlyPlayedResponse:
    def __init__(self, json):
        self.tracks = [track['track']['id'] for track in json['items']]