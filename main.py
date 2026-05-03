from pathlib import Path
import sys
import yt_dlp

BASE_DIR = Path(__file__).parent
LINKS_FILE = BASE_DIR / "links.txt"
DOWNLOAD_DIR = BASE_DIR / "downloads"

DOWNLOAD_DIR.mkdir(exist_ok=True)

def download_urls(urls):
    """Download videos from a list of URLs"""
    if not urls:
        print("No URLs to download")
        return
    
    ydl_opts = {
        "outtmpl": str(DOWNLOAD_DIR / "%(title)s.%(ext)s"),
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "quiet": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)

def download_from_file(file_path):
    """Download videos from a file containing URLs"""
    file_path = Path(file_path)
    if not file_path.exists():
        print(f"Error: File '{file_path}' not found")
        return
    
    with file_path.open("r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]
    
    download_urls(urls)

def is_url(text):
    """Check if text is a URL"""
    return text.startswith("http://") or text.startswith("https://")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        
        if is_url(arg):
            print(f"Downloading from URL: {arg}")
            download_urls([arg])
        else:
            print(f"Downloading from file: {arg}")
            download_from_file(arg)
    else:
        print("No argument provided. Using links.txt")
        if LINKS_FILE.exists():
            download_from_file(LINKS_FILE)
        else:
            print(f"Error: {LINKS_FILE} not found")
