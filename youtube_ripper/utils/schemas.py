"""
pydantic schemas
"""
from pydantic import BaseModel  # pylint: disable=no-name-in-module
from typing import List
from youtube_ripper.utils.enums import AudioFormats



class DownloadReq(BaseModel):
    """ Schema for download options passed to the Yagura """
    Url: List[str]
    IsPlaylist: bool


class AudioExtract(DownloadReq):
    """ Schema for a request to extract audio only """
    Format: AudioFormats



class ErrorSchema(BaseModel):  # pylint: disable=too-few-public-methods
    """Schema for simple Errors"""
    detail: str
