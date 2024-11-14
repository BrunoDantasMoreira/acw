# Automatically Change Wallpaper

A simple Python CLI tool for generating wallpapers from video frames and updating your wallpaper with a new frame each time you run it.

![apresentation](https://github.com/user-attachments/assets/12556d65-a598-4bc5-8a28-bd001a098089)


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
