import os
import requests
from bs4 import BeautifulSoup

def main():
    url = os.getenv("LAUNCHER_URL")
    key = os.getenv("LAUNCHER_KEY")
    version = os.getenv("VERSION")
    action = os.getenv("ACTION") # released, edited, deleted


    if url is None:
        print("url invalid")
        return

    if key is None:
        print("key invalid")
        return


    if action is None:
        print("action invalid")
        return

    data = {
        'action': action,
        'version': version,
        'key': key,
    }

    if action != 'deleted':
        response = requests.get('https://github.com/kLauncher/kLauncher/releases/tag/' + version)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        node = soup.select_one('.markdown-body')
        data['subject'] = str(node)

    requests.post(url, data=data)

if __name__ == '__main__':
    main()
