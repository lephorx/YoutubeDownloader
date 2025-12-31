from pathlib import Path
import yt_dlp

BASE_DIR = Path(__file__).parent
LINKS_FILE = BASE_DIR / "links.txt"
DOWNLOAD_DIR = BASE_DIR / "downloads"

DOWNLOAD_DIR.mkdir(exist_ok=True)

def download_from_file():
    with LINKS_FILE.open("r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    ydl_opts = {
        "outtmpl": str(DOWNLOAD_DIR / "%(title)s.%(ext)s"),
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "quiet": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)

if __name__ == "__main__":
    download_from_file()
