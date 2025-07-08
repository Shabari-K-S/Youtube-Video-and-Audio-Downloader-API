from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import yt_dlp
import os
from fastapi.responses import FileResponse
import tempfile
from starlette.background import BackgroundTask
import random

app = FastAPI()

class DownloadRequest(BaseModel):
    video_url: str

proxies = [
    'http://14.171.47.152:8080',
    'http://34.155.66.102:8080',
    'http://27.79.241.234:16000',
]

@app.post("/download-audio/")
def download_audio_api(request: DownloadRequest):
    temp_dir = tempfile.gettempdir()
    output_path = os.path.join(temp_dir, 'audio.%(ext)s')
    proxy = random.choice(proxies)
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'proxy': proxy,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([request.video_url])
        audio_file = os.path.join(temp_dir, 'audio.mp3')
        if os.path.exists(audio_file):
            def cleanup():
                try:
                    os.remove(audio_file)
                except Exception:
                    pass
            return FileResponse(audio_file, media_type='audio/mpeg', filename='audio.mp3', background=BackgroundTask(cleanup))
        else:
            raise HTTPException(status_code=500, detail="Download failed.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/download-video/")
def download_video_api(request: DownloadRequest):
    temp_dir = tempfile.gettempdir()
    output_path = os.path.join(temp_dir, 'video.%(ext)s')
    proxy = random.choice(proxies)
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        'outtmpl': output_path,
        'merge_output_format': 'mp4',
        'proxy': proxy,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([request.video_url])
        video_file = os.path.join(temp_dir, 'video.mp4')
        if os.path.exists(video_file):
            def cleanup():
                try:
                    os.remove(video_file)
                except Exception:
                    pass
            return FileResponse(video_file, media_type='video/mp4', filename='video.mp4', background=BackgroundTask(cleanup))
        else:
            raise HTTPException(status_code=500, detail="Download failed.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
