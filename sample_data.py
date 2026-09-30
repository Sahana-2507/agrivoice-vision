"""
AgriVoice Vision - Fallback & Sample Crop Disease Knowledge Base
===============================================================
Curated agronomical dataset for fallback offline operation and demonstration
under SIH Problem Statement SIH26131.

Includes:
- Standardized English disease diagnosis
- Agronomical severity assessment
- Eco-friendly / Organic remedies
- Targeted Chemical interventions
- Preventive cultural practices
- Multilingual translations for vernacular voice advisory (Hindi, Tamil, Marathi)
"""

from typing import Dict, Any, Optional

FALLBACK_DISEASES: Dict[str, Dict[str, Any]] = {
    "tomato_early_blight": {
        "id": "tomato_early_blight",
        "crop": "Tomato",
        "condition": "Tomato Early Blight (Alternaria solani)",
        "confidence": 0.94,
        "severity": "High",
        "symptoms": "Concentric rings (target board pattern) on older leaves surrounded by a yellow halo, eventual defoliation.",
        "organic_remedy": "Apply cold-pressed neem oil (0.5% concentration) or Trichoderma viride bio-fungicide (5g/L). Prune and destroy infected lower leaves.",
        "chemical_remedy": "Foliar spray of Mancozeb 75% WP (2.5 g/L) or Chlorothalonil 75% WP (2.0 g/L) at 7-10 day intervals during high humidity.",
        "prevention": "Ensure adequate row spacing (60x45 cm) for airflow, adopt drip irrigation to prevent leaf wetness, practice 3-year crop rotation.",
        "translations": {
            "hi": {
                "crop": "टमाटर",
                "condition": "टमाटर का अगेती झुलसा रोग (अर्ली ब्लाइट)",
                "severity": "उच्च (High)",
                "organic_remedy": "नीम का तेल (0.5%) या ट्राइकोडर्मा विरिडी (5 ग्राम/लीटर) का छिड़काव करें। संक्रमित निचली पत्तियों को तुरंत तोड़कर नष्ट कर दें।",
                "chemical_remedy": "मैंकोज़ेब 75% WP (2.5 ग्राम/लीटर) या क्लोरोथैलोनिल का 7-10 दिनों के अंतराल पर छिड़काव करें।",
                "prevention": "पौधों के बीच पर्याप्त दूरी रखें, ड्रिप सिंचाई अपनाएं ताकि पत्तियां गीली न रहें, और फसल चक्र का पालन करें।",
                "voice_summary": "किसान भाई, आपके टमाटर में अगेती झुलसा रोग के लक्षण हैं। नीम तेल या मैंकोज़ेब का छिड़काव करें और खराब निचली पत्तियां हटा दें।"
            },
            "ta": {
                "crop": "தக்காளி",
                "condition": "தக்காளி முன் பருவ கருகல் நோய் (Early Blight)",
                "severity": "அதிகம் (High)",
                "organic_remedy": "வேப்பெண்ணெய் கரைசல் (0.5%) அல்லது டிரைகோடெர்மா விரிடி (5 கிராம்/லிட்டர்) தெளிக்கவும். பாதிக்கப்பட்ட கீழ் இலைகளை அகற்றி அழிக்கவும்.",
                "chemical_remedy": "மேன்கோசெப் 75% WP (2.5 கிராம்/லிட்டர்) அல்லது குளோரோதலோனில் மருந்தை 7-10 நாட்கள் இடைவெளியில் தெளிக்கவும்.",
                "prevention": "செடிகளுக்கிடையே போதிய இடைவெளி விடவும், சொட்டு நீர் பாசனம் பயன்படுத்தவும், பயிர் சுழற்சி முறையைக் கடைப்பிடிக்கவும்.",
                "voice_summary": "விவசாயி தோழரே, உங்கள் தக்காளி பயிரில் முன் பருவ கருகல் நோய் தாக்கம் உள்ளது. வேப்பெண்ணெய் அல்லது மேன்கோசெப் தெளித்து கீழ் இலைகளை உடனே அகற்றவும்."
            },
            "mr": {
                "crop": "टोमॅटो",
                "condition": "टोमॅटोवरील करपा रोग (अर्ली ब्लाइट)",
                "severity": "जास्त (High)",
                "organic_remedy": "कडुनिंब तेल (०.५%) किंवा ट्रायकोडर्मा व्हिरिडी (५ ग्रॅम/लिटर) फवारा. झाडाची खालची रोगट पाने खुडून नष्ट करा.",
                "chemical_remedy": "मँकोझेब ७५% डब्ल्यूपी (२.५ ग्रॅम/लिटर) किंवा क्लोरोथॅलोनिल ७-१० दिवसांच्या अंतराने फवारा.",
                "prevention": "रोपांमध्ये योग्य अंतर ठेवा, ठिबक सिंचनाचा वापर करा जेणेकरून पाने ओली राहणार नाहीत आणि पिकांची फेरपालट करा.",
                "voice_summary": "शेतकरी बंधूंनो, तुमच्या टोमॅटो पिकावर करपा रोगाची लक्षणे दिसत आहेत. त्वरित निंबोळी तेल किंवा मँकोझेब फवारा आणि रोगट पाने काढून टाका."
            }
        }
    },

    "cotton_leaf_curl": {
        "id": "cotton_leaf_curl",
        "crop": "Cotton",
        "condition": "Cotton Leaf Curl Virus (CLCuV)",
        "confidence": 0.91,
        "severity": "High",
        "symptoms": "Upward or downward leaf curling, thickened veins, enations on underside of leaves, stunted crop growth.",
        "organic_remedy": "Spray 5% Neem Seed Kernel Extract (NSKE) or Beauveria bassiana (5g/L) to suppress whitefly vectors. Install 15-20 yellow sticky traps per acre.",
        "chemical_remedy": "Manage whitefly vectors with Diafenthiuron 50% WP (1.2 g/L) or Flonicamid 50% WG (0.3 g/L). Note: Viral infections have no direct curative chemicals.",
        "prevention": "Eradicate alternative weed hosts (Kanghi, Peeli Buti), sow CLCuV-tolerant certified hybrids, avoid excess vegetative growth from urea.",
        "translations": {
            "hi": {
                "crop": "कपास",
                "condition": "कपास का पत्ता मरोड़ रोग (लीफ कर्ल वायरस)",
                "severity": "उच्च (High)",
                "organic_remedy": "सफेद मक्खी नियंत्रण हेतु 5% नीम अर्क (NSKE) या ब्युवेरिया बासियाना का छिड़काव करें। प्रति एकड़ 15-20 पीले चिपचिपे ट्रैप लगाएं।",
                "chemical_remedy": "सफेद मक्खी को रोकने के लिए डायफेंथियूरॉन 50% WP (1.2 ग्राम/लीटर) या फ्लोनिकैमिड का छिड़काव करें। वायरस के लिए कोई सीधी दवा नहीं है।",
                "prevention": "खेत के मेड़ों से खरपतवार नष्ट करें, रोगरोधी संकर किस्में बोएं, और यूरिया का अधिक प्रयोग न करें।",
                "voice_summary": "किसान भाई, कपास में पत्ता मरोड़ रोग सफेद मक्खी से फैल रहा है। पीले ट्रैप लगाएं और नीम अर्क या डायफेंथियूरॉन का छिड़काव करें।"
            },
            "ta": {
                "crop": "பருத்தி",
                "condition": "பருத்தி இலை சுருள் நச்சுயிரி நோய் (Leaf Curl Virus)",
                "severity": "அதிகம் (High)",
                "organic_remedy": "வெள்ளை ஈக்களைக் கட்டுப்படுத்த 5% வேப்பங்கொட்டை சாறு அல்லது பியூவேரியா பாசியானா தெளிக்கவும். ஏக்கருக்கு 15-20 மஞ்சள் பொறிகளை வைக்கவும்.",
                "chemical_remedy": "வெள்ளை ஈக்களைக் கட்டுப்படுத்த டயாபென்தியூரான் 50% WP (1.2 கிராம்/லிட்டர்) அல்லது புளோனிகாமிட் தெளிக்கவும்.",
                "prevention": "வரப்புகளில் உள்ள களைகளை அகற்றவும், நோய் எதிர்ப்பு ரகங்களை பயிரிடவும், அளவுக்கு அதிகமாக தழைச்சத்து இடுவதை தவிர்க்கவும்.",
                "voice_summary": "பருத்தியில் இலை சுருள் நோய் பரப்பும் வெள்ளை ஈக்களை கட்டுப்படுத்த மஞ்சள் ஒட்டும் பொறிகள் வைக்கவும், வேப்பங்கொட்டை சாறு தெளிக்கவும்."
            },
            "mr": {
                "crop": "कापूस",
                "condition": "कापसावरील पाने आकसणे / चुरडा-मुरडा (लीफ कर्ल व्हायरस)",
                "severity": "जास्त (High)",
                "organic_remedy": "पांढरी माशी नियंत्रणासाठी ५% निंबोळी अर्क किंवा बिव्हेरिया बॅसियाना फवारा. एकरी १५-२० पिवळे चिकट सापळे लावा.",
                "chemical_remedy": "पांढऱ्या माशीसाठी डायफेंथियुरॉन ५०% WP (१.२ ग्रॅम/लिटर) किंवा फ्लोनिकामाइड फवारा. विषाणूवर थेट रासायनिक औषध नसते.",
                "prevention": "बांधावरील तण नष्ट करा, कीड प्रतिकारक वाणांची निवड करा आणि नत्र खतांचा अतिवापर टाळा.",
                "voice_summary": "शेतकरी मित्रांनो, कापसावर चुरडा-मुरडा रोग पांढऱ्या माशीमुळे पसरत आहे. पिवळे सापळे लावा आणि निंबोळी अर्क किंवा कीटकनाशकाची फवारणी करा."
            }
        }
    },

    "rice_blast": {
        "id": "rice_blast",
        "crop": "Rice (Paddy)",
        "condition": "Rice Blast (Magnaporthe oryzae)",
        "confidence": 0.96,
        "severity": "Critical",
        "symptoms": "Spindle-shaped elliptical lesions with gray or white centers and brown-reddish margins on leaf blades and neck nodes.",
        "organic_remedy": "Seed treatment and foliar spray with Pseudomonas fluorescens (10g/L or 2.5kg/ha). Apply 20% cow dung slurry supernatant with neem extract.",
        "chemical_remedy": "Immediate spray of Tricyclazole 75% WP (0.6 g/L) or Isoprothiolane 40% EC (1.5 mL/L) upon early symptom detection.",
        "prevention": "Avoid split application of nitrogen in excess, maintain balanced potassium nutrition, flood field to suppress airborne conidia.",
        "translations": {
            "hi": {
                "crop": "धान (चावल)",
                "condition": "धान का झोंका रोग (राइस ब्लास्ट)",
                "severity": "गंभीर (Critical)",
                "organic_remedy": "स्यूडोमोनास फ्लोरोसेंस (10 ग्राम/लीटर) से बीज उपचार और छिड़काव करें। 20% ताजे गोबर के घोल का निथरा पानी छिड़कें।",
                "chemical_remedy": "लक्षण दिखते ही ट्राइसाइक्लाजोल 75% WP (0.6 ग्राम/लीटर) या आइसोप्रोपियोलेन का तुरंत छिड़काव करें।",
                "prevention": "यूरिया का अधिक प्रयोग बंद करें, पोटाश की संतुलित मात्रा दें, और प्रमाणित उपचारित बीजों का ही उपयोग करें।",
                "voice_summary": "किसान भाई, धान में झोंका रोग से भारी नुकसान हो सकता है। तुरंत यूरिया बंद करें और ट्राइसाइक्लाजोल या स्यूडोमोनास का छिड़काव करें।"
            },
            "ta": {
                "crop": "நெல்",
                "condition": "நெல் குலை நோய் (Rice Blast)",
                "severity": "மிக தீவிரம் (Critical)",
                "organic_remedy": "சூடோமோனாஸ் புளோரசன்ஸ் (10 கிராம்/லிட்டர்) கொண்டு தெளிக்கவும் மற்றும் விதை நேர்த்தி செய்யவும். வேப்பம் சாறு கலவை பயன்படுத்தவும்.",
                "chemical_remedy": "டிரைசைக்ளோசோல் 75% WP (0.6 கிராம்/லிட்டர்) அல்லது ஐசோப்ரோதியோலேன் 40% EC உடனே தெளிக்கவும்.",
                "prevention": "அதிகப்படியான தழைச்சத்து இடுவதை தவிர்க்கவும், பொட்டாஷ் உரம் சரியாக இடவும், வயலில் நீர் அளவை சீராக வைக்கவும்.",
                "voice_summary": "நெல்லில் குலை நோய் தாக்கம் தீவிரமாக உள்ளது. உடனடியாக டிரைசைக்ளோசோல் பூஞ்சாணக்கொல்லி தெளித்து தழைச்சத்து இடுவதை நிறுத்துங்கள்."
            },
            "mr": {
                "crop": "भात (धान)",
                "condition": "भातावरील करपा / ब्लास्ट रोग",
                "severity": "अत्यंत गंभीर (Critical)",
                "organic_remedy": "स्यूडोमोनास फ्लोरोसन्स (१० ग्रॅम/लिटर) फवारा व बीजप्रक्रिया करा. गोमूत्र आणि निंबोळी अर्काचा वापर फायदेशीर ठरतो.",
                "chemical_remedy": "रोग दिसताच ट्रायसायक्लॅझोल ७५% WP (०.६ ग्रॅम/लिटर) किंवा आयसोप्रोथिओलेन फवारा.",
                "prevention": "युरियाचा अतिरिक्त वापर पूर्णपणे थांबवा, पोटॅश खताचा समतोल ठेवा आणि शेतात योग्य पाणी पातळी ठेवा.",
                "voice_summary": "शेतकरी बांधवांनो, भातावर ब्लास्ट करपा रोगाचा गंभीर प्रादुर्भाव आहे. ताबडतोब युरिया बंद करा आणि ट्रायसायक्लॅझोलची फवारणी करा."
            }
        }
    },

    "potato_late_blight": {
        "id": "potato_late_blight",
        "crop": "Potato",
        "condition": "Potato Late Blight (Phytophthora infestans)",
        "confidence": 0.95,
        "severity": "Critical",
        "symptoms": "Water-soaked irregular black/dark lesions on leaf margins turning necrotic, white cottony mildew under humid conditions.",
        "organic_remedy": "Prophylactic spray of Copper Oxychloride 50% WP (3.0 g/L) or Bordeaux Mixture (1%). Uproot and burn diseased plants.",
        "chemical_remedy": "Curative spray of Cymoxanil 8% + Mancozeb 64% WP (2.0 g/L) or Dimethomorph 50% WP (1.0 g/L) alternating with Fenamidone.",
        "prevention": "Plant certified disease-free certified tubers, avoid sprinkler/overhead irrigation, hill up soil firmly around stems to protect tubers.",
        "translations": {
            "hi": {
                "crop": "आलू",
                "condition": "आलू का पछेती झुलसा रोग (लेट ब्लाइट)",
                "severity": "गंभीर (Critical)",
                "organic_remedy": "कॉपर ऑक्सीक्लोराइड (3 ग्राम/लीटर) या बोर्डो मिश्रण (1%) का छिड़काव करें। गंभीर रूप से प्रभावित पौधों को जला दें।",
                "chemical_remedy": "साइमोक्सानिल 8% + मैंकोज़ेब 64% WP (2 ग्राम/लीटर) या डाइमॅथोमोर्फ का छिड़काव करें।",
                "prevention": "रोगमुक्त प्रमाणित बीजों का ही उपयोग करें, फव्वारा सिंचाई से बचें, और कंदों पर अच्छी तरह मिट्टी चढ़ाएं।",
                "voice_summary": "किसान भाई, आलू में पछेती झुलसा तेजी से फैलता है। तुरंत साइमोक्सानिल या कॉपर ऑक्सीक्लोराइड का सुरक्षात्मक छिड़काव करें।"
            },
            "ta": {
                "crop": "உருளைக்கிழங்கு",
                "condition": "உருளைக்கிழங்கு பின் பருவ கருகல் நோய் (Late Blight)",
                "severity": "மிக தீவிரம் (Critical)",
                "organic_remedy": "காப்பர் ஆக்ஸிகுளோரைடு (3 கிராம்/லிட்டர்) அல்லது போர்டோ கலவை (1%) தெளிக்கவும். நோய் தாக்கிய செடிகளை அகற்றவும்.",
                "chemical_remedy": "சைமோக்சானில் + மேன்கோசெப் கலவை (2 கிராம்/லிட்டர்) அல்லது டைமெத்தோமார்ப் தெளிக்கவும்.",
                "prevention": "சான்றளிக்கப்பட்ட விதைக்கிழங்குகளை நடவு செய்யவும், இலைகள் நனையாமல் பார்த்துக்கொள்ளவும், மண் அணைக்கவும்.",
                "voice_summary": "உருளைக்கிழங்கில் பின் பருவ கருகல் நோய் வேகமாக பரவக்கூடும். உடனே சைமோக்சானில் அல்லது காப்பர் ஆக்ஸிகுளோரைடு தெளிக்கவும்."
            },
            "mr": {
                "crop": "बटाटा",
                "condition": "बटाट्यावरील उशिरा येणारा करपा (लेट ब्लाइट)",
                "severity": "अत्यंत गंभीर (Critical)",
                "organic_remedy": "कॉपर ऑक्सिक्लोराईड (३ ग्रॅम/लिटर) किंवा बोर्डो मिश्रण (१%) फवारा. जास्त प्रादुर्भाव झालेली झाडे उपटून नष्ट करा.",
                "chemical_remedy": "सायमॉक्सॅनिल ८% + मँकोझेब ६४% WP (२ ग्रॅम/लिटर) किंवा डायमेथोमॉर्फ फवारा.",
                "prevention": "प्रमाणित निरोगी बेणे वापरा, तुषार सिंचन टाळा आणि बटाट्याच्या गड्ड्यांना मातीची चांगली भर लावा.",
                "voice_summary": "शेतकरी मित्रांनो, बटाट्यावर लेट ब्लाइटचा मोठा धोका आहे. त्वरित सायमॉक्सॅनिल किंवा कॉपर ऑक्सिक्लोराईडची फवारणी करा."
            }
        }
    },

    "spinach_downy_mildew": {
        "id": "spinach_downy_mildew",
        "crop": "Spinach (Palak)",
        "condition": "Spinach Downy Mildew (Peronospora effusa)",
        "confidence": 0.94,
        "severity": "Moderate",
        "symptoms": "Yellowish chlorotic lesions on upper leaf surface, purplish-gray fuzzy mildew on underside.",
        "organic_remedy": "Spray cold-pressed neem oil (0.5%) or Trichoderma harzianum (5g/L). Promptly remove and discard infected leaves.",
        "chemical_remedy": "Foliar spray of Metalaxyl 8% + Mancozeb 64% WP (2.0 g/L) or Copper Oxychloride 50% WP (2.5 g/L).",
        "prevention": "Adopt wider row spacing (25x15 cm) for aeration, use drip irrigation to prevent foliar wetness, rotate crops.",
        "translations": {
            "hi": {
                "crop": "पालक",
                "condition": "पालक का मृदुरोमिल फफूंदी रोग (डाउनी मिल्ड्यू)",
                "severity": "मध्यम (Moderate)",
                "organic_remedy": "नीम का तेल (0.5%) या ट्राइकोडर्मा (5 ग्राम/लीटर) का छिड़काव करें। खराब पत्तियों को हटा दें।",
                "chemical_remedy": "मेटालेक्सिल + मैंकोज़ेब (2 ग्राम/लीटर) या कॉपर ऑक्सीक्लोराइड (2.5 ग्राम/लीटर) का छिड़काव करें।",
                "prevention": "पौधों के बीच पर्याप्त दूरी रखें और पत्तियों पर सीधे पानी देने से बचें।",
                "voice_summary": "किसान भाई, पालक की फसल में डाउनी मिल्ड्यू फफूंद के लक्षण हैं। नीम तेल या मेटालेक्सिल का छिड़काव करें।"
            },
            "ta": {
                "crop": "கீரை",
                "condition": "கீரை கீழ்நோக்கு சாம்பல் நோய் (Downy Mildew)",
                "severity": "நடுத்தர தீவிரம் (Moderate)",
                "organic_remedy": "வேப்பெண்ணெய் கரைசல் (0.5%) அல்லது டிரைகோடெர்மா (5 கிராம்/லிட்டர்) தெளிக்கவும். பாதிக்கப்பட்ட இலைகளை அகற்றவும்.",
                "chemical_remedy": "மெட்டாலாக்சில் + மேன்கோசெப் (2 கிராம்/லிட்டர்) அல்லது காப்பர் ஆக்ஸிகுளோரைடு (2.5 கிராம்/லிட்டர்) தெளிக்கவும்.",
                "prevention": "செடிகளுக்கிடையே போதிய இடைவெளி விடவும், இலைகளில் தண்ணீர் தேங்காமல் சொட்டுநீர் பாசனம் அமைக்கவும்.",
                "voice_summary": "கீரையில் சாம்பல் நோய் தாக்கம் தெரிகிறது. வேப்பெண்ணெய் அல்லது மெட்டாலாக்சில் மருந்தை உடனே தெளிக்கவும்."
            },
            "mr": {
                "crop": "पालक",
                "condition": "पालकावरील केवडा / डाउनी मिल्ड्यू रोग",
                "severity": "मध्यम (Moderate)",
                "organic_remedy": "निंबोळी तेल (०.५%) किंवा ट्रायकोडर्मा (५ ग्रॅम/लिटर) फवारा. रोगट पाने तोडून टाका.",
                "chemical_remedy": "मेटालॅक्सिल + मँकोझेब (२ ग्रॅम/लिटर) किंवा कॉपर ऑक्सिक्लोराईड फवारा.",
                "prevention": "रोपांमध्ये योग्य अंतर ठेवा आणि पानांवर पाणी साचू देऊ नका.",
                "voice_summary": "शेतकरी मित्रांनो, पालकावर केवडा रोगाचा प्रादुर्भाव आहे. निंबोळी तेल किंवा मेटालॅक्सिलची फवारणी करा."
            }
        }
    },

    "sugarcane_red_rot": {
        "id": "sugarcane_red_rot",
        "crop": "Sugarcane",
        "condition": "Sugarcane Red Rot (Colletotrichum falcatum)",
        "confidence": 0.93,
        "severity": "High",
        "symptoms": "Yellowing and withering of third and fourth crown leaves, internal red discoloration with white cross-patches inside stalks.",
        "organic_remedy": "Apply Trichoderma viride enriched farmyard manure (2.5 kg/ha). Treat setts in aerated steam at 52°C for 30 minutes.",
        "chemical_remedy": "Dip seed setts in Carbendazim 50% WP (1.0 g/L) solution for 15 minutes before furrow placement.",
        "prevention": "Plant certified red-rot resistant varieties (Co 0238, Co 86032), avoid ratoon in infected plots, practice crop rotation with paddy.",
        "translations": {
            "hi": {
                "crop": "गन्ना",
                "condition": "गन्ने का लाल सड़न रोग (रेड रॉट)",
                "severity": "उच्च (High)",
                "organic_remedy": "ट्राइकोडर्मा विरिडी युक्त जैविक खाद डालें और बीज गन्नों का भाप उपचार करें।",
                "chemical_remedy": "बुवाई से पहले गन्ने के टुकड़ों को कार्बेन्डाजिम (1 ग्राम/लीटर) के घोल में 15 मिनट डुबोएं।",
                "prevention": "रोगरोधी किस्में (Co 86032) लगाएं और रोगग्रस्त खेत में पेड़ी गन्ना न लें।",
                "voice_summary": "किसान भाई, गन्ने में लाल सड़न रोग से बचाव के लिए कार्बेन्डाजिम से बीज उपचार करें और रोगरोधी किस्में लगाएं।"
            },
            "ta": {
                "crop": "கரும்பு",
                "condition": "கரும்பு செவ்வழுகல் நோய் (Red Rot)",
                "severity": "அதிகம் (High)",
                "organic_remedy": "டிரைகோடெர்மா விரிடி கலந்த தொழுவுரம் இடவும். விதை கரணைகளை நீராவி முறையில் நேர்த்தி செய்யவும்.",
                "chemical_remedy": "கார்பென்டாசிம் 50% WP (1 கிராம்/லிட்டர்) கரைசலில் கரணைகளை 15 நிமிடங்கள் ஊறவைத்து நடவு செய்யவும்.",
                "prevention": "நோய் எதிர்ப்பு ரகங்களான Co 86032 பயிரிடவும், பாதிக்கப்பட்ட வயலில் மறுதாம்பு பயிர் செய்வதை தவிர்க்கவும்.",
                "voice_summary": "கரும்பில் செவ்வழுகல் நோய் தாக்கத்தை கட்டுப்படுத்த கரணைகளை கார்பென்டாசிம் மருந்தால் நேர்த்தி செய்து நடவு செய்யவும்."
            },
            "mr": {
                "crop": "ऊस",
                "condition": "उसावरील तांबडे कूज रोग (रेड रॉट)",
                "severity": "जास्त (High)",
                "organic_remedy": "ट्रायकोडर्मा व्हिरिडी मिसळलेले शेणखत वापरा. बेणे प्रक्रिया करा.",
                "chemical_remedy": "लागवडीपूर्वी कार्बेन्डाझिम (१ ग्रॅम/लिटर) द्रावणात बेणे १५ मिनिटे बुडवा.",
                "prevention": "रोगप्रतिकारक वाण (Co 86032) वापरा आणि रोगट शेतात खोडवा घेऊ नका.",
                "voice_summary": "शेतकरी बांधवांनो, उसावरील तांबडे कूज रोगासाठी कार्बेन्डाझिमने बेणे प्रक्रिया करा आणि निरोगी बेणे वापरा."
            }
        }
    },

    "banana_panama_wilt": {
        "id": "banana_panama_wilt",
        "crop": "Banana",
        "condition": "Banana Panama Wilt (Fusarium oxysporum f. sp. cubense)",
        "confidence": 0.92,
        "severity": "Critical",
        "symptoms": "Yellowing of lower leaves along margins, petiole collapse, vertical pseudostem splitting, vascular discolouration.",
        "organic_remedy": "Apply Pseudomonas fluorescens (25g/plant) mixed with 500g neem cake in the root basin at 2-month intervals.",
        "chemical_remedy": "Corm injection or soil drenching around basin with Carbendazim 0.2% (2.0 g/L).",
        "prevention": "Plant certified tissue culture plantlets, adjust acidic soils with agricultural lime to pH 6.5-7.0, avoid flood irrigation.",
        "translations": {
            "hi": {
                "crop": "केला",
                "condition": "केले का पनामा विल्ट रोग (उकठा)",
                "severity": "गंभीर (Critical)",
                "organic_remedy": "स्यूडोमोनास फ्लोरोसेंस (25 ग्राम/पौधा) नीम की खली के साथ जड़ों में डालें।",
                "chemical_remedy": "कार्बेन्डाजिम (2 ग्राम/लीटर) के घोल से तने के पास मिट्टी की ड्रेन्चिंग करें।",
                "prevention": "रोगमुक्त टिशू कल्चर पौधे लगाएं और खेत में पानी का जमाव न होने दें।",
                "voice_summary": "किसान भाई, केले में पनामा विल्ट की रोकथाम हेतु कार्बेन्डाजिम या स्यूडोमोनास का तने के पास छिड़काव करें।"
            },
            "ta": {
                "crop": "வாழை",
                "condition": "வாழை பனாமா வாடல் நோய் (Panama Wilt)",
                "severity": "மிக தீவிரம் (Critical)",
                "organic_remedy": "சூடோமோனாஸ் புளோரசன்ஸ் (25 கிராம்/மரம்) மற்றும் வேப்பம்பிண்ணாக்கு வேர்ப்பகுதியில் இடவும்.",
                "chemical_remedy": "கார்பென்டாசிம் 0.2% (2 கிராம்/லிட்டர்) கரைசலை மரத்தின் தூர்ப்பகுதியில் ஊற்றவும்.",
                "prevention": "சான்றளிக்கப்பட்ட திசு வளர்ப்பு கன்றுகளை நடவு செய்யவும், நிலத்தில் நீர் தேங்குவதை தவிர்க்கவும்.",
                "voice_summary": "வாழையில் பனாமா வாடல் நோய் தென்பட்டால் கார்பென்டாசிம் கரைசலை மரத்தின் வேர்ப்பகுதியில் உடனடியாக ஊற்றவும்."
            },
            "mr": {
                "crop": "केळी",
                "condition": "केळीवरील पनामा मर रोग (विल्ट)",
                "severity": "अत्यंत गंभीर (Critical)",
                "organic_remedy": "स्यूडोमोनास फ्लोरोसन्स (२५ ग्रॅम/झाड) निंबोळी पेंडीसोबत मुळांच्या भागात टाका.",
                "chemical_remedy": "कार्बेन्डाझिम (२ ग्रॅम/लिटर) द्रावणाने झाडाच्या बुंध्याजवळ आळवणी करा.",
                "prevention": "निरोगी टिशू कल्चर रोपांची लागवड करा आणि शेतात पाणी साचू देऊ नका.",
                "voice_summary": "शेतकरी मित्रांनो, केळीवरील पनामा रोगासाठी कार्बेन्डाझिम द्रावणाची झाडाच्या मुळाशी आळवणी करा."
            }
        }
    },

    "groundnut_tikka": {
        "id": "groundnut_tikka",
        "crop": "Groundnut (Peanut)",
        "condition": "Groundnut Tikka Leaf Spot (Cercospora personata)",
        "confidence": 0.94,
        "severity": "Moderate",
        "symptoms": "Dark brown to black necrotic spots with prominent bright yellow halo on upper leaf surfaces.",
        "organic_remedy": "Foliar spray of 5% Neem Seed Kernel Extract (NSKE) or Panchagavya 3% at 10-12 day intervals.",
        "chemical_remedy": "Foliar spray of Chlorothalonil 75% WP (2.0 g/L) or Hexaconazole 5% EC (2.0 mL/L).",
        "prevention": "Seed treatment with Trichoderma viride (4g/kg seed), practice crop rotation, burn infected crop residue.",
        "translations": {
            "hi": {
                "crop": "मूंगफली",
                "condition": "मूंगफली का टिक्का रोग (लीफ स्पॉट)",
                "severity": "मध्यम (Moderate)",
                "organic_remedy": "5% नीम बीज अर्क (NSKE) या पंचगव्य (3%) का 10 दिनों के अंतराल पर छिड़काव करें।",
                "chemical_remedy": "क्लोरोथैलोनिल (2 ग्राम/लीटर) या हेक्साकोनाज़ोल (2 मिली/लीटर) का छिड़काव करें।",
                "prevention": "ट्राइकोडर्मा से बीज उपचार करें और फसल चक्र अपनाएं।",
                "voice_summary": "किसान साथी, मूंगफली में टिक्का रोग के धब्बे दिखने पर हेक्साकोनाज़ोल या नीम अर्क का छिड़काव करें।"
            },
            "ta": {
                "crop": "வேர்க்கடலை",
                "condition": "வேர்க்கடலை டிக்கா இலைப்புள்ளி நோய் (Tikka Disease)",
                "severity": "நடுத்தர தீவிரம் (Moderate)",
                "organic_remedy": "5% வேப்பங்கொட்டை சாறு அல்லது பஞ்சகவ்யா 3% தெளிக்கவும்.",
                "chemical_remedy": "குளோரோதலோனில் (2 கிராம்/லிட்டர்) அல்லது ஹெக்ஸாகோனசோல் (2 மி.லி/லிட்டர்) தெளிக்கவும்.",
                "prevention": "டிரைகோடெர்மா கொண்டு விதை நேர்த்தி செய்யவும், பயிர் சுழற்சி முறையைக் கடைப்பிடிக்கவும்.",
                "voice_summary": "வேர்க்கடலையில் டிக்கா இலைப்புள்ளி நோயைக் கட்டுப்படுத்த ஹெக்ஸாகோனசோல் அல்லது வேப்பங்கொட்டை சாறு தெளிக்கவும்."
            },
            "mr": {
                "crop": "भुईमूग",
                "condition": "भुईमुगावरील टिक्का रोग (पानावरील ठिपके)",
                "severity": "मध्यम (Moderate)",
                "organic_remedy": "५% निंबोळी अर्क किंवा पंचगव्य ३% फवारा.",
                "chemical_remedy": "क्लोरोथॅलोनिल (२ ग्रॅम/लिटर) किंवा हेक्साकोनॅझोल (२ मिली/लिटर) फवारा.",
                "prevention": "ट्रायकोडर्माने बीजप्रक्रिया करा आणि पिकांची फेरपालट करा.",
                "voice_summary": "शेतकरी बांधवांनो, भुईमुगावरील टिक्का रोगासाठी हेक्साकोनॅझोल किंवा निंबोळी अर्काची फवारणी करा."
            }
        }
    },

    "cotton_bollworm": {
        "id": "cotton_bollworm",
        "crop": "Cotton",
        "condition": "Cotton Bollworm Infestation (Helicoverpa armigera / Pink Bollworm)",
        "confidence": 0.93,
        "severity": "High",
        "symptoms": "Bored holes in flower buds and bolls plugged with larval excrement, rosette flowers, boll drop.",
        "organic_remedy": "Install 6-8 pheromone traps per acre. Spray Bacillus thuringiensis (Bt) @ 2g/L or 5% NSKE.",
        "chemical_remedy": "Foliar spray of Emamectin Benzoate 5% SG (0.5 g/L) or Spinosad 45% SC (0.3 mL/L).",
        "prevention": "Destroy crop stalks immediately after last picking, avoid ratoon cotton, plant marigold / castor trap crops.",
        "translations": {
            "hi": {
                "crop": "कपास",
                "condition": "कपास की बॉलवर्म / गुलाबी सुंडी कीट",
                "severity": "उच्च (High)",
                "organic_remedy": "प्रति एकड़ 6-8 फेरोमोन ट्रैप लगाएं। बीटी (2 ग्राम/लीटर) या नीम अर्क का छिड़काव करें।",
                "chemical_remedy": "इमामेक्टिन बेंजोएट 5% SG (0.5 ग्राम/लीटर) या स्पिनोसैड का छिड़काव करें।",
                "prevention": "फसल कटाई के बाद डंठल नष्ट करें और ट्रैप फसलें लगाएं।",
                "voice_summary": "किसान भाई, कपास में बॉलवर्म सुंडी को रोकने के लिए फेरोमोन ट्रैप लगाएं और इमामेक्टिन बेंजोएट का छिड़काव करें।"
            },
            "ta": {
                "crop": "பருத்தி",
                "condition": "பருத்தி காய்ப்புழு தாக்குதல் (Bollworm Infestation)",
                "severity": "அதிகம் (High)",
                "organic_remedy": "ஏக்கருக்கு 6-8 இனக்கவர்ச்சி பொறிகளை அமைக்கவும். பேசிலஸ் துரிஞ்சியென்சிஸ் (Bt) அல்லது வேப்பங்கொட்டை சாறு தெளிக்கவும்.",
                "chemical_remedy": "எமாமெக்டின் பென்சோயேட் 5% SG (0.5 கிராம்/லிட்டர்) அல்லது ஸ்பைனோசாட் தெளிக்கவும்.",
                "prevention": "அறுவடைக்கு பின் பருத்தி செடிகளை அழிக்கவும், வரப்புகளில் செண்டுமல்லி கவர்ச்சி பயிர் நடவும்.",
                "voice_summary": "பருத்தியில் காய்ப்புழு தாக்குதலை கட்டுப்படுத்த இனக்கவர்ச்சி பொறிகள் வைத்து எமாமெக்டின் மருந்து தெளிக்கவும்."
            },
            "mr": {
                "crop": "कापूस",
                "condition": "कापसावरील बोंडअळीचा प्रादुर्भाव (पिंक / अमेरिकन)",
                "severity": "जास्त (High)",
                "organic_remedy": "एकरी ६-८ कामगंध सापळे लावा. बीटी किंवा ५% निंबोळी अर्क फवारा.",
                "chemical_remedy": "इमामेक्टिन बेंझोएट ५% SG (०.५ ग्रॅम/लिटर) किंवा स्पिनोसॅड फवारा.",
                "prevention": "वेचणीनंतर शेतातील पराट्या नष्ट करा आणि खोडवा घेऊ नका.",
                "voice_summary": "शेतकरी मित्रांनो, बोंडअळीच्या नियंत्रणासाठी कामगंध सापळे लावा आणि इमामेक्टिन बेंझोएट फवारा."
            }
        }
    },

    "tomato_leaf_curl": {
        "id": "tomato_leaf_curl",
        "crop": "Tomato",
        "condition": "Tomato Leaf Curl Virus (ToLCV)",
        "confidence": 0.95,
        "severity": "High",
        "symptoms": "Upward curling and crinkling of leaves, thick leathery texture, yellow margins, stunted bushy plants.",
        "organic_remedy": "Install yellow sticky traps (15-20 traps/acre). Spray 5% Neem Seed Kernel Extract (NSKE) to control whiteflies.",
        "chemical_remedy": "Spray Diafenthiuron 50% WP (1.2 g/L) or Imidacloprid 17.8% SL (0.5 mL/L) to suppress whitefly vectors.",
        "prevention": "Remove solanaceous weeds around fields, use reflective silver mulching sheets, plant maize border barrier rows.",
        "translations": {
            "hi": {
                "crop": "टमाटर",
                "condition": "टमाटर का पर्ण कुंचन रोग (पत्ता मरोड़ वायरस)",
                "severity": "उच्च (High)",
                "organic_remedy": "पीले स्टिकी ट्रैप (15/एकड़) लगाएं और सफेद मक्खी रोकने के लिए नीम अर्क (NSKE) का छिड़काव करें।",
                "chemical_remedy": "डायफेंथियूरॉन (1.2 ग्राम/लीटर) या इमिडाक्लोप्रिड का छिड़काव करें।",
                "prevention": "खेत के पास से खरपतवार नष्ट करें और सिल्वर मल्चिंग शीट अपनाएं।",
                "voice_summary": "किसान साथी, टमाटर में पत्ता मरोड़ सफेद मक्खी से फैलता है। पीले चिपचिपे ट्रैप लगाएं और इमिडाक्लोप्रिड का छिड़काव करें।"
            },
            "ta": {
                "crop": "தக்காளி",
                "condition": "தக்காளி இலைச்சுருள் நச்சுயிரி நோய் (Tomato Leaf Curl)",
                "severity": "அதிகம் (High)",
                "organic_remedy": "ஏக்கருக்கு 15 மஞ்சள் ஒட்டும் பொறிகளை வைக்கவும். வெள்ளை ஈக்களை கட்டுப்படுத்த 5% வேப்பங்கொட்டை சாறு தெளிக்கவும்.",
                "chemical_remedy": "டயாபென்தியூரான் 50% WP (1.2 கிராம்/லிட்டர்) அல்லது இமிடாக்குளோப்ரிட் தெளிக்கவும்.",
                "prevention": "வரப்புகளில் உள்ள களைகளை அகற்றவும், வெள்ளி நிற மூடாக்கு தாள்களைப் பயன்படுத்தவும்.",
                "voice_summary": "தக்காளியில் இலைச்சுருள் நோய் பரப்பும் வெள்ளை ஈக்களை கட்டுப்படுத்த மஞ்சள் பொறிகள் வைத்து டயாபென்தியூரான் தெளிக்கவும்."
            },
            "mr": {
                "crop": "टोमॅटो",
                "condition": "टोमॅटोवरील पाने आकसणे (लीफ कर्ल व्हायरस)",
                "severity": "जास्त (High)",
                "organic_remedy": "एकरी १५ पिवळे चिकट सापळे लावा आणि पांढऱ्या माशीसाठी निंबोळी अर्क फवारा.",
                "chemical_remedy": "डायफेंथियुरॉन (१.२ ग्रॅम/लिटर) किंवा इमिडाक्लोप्रिड फवारा.",
                "prevention": "बांधावरील तण नष्ट करा आणि सिल्व्हर मल्चिंग पेपरचा वापर करा.",
                "voice_summary": "शेतकरी बांधवांनो, टोमॅटोवरील लीफ कर्लसाठी पिवळे सापळे लावा आणि कीटकनाशकाची फवारणी करा."
            }
        }
    }
}


def get_sample_disease(disease_key: str) -> Optional[Dict[str, Any]]:
    """Retrieve sample disease data by key with case-insensitive fallback."""
    if not disease_key:
        return None
    normalized_key = disease_key.strip().lower().replace(" ", "_").replace("-", "_")
    return FALLBACK_DISEASES.get(normalized_key)


def get_all_sample_diseases() -> Dict[str, Dict[str, Any]]:
    """Return all fallback disease records."""
    return FALLBACK_DISEASES


def get_localized_advisory(disease_key: str, lang: str = "en") -> Dict[str, str]:
    """
    Format advisory text based on specified language code ('en', 'hi', 'ta', 'mr').
    Ensures safe fallback to English if the translation is missing.
    """
    data = get_sample_disease(disease_key)
    if not data:
        return {
            "crop": "Unknown Crop",
            "condition": "Unknown Condition",
            "severity": "Moderate",
            "organic_remedy": "Consult local Krishi Vigyan Kendra (KVK).",
            "chemical_remedy": "Consult an agricultural extension officer.",
            "prevention": "Practice clean cultivation and sanitation.",
            "voice_summary": "Condition could not be determined. Please consult local agronomists."
        }

    lang = lang.lower().strip()
    if lang in ["hi", "ta", "mr"] and lang in data["translations"]:
        trans = data["translations"][lang]
        return {
            "crop": trans.get("crop", data["crop"]),
            "condition": trans.get("condition", data["condition"]),
            "severity": trans.get("severity", data["severity"]),
            "organic_remedy": trans.get("organic_remedy", data["organic_remedy"]),
            "chemical_remedy": trans.get("chemical_remedy", data["chemical_remedy"]),
            "prevention": trans.get("prevention", data["prevention"]),
            "voice_summary": trans.get("voice_summary", f"{data['condition']} detected on {data['crop']}.")
        }

    # Default to English
    return {
        "crop": data["crop"],
        "condition": data["condition"],
        "severity": data["severity"],
        "organic_remedy": data["organic_remedy"],
        "chemical_remedy": data["chemical_remedy"],
        "prevention": data["prevention"],
        "voice_summary": f"Detected {data['condition']} on {data['crop']} with {int(data['confidence']*100)}% confidence. Severity is {data['severity']}."
    }
