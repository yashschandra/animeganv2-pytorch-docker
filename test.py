from PIL import Image
from io import BytesIO
import requests
import base64
import sys

lambda_url = 'http://localhost:9000/2015-03-31/functions/function/invocations'
server_url = 'http://localhost:9000'
input_path = 'input.png'
output_path = 'output.jpeg'

if __name__ == '__main__':
    test_type = sys.argv[1]
    if test_type == 'lambda':
        url = lambda_url
    elif test_type == 'server':
        url = server_url
    else:
        print('invalid argument')
        exit
    input = Image.open(input_path)
    buffered = BytesIO()
    input.save(buffered, "PNG")
    input_data = base64.b64encode(buffered.getvalue())
    res = requests.post(url, json = {'input': input_data, 'pretrained': 'face_paint_512_v2'})
    output = Image.open(BytesIO(base64.b64decode(res.json()['output']))).convert("RGB")
    output.save(output_path, "JPEG")