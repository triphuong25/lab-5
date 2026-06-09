import urllib.request
import pathlib
import mimetypes
import uuid
path = pathlib.Path(r'e:\phuong\triển khai it và iot\lab5_dockerized_multimodel_aiot_inference_service_v4_code\lab5_dockerized_multimodel_aiot_inference_service_v4\sample_images')
imgs = list(path.glob('*.*'))
print('found', len(imgs))
img = imgs[0]
url = 'http://127.0.0.1:8000/classify-image?top_k=3'
boundary = '----WebKitFormBoundary' + uuid.uuid4().hex
data = bytearray()
with img.open('rb') as f:
    filedata = f.read()
content_type = mimetypes.guess_type(str(img))[0] or 'application/octet-stream'
data.extend(b'--' + boundary.encode() + b'\r\n')
data.extend(b'Content-Disposition: form-data; name="file"; filename="' + img.name.encode() + b'"\r\n')
data.extend(b'Content-Type: ' + content_type.encode() + b'\r\n\r\n')
data.extend(filedata)
data.extend(b'\r\n')
data.extend(b'--' + boundary.encode() + b'--\r\n')
req = urllib.request.Request(url, data=bytes(data), headers={'Content-Type': 'multipart/form-data; boundary=' + boundary})
with urllib.request.urlopen(req) as resp:
    print('status', resp.status)
    print(resp.read(1000).decode(errors='replace'))
