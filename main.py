from googleapiclient.discovery import build
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_video_views(video_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.videos().list(
        part='statistics',
        id=video_id
    )
    response = request.execute()

    if 'items' in response and len(response['items']) > 0:
        views = response['items'][0]['statistics']['viewCount']
        return views
    else:
        return None

api_key = 'Тут API Ключ из Google'
video_id = 'hTSaweR8qMI'
views = get_video_views(video_id, api_key)

if views:
    print(f'Количество просмотров: {views}')
else:
    print('Не удалось получить данные о видео.')

numviews = str(views)

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name(r'C:\spiritual-verve-463304-k7-5d2a46ddce53.json', scope)

client = gspread.authorize(creds)

spreadsheet = client.open("NewDF")

worksheet = spreadsheet.get_worksheet(0)

worksheet.update(range_name='A1', values=[[numviews]])
