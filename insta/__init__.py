import pandas as pd
import os
from datetime import datetime
from instagrapi import Client




SESSION_ID = os.getenv('INSTA_SESSION_ID')
cl = Client()
cl.login_by_sessionid(SESSION_ID)


def download_media(username: str, qtdmedia: int, output: str = None) -> dict:
    # TYPE CHECK
    if not isinstance(username, str):
        raise TypeError(f"`username` Expected str; got {type(username).__name__}")
    if not isinstance(qtdmedia, int):
        raise TypeError(f"`qtdmedia` Expected int; got {type(qtdmedia).__name__}")
    if not isinstance(output, (str | None)):
        raise TypeError(f"`output` Expected str or None; got {type(output).__name__}")

    if (isinstance(output, str)) and (not os.path.isdir(output)):
        os.mkdir(output)
    

    user_id = cl.user_id_from_username(username)
    medias = cl.user_medias(user_id, qtdmedia)
    data = []

    # Para posterior análise manual
    additional_data = {
        'people': None,
        'bg_simple': None,
        'bg_image': None,
        'title': None,
        'text': None,
        'extra': None
    }

    
    for m in medias:
        media_dict = m.dict()

        # SET Video to true
        is_video = 1

        # Photo
        if m.media_type == 1:
            is_video = 0

        # Album
        elif m.media_type == 8:
            i = 0
            for path in cl.album_download(m.pk, folder=output):
                # Media específica do album
                album_media = media_dict['resources'][i]

                # Photo
                if album_media['media_type'] == 1:
                    is_video = 0
                
                data.append({
                    'pk': album_media['pk'],
                    'id': media_dict['id'],
                    'user': media_dict['user']['username'],
                    'like_count': media_dict['like_count'],
                    'comment_count': media_dict['comment_count'],
                    'taken_at': media_dict['taken_at'],
                    'caption_text': media_dict['caption_text'],
                    'file_path': os.path.basename(path),
                    'video': is_video,
                    # **additional_data
                })
                i += 1
            continue

        if is_video:
            path = cl.video_download(m.pk, folder=output)
        else:
            path = cl.photo_download(m.pk, folder=output)
            
        print(f"http://instagram.com/p/{m.code}/", os.path.basename(path))

        data.append({
            'pk': media_dict['pk'],
            'id': media_dict['id'],
            'user': media_dict['user']['username'],
            'like_count': media_dict['like_count'],
            'comment_count': media_dict['comment_count'],
            'taken_at': media_dict['taken_at'],
            'caption_text': media_dict['caption_text'],
            'file_path': os.path.basename(path),
            'video': is_video,
            # **additional_data
        })
    return data

def getinfo_media(username: str, qtdmedia: int) -> dict:
    # TYPE CHECK
    if not isinstance(username, str):
        raise TypeError(f"`username` Expected str; got {type(username).__name__}")
    if not isinstance(qtdmedia, int):
        raise TypeError(f"`qtdmedia` Expected int; got {type(qtdmedia).__name__}")

    

    user_id = cl.user_id_from_username(username)
    medias = cl.user_medias(user_id, qtdmedia)
    data = []

    
    for m in medias:
        media_dict = m.dict()

        # SET Video to true
        is_video = 1

        # Photo
        if m.media_type == 1:
            is_video = 0

        # Album
        elif m.media_type == 8:
            for i in range(len(media_dict['resources'])):
                # Media específica do album
                album_media = media_dict['resources'][i]

                # Photo
                if album_media['media_type'] == 1:
                    is_video = 0
                
                data.append({
                    'pk': album_media['pk'],
                    'id': media_dict['id'],
                    'user': media_dict['user']['username'],
                    'like_count': media_dict['like_count'],
                    'comment_count': media_dict['comment_count'],
                    'taken_at': media_dict['taken_at'],
                    'caption_text': media_dict['caption_text'],
                    'video': is_video,
                })
            continue
            

        data.append({
                'pk': media_dict['pk'],
                'id': media_dict['id'],
                'user': media_dict['user']['username'],
                'like_count': media_dict['like_count'],
                'comment_count': media_dict['comment_count'],
                'taken_at': media_dict['taken_at'],
                'caption_text': media_dict['caption_text'],
                'video': is_video,
        })
    return data

def data_to_csv(data: dict) -> None:
    df = pd.DataFrame(data)

    # current date and time
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")

    
    csv_filename = f"insta_{timestamp}.csv"
    df.to_csv(csv_filename, index=False)

    print(f"CSV file '{csv_filename}' has been created.")
