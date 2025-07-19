
# 🎵 YouTube Video & Audio Downloader API

A simple FastAPI-based backend service to download YouTube videos and audio in `.mp4` and `.mp3` formats using `yt-dlp`. Built for speed, efficiency, and portability with Docker support.

[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-enabled-yellow)](https://github.com/yt-dlp/yt-dlp)
[![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker)](https://www.docker.com/)

---

## 🚀 Features

* 🔊 Download **audio** from YouTube in `MP3` format.
* 🎬 Download **video** from YouTube in `MP4` format.
* 📦 Built with FastAPI for blazing-fast performance.
* 🐳 Docker-ready for production deployment.
* 🔐 Proxy support (you can add your own list of proxies).

---

## 📦 Installation

### 🔧 Requirements

* Python 3.8+
* FFmpeg
* `yt-dlp`
* FastAPI + Uvicorn
* Docker (optional but recommended)

### 🧪 Local Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Shabari-K-S/Youtube-Video-and-Audio-Downloader-API.git
   cd Youtube-Video-and-Audio-Downloader-API
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server**:

   ```bash
   uvicorn app.main:app --reload
   ```

4. **Access API** at [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Docker Setup

1. **Build the Docker image**:

   ```bash
   docker build -t yt-downloader-api .
   ```

2. **Run the container**:

   ```bash
   docker run -p 8000:8000 yt-downloader-api
   ```

---

## 🛠️ API Endpoints

### 🔉 `/download-audio/` (POST)

Download audio from a YouTube video.

* **Request Body**:

```json
{
  "video_url": "https://www.youtube.com/watch?v=example"
}
```

* **Response**: Returns an `.mp3` file.

---

### 🎥 `/download-video/` (POST)

Download full video in MP4 format.

* **Request Body**:

```json
{
  "video_url": "https://www.youtube.com/watch?v=example"
}
```

* **Response**: Returns a `.mp4` file.

---

## 🌐 Proxy Configuration

To enable proxy usage, update the `proxies` list in `main.py`:

```python
proxies = [
  "http://your-proxy-1.com",
  "http://your-proxy-2.com"
]
```

If not using proxies, you can leave it empty or disable proxy field in `yt-dlp` options.

---

## 📂 Folder Structure

```
.
├── app/
│   └── main.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 👨‍💻 Author

Made with ❤️ by [Shabari K S](https://github.com/Shabari-K-S)

