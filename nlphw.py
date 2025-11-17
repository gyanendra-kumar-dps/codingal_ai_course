import requests
from config import api_key
API_URL = "https://router.huggingface.co/hf-inference/models/tabularisai/multilingual-sentiment-analysis"
headers = {
    "Authorization": f"Bearer {api_key}",
}
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
while True:
    inp=input('Enter a sentence for analysis:')
    output = query({
        "inputs": f"{inp}",
    })
    for i in output[0]:
        print(f"{i['label']}:- {i['score']*100:.4f}%")
#https://huggingface.co/classla/multilingual-IPTC-news-topic-classifier