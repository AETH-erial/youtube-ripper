""" Watch tower for ripping things off of youtube """
from yt_dlp import YoutubeDL
from typing import Union



class Yagura:
    """ Client for interacting with the yt-dlp API """
    def __init__(self, username: str, password: str):
        """ Init for the Yagura class

        :type username: str
        :param username: the username to authenticate with
        :type password: str
        :param password: password to the account"""

        self.username = username
        self.password = password
        self.urls = []

    def _add_link(self, link: str) -> None:
        """ add a link to the list of videos to download

        :type link: str
        :param link: the link to add to the queue
        :rtype: None
        :returns: None

        """
        self.urls.append(link)



