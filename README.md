# Visual Search Shopping Assistant

## Description
The Visual Search Shopping Assistant is an innovative web application that combines computer vision and e-commerce API integration to provide a unique shopping experience. Users can upload images of products they're interested in, and the application will analyze the image, identify key features, and search for similar products available for purchase.

## Features
- Image upload and analysis using Google's Gemini AI
- Product search integration with eBay API
- Flask-based RESTful API backend
- React Native frontend for mobile compatibility

## Technologies Used
- Backend: Python, Flask
- Frontend: React Native
- AI/ML: Google Gemini AI
- E-commerce Integration: eBay API

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.7+
- Node.js and npm
- Google Cloud account with Gemini API access
- eBay Developer account

## Installation

### Backend Setup
1. Clone the repository:
   ```
   git clone https://github.com/your-username/visual-search-shopping-assistant.git
   cd visual-search-shopping-assistant
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   - Create a `.env` file in the project root
   - Add your Google API key and eBay API credentials:
     ```
     GOOGLE_API_KEY=your_google_api_key
     EBAY_APP_ID=your_ebay_app_id
     ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install the required npm packages:
   ```
   npm install
   ```

## Usage

### Running the Backend
1. From the project root, activate the virtual environment if not already active.
2. Start the Flask server:
   ```
   python app.py
   ```
   The server will start running on `http://localhost:5000`.

### Running the Frontend
1. In a new terminal, navigate to the frontend directory.
2. Start the React Native development server:
   ```
   npx react-native start
   ```
3. In another terminal, run the app on an emulator or device:
   ```
   npx react-native run-android  # For Android
   # or
   npx react-native run-ios      # For iOS
   ```

## API Endpoints

- `GET /health`: Health check endpoint
- `POST /upload`: Upload and analyze an image, returns labels and similar products

## Contributing
Contributions to the Visual Search Shopping Assistant are welcome. Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
Your Name - noumannsyed@gmail.com

Project Link: [https://github.com/nomy950/visual-search-shopping-assistant](https://github.com/nomy950/visual-search-shopping-assistant)

## Acknowledgements
- [Google Gemini AI](https://cloud.google.com/vertex-ai/docs/generative-ai/start/quickstarts/api-quickstart)
- [eBay Developers Program](https://developer.ebay.com/)
- [Flask](https://flask.palletsprojects.com/)
- [React Native](https://reactnative.dev/)
