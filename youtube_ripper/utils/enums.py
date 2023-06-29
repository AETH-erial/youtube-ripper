""" Generic Enums for validation etc """
from enum import Enum



class AudioFormats(Enum):
    """ Enum for picking an audio format """
    MP3 = 'mp3'
    FLAC = 'flac'
    WAV = 'wav'