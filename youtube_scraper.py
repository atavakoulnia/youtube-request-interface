from pickle import NONE
import requests
from bs4 import BeautifulSoup
from googleapiclient.discovery import build

API_KEY = 'insert key here'

def youtube(title):

    youtube = build('youtube', 'v3', developerKey=API_KEY)

    request = youtube.search().list(
        part = 'snippet',
        # searches what user inputs and adds the string 'trailer'
        q = title + ' trailer',
        maxResults = 1,
    )
    result = request.execute()

    for video in result['items']:
        video_title = video['snippet']['title']
        video_url = f"https://www.youtube.com/watch?v={video['id']['videoId']}"
        data = {'title': video_title, 'url': video_url}
        return data
