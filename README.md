# 🌾 AgriVoice Vision - Kisan AI Diagnostic System

**SIH Problem Statement SIH26131**: Early detection and multimodal management of crop diseases and pest infestations.

AgriVoice Vision is an AI-powered agricultural diagnosis and surveillance platform designed for Indian smallholder farmers and Krishi Vigyan Kendra (KVK) extension officers.

---

## 🚀 Key Features

1. **Multimodal Visual Crop Pathology**:
   - Live AI analysis powered by Google's latest multimodal models (`gemini-flash-lite-latest`, `gemini-3.5-flash-lite`, `gemini-3.1-flash-lite`).
   - Automatic client-side image optimization (downscaled to 1024px) for low-bandwidth cellular environments.
   - Dual-action management protocol: Organic & Eco-friendly biocontrols, targeted chemical remedies with dilution ratios, and preventive agricultural cultural practices.

2. **Vernacular Voice Synthesis (Audio Advisory)**:
   - Real-time regional voice output in **Tamil (தமிழ்)**, **Hindi (हिन्दी)**, **Marathi (मराठी)**, and **English**.
   - Integrated gTTS playback with audio caching and network retry safeguards.

3. **Speech-to-Text Vernacular Symptom Query**:
   - Hands-free voice querying using the browser Web Speech API.
   - One-click simulation chips for field conditions (Paddy blast, Tomato leaf curl, Spinach downy mildew, Sugarcane red rot).

4. **Tamil Nadu District Surveillance Outbreak Radar**:
   - Real-time monitoring telemetry across agricultural districts (Thanjavur, Coimbatore, Madurai, Salem, etc.).
   - Critical quarantine escalation indicators and dedicated KVK extension officer emergency protocols.

---

## 🛠️ Local Quickstart

### Prerequisites
- Python 3.10+
- A Google Gemini API Key ([Get one here](https://aistudio.google.com/))

### 1. Clone & Setup Environment
```bash
git clone <your-repo-url>
cd agrivoice-vision
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure API Key
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 3. Run Application
```bash
streamlit run app.py
```
Or simply double-click `run.bat` on Windows.

---

## 🌐 Cloud Deployment Options

### Option 1: Streamlit Community Cloud (Recommended - Free & 2 Minutes)
1. Push your repository to GitHub.
2. Sign in to [share.streamlit.io](https://share.streamlit.io/).
3. Click **"New app"** and select your repository, branch (`main`/`master`), and main file path (`app.py`).
4. Click **"Advanced settings"** -> **"Secrets"** and enter:
   ```toml
   GEMINI_API_KEY = "your_actual_gemini_api_key"
   ```
5. Click **"Deploy!"** Your app will be live with HTTPS.

### Option 2: Docker / Container Deployment (Render, Cloud Run, Railway, Hugging Face)
This repository includes a production-ready `Dockerfile`:
```bash
# Build Docker image
docker build -t agrivoice-vision .

# Run Docker container
docker run -p 8501:8501 -e GEMINI_API_KEY="your_api_key" agrivoice-vision
```

---

## 🛡️ Zero-Downtime Offline Guard
If internet connectivity is interrupted or API quotas are exhausted, AgriVoice Vision automatically engages its built-in agronomy knowledge base (`sample_data.py`), guaranteeing zero crashes and 100% uptime during field evaluations.
