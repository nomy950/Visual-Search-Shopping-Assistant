import base64
import google.generativeai as genai
from PIL import Image
import os

# Replace with your actual API key
GOOGLE_API_KEY = os.getenv("gemini_api")

genai.configure(api_key=GOOGLE_API_KEY)

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def analyze_image(image_path):
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    image = Image.open(image_path)
    
    prompt = """
    Analyze this image and provide a list of keywords or labels that best describe the main objects, 
    colors, and overall theme of the image. Focus on elements that would be relevant for a shopping 
    context. Separate each keyword or short phrase with a comma. Limit your response to 10 keywords 
    or phrases.
    """

    response = model.generate_content(contents=[prompt, image])
    
    # Split the response into a list of labels
    labels = [label.strip() for label in response.text.split(',')]
    
    return labels[:10] 

# Uncomment the following line to test the function independently
# print(analyze_image('path/to/your/image.jpg'))