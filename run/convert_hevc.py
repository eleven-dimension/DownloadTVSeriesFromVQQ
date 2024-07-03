import os
import subprocess

def convert_hevc_to_h264(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(".mp4"):
                input_file = os.path.join(root, file)
                output_file = os.path.join(output_dir, file)

                command = [
                    "ffmpeg",
                    "-i", input_file,
                    "-c:v", "libx264",
                    "-preset", "slow",
                    "-crf", "22",
                    "-c:a", "copy",
                    output_file
                ]

                print(f"Converting {input_file} to {output_file}")
                subprocess.run(command, check=True)

input_directory = "videos"
output_directory = "converted_videos"

convert_hevc_to_h264(input_directory, output_directory)
