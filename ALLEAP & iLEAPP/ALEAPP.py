import requests
import os
from github import Github
import subprocess
from urllib import request
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

def internet_on():
    try:
        request.urlopen('http://github.com', timeout=1)
        return True
    except request.URLError as err: 
        return False

if internet_on():
    for name in 'src':
        if name == "aleappGUI.exe":
            os.remove(name)

    g = Github(ACCESS_TOKEN)

    session = requests.Session()
    repository = "abrignoni/ALEAPP"
    assets = g.get_repo(repository).get_latest_release().get_assets()

    for asset in assets:
        if asset.name == "aleappGUI.exe":
            url = asset.browser_download_url

    response = session.get(url)

    with open('src\\aleappGUI.exe', 'wb') as f:
        f.write(response.content)

    process = subprocess.Popen([r"src\\aleappGUI.exe"])
    process.wait()

else:
    process = subprocess.Popen([r"src\\aleappGUI.exe"])
    process.wait()