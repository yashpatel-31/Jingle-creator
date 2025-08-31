# 🎶 AI Generative Advertisement Jingle Creator  

An end-to-end AI-powered tool that automatically generates **catchy advertisement jingles** from user input. The system creates both **text-based jingles** and a **sung version (audio)** using text-to-speech.  

Built with **Flask backend** and a simple **HTML/CSS frontend**.  

---

## ✨ Features  

### 🎯 Core Functionality  
- **AI Jingle Generation**: Creates short, catchy jingles based on product, audience, and style.  
- **Text-to-Speech**: Converts generated text into audio format.  
- **Audio Playback**: Listen to jingles directly in the browser.  
- **Download Option**: Save generated jingle as `.mp3`.  

### 🖥️ User Interface  
- **Simple Web Form**: Input product name, audience, and style.  
- **Responsive Design**: Works on desktop and mobile.  
- **Audio Player**: Embedded playback for generated jingles.  
- **Error Messages**: Friendly handling for API or TTS errors.  

### 📁 File Support  
- **Audio Format**: MP3 output for generated jingles.  
- **History Option (Optional)**: Store previously generated jingles in a `generated/` folder.  

---

## 🚀 Quick Start  

### Prerequisites  
- Python 3.8 or higher  
- Flask installed (`pip install flask`)  
- TTS library (e.g., gTTS or pyttsx3)  

### Installation  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/jingle-creator.git
   cd jingle-creator
