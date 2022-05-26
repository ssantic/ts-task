import requests
from requests.structures import CaseInsensitiveDict

url = "http://3.71.186.106/download_file?file_name=sample_new.txt"

headers = CaseInsensitiveDict()
headers["accept"] = "application/json"
resp = requests.get(url, headers=headers)

if resp.status_code == 200:
    open('sample_new.txt', 'wb').write(resp.content)
    print("File sample_new.txt downloaded successfully")


