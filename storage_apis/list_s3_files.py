import requests
from requests.structures import CaseInsensitiveDict

url = "http://3.71.186.106/list_files_s3"

headers = CaseInsensitiveDict()
headers["accept"] = "application/json"


resp = requests.get(url, headers=headers)

print(resp.status_code)
print(resp.json())
