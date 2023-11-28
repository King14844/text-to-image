from flask import Flask, request, send_file
from flask_cors import CORS
import requests
from io import BytesIO

app = Flask(__name__)
CORS(app)

@app.route('/get_image', methods=['POST'])
def get_image():
    try:
        prompt = request.json.get('prompt')
        api_url = "https://api.cloudflare.com/client/v4/accounts/5c1c6af74ad6452839b1694dbda5e0cb/ai/run/@cf/stabilityai/stable-diffusion-xl-base-1.0"
        headers = {
            "Authorization": "Bearer LnmUDKtQLE60q5QUrudE4N1EUe3kNNgdVf2K9K23",
            "Content-Type": "application/json",
        }
        data = {"prompt": prompt}
        response = requests.post(api_url, headers=headers, json=data)
        if response.status_code == 200:
            image_data = response.content
            image_bytesio = BytesIO(image_data)
            return send_file(image_bytesio, mimetype='image/png')
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run()
