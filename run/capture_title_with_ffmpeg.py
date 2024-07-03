import os
import subprocess

def capture_images(input_dir, output_dir, timestamp='00:03:20'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".mp4"):
            input_path = os.path.join(input_dir, filename)
            output_filename = os.path.splitext(filename)[0] + '.jpg'
            output_path = os.path.join(output_dir, output_filename)

            timestamp_per_episode = timestamp
            if '14' in filename or '15' in filename:
                timestamp_per_episode = '00:03:21'
            if '17' in filename:
                timestamp_per_episode = '00:03:08'
            command = [
                'ffmpeg',
                '-i', input_path,
                '-ss', timestamp_per_episode,
                '-vframes', '1',
                output_path
            ]

            subprocess.run(command, check=True)

input_directory = './videos'
output_directory = './screenshots'

capture_images(input_directory, output_directory)
