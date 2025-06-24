import google.generativeai as genai
from PIL import Image
import os
from dotenv import load_dotenv # Import load_dotenv

# Load environment variables from .env file
load_dotenv() 

# Get API key from environment variable
API_KEY = os.getenv("GOOGLE_API_KEY") 

IMAGE_PATH = "img2.png" 

# Configure the API client
genai.configure(api_key=API_KEY)

def extract_transactions_from_image(image_path: str):
    """
    Extracts transaction data from a bank statement image using Google Gemini Pro Vision.
    Args:
        image_path (str): The path to the image file.

    Returns:
        str: A Markdown table of the extracted transactions, or an error message.
    """
    try:
        # Load the image
        img = Image.open(image_path)

        model = genai.GenerativeModel('gemini-2.5-flash') 

        prompt_parts = [
            "You are an expert at extracting financial transaction data from bank statements.",
            "Analyze the provided image of a bank statement.",
            "Extract all individual transactions into a Markdown table.",
            "The table should have the following columns: 'Date', 'Description', 'Amount', 'Balance'.",
            "For the 'Amount' column:",
            "- Date format should be : YYYY-MM-DD"
            "- If the transaction is a withdrawal or a debit, precede the amount with a minus sign (e.g., -200.00).",
            "- If the transaction is a deposit or a credit, provide the amount as a positive number (e.g., 694.81).",
            "- The 'Previous balance' entry does not have an 'Amount', so leave that cell empty.",
            "Ensure the table is correctly formatted Markdown.",
            "Here is the image:",
            img 
        ]

        print("Sending request to Google AI Studio...")
        response = model.generate_content(prompt_parts)
        print("Response received.")

        return response.text

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # The API_KEY check now verifies if it was loaded from the environment
    if API_KEY is None: # Check if API_KEY is None, which means it wasn't found in .env
        print("ERROR: API key not found. Please ensure 'GOOGLE_API_KEY' is set in your .env file.")
    elif not os.path.exists(IMAGE_PATH):
        print(f"ERROR: Image not found at '{IMAGE_PATH}'. Please ensure the image is in the correct directory.")
    else:
        extracted_data = extract_transactions_from_image(IMAGE_PATH)

        print("\n--- Extracted Transactions ---")
        print(extracted_data)
        print("\n------------------------------")
