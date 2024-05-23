import streamlit as st
import pandas as pd
import os
import google.generativeai as genai

# Set up the Streamlit app title
st.title("Gemini Bot with Dataset")

# Configure the Google API key
os.environ['GOOGLE_API_KEY'] = "AIzaSyBzzjX6c1-BkLYppkDNjjQk2-DtGoIG1mo"  # Replace with your actual API key
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Select the model
model = genai.GenerativeModel('gemini-pro')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me anything!"}
    ]

# File uploader for the dataset
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# Load and display the dataset if uploaded
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Dataset:")
    st.write(data)
else:
    data = None

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to process and store query and response
def llm_function(query):
    response_content = ""

    if data is not None:
        # Provide context about the dataset
        dataset_context = data.to_string(index=False)
        full_context_query = f"Given the following dataset:\n\n{dataset_context}\n\nAnswer the following query: {query}"

        # Use the LLM to interpret the user's query within the dataset context
        response = model.generate_content(full_context_query)
        response_content = response.text

    if response_content == "":
        response_content = "I couldn't find anything relevant in the dataset. Let me generate an answer."

    # Displaying the Assistant Message
    with st.chat_message("assistant"):
        st.markdown(response_content)

    # Storing the User Message
    st.session_state.messages.append({"role": "user", "content": query})
    # Storing the Assistant Message
    st.session_state.messages.append({"role": "assistant", "content": response_content})

# Accept user input
query = st.chat_input("What's up?")

# Call the function when input is provided
if query:
    # Displaying the User Message
    with st.chat_message("user"):
        st.markdown(query)

    llm_function(query)
