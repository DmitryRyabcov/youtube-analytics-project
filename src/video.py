
import os
from src.channel import YouTube


class Video(YouTube):

    def __init__(self, video_id):
        youtube = self.get_service()
        self.video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                    id=video_id).execute()
        self.video_id = video_id
        self.title = self.video_response['items'][0]['snippet']['title']
        self.url = f'https://youtu.be/{self.video_id}'
        self.view_count = self.video_response['items'][0]['statistics']['viewCount']
        self.like_count = self.video_response['items'][0]['statistics']['likeCount']
        self.comment_count = self.video_response['items'][0]['statistics']['commentCount']


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
