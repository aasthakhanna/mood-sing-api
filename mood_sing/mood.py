from spotify_client import SpotifyClient
from response_objects import AudioFeatures

def get_mood(spotify_client: SpotifyClient):
    tracks = spotify_client.get_recently_played().tracks
    audio_features = spotify_client.get_audio_features(tracks).audio_features
        
    return calculate_mood(audio_features)

def calculate_mood(audio_features: AudioFeatures):
    length = len(audio_features)
    total_valence = sum(audio.valence for audio in audio_features) / length
    total_danceability = sum(audio.danceability for audio in audio_features) / length
    total_energy = sum(audio.energy for audio in audio_features) / length

    # TODO: make this logic more nuanced
    # red makes the mood happier
    # green makes the mood happier combined with red
    # blue makes the mood sadder
    red = int((total_danceability + total_energy) / 2 * 255)
    green = int(total_valence * 255)
    blue = int((1 - ((total_danceability + total_energy + total_valence) / 3)) * 255)
    
    return rgb_to_hex(red, green, blue)

def rgb_to_hex(red: int, green: int, blue: int):
    return '#{:02x}{:02x}{:02x}'.format(red, green, blue)

