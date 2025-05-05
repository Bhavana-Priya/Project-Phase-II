import google.generativeai as genai

# Configure API Key
genai.configure(api_key="AIzaSyBPhZxnaxC70Mw9K1UwL40CRgpr1hx73xk")  # Replace with your actual key

# Initialize the model globally
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Function to get a Gemini response
def get_gemini_response(user_question):
    try:
        # Start chat with strict instructions
        chat = model.start_chat(
            history=[],
            system_instruction=(
                "You are a Stock Market bot. Always reply with **2-3 short lines**.\n"
                "Do not exceed 150 characters in total. Be **very concise** and to the point.\n"
                "Avoid any extra details or explanations. Stick to the basics."
            )
        )
        # Send message and get response
        response = chat.send_message(user_question)
        return response.text.strip()  # Ensure it's trimmed of any unnecessary whitespace
    except Exception as e:
        print(f"Error: {e}")
        return "Oops! Something went wrong while fetching a response."

