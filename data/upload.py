import os
import requests
from bs4 import BeautifulSoup


def main():
    url = os.getenv("LAUNCHER_URL")
    key = os.getenv("LAUNCHER_KEY")
    version = os.getenv("VERSION")
    
    delete = os.getenv("DELETE")


    if url is None:
        print("url invalid")
        return

    if key is None:
        print("key invalid")
        return


    if delete is None:
        print("key invalid")
        return


    if delete == 'DELETE':
        data = {
            'delete': 'delete'
        }
        requests.post(url, data=data)

    else:
        response = requests.get('https://github.com/kLauncher/kLauncher/releases/tag/' + version)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        node = soup.select_one('.markdown-body')

        version = response.url[response.url.rfind('/')+1:]
        data = {
            'version': version,
            'subject': str(node),
            'key': key,
        }
        requests.post(url, data=data)

if __name__ == '__main__':
    main()

