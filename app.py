from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

application = Flask(__name__)

@application.route('/')
def home():
    return "🎵 AI Music Composer backend is running on Render!"

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8000))
    application.run(host='0.0.0.0', port=port)
