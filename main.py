import streamlit as st
import os
from streamlit_option_menu import option_menu
from gemini_util import (load_gemini_pro_model, gemini_pro_vision_response, embedding_model_response, gemini_pro_response)
from PIL import Image


# getting current working directory
working_directory = os.path.dirname(os.path.abspath(__file__))


# page configurations
st.set_page_config(
    page_title="Gemini AI",
    page_icon="✨",
    layout="centered"
)


with st.sidebar:

    selected = option_menu("Gemini AI",
                           ['Chat',
                            'Image Captioning',
                            'Embed text',
                            'Ask me Anything'],
                            menu_icon='robot', icons=['chat-left', 'image-fill', 'textarea-t', 'patch-question-fill'],
                            default_index=0)


# function to translate role between gemini pro and streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == 'model':
        return "assistant"
    else:
        return user_role


# for Chat
if selected == "Chat":

    model = load_gemini_pro_model()

    # initialize chat sessions in streamlit if not alreday present
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])


    # streamlit page title
        st.title("🤖 Bot")

    # disply the chat history
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    
    # input field for user message
    user_promts = st.chat_input("Ask me anything...")

    if user_promts:
        st.chat_message("user").markdown(user_promts)

        gemini_response = st.session_state.chat_session.send_message(user_promts)


        # display on streamlit webpage
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)



# Image Captioning Page
            
if selected == 'Image Captioning':

    # streamlit page title
    st.title("📷 Snap Narrate")

    upload_image = st.file_uploader("Upload an Image...", type=['jpg, jpeg', 'png'])

    if st.button("Generate Caption"):

        image = Image.open(upload_image)

        col1, col2 = st.columns(2)

        with col1:
            resized_image = image.resize((800, 500))
            st.image(resized_image)

        default_prompt = "write a short caption for this image"

        # getting the response from gemini_pro_response_model
        caption = gemini_pro_vision_response(default_prompt, image)

        with col2:
            st.info(caption)

# text embedding
            
if selected == 'Embed text':

    st.title('🔡 Embed Text')

    # input text
    input_text = st.text_area(label='', placeholder="Enter the text to get embedding")

    if st.button("Get Embedding"):
        response = embedding_model_response(input_text)
        st.markdown(response)



# for Ask me Anything

if selected == "Ask me Anything":
    st.title("Ask me Anything....❓")

    # text box to enter prompt 
    user_promt = st.text_area(label="", placeholder="Ask Gemini-Pro.....")

    if st.button("Get an Answer"):
        response = gemini_pro_response(user_promt)
        st.markdown(response)