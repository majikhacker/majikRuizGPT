The st.RudeBot is a conversational chatbot powered by OpenAI's API GPT models and the user interface was done with Streamlit. It allows users to engage in natural language conversations by providing prompts and receiving slightly sarcastic yet efficient AI-generated responses. 

 ## Requirements 

    - Python 3.7+		- Streamlit		- OpenAI API Key 

 ## Getting Started 

  1. Install the required Python packages: 

    -  pip install streamlit 

  2. Obtain an OpenAI API Key: 

    - Sign up for an account on the [OpenAI website](https://openai.com/) 

    - Retrieve your API key from your OpenAI account dashboard. 

  3. Clone or download the MajikRuizGPT repository to your local machine. 

  4. Navigate to the directory containing the script. 

  5. Open the script `majikruiz_gpt.py` in a text editor. 

  6. Replace `st.secrets["OPENAI_API_KEY"]` with your actual OpenAI API Key. 

  7. Save the changes to the script. 

  8. Run the script using the following command: 

     -streamlit run majikruiz_gpt.py 

  9. Access the chatbot interface in your web browser. 

 ## Issues with OpenAI Module 

     - The script uses the `openai` module for interacting with the OpenAI API. 

     - Note that there may be issues with module versions and dependencies. 

     - In newer versions of the OpenAI module, the recommended approach is to use `from openai import OpenAI` and then instantiate `OpenAI` as a variable (e.g.,`client`)to avoid importing the entire module. 

     - Depending on your version, model, and dependencies, you may need to adjust the import statements and usage accordingly. 

 
