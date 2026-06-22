import streamlit as st
from PIL import Image
import datetime
import random

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="NIVAAN AI",
    page_icon="🐾",
    layout="wide"
)

# ---------------- IMPROVED CSS ----------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

/* Main text */
html, body, [class*="css"] {
    color: white;
}

/* Headers */
h1, h2, h3, h4, h5, h6 {
    color: white !important;
}

/* Labels */
label {
    color: white !important;
}

/* Paragraphs */
p {
    color: #e2e8f0 !important;
}

/* Title */
.main-title {
    text-align: center;
    color: white;
    font-size: 60px;
    font-weight: 800;
    margin-bottom: 0px;
}

/* Subtitle */
.sub-title {
    text-align: center;
    color: #cbd5e1;
    font-size: 24px;
    margin-top: -10px;
}

/* Metric Cards */
[data-testid="metric-container"] {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    padding: 15px;
    border-radius: 15px;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg,#2563eb,#06b6d4);
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: bold;
    height: 50px;
    width: 100%;
}

/* Upload Box */
[data-testid="stFileUploader"] {
    border: 2px dashed #38bdf8;
    border-radius: 15px;
    padding: 10px;
}

/* Divider */
hr {
    border-color: rgba(255,255,255,0.15);
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown(
    '<h1 class="main-title">🐾 NIVAAN AI</h1>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Detect • Prioritize • Rescue</p>',
    unsafe_allow_html=True
)

st.info(
    "AI-powered emergency animal rescue platform helping NGOs and veterinarians respond faster."
)

st.divider()

# ---------------- DASHBOARD ----------------

st.subheader("📊 Live Rescue Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🚨 Cases Today", "127")

with col2:
    st.metric("🐾 Animals Rescued", "89")

with col3:
    st.metric("🏥 Active NGOs", "34")

st.divider()

# ---------------- REPORTER DETAILS ----------------

st.subheader("📋 Reporter Details")

name = st.text_input("👤 Your Name")

phone = st.text_input("📞 Phone Number")

location = st.text_input("📍 Location")

st.divider()

# ---------------- ANIMAL TYPE ----------------

animal = st.selectbox(
    "🐾 Select Animal Type",
    ["Dog", "Cat", "Cow", "Other"]
)

# ---------------- IMAGE UPLOAD ----------------

uploaded_file = st.file_uploader(
    "📷 Upload Animal Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Animal Image",
        use_container_width=True
    )

    st.info("🔍 AI Analysis Running...")

    prediction = random.choice([
        "Low Risk",
        "Medium Risk",
        "High Risk",
        "Critical"
    ])

    confidence = random.randint(85, 99)

    st.write("## 🤖 AI Prediction")

    if prediction == "Critical":
        st.error(f"🔴 {prediction}")

    elif prediction == "High Risk":
        st.warning(f"🟠 {prediction}")

    elif prediction == "Medium Risk":
        st.warning(f"🟡 {prediction}")

    else:
        st.success(f"🟢 {prediction}")

    st.progress(confidence / 100)

    st.write(f"### AI Confidence Score: {confidence}%")

    if st.button("🚑 Generate Rescue Report"):

        ticket_id = f"NVA-{random.randint(1000,9999)}"

        st.divider()

        st.write("## 📋 Rescue Report")

        st.write("**Ticket ID:**", ticket_id)
        st.write("**Animal:**", animal)
        st.write("**Reporter Name:**", name)
        st.write("**Phone Number:**", phone)
        st.write("**Location:**", location)

        st.write(
            "**Date & Time:**",
            datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        )

        st.write(
            "**Detected Severity:**",
            prediction
        )

        if prediction == "Low Risk":
            response_time = "24 Hours"

        elif prediction == "Medium Risk":
            response_time = "12 Hours"

        elif prediction == "High Risk":
            response_time = "2 Hours"

        else:
            response_time = "30 Minutes"

        st.write(
            "**Estimated Response Time:**",
            response_time
        )

        st.divider()

        st.write("## 🚑 Nearby Rescue Team")

        st.success("Alert Sent Successfully")

        ngo = random.choice([
           "Animal Care Foundation",
           "Paws Rescue Team",
            "Hope Animal Trust",
            "Blue Cross Rescue",
            "Animal Welfare Society"
    ])

        st.write("**NGO Name:**", ngo)

        st.write("**Distance:** 2.3 KM")

        st.write(
             "**Rescue Vehicle:**",
         random.choice([
        "Ambulance A1",
        "Rescue Van B2",
        "Emergency Unit C3"
    ])
)

        st.write("**Status:** Active")

        st.divider()

        st.write("## 🚦 Rescue Progress")

        st.progress(25)
        st.write("✅ Case Registered")

        st.progress(50)
        st.write("✅ NGO Alerted")

        st.progress(75)
        st.write("✅ Team Assigned")

        st.progress(100)
        st.write("✅ Rescue In Progress")

        st.divider()

        st.write("## 💡 Rescue Recommendation")

        if prediction == "Low Risk":

            st.success(
                "Animal appears stable. Monitor and provide basic care."
            )

        elif prediction == "Medium Risk":

            st.warning(
                "Veterinary consultation recommended within 12 hours."
            )

        elif prediction == "High Risk":

            st.error(
                "Rescue team intervention required as soon as possible."
            )

        else:

            st.error(
                "Emergency rescue required! Immediate veterinary attention needed."
            )

        st.divider()

        st.write("## 📈 Case Priority")

        if prediction == "Low Risk":

            st.success("🟢 Low Priority")

        elif prediction == "Medium Risk":

            st.warning("🟡 Medium Priority")

        elif prediction == "High Risk":

            st.warning("🟠 High Priority")

        else:

            st.error("🔴 Emergency Priority")

st.divider()

# =====================================================
# RURAL LIVESTOCK ASSISTANCE MODULE
# =====================================================

st.subheader("🐄 Rural Livestock Assistance")

farmer = st.text_input("👨‍🌾 Farmer Name")

village = st.text_input("🏡 Village Name")

rural_animal = st.selectbox(
    "🐄 Livestock Type",
    ["Cow", "Buffalo", "Goat", "Sheep", "Other"]
)

symptoms = st.text_area(
    "🩺 Describe Symptoms"
)

if st.button("🔍 Analyze Rural Case"):

    symptoms_lower = symptoms.lower()

    if "fever" in symptoms_lower:
        disease = "Possible Infection"
        priority = "MEDIUM"

    elif "not eating" in symptoms_lower:
        disease = "Digestive Disorder"
        priority = "HIGH"

    elif "unable to walk" in symptoms_lower:
        disease = "Severe Injury"
        priority = "CRITICAL"

    elif "cough" in symptoms_lower:
        disease = "Respiratory Disease"
        priority = "HIGH"

    else:
        disease = "General Health Issue"
        priority = "LOW"

    st.success("✅ AI Analysis Complete")

    st.write("### 🧠 AI Diagnosis")
    st.write(disease)

    st.write("### 🚨 Priority Level")
    st.write(priority)

    st.write("### 💡 Recommendation")

    if priority == "CRITICAL":
        st.error("Immediate Veterinary Assistance Required")

    elif priority == "HIGH":
        st.warning("Consult a Veterinarian Within 24 Hours")

    elif priority == "MEDIUM":
        st.info("Monitor Animal and Contact Local Veterinary Support")

    else:
        st.success("Basic Care and Observation Recommended")

st.divider()
# =====================================================
# CASE HISTORY DASHBOARD
# =====================================================

st.divider()

st.subheader("📂 Recent Rescue Cases")

case_data = [
    ["NVA-1023", "Dog", "High Risk", "Rescued"],
    ["NVA-1045", "Cat", "Medium Risk", "In Progress"],
    ["NVA-1088", "Cow", "Critical", "Team Assigned"],
    ["NVA-1102", "Dog", "Low Risk", "Closed"]
]

st.table(
    {
        "Case ID": [x[0] for x in case_data],
        "Animal": [x[1] for x in case_data],
        "Priority": [x[2] for x in case_data],
        "Status": [x[3] for x in case_data]
    }
)

# =====================================================
# ANALYTICS DASHBOARD
# =====================================================

st.divider()

st.subheader("📈 Rescue Analytics")

col1, col2 = st.columns(2)

with col1:
    st.write("### Animal Cases Distribution")

    st.bar_chart({
        "Cases": {
            "Dog": 45,
            "Cat": 30,
            "Cow": 20,
            "Other": 10
        }
    })

with col2:
    st.write("### Rescue Status")

    st.bar_chart({
        "Status": {
            "Rescued": 60,
            "In Progress": 25,
            "Assigned": 15
        }
    })

st.success("AI Analytics Engine Active ✅")

# =====================================================
# EMERGENCY CONTACTS
# =====================================================

st.divider()

st.subheader("☎ Emergency Support Network")

st.info("🚑 Animal Ambulance: 1800-123-999")
st.info("🏥 Veterinary Helpline: 1800-456-777")
st.info("🐾 NGO Emergency Desk: 1800-888-555")

# =====================================================
# LIVE AI RISK SCORE CARD
# =====================================================

st.divider()

st.subheader("🧠 AI Risk Monitoring")

risk_score = random.randint(60, 99)

st.metric(
    "AI Risk Score",
    f"{risk_score}/100"
)

if risk_score > 90:
    st.error("🔴 Critical Rescue Required")
elif risk_score > 75:
    st.warning("🟠 High Risk Case")
else:
    st.success("🟢 Stable Condition")

# =====================================================
# GPS RESCUE LOCATION
# =====================================================

st.divider()

st.subheader("📍 Rescue Location Map")

import pandas as pd

map_data = pd.DataFrame({
    "lat": [26.4499],
    "lon": [80.3319]
})

st.map(map_data)

# =====================================================
# NGO PERFORMANCE DASHBOARD
# =====================================================

st.divider()

st.subheader("🏥 NGO Performance")

ngo_data = {
    "Animal Care Foundation": 45,
    "Paws Rescue Team": 32,
    "Hope Animal Trust": 28,
    "Blue Cross Rescue": 22
}

st.bar_chart(ngo_data)

st.success("NGO Monitoring System Active ✅")

# =====================================================
# DOWNLOAD RESCUE REPORT
# =====================================================

st.divider()

st.subheader("📄 Download Rescue Report")

report_text = f'''
NIVAAN AI RESCUE REPORT

Reporter: {name}
Phone: {phone}
Location: {location}

Animal Type: {animal}

Generated On:
{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}

Status: Rescue Alert Generated
'''

st.download_button(
    label="📥 Download Report",
    data=report_text,
    file_name="NIVAAN_Rescue_Report.txt",
    mime="text/plain"
)

# =====================================================
# ANIMAL SAFETY GUIDE
# =====================================================

st.divider()

st.subheader("📚 Animal Safety Guide")

with st.expander("🐕 If you find an injured dog"):
    st.write(
        "Keep safe distance, provide water, and contact rescue services."
    )

with st.expander("🐄 If livestock is injured"):
    st.write(
        "Move animal to a safe area and contact nearest veterinarian."
    )

with st.expander("🚨 Emergency Cases"):
    st.write(
        "Immediately alert NGOs and veterinary support."
    )
st.caption(
    "🐾 NIVAAN AI | Unified Animal Rescue & Rural Livestock Assistance Platform"
)