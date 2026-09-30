# 🚀 AgriVoice Vision - Complete Deployment Guide

This guide provides instructions to deploy AgriVoice Vision with zero errors, persistent live Gemini multimodal vision inference, and network resilience.

---

## 🌟 Method 1: Streamlit Community Cloud (Recommended - Free)

Streamlit Community Cloud is the fastest and easiest way to deploy Streamlit apps for free with automatic SSL/HTTPS.

### Step 1: Create a GitHub Repository
1. Initialize Git and commit your project (already prepared in this workspace):
   ```bash
   git add .
   git commit -m "feat: AgriVoice Vision production release"
   ```
2. Create a new repository on [GitHub](https://github.com/new) (e.g., `agrivoice-vision`).
3. Push your repository:
   ```bash
   git remote add origin https://github.com/<YOUR_USERNAME>/agrivoice-vision.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
2. Click **"New app"**.
3. Select:
   - **Repository:** `<YOUR_USERNAME>/agrivoice-vision`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. Expand **"Advanced settings..."** before deploying:
   - Under **Secrets**, paste:
     ```toml
     GEMINI_API_KEY = "your_actual_gemini_api_key_here"
     ```
5. Click **"Deploy!"**.
6. Streamlit Cloud will automatically install dependencies from `requirements.txt` and launch the application.

---

## 🐳 Method 2: Docker Container Deployment

You can run AgriVoice Vision anywhere Docker is supported (Google Cloud Run, AWS App Runner, Azure Container Apps, DigitalOcean, self-hosted VPS).

### Step 1: Build the Container
```bash
docker build -t agrivoice-vision:latest .
```

### Step 2: Run the Container
```bash
docker run -d \
  --name agrivoice \
  -p 8501:8501 \
  -e GEMINI_API_KEY="your_actual_gemini_api_key" \
  agrivoice-vision:latest
```
Access the application at `http://localhost:8501`.

---

## ☁️ Method 3: Render (Web Service)

1. Connect your GitHub repository to [Render](https://render.com/).
2. Create a **New Web Service**.
3. Settings:
   - **Runtime:** `Python` or `Docker`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
4. Under **Environment Variables**, add:
   - `GEMINI_API_KEY`: `your_actual_gemini_api_key`
5. Click **Deploy Web Service**.

---

## 🤗 Method 4: Hugging Face Spaces

1. Create a new Space on [Hugging Face Spaces](https://huggingface.co/spaces).
2. Choose **Streamlit** SDK.
3. Push the files or connect your GitHub repository.
4. In Space **Settings** -> **Variables and secrets**, add a secret:
   - Name: `GEMINI_API_KEY`
   - Value: `your_actual_gemini_api_key`
5. The Space will build and deploy automatically.

---

## 🔧 Technical Network & Reliability Safeguards Implemented

| Issue | Root Cause | Solution Implemented |
|---|---|---|
| **"Demo Fallback" always triggering** | Deprecated model IDs (`gemini-2.5-flash`, `gemini-1.5-flash`) & quota-exhausted models (`gemini-3.8-flash`) | Implemented intelligent multi-tier model cascade prioritizing ultra-fast high-quota models (`gemini-flash-lite-latest`, `gemini-3.5-flash-lite`, `gemini-3.1-flash-lite`, followed by `gemini-flash-latest` and `gemini-3.8-flash`). |
| **Network Socket Timeouts** | Uncompressed mobile smartphone camera photos (5-15MB) sent over HTTP | Client-side LANCZOS downscaling to max 1024px, preserving diagnostic lesions while reducing payload by 95%. |
| **Connection Drops / Jitter** | Tight 10-second client timeout | Increased timeout to 30 seconds (`http_options={"timeout": 30000}`) with automatic 2-stage retry on 429/503 errors. |
| **Audio (gTTS) Drops** | Single-shot network call to Google TTS | Wrapped with dual-attempt retry and graceful silent fallback. |
| **Cloud Secrets Missing** | Only checking `os.getenv` | Added seamless fallback checking `st.secrets["GEMINI_API_KEY"]` for cloud deployments. |
| **Deployment Missing gTTS** | Missing from `requirements.txt` | Added `gTTS>=2.5.0` to `requirements.txt`. |
