from googleapiclient.discovery import build
import os
import json
api_key: str = os.getenv('API_KEY')
class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.id = channel_id
        channel = self.get_service().channels().list(id=self.id, part='snippet,statistics').execute()
        self.info = channel
        self.title = self.info['items'][0]['snippet']['title']
        self.description = self.info['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/' + self.info['items'][0]['snippet']['customUrl']
        self.subscriberCount = int(self.info['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(self.info['items'][0]['statistics']['videoCount'])
        self.viewCount = int(self.info['items'][0]['statistics']['viewCount'])

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        return self.info

    @classmethod
    def get_service(cls):
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self, name):
        with open(name, 'w') as file:
            json.dump(self.__dict__, file, indent=4)



