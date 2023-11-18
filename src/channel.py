
class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str, channel):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.id = channel_id
        self.info = channel.info
        self.title = self.info['items'][0]['snippet']['title']
        self.description = self.info['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/' + self.info['items'][0]['snippet']['customUrl']
        self.subscriberCount = int(self.info['items'][0]['statistics']['subscriberCount'])
        self.videoCount = int(self.info['items'][0]['statistics']['videoCount'])
        self.viewCount = int(self.info['items'][0]['statistic']['viewCount'])

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        return self.info
