# Step 1: Setup GROQ API Key
import os
from dotenv import load_dotenv

load_dotenv()
# GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

# Step 2: Convert image to required format
import base64    #converts bits into strings 

# image_path="acne.jpg"


def encode_image(image_path):
    image_file=open(image_path,"rb") #read in binary format
    return base64.b64encode(image_file.read()).decode('utf-8')#encoding in base64 and then decoding it in utf-8 format
# Step 3: Setup Multifmodal LLM
from groq import Groq

# query="Is there something wrong with my face?"
# model="meta-llama/llama-4-scout-17b-16e-instruct"
def analyze_image_with_query(query,model,encoded_image):
    client=Groq(api_key=os.getenv("GROQ_API_KEY"))


    #Format in which Groq understands the data
    messages=[
        {
            "role":"user",
            "content": [
                {
                    "type": "text",
                    "text": query
                },
                {
                    "type":"image_url",
                    "image_url":{
                    "url":f"data:image/jpeg;base64,{encoded_image}",
                    },
                },

            ],
        }
    ]

    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )
    return chat_completion.choices[0].message.content