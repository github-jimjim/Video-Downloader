# Universal Video Downloader and Converter

This program allows you to download videos from various websites, including those with restricted or adult content (porn), convert video formats, and check video quality. It includes multiple converters and supports downloading audio and video in different qualities.

## Features

- **Downloader**:  
  Download videos by providing a URL. You can choose the desired quality and save the file to a specified directory. For YouTube, audio + video combined downloads are limited to 360p.

- **Converters**:  
  Two converters are included to ensure format conversion works even if one fails. Convert downloaded `.webm` files to `.mp4` or other desired formats.

- **Quality Checker**:  
  Analyze the downloaded video's quality to verify its resolution and encoding properties.

- **FFmpeg Support**:  
  While FFmpeg is optional, it is highly recommended for optimal performance and compatibility.

## Requirements

- Python 3.8 or higher
- Internet connection for downloading videos
- Optional: FFmpeg for enhanced functionality

## Installation

1. Clone this repository or download the files.
2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional) Install FFmpeg for better compatibility:
   - [FFmpeg Installation Guide](https://github.com/yt-dlp/yt-dlp#installing-ffmpeg)

## Usage

### 1. Download Videos
1. Run the `downloader.py` script:
   ```bash
   python downloader.py
   ```
2. Enter the video URL when prompted.
3. Choose the desired video quality from the options provided.
4. Specify the directory where the file will be saved.

   **Note:** 
   - For YouTube, combined audio and video downloads are restricted to 360p.
   - The program supports downloading from websites, including restricted or adult content platforms.

### 2. Convert Videos
1. Run either `converter1.py` or `converter2.py`:
   ```bash
   python converter1.py
   ```
   or
   ```bash
   python converter2.py
   ```
2. Specify the `.webm` file to be converted.
3. Choose the output format (e.g., `.mp4`).

### 3. Check Video Quality
1. Run the `check_quality.py` script:
   ```bash
   python check_quality.py
   ```
2. Provide the path to the video file.
3. The script will display the video's resolution, codec, and other quality details.

## Known Limitations

- Combined audio and video downloads are restricted to 360p for YouTube due to platform limitations.
- FFmpeg is not mandatory but provides better handling of video and audio conversions.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer

This program is intended for personal use only. Downloading videos from certain websites may violate their terms of service. Ensure you have permission to download content before using this program.
