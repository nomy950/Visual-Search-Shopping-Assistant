import requests
import json

def test_health_check():
    response = requests.get('http://127.0.0.1:5000/health')
    print("Health Check Response:", response)
    assert response.status_code == 200
    assert response.json()['status'] == 'healthy'

def test_upload_file():
    url = 'http://127.0.0.1:5000/upload'
    
    # Replace 'path/to/test/image.jpg' with the path to an actual test image on your system
    files = {'file': open('uploads/jar.png', 'rb')}
    
    response = requests.post(url, files=files)
    print(response.json())
    print("Upload Response:", json.dumps(response.json(), indent=2))
    assert response.status_code == 200
    assert 'labels' in response.json()
    assert 'similar_items' in response.json()

if __name__ == '__main__':
    print("Testing Health Check...")
    test_health_check()
    print("\nTesting File Upload...")
    test_upload_file()
    print("\nAll tests completed successfully!")