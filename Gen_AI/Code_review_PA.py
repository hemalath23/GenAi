import google.generativeai as genai
import streamlit as st

# Setting up the API key
key = "AIzaSyCkHinVvbYz40fG3x0KWx7BW9uqr-uBBBY"  # Replace this with your secure API key
genai.configure(api_key=key)

# Sidebar with instructions
st.sidebar.title("📑 Code Review Instructions")
st.sidebar.subheader("How to Use:")
st.sidebar.write("""
1. **Enter your Python code** into the text area provided.
2. Click on the **'Review'** button to analyze your code.
3. The AI will identify potential errors, suggest improvements, and provide code fixes.
4. If the AI detects non-Python code, it will inform you accordingly.
5. You can enter new code or modify the existing one for further review.
""")
st.sidebar.subheader("Tips for Better Review:")
st.sidebar.write("""
- Make sure to format your code properly (indentation, syntax).
- The more context you provide, the more accurate the review will be.
- For longer code snippets, break them into smaller sections for easier analysis.
""")
st.sidebar.subheader("Contact:")
st.sidebar.write("For any questions or feedback, reach out to our support team.")

# Main page setup
st.title("👨‍💻 Your Code Review !!")
st.subheader("Issues with your Python code? Review your codebase now!")

# Taking user input for the Python code
user_prompt = st.text_area("Enter your Python code...")

# If the button is clicked, generate responses
if st.button("Review"):
    model = genai.GenerativeModel(
        model_name="models/gemini-1.5-pro-latest",
        system_instruction="""
            You are a friendly AI assistant.
            Given a Python code to review, analyze the submitted code and identify bugs, errors, or areas of improvement.
            Provide the fixed code snippets.
            Explain the reasoning behind code corrections or suggestions.
            If the code is not in Python, politely remind the user that you are a Python code review assistant.
        """,
    )

    # If the prompt is provided
    if user_prompt:
        response = model.generate_content(user_prompt)
        
        # Display the AI's response on the main page
        st.write(response.text)
