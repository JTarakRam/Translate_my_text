# Build your Translator with LLMs.

This is a simple web application that translates text between different languages using the OpenAI API and Streamlit.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.7+
- `streamlit` package (`pip install streamlit`)
- `openai` package (`pip install openai`)

## Getting Started

1. Clone the repository: 'git clone https://github.com/your-username/language-translation-app.git'

2. Navigate to the project directory: `cd Translate`

3. Install the required dependencies: `pip install -r requirements.txt`

4. Set up your OpenAI API key:

- Create a file named `secret_key.py` in the project directory.
- Inside `secret_key.py`, define the `openapi_key` variable with your OpenAI API key.

## Setup API Key

openapi_key = `your_openai_api_key`

Run the application: `streamlit run app.py`

Open your web browser and access the application at http://localhost:8501.

## Test your Translator 

Enter the text you want to translate in the provided text area.

- Select the source language from the dropdown menu.
- Select the target language from the dropdown menu.
- Click the **Translate** button.
- The translated text will be displayed



Feel free to customize the README file according to your project's specific details and requirements.






