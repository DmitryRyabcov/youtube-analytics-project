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

    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__id = channel_id
        channel = self.get_service().channels().list(id=self.__id, part='snippet,statistics').execute()
        self.info = channel
        self.title = self.info['items'][0]['snippet']['title']
        self.description = self.info['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/' + self.info['items'][0]['snippet']['customUrl']
        self.subscriberCount = int(self.info['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(self.info['items'][0]['statistics']['videoCount'])
        self.viewCount = int(self.info['items'][0]['statistics']['viewCount'])

    @property
    def id(self):
        return self.__id

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        return self.info

    def to_json(self, name):
        with open(name, 'w') as file:
            json.dump(self.__dict__, file, indent=4)



