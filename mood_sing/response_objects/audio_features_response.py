class AudioFeaturesResponse:
    def __init__(self, json):
        self.audio_features = [AudioFeatures(track) for track in json['audio_features']]

class AudioFeatures:
    def __init__(self, track):
        self.danceability = track['danceability']
        self.energy = track['energy']
        self.valence = track['valence']