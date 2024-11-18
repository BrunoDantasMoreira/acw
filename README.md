# Automatically Change Wallpaper

A simple Python CLI tool for generating wallpapers from video frames and updating your wallpaper with a new frame each time you run it.

![apresentation](https://private-user-images.githubusercontent.com/68398839/385354480-dafc4c99-7ea5-4bf0-bf80-c4b7937959c7.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzE5NTk2ODQsIm5iZiI6MTczMTk1OTM4NCwicGF0aCI6Ii82ODM5ODgzOS8zODUzNTQ0ODAtZGFmYzRjOTktN2VhNS00YmYwLWJmODAtYzRiNzkzNzk1OWM3LmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDExMTglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMTE4VDE5NDk0NFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWYzZGYxMTY3YzVhZWNlZTMyZWQwNTRiYWJlNDUyODdjZjcxMmUyMTc0NTc3ZGE2ZjU5MmM3MTg5MTYzMmE4MzYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0._a3IXJ_OEJNSqIfPCTBExOllfA8mixZ6dk0GUGv0jMs)


## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [Configuration](#configuration)
- [License](#license)

## Features
1. **Video to Screenshots**: Extracts frames from a video and saves them as individual images in a specified folder.
2. **Automatic Wallpaper Update**: Changes your wallpaper to the next frame in the sequence when run with the `next` argument.

## Usage
To start using the tool, you can either:
- Extract frames from a video.
- Set the wallpaper to the next saved frame.

### CLI Options
Run the program using the command line:
```bash
python main.py [option]
```
### Example Usage

  Extracting Frames from Video:
```bash

python main.py screenshots /path/to/video/file
```

Changing Wallpaper:
```bash

python main.py next
```

## Installation

Clone this repository:
```bash

git clone https://github.com/BrunoDantasMoreira/automatically-change-wallpaper.git
```

Install dependencies:
```bash

pip install -r requirements.txt
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE.md) for details.
