from googleapiclient.discovery import build
import os
import json


class YouTube():
    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube


class Channel(YouTube):
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        channel = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.title = channel["items"][0]["snippet"]["title"]
        self.description = channel["items"][0]["snippet"]["description"]
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.viewCount = channel["items"][0]["statistics"]["viewCount"]
        self.subscriberCount = int(channel["items"][0]["statistics"]["subscriberCount"])
        self.video_count = channel["items"][0]["statistics"]["videoCount"]

    @property
    def channel_id(self):
        return self.__channel_id

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        return self.info

    def to_json(self, name):
        with open(name, 'w') as file:
            json.dump(self.__dict__, file, indent=4)

    def __str__(self) -> str:
        return f'{self.title}{self.url}'

    def __add__(self, other: int):
        return self.subscriberCount + other.subscriberCount

    def __sub__(self, other: int):
        return self.subscriberCount - other.subscriberCount

    def __lt__(self, other: int):
        return self.subscriberCount < other.subscriberCount

    def __gt__(self, other: int):
        return self.subscriberCount > other.subscriberCount

    def __le__(self, other: int):
        return self.subscriberCount <= other.subscriberCount

    def __ge__(self, other: int):
        return self.subscriberCount >= other.subscriberCount

    def __eq__(self, other: int):
        return self.subscriberCount == other.subscriberCount



