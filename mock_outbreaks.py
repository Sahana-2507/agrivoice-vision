"""
AgriVoice Vision - Tamil Nadu Crop Disease Incident Surveillance Telemetry
==========================================================================
Synthesized surveillance telemetry representing field logs reported by
farmers and Krishi Vigyan Kendras (KVK) across key agricultural districts
in Tamil Nadu for SIH26131 outbreak analytics and early warning systems.
"""

from datetime import datetime, timedelta
import pandas as pd
import streamlit as st

# Comprehensive list of recent crop disease outbreak logs across Tamil Nadu agricultural districts
RAW_INCIDENTS = [
    {
        "District": "Thanjavur",
        "Crop": "Paddy (Rice)",
        "Disease": "Rice Blast (Magnaporthe oryzae)",
        "Severity": "Critical",
        "ReportedDate": "2026-09-27",
        "AffectedAreaAcres": 340,
        "Status": "Alert Active",
        "Latitude": 10.7870,
        "Longitude": 79.1378
    },
    {
        "District": "Thanjavur",
        "Crop": "Paddy (Rice)",
        "Disease": "Bacterial Leaf Blight",
        "Severity": "High",
        "ReportedDate": "2026-09-25",
        "AffectedAreaAcres": 210,
        "Status": "Spreading",
        "Latitude": 10.8200,
        "Longitude": 79.1800
    },
    {
        "District": "Coimbatore",
        "Crop": "Cotton",
        "Disease": "Bollworm Infestation (Helicoverpa)",
        "Severity": "High",
        "ReportedDate": "2026-09-26",
        "AffectedAreaAcres": 185,
        "Status": "Alert Active",
        "Latitude": 11.0168,
        "Longitude": 76.9558
    },
    {
        "District": "Coimbatore",
        "Crop": "Tomato",
        "Disease": "Tomato Leaf Curl",
        "Severity": "Moderate",
        "ReportedDate": "2026-09-24",
        "AffectedAreaAcres": 95,
        "Status": "Under Containment",
        "Latitude": 11.0800,
        "Longitude": 76.9200
    },
    {
        "District": "Madurai",
        "Crop": "Banana",
        "Disease": "Panama Wilt (Fusarium)",
        "Severity": "Critical",
        "ReportedDate": "2026-09-28",
        "AffectedAreaAcres": 230,
        "Status": "Alert Active",
        "Latitude": 9.9252,
        "Longitude": 78.1198
    },
    {
        "District": "Madurai",
        "Crop": "Spinach",
        "Disease": "Downy Mildew",
        "Severity": "Low",
        "ReportedDate": "2026-09-23",
        "AffectedAreaAcres": 45,
        "Status": "Controlled",
        "Latitude": 9.9800,
        "Longitude": 78.1500
    },
    {
        "District": "Salem",
        "Crop": "Sugarcane",
        "Disease": "Sugarcane Red Rot",
        "Severity": "High",
        "ReportedDate": "2026-09-27",
        "AffectedAreaAcres": 290,
        "Status": "Spreading",
        "Latitude": 11.6643,
        "Longitude": 78.1460
    },
    {
        "District": "Salem",
        "Crop": "Groundnut",
        "Disease": "Tikka Leaf Spot",
        "Severity": "Moderate",
        "ReportedDate": "2026-09-22",
        "AffectedAreaAcres": 120,
        "Status": "Controlled",
        "Latitude": 11.5900,
        "Longitude": 78.2000
    },
    {
        "District": "Tiruchirappalli",
        "Crop": "Paddy (Rice)",
        "Disease": "Rice Blast",
        "Severity": "High",
        "ReportedDate": "2026-09-26",
        "AffectedAreaAcres": 195,
        "Status": "Alert Active",
        "Latitude": 10.7905,
        "Longitude": 78.7047
    },
    {
        "District": "Tiruchirappalli",
        "Crop": "Banana",
        "Disease": "Panama Wilt",
        "Severity": "Moderate",
        "ReportedDate": "2026-09-25",
        "AffectedAreaAcres": 110,
        "Status": "Under Containment",
        "Latitude": 10.8500,
        "Longitude": 78.6800
    },
    {
        "District": "Dindigul",
        "Crop": "Tomato",
        "Disease": "Tomato Early Blight",
        "Severity": "High",
        "ReportedDate": "2026-09-27",
        "AffectedAreaAcres": 160,
        "Status": "Alert Active",
        "Latitude": 10.3673,
        "Longitude": 77.9803
    },
    {
        "District": "Dindigul",
        "Crop": "Spinach",
        "Disease": "Downy Mildew",
        "Severity": "Moderate",
        "ReportedDate": "2026-09-24",
        "AffectedAreaAcres": 70,
        "Status": "Controlled",
        "Latitude": 10.4200,
        "Longitude": 78.0100
    },
    {
        "District": "Erode",
        "Crop": "Sugarcane",
        "Disease": "Sugarcane Red Rot",
        "Severity": "Critical",
        "ReportedDate": "2026-09-28",
        "AffectedAreaAcres": 310,
        "Status": "Spreading",
        "Latitude": 11.3410,
        "Longitude": 77.7172
    },
    {
        "District": "Erode",
        "Crop": "Groundnut",
        "Disease": "Tikka Leaf Spot",
        "Severity": "Moderate",
        "ReportedDate": "2026-09-23",
        "AffectedAreaAcres": 85,
        "Status": "Under Containment",
        "Latitude": 11.3800,
        "Longitude": 77.6800
    },
    {
        "District": "Tirunelveli",
        "Crop": "Paddy (Rice)",
        "Disease": "Bacterial Leaf Blight",
        "Severity": "High",
        "ReportedDate": "2026-09-25",
        "AffectedAreaAcres": 175,
        "Status": "Alert Active",
        "Latitude": 8.7139,
        "Longitude": 77.7567
    },
    {
        "District": "Tirunelveli",
        "Crop": "Banana",
        "Disease": "Panama Wilt",
        "Severity": "High",
        "ReportedDate": "2026-09-26",
        "AffectedAreaAcres": 140,
        "Status": "Under Containment",
        "Latitude": 8.7800,
        "Longitude": 77.7200
    },
    {
        "District": "Cuddalore",
        "Crop": "Sugarcane",
        "Disease": "Sugarcane Red Rot",
        "Severity": "High",
        "ReportedDate": "2026-09-27",
        "AffectedAreaAcres": 225,
        "Status": "Alert Active",
        "Latitude": 11.7480,
        "Longitude": 79.7714
    },
    {
        "District": "Cuddalore",
        "Crop": "Groundnut",
        "Disease": "Tikka Leaf Spot",
        "Severity": "Low",
        "ReportedDate": "2026-09-21",
        "AffectedAreaAcres": 65,
        "Status": "Controlled",
        "Latitude": 11.7100,
        "Longitude": 79.7200
    },
    {
        "District": "Vellore",
        "Crop": "Groundnut",
        "Disease": "Tikka Leaf Spot",
        "Severity": "High",
        "ReportedDate": "2026-09-26",
        "AffectedAreaAcres": 180,
        "Status": "Alert Active",
        "Latitude": 12.9165,
        "Longitude": 79.1325
    },
    {
        "District": "Vellore",
        "Crop": "Tomato",
        "Disease": "Tomato Leaf Curl",
        "Severity": "Moderate",
        "ReportedDate": "2026-09-24",
        "AffectedAreaAcres": 90,
        "Status": "Under Containment",
        "Latitude": 12.9600,
        "Longitude": 79.1800
    }
]


@st.cache_data
def get_outbreaks_dataframe() -> pd.DataFrame:
    """Return a cached copy of Tamil Nadu crop outbreak incident logs."""
    df = pd.DataFrame(RAW_INCIDENTS)
    df["ReportedDate"] = pd.to_datetime(df["ReportedDate"])
    return df


@st.cache_data
def get_critical_alerts() -> pd.DataFrame:
    """Filter records requiring urgent regional intervention."""
    df = get_outbreaks_dataframe()
    return df[df["Severity"].isin(["Critical", "High"])].sort_values(by="ReportedDate", ascending=False)


def get_district_summary(district: str) -> pd.DataFrame:
    """Retrieve outbreak statistics for a specific district with safe lowercase matching."""
    df = get_outbreaks_dataframe()
    if not district:
        return df.head(0)
    return df[df["District"].str.lower() == district.strip().lower()]


if __name__ == "__main__":
    print("=== AgriVoice Vision Outbreak Surveillance Logs (Tamil Nadu) ===")
    df = get_outbreaks_dataframe()
    print(f"Total Logged Incidents: {len(df)}")
    print(df[["District", "Crop", "Disease", "Severity", "ReportedDate"]].to_string(index=False))
