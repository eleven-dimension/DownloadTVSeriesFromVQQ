import re
import json
import os

def get_m3u8_url(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        file_content = file.read()

    pattern = r'getinfo_callback_\d+\((\{.*?\})\)'
    match = re.search(pattern, file_content)

    if match:
        json_str = match.group(1)
        try:
            json_obj = json.loads(json_str)
            return json_obj["vl"]["vi"][0]["ul"]["ui"][0]["url"]
        except json.JSONDecodeError as e:
            print("json error:", e)
            return ""
    return ""

if __name__ == "__main__":
    responses_dir = './responses'
    output_file = './m3u8/m3u8_urls.txt'

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    urls = []
    for filename in os.listdir(responses_dir):
        filepath = os.path.join(responses_dir, filename)
        if os.path.isfile(filepath):
            url = get_m3u8_url(filepath)
            if url:
                urls.append(url)

    print(len(urls))
    with open(output_file, 'w') as file:
        for url in urls:
            file.write(url + '\n')