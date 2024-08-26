from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import traceback
from werkzeug.utils import secure_filename
from config import Config
from gemini_api import analyze_image
from ebay_api import search_ebay

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            print(f"File saved successfully at {file_path}. Analyzing image...")
            # Analyze the image using Gemini
            try:
                labels = analyze_image(file_path)
                print(f"Image analysis complete. Labels: {labels}")
            except Exception as e:
                print(f"Error during image analysis: {str(e)}")
                print(f"Traceback: {traceback.format_exc()}")
                return jsonify({'error': f"Image analysis failed: {str(e)}"}), 500
            
            # Search for similar products on eBay
            search_query = ' '.join(labels[:3])  # Use top 3 labels for search
            similar_items = search_ebay(search_query)
            
            return jsonify({'message': 'File uploaded and analyzed successfully', 
                            'labels': labels,
                            'similar_items': similar_items,
                            'file_path': file_path}), 200
        return jsonify({'error': 'File type not allowed'}), 400
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print(f"Traceback: {traceback.format_exc()}")
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)