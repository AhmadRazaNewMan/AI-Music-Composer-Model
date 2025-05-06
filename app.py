from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return "🎵 AI Music Composer backend is running on Render!"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Flask app is running on port: {port}")

    app.run(host='0.0.0.0', port=port)
