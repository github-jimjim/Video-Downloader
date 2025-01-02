import os
import yt_dlp
import zipfile
import easygui
from concurrent.futures import ThreadPoolExecutor, as_completed


def list_formats(url):
    with yt_dlp.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get('formats', [])
        format_options = [f"{f['format_id']}: {f['format']} - {f.get('height', 'N/A')}p" for f in formats]
        return format_options


def download_video(url, output_dir, quality):
    try:
        print(f"\nDownloading: {url}")
        ydl_opts = {
            'format': quality,
            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
            'concurrent_frag_downloads': 5,
            'threads': 4,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get('title', None)
            uploader = info_dict.get('uploader', None)

            print(f"Title: {title}\nAuthor: {uploader}")
            print("Download completed!")
            return os.path.join(output_dir, f"{title}.{info_dict['ext']}")

    except Exception as e:
        print(f"An error has occurred while downloading {url}: {e}")
        return None


def download(urls, output_dir, quality):
    try:
        os.makedirs(output_dir, exist_ok=True)
        downloaded_files = []

        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = {executor.submit(download_video, url, output_dir, quality): url for url in urls}

            for future in as_completed(futures):
                result = future.result()
                if result:
                    downloaded_files.append(result)

        if len(downloaded_files) > 1:
            zip_file_path = os.path.join(output_dir, 'downloaded_videos.zip')
            with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
                for file in downloaded_files:
                    zip_file.write(file, os.path.basename(file))

            print(f"\nAll videos have been zipped into: {zip_file_path}")
        elif len(downloaded_files) == 1:
            single_video_path = downloaded_files[0]
            print(f"\nSingle video downloaded to: {single_video_path}")
        else:
            print("\nNo videos were downloaded.")

    except Exception as e:
        print(f"An error has occurred: {e}")


def main():
    video_urls_input = easygui.enterbox("Enter the YouTube URLs (space-separated):")
    video_urls = video_urls_input.split()

    output_directory = easygui.diropenbox("Select the output directory:")
    if not output_directory:
        output_directory = os.path.join(os.path.expanduser("~"), "Downloads")

    format_options = list_formats(video_urls[0])
    quality_input = easygui.choicebox("Select the desired quality:", choices=format_options)

    if quality_input:
        selected_quality = quality_input.split(":")[0]
        download(video_urls, output_directory, selected_quality)
    else:
        easygui.msgbox("No quality selected. Exiting.")


if __name__ == "__main__":
    main()
