import requests
from PIL import Image
from io import BytesIO
from config import api_key
from time import time
url="https://api-interface.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
def gen_image():
    while True:
        inp=input("Enter your prompt:")
        header={"Authorization":f"Bearer {api_key}","Accept":"image/png"}
        inpu={"inputs":inp}
        res=requests.post(url,headers=header,json=inpu,timeout=30)
        if 'image' in res.headers.get("Content-Type"):
            img=Image.open(BytesIO(res.content))
            img.save(f"file{time()}",)
        
gen_image()