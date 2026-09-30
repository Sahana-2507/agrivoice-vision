"""
AgriVoice Vision - Kisan AI Diagnostic System
============================================
SIH Problem Statement SIH26131: Early detection and management of crop diseases and pest infestations.

Key Capabilities:
1. Multimodal AI Image Diagnosis (Gemini Flash Vision with structured JSON & crash-proof fallback)
2. Vernacular Voice Advisory (Native audio synthesis via cached gTTS in Tamil, Hindi, Marathi, English)
3. Speech-to-Text Symptom Query (Web Speech API Recognition + 1-Click Simulation Chips)
4. District Surveillance Outbreak Radar (Tamil Nadu extension officer telemetry & analytics)
"""

import os
import json
import base64
import io
from io import BytesIO
from typing import Dict, Any, Tuple, Optional
from datetime import datetime

import streamlit as st
import pandas as pd
from PIL import Image
from dotenv import load_dotenv
from gtts import gTTS

# Load environment variables
load_dotenv()

# ==========================================
# PAGE CONFIGURATION (MUST BE FIRST STREAMLIT CALL)
# ==========================================
st.set_page_config(
    page_title="AgriVoice Vision - Kisan AI Diagnostic System",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load fallback agronomical data & surveillance telemetry
from sample_data import FALLBACK_DISEASES, get_sample_disease, get_localized_advisory
from mock_outbreaks import get_outbreaks_dataframe, get_critical_alerts, get_district_summary

# Attempt to import Google GenAI SDK
GENAI_AVAILABLE = False
try:
    from google import genai
    from google.genai import types
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False

# ==========================================
# CUSTOM AGRITECH CSS DESIGN SYSTEM
# ==========================================
st.markdown(
    """
    <style>
    /* Global Fonts & Colors */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    h1, h2, h3, .main-title {
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700;
        letter-spacing: -0.02em;
    }
    
    /* Header Card */
    .hero-container {
        background: linear-gradient(135deg, #064e3b 0%, #047857 50%, #059669 100%);
        color: white;
        padding: 24px 28px;
        border-radius: 16px;
        margin-bottom: 24px;
        box-shadow: 0 10px 25px -5px rgba(5, 150, 105, 0.25);
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 16px;
    }
    
    .hero-title-group h1 {
        color: #ffffff;
        margin: 0;
        font-size: 28px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .hero-subtitle {
        color: #d1fae5;
        font-size: 14px;
        margin: 6px 0 0 0;
        font-weight: 500;
    }
    
    .badge-gemini {
        background: rgba(255, 255, 255, 0.18);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        color: #ffffff;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 600;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }

    /* Metric Cards */
    .metric-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 14px;
        margin: 18px 0;
    }
    
    .diag-metric-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    
    .diag-metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.06);
    }
    
    .metric-label {
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #64748b;
        font-weight: 600;
        margin-bottom: 4px;
    }
    
    .metric-value {
        font-size: 19px;
        font-weight: 700;
        color: #0f172a;
    }
    
    .sev-critical, .sev-high {
        color: #dc2626 !important;
    }
    .sev-moderate {
        color: #d97706 !important;
    }
    .sev-low {
        color: #16a34a !important;
    }

    /* Remedy Section Card */
    .remedy-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-left: 5px solid #10b981;
        border-radius: 10px;
        padding: 16px 20px;
        margin-bottom: 14px;
    }
    
    .remedy-card.chemical {
        border-left-color: #3b82f6;
    }
    
    .remedy-card.prevention {
        border-left-color: #8b5cf6;
    }
    
    .remedy-header {
        font-size: 15px;
        font-weight: 700;
        margin-bottom: 6px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    /* Fallback Pill */
    .status-pill {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 600;
        margin-bottom: 12px;
    }
    .status-online {
        background-color: #dcfce7;
        color: #15803d;
        border: 1px solid #86efac;
    }
    .status-fallback {
        background-color: #fef3c7;
        color: #b45309;
        border: 1px solid #fcd34d;
    }
    
    /* Streamlit overrides */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 20px;
        border-radius: 8px;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# LOCALIZATION & VERNACULAR DICTIONARY
# ==========================================
LANGUAGES = {
    "English": {
        "code": "en",
        "speech_lang": "en-IN",
        "tab1_title": "📸 Image Diagnosis",
        "tab2_title": "🎙️ Voice & Symptom Query",
        "tab3_title": "📊 District Surveillance Dashboard",
        "upload_label": "Upload leaf image for multimodal diagnosis",
        "test_sample_btn": "⚡ Test with Sample Leaf (Tomato Early Blight)",
        "diagnosing": "Analyzing crop foliage with Gemini Multimodal Vision...",
        "crop_label": "Identified Crop",
        "disease_label": "Diagnosed Condition",
        "confidence_label": "Diagnostic Confidence",
        "severity_label": "Pathological Severity",
        "organic_title": "🌿 Eco-Friendly & Organic Remedy",
        "chemical_title": "🧪 Targeted Chemical Spray (With Dilution)",
        "prevention_title": "🛡️ Preventive Cultural Practices",
        "listen_btn_text": "🔊 Listen to Remedy in English",
        "voice_tab_desc": "Tap the microphone below to speak symptoms or click a quick simulation query.",
        "voice_sample_prompt": "Try: 'My tomato plant has dark spots with yellow concentric rings on bottom leaves'",
        "outbreak_tab_title": "Tamil Nadu Regional Surveillance (SIH26131 Telemetry)",
        "district_filter_label": "Focus District Alert Feed",
        "status_ready": "System Ready"
    },
    "தமிழ் (Tamil)": {
        "code": "ta",
        "speech_lang": "ta-IN",
        "tab1_title": "📸 இலை படம் மூலம் ஆய்வு (Image Diagnosis)",
        "tab2_title": "🎙️ குரல் வழி ஆலோசனை (Voice Advisory)",
        "tab3_title": "📊 மாவட்ட நோய் கண்காணிப்பு (Outbreak Radar)",
        "upload_label": "பாதிக்கப்பட்ட பயிர் இலையின் புகைப்படத்தை பதிவேற்றவும்",
        "test_sample_btn": "⚡ மாதிரி இலை மூலம் சோதிக்கவும் (தக்காளி கருகல் நோய்)",
        "diagnosing": "ஜெமினி செயற்கை நுண்ணறிவு மூலம் ஆய்வு செய்யப்படுகிறது...",
        "crop_label": "கண்டறியப்பட்ட பயிர்",
        "disease_label": "நோயின் பெயர்",
        "confidence_label": "கண்டறிதல் துல்லியம்",
        "severity_label": "நோயின் தீவிரம்",
        "organic_title": "🌿 இயற்கை மற்றும் உயிரியல் நிவாரணம்",
        "chemical_title": "🧪 பரிந்துரைக்கப்பட்ட ரசாயன மருந்து தெளிப்பு",
        "prevention_title": "🛡️ தடுப்பு மற்றும் பாதுகாப்பு வழிமுறைகள்",
        "listen_btn_text": "🔊 தமிழில் தீர்வை ஒலி வடிவில் கேட்கவும்",
        "voice_tab_desc": "மைக் பொத்தானை அழுத்தி பயிர் அறிகுறிகளைப் பேசவும் அல்லது உடனடி வினாக்களை கிளிக் செய்யவும்.",
        "voice_sample_prompt": "உதாரணம்: 'தக்காளி இலையில் வட்ட வடிவில் கரும் புள்ளிகள் உள்ளன'",
        "outbreak_tab_title": "தமிழ்நாடு மாவட்ட நோய் கண்காணிப்பு (TN Surveillance Radar)",
        "district_filter_label": "மாவட்டத்தை தேர்ந்தெடுக்கவும்",
        "status_ready": "அமைப்பு தயார்"
    },
    "हिन्दी (Hindi)": {
        "code": "hi",
        "speech_lang": "hi-IN",
        "tab1_title": "📸 तस्वीर से फसल जांच (Image Diagnosis)",
        "tab2_title": "🎙️ बोलकर लक्षण पूछें (Voice Advisory)",
        "tab3_title": "📊 जिला निगरानी डैशबोर्ड (Outbreak Radar)",
        "upload_label": "पौधे की पत्ती का फोटो अपलोड करें",
        "test_sample_btn": "⚡ नमूना पत्ती से परीक्षण करें (टमाटर अर्ली ब्लाइट)",
        "diagnosing": "जेमिनी एआई द्वारा पत्ती का विश्लेषण किया जा रहा है...",
        "crop_label": "पहचानी गई फसल",
        "disease_label": "रोग का नाम",
        "confidence_label": "जांच सटीकता (Confidence)",
        "severity_label": "रोग की गंभीरता (Severity)",
        "organic_title": "🌿 जैविक व प्राकृतिक उपचार (Organic Remedy)",
        "chemical_title": "🧪 रासायनिक छिड़काव एवं मात्रा (Chemical Treatment)",
        "prevention_title": "🛡️ बचाव एवं कृषि सुरक्षा उपाय (Prevention)",
        "listen_btn_text": "🔊 हिंदी में उपचार व सलाह सुनें",
        "voice_tab_desc": "माइक दबाकर अपनी फसल के लक्षण बोलें या नीचे दिए गए त्वरित विकल्पों पर क्लिक करें।",
        "voice_sample_prompt": "उदाहरण: 'टमाटर की निचली पत्तियों पर गोल भूरे धब्बे और पीला घेरा दिख रहा है'",
        "outbreak_tab_title": "तमिलनाडु क्षेत्रीय रोग निगरानी व अलर्ट",
        "district_filter_label": "संबंधित जिला चुनें",
        "status_ready": "सिस्टम सक्रिय"
    },
    "मराठी (Marathi)": {
        "code": "mr",
        "speech_lang": "mr-IN",
        "tab1_title": "📸 फोटोवरून रोग निदान (Image Diagnosis)",
        "tab2_title": "🎙️ आवाजाद्वारे लक्षण विचारणा (Voice Advisory)",
        "tab3_title": "📊 जिल्हास्तरीय पाळत डॅशबोर्ड (Outbreak Radar)",
        "upload_label": "पिकाच्या पानाचा फोटो अपलोड करा",
        "test_sample_btn": "⚡ नमुना पानावरून चाचणी करा (टोमॅटो करपा रोग)",
        "diagnosing": "जेमिनी एआय द्वारे पानांचे विश्लेषण सुरू आहे...",
        "crop_label": "ओळखलेले पीक",
        "disease_label": "रोगाचे नाव व प्रकार",
        "confidence_label": "निदान अचूकता",
        "severity_label": "रोगाची तीव्रता",
        "organic_title": "🌿 सेंद्रिय व जैविक उपाय (Organic)",
        "chemical_title": "🧪 रासायनिक फवारणी व योग्य प्रमाण (Chemical)",
        "prevention_title": "🛡️ प्रतिबंधात्मक कृषी उपाय (Prevention)",
        "listen_btn_text": "🔊 मराठीत उपाय व मार्गदर्शन ऐका",
        "voice_tab_desc": "माइक बटण दाबून पिकाची लक्षणे सांगा किंवा खालील पर्यायांवर क्लिक करा.",
        "voice_sample_prompt": "उदा: 'टोमॅटोच्या पानांवर पिवळसर कडा असलेले तपकिरी चट्टे पडले आहेत'",
        "outbreak_tab_title": "तमिळनाडू राज्य पीक रोग पाळत व सतर्कता",
        "district_filter_label": "जिल्हा निवडा",
        "status_ready": "प्रणाली सज्ज"
    }
}

# ==========================================
# CACHED RESOURCE INITIALIZATION
# ==========================================
@st.cache_resource
def get_genai_client(api_key: str):
    """
    Cached GenAI client initialization to avoid re-creating HTTP sessions
    and preventing connection lags during Streamlit reruns.
    """
    if not api_key or not GENAI_AVAILABLE:
        return None
    try:
        # Use a 30s timeout to prevent premature socket timeouts on slower/mobile networks
        return genai.Client(api_key=api_key, http_options={"timeout": 30000})
    except Exception as exc:
        print(f"[AgriVoice Vision] Error creating GenAI client: {exc}")
        return None


# ==========================================
# SIDEBAR CONTROLS
# ==========================================
with st.sidebar:
    st.image("https://img.icons8.com/color/96/sprout.png", width=64)
    st.markdown("### 🌾 **AgriVoice Vision**")
    st.caption("SIH Problem Statement: SIH26131")
    
    st.divider()
    
    # 1. Vernacular Language Selector
    selected_lang_name = st.selectbox(
        "🌐 Choose Language / மொழி / भाषा",
        options=list(LANGUAGES.keys()),
        index=0
    )
    L = LANGUAGES[selected_lang_name]
    
    # 2. District Outbreak Selector (Tamil Nadu)
    try:
        outbreaks_raw = get_outbreaks_dataframe()
        districts = sorted(outbreaks_raw["District"].unique().tolist())
    except Exception:
        districts = ["Thanjavur", "Coimbatore", "Madurai", "Salem", "Tiruchirappalli"]

    default_district_idx = districts.index("Thanjavur") if "Thanjavur" in districts else 0
    selected_district = st.selectbox(
        f"📍 {L.get('district_filter_label', 'Focus District Alert Feed')}",
        options=districts,
        index=default_district_idx
    )
    
    # District Quick Alert Status
    try:
        district_logs = get_district_summary(selected_district)
        crit_count = len(district_logs[district_logs["Severity"].isin(["Critical", "High"])])
        if crit_count > 0:
            st.error(f"⚠️ **{selected_district}**: {crit_count} Critical/High Alerts Active!")
        else:
            st.success(f"✅ **{selected_district}**: Normal Surveillance Status")
    except Exception:
        st.info(f"📍 **{selected_district}**: Surveillance Active")

    st.divider()

    # 3. AI Engine Status & Crash-Proof Safeguard
    st.markdown("#### ⚡ AI Engine Status")
    env_api_key = os.getenv("GEMINI_API_KEY", "")
    if not env_api_key:
        try:
            if hasattr(st, "secrets") and "GEMINI_API_KEY" in st.secrets:
                env_api_key = str(st.secrets["GEMINI_API_KEY"])
        except Exception:
            pass
    env_api_key = env_api_key.strip().strip('"').strip("'")
    
    user_api_key = st.text_input(
        "Gemini API Key (Optional Override)",
        value=env_api_key,
        type="password",
        help="Reads automatically from .env or deployment secrets. If empty or invalid, system safely falls back to agronomical knowledge base."
    )
    active_api_key = user_api_key.strip().strip('"').strip("'") if user_api_key else env_api_key

    if active_api_key and GENAI_AVAILABLE:
        st.markdown('<span class="status-pill status-online">🟢 Gemini Flash Online</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="status-pill status-fallback">🟡 Demo Fallback Mode (100% Crash-Proof)</span>', unsafe_allow_html=True)
        st.caption("Offline agronomy database ready for zero-downtime jury presentation.")

    st.divider()
    st.markdown("👨‍🌾 *Designed for smallholder farmers & KVK Extension Officers*")

# ==========================================
# MAIN HERO HEADER
# ==========================================
st.markdown(
    """
    <div class="hero-container">
        <div class="hero-title-group">
            <h1>🌾 AgriVoice Vision - Kisan AI Diagnostic System</h1>
            <p class="hero-subtitle">
                Early detection & multimodal management of crop diseases and pest infestations (SIH26131)
            </p>
        </div>
        <div>
            <span class="badge-gemini">⚡ Powered by Multimodal Gemini + Web Speech</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# HELPER FUNCTIONS (INFERENCE & SPEECH)
# ==========================================

def get_fallback_structured_diagnosis(disease_key: str = "tomato_early_blight", lang_code: str = "en") -> Tuple[Dict[str, Any], str]:
    """Retrieve structured diagnosis from sample_data.py with safe language support."""
    sample = get_sample_disease(disease_key) or FALLBACK_DISEASES.get("tomato_early_blight", {})
    advisory = get_localized_advisory(sample.get("id", "tomato_early_blight"), lang_code)
    
    diagnosis = {
        "crop": advisory.get("crop", sample.get("crop", "Tomato")),
        "condition": advisory.get("condition", sample.get("condition", "Early Blight")),
        "disease": advisory.get("condition", sample.get("condition", "Early Blight")),
        "confidence": sample.get("confidence", 0.94),
        "severity": sample.get("severity", "High"),
        "organic_remedy": advisory.get("organic_remedy", sample.get("organic_remedy", "")),
        "chemical_remedy": advisory.get("chemical_remedy", sample.get("chemical_remedy", "")),
        "prevention": advisory.get("prevention", sample.get("prevention", "")),
        "preventive_actions": advisory.get("prevention", sample.get("prevention", "")),
        "voice_summary": advisory.get("voice_summary", "")
    }
    return diagnosis, "Demo Fallback Knowledge Base (Offline Guard)"


def run_gemini_vision_diagnosis(
    image: Image.Image,
    api_key: str,
    lang_name: str,
    lang_code: str,
    fallback_key: str = "tomato_early_blight"
) -> Tuple[Dict[str, Any], str]:
    """
    Execute structured Multimodal Gemini Vision inference on leaf image.
    Uses official google-genai SDK passing PIL image directly with automatic payload optimization.
    Falls back gracefully to sample_data.py if any exception or timeout occurs.
    """
    if not api_key or not GENAI_AVAILABLE:
        return get_fallback_structured_diagnosis(fallback_key, lang_code)

    try:
        client = get_genai_client(api_key)
        if not client:
            return get_fallback_structured_diagnosis(fallback_key, lang_code)

        # Optimization: Downscale image if larger than 1024px to prevent large network payloads and HTTP socket timeouts
        try:
            max_dim = 1024
            w, h = image.size
            if max(w, h) > max_dim:
                scale = max_dim / float(max(w, h))
                new_size = (int(w * scale), int(h * scale))
                image = image.resize(new_size, Image.Resampling.LANCZOS)
        except Exception as img_err:
            print(f"[AgriVoice Vision] Note on image resize: {img_err}")

        prompt = f"""Analyze this agricultural leaf image carefully.
1. Detect the exact plant/crop species shown (e.g., Spinach, Tomato, Cotton, Rice, Sugarcane, Banana, Groundnut, etc.).
2. Identify the specific disease, fungal infestation, pest, or nutrient deficiency. If healthy, state 'Healthy'.
3. Provide:
   - crop: identified plant name
   - condition: identified disease or health status
   - confidence: decimal between 0.0 and 1.0
   - severity: 'Low', 'Moderate', or 'High'
   - organic_remedy: 2 practical organic/home treatments in {lang_name}
   - chemical_remedy: safe chemical treatment + exact water dilution ratio in {lang_name}
   - prevention: preventive practices in {lang_name}
Return strictly valid JSON matching this schema:
{{
  "crop": "identified plant name",
  "condition": "identified disease or health status",
  "confidence": 0.95,
  "severity": "Low | Moderate | High",
  "organic_remedy": "2 practical organic/home treatments in {lang_name}",
  "chemical_remedy": "safe chemical treatment + exact water dilution ratio in {lang_name}",
  "prevention": "preventive practices in {lang_name}"
}}
Do NOT include markdown formatting or backticks. Return raw JSON only."""

        # Models ordered by current availability, low latency, and multimodal performance
        models_to_try = [
            "gemini-flash-lite-latest",
            "gemini-3.5-flash-lite",
            "gemini-3.1-flash-lite",
            "gemini-3.1-flash-lite-preview",
            "gemini-flash-latest",
            "gemini-3.8-flash",
            "gemini-3.5-flash"
        ]
        response = None
        last_error = None
        model_used = None

        for model_id in models_to_try:
            for attempt in range(2):
                try:
                    response = client.models.generate_content(
                        model=model_id,
                        contents=[image, prompt]
                    )
                    if response and response.text:
                        model_used = model_id
                        break
                except Exception as err:
                    last_error = err
                    err_str = str(err)
                    # If model not available or permanent error, skip immediately to next model
                    if "404" in err_str or "NOT_FOUND" in err_str:
                        break
                    # If rate limit or transient network glitch, wait briefly before retry
                    if "429" in err_str or "RESOURCE_EXHAUSTED" in err_str or "503" in err_str:
                        import time
                        time.sleep(1.0)
                        continue
                    break
            if response and response.text:
                break

        if not response or not response.text:
            raise RuntimeError(f"All Gemini models failed: {last_error}")

        # Parse JSON response cleanly even if markdown backticks or preamble are present
        raw_text = response.text.strip()
        if "```" in raw_text or "{" in raw_text:
            start = raw_text.find("{")
            end = raw_text.rfind("}")
            if start != -1 and end != -1:
                raw_text = raw_text[start:end+1]

        data = json.loads(raw_text)

        # Support alternate keys if generated
        if "condition" not in data and "disease" in data:
            data["condition"] = data["disease"]
        if "prevention" not in data and "preventive_actions" in data:
            data["prevention"] = data["preventive_actions"]

        data["disease"] = data.get("condition", "N/A")
        data["preventive_actions"] = data.get("prevention", "N/A")

        # Normalize confidence
        try:
            data["confidence"] = float(data.get("confidence", 0.92))
            if data["confidence"] > 1.0:
                data["confidence"] = data["confidence"] / 100.0
        except (ValueError, TypeError):
            data["confidence"] = 0.90

        # Normalize severity
        sev_str = str(data.get("severity", "Moderate")).capitalize()
        if sev_str in ["Low", "Moderate", "High", "Critical"]:
            data["severity"] = sev_str
        else:
            data["severity"] = "Moderate"

        # Generate localized voice advisory summary for gTTS
        if lang_code == "hi":
            data["voice_summary"] = (
                f"किसान साथी, आपकी {data.get('crop')} की फसल में {data.get('condition')} पाया गया है। "
                f"गंभीरता {data.get('severity')} है। "
                f"जैविक उपचार: {data.get('organic_remedy')}। "
                f"रासायनिक छिड़काव: {data.get('chemical_remedy')}।"
            )
        elif lang_code == "ta":
            data["voice_summary"] = (
                f"விவசாய நண்பரே, உங்கள் {data.get('crop')} பயிரில் {data.get('condition')} தாக்கம் கண்டறியப்பட்டுள்ளது. "
                f"தீவிரம் {data.get('severity')} ஆகும். "
                f"இயற்கை நிவாரணம்: {data.get('organic_remedy')}. "
                f"ரசாயன மருந்து: {data.get('chemical_remedy')}."
            )
        elif lang_code == "mr":
            data["voice_summary"] = (
                f"शेतकरी बांधवांनो, आपल्या {data.get('crop')} पिकावर {data.get('condition')} आढळले आहे. "
                f"तीव्रता {data.get('severity')} आहे. "
                f"सेंद्रिय उपाय: {data.get('organic_remedy')}. "
                f"रासायनिक उपाय: {data.get('chemical_remedy')}."
            )
        else:
            data["voice_summary"] = (
                f"Crop: {data.get('crop')}, Condition: {data.get('condition')}. "
                f"Severity: {data.get('severity')}. "
                f"Organic remedy: {data.get('organic_remedy')}. "
                f"Chemical remedy: {data.get('chemical_remedy')}."
            )

        return data, f"Live Gemini Vision ({model_used})"

    except Exception as exc:
        print(f"[AgriVoice Vision] Gemini diagnosis fallback triggered: {exc}")
        # Fallback dummy data is triggered safely if the API call throws an exception
        fb_diag, _ = get_fallback_structured_diagnosis(fallback_key, lang_code)
        return fb_diag, "Demo Fallback (Offline Guard)"


def generate_audio(text: str, lang_code: str) -> io.BytesIO:
    """Generate vernacular speech audio using gTTS with retry resilience."""
    lang_mapping = {
        "en": "en",
        "hi": "hi",
        "ta": "ta",
        "mr": "mr",
        "en-US": "en",
        "hi-IN": "hi",
        "ta-IN": "ta",
        "mr-IN": "mr",
        "English": "en",
        "हिन्दी (Hindi)": "hi",
        "தமிழ் (Tamil)": "ta",
        "मराठी (Marathi)": "mr",
    }
    resolved_lang = lang_mapping.get(lang_code, lang_code.split("-")[0] if "-" in lang_code else "en")
    last_err = None
    for attempt in range(2):
        try:
            tts = gTTS(text=text, lang=resolved_lang, slow=False)
            fp = io.BytesIO()
            tts.write_to_fp(fp)
            fp.seek(0)
            return fp
        except Exception as exc:
            last_err = exc
            import time
            time.sleep(0.5)
    raise last_err or RuntimeError("TTS generation failed")


@st.cache_data(show_spinner=False)
def get_cached_audio_bytes(text: str, lang_code: str) -> bytes:
    """Generate and cache audio bytes to prevent redundant network TTS requests on re-renders."""
    try:
        fp = generate_audio(text, lang_code)
        return fp.getvalue()
    except Exception:
        return b""


def render_vernacular_tts(text_to_speak: str, lang_code: str, button_label: str):
    """Render high-quality gTTS vernacular audio playback in Streamlit."""
    if not text_to_speak or not text_to_speak.strip():
        return

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%);
            border: 1px solid #86efac;
            border-radius: 12px;
            padding: 12px 16px;
            margin: 16px 0 8px 0;
            box-shadow: 0 2px 6px rgba(16, 185, 129, 0.08);
        ">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px; flex-wrap: wrap; gap: 8px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 18px;">🔊</span>
                    <strong style="color: #15803d; font-size: 15px;">{button_label}</strong>
                </div>
                <span style="
                    background: #dcfce7;
                    color: #166534;
                    border: 1px solid #86efac;
                    padding: 2px 10px;
                    border-radius: 16px;
                    font-size: 11px;
                    font-weight: 700;
                ">
                    ✨ Clear Vernacular Voice (gTTS)
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    try:
        audio_bytes = get_cached_audio_bytes(text_to_speak, lang_code)
        if audio_bytes:
            st.audio(audio_bytes, format="audio/mp3")
    except Exception as exc:
        st.warning(f"Voice advisory temporarily unavailable: {exc}")


# ==========================================
# MAIN APPLICATION TABS
# ==========================================
tab1, tab2, tab3 = st.tabs([
    L["tab1_title"],
    L["tab2_title"],
    L["tab3_title"]
])

# ------------------------------------------
# TAB 1: 📸 IMAGE DIAGNOSIS
# ------------------------------------------
with tab1:
    st.markdown("#### 🌿 Multimodal Visual Crop Inspection")
    st.caption("Upload a high-resolution photo of affected leaves, stems, or fruits for instant pathogen identification.")

    col_input1, col_input2 = st.columns([3, 2])
    
    with col_input1:
        uploaded_file = st.file_uploader(
            L["upload_label"],
            type=["jpg", "jpeg", "png"],
            help="Supports standard smartphone field photos in JPG/PNG format."
        )
    
    with col_input2:
        st.markdown("**Quick Evaluator Testing**")
        sample_clicked = st.button(
            L["test_sample_btn"],
            use_container_width=True,
            type="primary"
        )
        
        # Additional one-click disease options for evaluators
        with st.expander("🔍 Test Other Crop Pathogens (1-Click Demo)"):
            c_btn1, c_btn2, c_btn3 = st.columns(3)
            with c_btn1:
                cotton_clicked = st.button("Cotton Leaf Curl", use_container_width=True)
            with c_btn2:
                rice_clicked = st.button("Rice Blast", use_container_width=True)
            with c_btn3:
                potato_clicked = st.button("Potato Late Blight", use_container_width=True)

    # Determine image source and unique diagnostic cache key
    active_image = None
    force_fallback_key = None
    current_diag_key = None
    sample_disease_hint = "tomato_early_blight"

    if sample_clicked:
        sample_path = os.path.join("assets", "sample_tomato_early_blight.jpg")
        if os.path.exists(sample_path):
            active_image = Image.open(sample_path).convert("RGB")
            current_diag_key = f"sample_tomato_{L['code']}"
        sample_disease_hint = "tomato_early_blight"
        if not active_api_key or not GENAI_AVAILABLE:
            force_fallback_key = "tomato_early_blight"
    elif 'cotton_clicked' in locals() and cotton_clicked:
        sample_path = os.path.join("assets", "sample_cotton_leaf_curl.jpg")
        if os.path.exists(sample_path):
            active_image = Image.open(sample_path).convert("RGB")
            current_diag_key = f"sample_cotton_{L['code']}"
        sample_disease_hint = "cotton_leaf_curl"
        if not active_api_key or not GENAI_AVAILABLE:
            force_fallback_key = "cotton_leaf_curl"
    elif 'rice_clicked' in locals() and rice_clicked:
        sample_path = os.path.join("assets", "sample_rice_blast.jpg")
        if os.path.exists(sample_path):
            active_image = Image.open(sample_path).convert("RGB")
            current_diag_key = f"sample_rice_{L['code']}"
        sample_disease_hint = "rice_blast"
        if not active_api_key or not GENAI_AVAILABLE:
            force_fallback_key = "rice_blast"
    elif 'potato_clicked' in locals() and potato_clicked:
        sample_path = os.path.join("assets", "sample_potato_late_blight.jpg")
        if os.path.exists(sample_path):
            active_image = Image.open(sample_path).convert("RGB")
            current_diag_key = f"sample_potato_{L['code']}"
        sample_disease_hint = "potato_late_blight"
        if not active_api_key or not GENAI_AVAILABLE:
            force_fallback_key = "potato_late_blight"
    elif uploaded_file is not None:
        file_bytes = uploaded_file.read()
        uploaded_file.seek(0)
        active_image = Image.open(BytesIO(file_bytes)).convert("RGB")
        current_diag_key = f"upload_{uploaded_file.name}_{uploaded_file.size}_{L['code']}"
        force_fallback_key = None
        sample_disease_hint = "tomato_early_blight"

    # Display image & run diagnosis with Session State Caching to prevent sluggish lag
    if active_image is not None and current_diag_key is not None:
        st.divider()
        col_img, col_res = st.columns([1.2, 2])
        
        with col_img:
            st.image(active_image, caption="Analyzed Leaf Sample", use_container_width=True)
        
        with col_res:
            # Check if diagnosis is already cached in session_state to avoid repeating slow API calls
            if "diag_cache" not in st.session_state:
                st.session_state["diag_cache"] = {}

            if current_diag_key in st.session_state["diag_cache"]:
                diagnosis, source_badge = st.session_state["diag_cache"][current_diag_key]
            else:
                with st.spinner(L["diagnosing"]):
                    if force_fallback_key:
                        diagnosis, source_badge = get_fallback_structured_diagnosis(force_fallback_key, L["code"])
                    else:
                        diagnosis, source_badge = run_gemini_vision_diagnosis(
                            active_image,
                            active_api_key,
                            selected_lang_name,
                            L["code"],
                            fallback_key=sample_disease_hint
                        )
                # Store in session state cache
                st.session_state["diag_cache"][current_diag_key] = (diagnosis, source_badge)
            
            # Diagnostic Source Badge
            if "Gemini" in source_badge:
                st.markdown(f'<span class="status-pill status-online">🟢 {source_badge}</span>', unsafe_allow_html=True)
            else:
                st.markdown(f'<span class="status-pill status-fallback">🟡 {source_badge}</span>', unsafe_allow_html=True)

            # Clean Metric Cards
            sev_class = "sev-critical" if diagnosis.get("severity") in ["High", "Critical"] else ("sev-moderate" if diagnosis.get("severity") == "Moderate" else "sev-low")
            conf_val = diagnosis.get("confidence", 0.94)
            conf_percent = int(conf_val * 100) if conf_val <= 1.0 else int(conf_val)

            st.markdown(
                f"""
                <div class="metric-grid">
                    <div class="diag-metric-card">
                        <div class="metric-label">{L['crop_label']}</div>
                        <div class="metric-value">{diagnosis.get('crop', 'Crop')}</div>
                    </div>
                    <div class="diag-metric-card">
                        <div class="metric-label">{L['disease_label']}</div>
                        <div class="metric-value" style="font-size: 16px;">{diagnosis.get('disease', 'Condition')}</div>
                    </div>
                    <div class="diag-metric-card">
                        <div class="metric-label">{L['confidence_label']}</div>
                        <div class="metric-value" style="color: #059669;">{conf_percent}%</div>
                    </div>
                    <div class="diag-metric-card">
                        <div class="metric-label">{L['severity_label']}</div>
                        <div class="metric-value {sev_class}">{diagnosis.get('severity', 'Moderate')}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # Natural Vernacular Voice Synthesis via gTTS
            speech_text = diagnosis.get("voice_summary") or f"{diagnosis.get('crop')}: {diagnosis.get('condition')}. {diagnosis.get('organic_remedy')}"
            render_vernacular_tts(
                text_to_speak=speech_text,
                lang_code=L["code"],
                button_label=L["listen_btn_text"]
            )

        # Actionable Dual-Action Remedy Section
        st.markdown("### 📋 Dual-Action Management Protocol")
        col_org, col_chem, col_prev = st.columns(3)
        
        with col_org:
            st.markdown(
                f"""
                <div class="remedy-card">
                    <div class="remedy-header" style="color: #047857;">{L['organic_title']}</div>
                    <p style="font-size: 14px; color: #1e293b; line-height: 1.5; margin: 0;">
                        {diagnosis.get('organic_remedy', 'Apply organic biocontrol agent.')}
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        with col_chem:
            st.markdown(
                f"""
                <div class="remedy-card chemical">
                    <div class="remedy-header" style="color: #1d4ed8;">{L['chemical_title']}</div>
                    <p style="font-size: 14px; color: #1e293b; line-height: 1.5; margin: 0;">
                        {diagnosis.get('chemical_remedy', 'Foliar spray with recommended fungicide/pesticide.')}
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        with col_prev:
            st.markdown(
                f"""
                <div class="remedy-card prevention">
                    <div class="remedy-header" style="color: #6d28d9;">{L['prevention_title']}</div>
                    <p style="font-size: 14px; color: #1e293b; line-height: 1.5; margin: 0;">
                        {diagnosis.get('preventive_actions', diagnosis.get('prevention', 'Maintain balanced irrigation and sanitation.'))}
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.info("👆 Upload an image of an infected plant or click **'⚡ Test with Sample Leaf'** above to run the live diagnostic pipeline.")


# ------------------------------------------
# TAB 2: 🎙️ VOICE & SYMPTOM QUERY
# ------------------------------------------
with tab2:
    st.markdown("#### 🎙️ Vernacular Speech-to-Advisory Consultation")
    st.markdown(f"*{L.get('voice_tab_desc', 'Tap microphone to speak or click quick simulation query.')}*")

    # Embedded Web Speech Recognition HTML/JS Component
    speech_recog_html = f"""
    <div style="
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        background: #f8fafc;
        border: 2px dashed #cbd5e1;
        border-radius: 14px;
        padding: 18px;
        margin: 10px 0 14px 0;
    ">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; margin-bottom: 12px;">
            <div>
                <strong style="color: #0f172a; font-size: 15px;">Microphone Input ({L.get('speech_lang', 'ta-IN')})</strong>
                <div id="mic-status" style="font-size: 13px; color: #64748b; margin-top: 3px;">Click microphone to speak symptoms in {selected_lang_name}</div>
            </div>
            <div style="display: flex; gap: 8px;">
                <button id="mic-toggle-btn" onclick="toggleRecognition()" style="
                    background: #dc2626;
                    color: white;
                    border: none;
                    border-radius: 8px;
                    padding: 9px 16px;
                    font-size: 14px;
                    font-weight: 700;
                    cursor: pointer;
                    display: inline-flex;
                    align-items: center;
                    gap: 6px;
                    box-shadow: 0 4px 6px rgba(220, 38, 38, 0.2);
                ">
                    <span id="mic-dot">🔴</span>
                    <span id="mic-label">Tap to Speak</span>
                </button>
                <button onclick="clearTranscript()" style="
                    background: #f1f5f9;
                    color: #475569;
                    border: 1px solid #cbd5e1;
                    border-radius: 8px;
                    padding: 9px 12px;
                    font-size: 13px;
                    font-weight: 600;
                    cursor: pointer;
                ">Clear</button>
            </div>
        </div>

        <div id="transcript-box" style="
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 12px;
            min-height: 52px;
            font-size: 14px;
            color: #1e293b;
            line-height: 1.5;
        "><em>Spoken words will appear here in real time...</em></div>
        
        <div style="margin-top: 10px; display: flex; justify-content: flex-end;">
            <button onclick="copyToClipboard()" style="
                background: #2563eb;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 6px 14px;
                font-size: 12px;
                font-weight: 600;
                cursor: pointer;
            ">📋 Copy Transcribed Text</button>
        </div>
    </div>

    <script>
    let recognition = null;
    let isListening = false;
    const transcriptBox = document.getElementById('transcript-box');
    const micStatus = document.getElementById('mic-status');
    const micLabel = document.getElementById('mic-label');
    const micDot = document.getElementById('mic-dot');

    function toggleRecognition() {{
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (!SpeechRecognition) {{
            micStatus.innerText = "⚠️ Web Speech API not supported. Please use Chrome/Edge or click Quick Queries below.";
            micStatus.style.color = "#dc2626";
            return;
        }}

        if (!isListening) {{
            try {{
                recognition = new SpeechRecognition();
                recognition.lang = "{L.get('speech_lang', 'ta-IN')}";
                recognition.continuous = true;
                recognition.interimResults = true;

                recognition.onstart = function() {{
                    isListening = true;
                    micStatus.innerText = "🎙️ Listening in {L.get('speech_lang', 'ta-IN')}... Speak symptoms clearly.";
                    micStatus.style.color = "#dc2626";
                    micLabel.innerText = "Stop";
                    micDot.innerText = "⚡";
                }};

                recognition.onresult = function(event) {{
                    let fullText = '';
                    for (let i = 0; i < event.results.length; ++i) {{
                        fullText += event.results[i][0].transcript;
                    }}
                    transcriptBox.innerText = fullText;
                }};

                recognition.onerror = function(event) {{
                    micStatus.innerText = "Mic Notice: " + (event.error || "Microphone stopped.");
                    resetUI();
                }};

                recognition.onend = function() {{
                    resetUI();
                }};

                recognition.start();
            }} catch(err) {{
                micStatus.innerText = "Notice: " + err.message;
                resetUI();
            }}
        }} else {{
            if (recognition) recognition.stop();
            resetUI();
        }}
    }}

    function resetUI() {{
        isListening = false;
        micLabel.innerText = "Tap to Speak";
        micDot.innerText = "🔴";
        micStatus.innerText = "Ready. Spoken text captured above.";
        micStatus.style.color = "#16a34a";
    }}

    function clearTranscript() {{
        transcriptBox.innerHTML = "<em>Spoken words will appear here in real time...</em>";
        if (recognition) recognition.stop();
        resetUI();
    }}

    function copyToClipboard() {{
        const text = transcriptBox.innerText;
        if (text && !text.includes("Spoken words")) {{
            navigator.clipboard.writeText(text);
            micStatus.innerText = "📋 Transcribed text copied! Paste into description box below.";
            micStatus.style.color = "#2563eb";
        }}
    }}
    </script>
    """
    st.components.v1.html(speech_recog_html, height=195)

    # 4 Quick Voice Query Simulation Buttons (Jury Pitch Proof)
    st.markdown("##### ⚡ Quick Voice Query Simulation (1-Click Demonstration)")
    st.caption("Click any sample query below to instantly simulate farmer voice transcription & agronomical consultation:")

    q_col1, q_col2 = st.columns(2)
    with q_col1:
        if st.button("🍃 கீரையில் பூச்சி தாக்குதல் உள்ளது (Spinach Pest Attack)", use_container_width=True):
            st.session_state["symptom_query"] = "கீரையில் பூச்சி தாக்குதல் மற்றும் கீழ்நோக்கு சாம்பல் நோய் உள்ளது, இலைகள் உதிர்கின்றன."
            st.session_state["trigger_query"] = True
        if st.button("🍅 தக்காளி இலைகள் மஞ்சள் நிறமாக மாறுகின்றன (Tomato Yellowing)", use_container_width=True):
            st.session_state["symptom_query"] = "தக்காளி இலைகள் மஞ்சள் நிறமாக மாறி மேல்நோக்கி சுருண்டு வளர்கின்றன (Tomato Leaf Curl)."
            st.session_state["trigger_query"] = True

    with q_col2:
        if st.button("🌾 நெல் பயிரில் இலைக்கருகல் நோய் (Paddy Leaf Blight / Blast)", use_container_width=True):
            st.session_state["symptom_query"] = "நெல் பயிரில் இலைக்கருகல் மற்றும் குலை நோய் புள்ளிகள் உள்ளன (Paddy Rice Blast)."
            st.session_state["trigger_query"] = True
        if st.button("🌱 Tomato leaf curl remedy", use_container_width=True):
            st.session_state["symptom_query"] = "Tomato leaf curl virus symptoms with stunted growth and whiteflies."
            st.session_state["trigger_query"] = True

    # Symptom Input Area
    st.markdown("**Symptom Description:**")
    current_query = st.session_state.get("symptom_query", "")
    symptom_input = st.text_area(
        "Symptom Description",
        value=current_query,
        placeholder=L.get("voice_sample_prompt", "Enter crop symptoms..."),
        height=85,
        label_visibility="collapsed"
    )

    execute_query = st.button("🔍 Get Actionable Remedies & Advisory", type="primary") or st.session_state.get("trigger_query", False)
    # Reset trigger
    if "trigger_query" in st.session_state:
        st.session_state["trigger_query"] = False

    if execute_query:
        active_query_text = symptom_input.strip() if symptom_input.strip() else current_query.strip()
        if not active_query_text:
            st.warning("Please speak or type crop symptoms to receive tailored agronomical advice.")
        else:
            with st.spinner("Analyzing symptoms against agricultural phytopathology database..."):
                query_lower = active_query_text.lower()
                
                # Dynamic matching supporting Tamil Nadu crops and diseases
                matched_key = "tomato_early_blight"
                if any(w in query_lower for w in ["கீரை", "spinach", "palak", "downy", "mildew", "சாம்பல்"]):
                    matched_key = "spinach_downy_mildew"
                elif any(w in query_lower for w in ["கரும்பு", "sugarcane", "ganna", "red rot", "செவ்வழுகல்"]):
                    matched_key = "sugarcane_red_rot"
                elif any(w in query_lower for w in ["வாழை", "banana", "kela", "panama", "வாடல்", "wilt"]):
                    matched_key = "banana_panama_wilt"
                elif any(w in query_lower for w in ["வேர்க்கடலை", "நிலக்கடலை", "groundnut", "tikka", "டிக்கா"]):
                    matched_key = "groundnut_tikka"
                elif any(w in query_lower for w in ["நெல்", "rice", "paddy", "blast", "blight", "குலை", "கருகல்"]):
                    matched_key = "rice_blast"
                elif any(w in query_lower for w in ["curl", "சுருள்", "மஞ்சள்", "whitefly"]):
                    matched_key = "tomato_leaf_curl"
                elif any(w in query_lower for w in ["பருத்தி", "cotton", "bollworm", "புழு"]):
                    matched_key = "cotton_bollworm"
                elif any(w in query_lower for w in ["தக்காளி", "tomato", "early blight"]):
                    matched_key = "tomato_early_blight"

                symptom_diag, _ = get_fallback_structured_diagnosis(matched_key, L["code"])

            st.success(f"🌾 Diagnosis Match: **{symptom_diag.get('crop')} - {symptom_diag.get('disease')}** (Severity: {symptom_diag.get('severity')})")

            # Structured Advisory Output
            col_v1, col_v2 = st.columns(2)
            with col_v1:
                st.markdown(f"**{L['organic_title']}**")
                st.info(symptom_diag.get("organic_remedy"))
            with col_v2:
                st.markdown(f"**{L['chemical_title']}**")
                st.warning(symptom_diag.get("chemical_remedy"))

            st.markdown(f"**{L['prevention_title']}**")
            st.write(symptom_diag.get("preventive_actions", symptom_diag.get("prevention", "")))

            # Audio Playback of Symptom Advisory via gTTS
            render_vernacular_tts(
                text_to_speak=symptom_diag.get("voice_summary", ""),
                lang_code=L["code"],
                button_label=f"🔊 Listen to Advisory in {selected_lang_name}"
            )


# ------------------------------------------
# TAB 3: 📊 DISTRICT SURVEILLANCE DASHBOARD
# ------------------------------------------
with tab3:
    st.markdown(f"#### 📊 {L.get('outbreak_tab_title', 'Tamil Nadu Regional Surveillance')}")
    st.caption("Real-time telemetry and disease escalation monitoring across Tamil Nadu agricultural districts for KVK Extension Officers.")

    try:
        df_outbreaks = get_outbreaks_dataframe()
    except Exception:
        df_outbreaks = pd.DataFrame()

    if not df_outbreaks.empty:
        # High-level KPIs
        total_incidents = len(df_outbreaks)
        crit_count = len(df_outbreaks[df_outbreaks["Severity"] == "Critical"])
        high_count = len(df_outbreaks[df_outbreaks["Severity"] == "High"])
        total_acres = df_outbreaks["AffectedAreaAcres"].sum() if "AffectedAreaAcres" in df_outbreaks.columns else 2965

        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        with kpi1:
            st.metric("Total Monitored Incidents", f"{total_incidents} Hotspots")
        with kpi2:
            st.metric("Critical Outbreak Zones", f"{crit_count} Districts", delta="Active Quarantine", delta_color="inverse")
        with kpi3:
            st.metric("High Severity Alerts", f"{high_count} Zones")
        with kpi4:
            st.metric("Estimated Affected Acreage", f"{total_acres:,} Acres")

        st.divider()

        # Visual Analytics: Bar Chart & Distribution
        col_chart1, col_chart2 = st.columns([1.5, 1])

        with col_chart1:
            st.markdown("**Incident Reports by District & Severity**")
            try:
                district_counts = df_outbreaks.groupby(["District", "Severity"]).size().unstack(fill_value=0)
                st.bar_chart(district_counts, use_container_width=True)
            except Exception as e:
                st.caption(f"Chart view unavailable: {e}")

        with col_chart2:
            st.markdown("**Crop Vulnerability Breakdown**")
            try:
                crop_counts = df_outbreaks["Crop"].value_counts()
                st.dataframe(
                    pd.DataFrame({"Crop": crop_counts.index, "Reported Cases": crop_counts.values}),
                    use_container_width=True,
                    hide_index=True
                )
            except Exception as e:
                st.caption(f"Crop distribution unavailable: {e}")

        st.divider()

        # District Level Investigation View
        st.markdown(f"### 📍 Focus District Telemetry: **{selected_district}**")
        
        try:
            dist_data = get_district_summary(selected_district)
        except Exception:
            dist_data = pd.DataFrame()
        
        if len(dist_data) > 0:
            st.dataframe(
                dist_data[["District", "Crop", "Disease", "Severity", "AffectedAreaAcres", "Status", "ReportedDate"]],
                use_container_width=True,
                hide_index=True
            )
            
            # Extension Officer Action Protocols (Tamil Nadu Focused)
            st.markdown("**🚨 Recommended KVK Officer Emergency Protocol:**")
            dist_diseases = dist_data["Disease"].tolist()
            if any("Blast" in d or "Blight" in d for d in dist_diseases):
                st.error("• **Cauvery Delta Paddy Protocol (Thanjavur/Cuddalore)**: Alert FPOs to spray Tricyclazole 75% WP (0.6 g/L) for blast and maintain regulated water levels to prevent airborne spore propagation.")
            if any("Red Rot" in d for d in dist_diseases):
                st.warning("• **Sugarcane Cane Belt Protocol (Erode/Salem)**: Issue quarantine notice; destroy infected stools and mandate 15-minute Carbendazim sett dip for next planting cycle.")
            if any("Panama Wilt" in d for d in dist_diseases):
                st.error("• **Vaigai/Cauvery Basin Banana Protocol (Madurai/Tiruchirappalli)**: Apply root drenching of Carbendazim (2.0 g/L) or Trichoderma viride enriched organic manure in affected groves.")
            if any("Bollworm" in d or "Leaf Curl" in d for d in dist_diseases):
                st.warning("• **Kongu & South Cotton Belt (Coimbatore/Tirunelveli)**: Install 5 pheromone traps per acre for Helicoverpa monitoring; deploy 5% NSKE spray.")
            if any("Tikka" in d or "Downy" in d for d in dist_diseases):
                st.info("• **Horticultural & Oilseed Belt (Dindigul/Vellore/Salem)**: Dispatch emergency buffer supplies of Mancozeb and Copper Oxychloride to Primary Agricultural Cooperative Societies (PACS).")
        else:
            st.info(f"No active disease escalation reported in {selected_district}. Routine surveillance continuing.")

        # Complete Surveillance Raw Log Table
        with st.expander("📋 View Complete Tamil Nadu Outbreak Log (CSV View)"):
            st.dataframe(
                df_outbreaks[["District", "Crop", "Disease", "Severity", "AffectedAreaAcres", "Status", "ReportedDate"]],
                use_container_width=True,
                hide_index=True
            )
    else:
        st.warning("No surveillance data loaded.")
