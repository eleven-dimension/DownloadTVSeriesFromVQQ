import os
import subprocess

input_file = 'm3u8/m3u8_urls.txt'
output_dir = './videos'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(input_file, 'r', encoding='utf-8') as file:
    for i, line in enumerate(file, start=1):
        m3u8_url = line.strip()
        
        output_filename = os.path.join(output_dir, f'{i:02d}.mp4')
        
        ffmpeg_command = [
            'ffmpeg',
            '-i', m3u8_url,
            '-c', 'copy',
            output_filename
        ]

        try:
            subprocess.run(ffmpeg_command, check=True)
            print(f"Downloaded: {output_filename}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to download {m3u8_url}: {e}")