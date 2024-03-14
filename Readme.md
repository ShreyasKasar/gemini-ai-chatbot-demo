# Gemini AI

Gemini AI is a Streamlit web application that integrates with Google's Generative AI models for various tasks such as chat, image captioning, text embedding, and asking questions.

## Features

- **Chat**: Engage in conversation with Gemini AI using natural language prompts.
- **Image Captioning**: Upload an image and generate a descriptive caption for it.
- **Embed Text**: Get embeddings for input text using pre-trained models.
- **Ask me Anything**: Ask Gemini AI any question and receive a response.

## Getting Started

1. Clone this repository:

    ```bash
    git clone https://github.com/ShreyasKasar/gemini-ai-chatbot-demo.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up Google API Key:
   
   - Obtain a Google API Key from the Google Cloud Console.
   - Create a `config.json` file in the project directory with the following structure:

    ```json
    {
        "GOOGLE_API_KEY": "your-api-key"
    }
    ```

4. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

5. Interact with Gemini AI through the web interface.




