import os
import json
import google.generativeai as genai
from PIL import Image

# getting current working directory
working_directory = os.path.dirname(os.path.abspath(__file__))


config_file_path = f"{working_directory}/config.json"
config_data = json.load(open(config_file_path))


# load api key
GOOGLE_API_KEY = config_data["GOOGLE_API_KEY"]


# configuring google.genai with API Key
genai.configure(api_key=GOOGLE_API_KEY)


'''
Chat
'''

# function to load gemini-pro-model for chatbot
def load_gemini_pro_model():
    gemini_pro_model = genai.GenerativeModel("gemini-pro")
    return gemini_pro_model


'''
Image Captioning
'''

# function for image captioning
def gemini_pro_vision_response(prompt, image):
    gemini_pro_vision_model = genai.GenerativeModel("gemini-pro-vision")
    response = gemini_pro_vision_model.generate_content([prompt, image])
    result = response.text
    return result


'''
Embeddings Text    
'''

# for Embeddings Text
def embedding_model_response(input_text):
    embedding_model = "models/embedding-001"
    embedding = genai.embed_content(model=embedding_model, content=input_text, task_type="retrieval_document")
    embedding_list = embedding["embedding"]
    return embedding_list



# function to get a response from gemini-pro LLM

def gemini_pro_response(user_prompt):
    gemini_pro_model = genai.GenerativeModel("gemini-pro")
    response = gemini_pro_model.generate_content(user_prompt)
    result = response.text
    return result

