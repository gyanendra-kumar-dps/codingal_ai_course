import requests
from PIL import Image
from io import BytesIO
from config import api_key
url="https://api-interface.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
def gen_image(inp):
    header={"Authorization":f"Bearer {api_key}"}
    input={"inputs":inp}
    res=requests.post(url,headers=header,json=input,timeout=30)
    if 'image' in res.headers.get("Content-Type"):
        img=Image.open(BytesIO(res.content))
        return img

while True:
    inputs=input("Enter your prompt:")
    gen_image(inputs)