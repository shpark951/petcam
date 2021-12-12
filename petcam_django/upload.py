import requests as req
import os
url= 'http://192.168.0.10:8000/api/snapshot/'
file_name = 'background.jpg'
file_path = os.path.join('', file_name)

data = {
    'username': 'park',
    'size': os.path.getsize(file_name),
    'filename': file_name,
    'content_type': 'image/jpg'
}
res = req.post(url, data=data, files={'image_file': open(file_path, 'br')})
if res.status_code == 200:
    print(res.json())
else:
    print(res.text)