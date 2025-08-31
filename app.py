import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from gtts import gTTS
import requests

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/jingles'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Gemini 2.0 Flash API details
GEMINI_API_KEY = "AIzaSyAiSDog-b-K7iBV7Y5a3ugUpYKZ9Kj-iqo"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=" + GEMINI_API_KEY

def generate_jingle_text(product, audience, style):
    prompt = (
        f"Write a short catchy advertisement jingle for {product}, targeting {audience}, in a {style} tone. "
        "Give two versions: one in English and one in Hinglish (mix of Hindi and English). "
        "Format: \nEnglish: <jingle>\nHinglish: <jingle>"
    )
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    try:
        response = requests.post(GEMINI_API_URL, json=data, headers=headers, timeout=15)
        response.raise_for_status()
        result = response.json()
        # Extract jingle text
        jingle = result['candidates'][0]['content']['parts'][0]['text']
        return jingle
    except Exception as e:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    product = data.get('product', '').strip()
    audience = data.get('audience', '').strip()
    style = data.get('style', '').strip()
    if not product or not audience or not style:
        return jsonify({'error': 'All fields are required.'}), 400
    jingle_text = generate_jingle_text(product, audience, style)
    if not jingle_text:
        return jsonify({'error': 'Failed to generate jingle. Please try again.'}), 500
    # Convert to audio
    try:
        tts = gTTS(jingle_text)
        filename = f"jingle_{product.replace(' ', '_')}_{audience.replace(' ', '_')}_{style.replace(' ', '_')}.mp3"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        tts.save(filepath)
        audio_url = f"/static/jingles/{filename}"
        return jsonify({'jingle': jingle_text, 'audio_url': audio_url, 'download_url': audio_url})
    except Exception as e:
        return jsonify({'error': 'Failed to generate audio.'}), 500

@app.route('/static/jingles/<filename>')
def serve_jingle(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
