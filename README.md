## Installation

First install the yt-dlp package with:

```bash
pip install yt-dlp
```

Create a `downloads` folder (or the script will create it automatically).

## Usage

The script supports three usage modes:

### 1. Default mode (using links.txt)
Create a `links.txt` file and insert your desired YouTube video URLs (one per line), then run:

```bash
python main.py
```

### 2. Download from a custom file
Use a custom file instead of `links.txt`:

```bash
python main.py mylinks234.txt
```

### 3. Download a single video directly
Pass a YouTube URL directly:

```bash
python main.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

All downloaded videos will be saved to the `downloads` folder in MP4 format.