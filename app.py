import pandas as pd
import pickle as pk
import streamlit as st
import base64

# ----- Function to convert video to base64
def get_video_base64(video_path):
    with open(video_path, "rb") as video_file:
        video_bytes = video_file.read()
    return base64.b64encode(video_bytes).decode()

# Load model
model = pk.load(open('/Users/janhavii/Desktop/Projects/ML Mini Projects/House Rent Prediction/House_prediction_model.pkl', 'rb'))
data = pd.read_csv('/Users/janhavii/Desktop/Projects/ML Mini Projects/House Rent Prediction/Cleaned_data.csv')

# Convert video to base64
video_base64 = get_video_base64("/Users/janhavii/Desktop/Projects/ML Mini Projects/House Rent Prediction/background.mp4")

# Inject HTML for background video
st.markdown(f"""
    <style>
    html, body, .stApp {{
        height: 100%;
        margin: 0;
        padding: 0;
        background: transparent !important;
    }}

    video#bgvid {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%) rotate(-90deg);
        min-width: 100vh;
        min-height: 100vw;
        object-fit: cover;
        z-index: -1;
        opacity: 0.7;
    }}

    .glass-box {{
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 20px;
        max-width: 700px;
        margin: 5rem auto;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);
        border: 1px solid rgba(255, 255, 255, 0.18);
    }}

    
    </style>

    <video autoplay muted loop id="bgvid">
        <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
    </video>
    """, unsafe_allow_html=True)

# ---- Streamlit UI inside glass box

st.markdown(
    f"""
    <div class="glass-box">
        <h2 style='text-align: center; color: black;'>🏠 Mumbai Houses Price Predictor</h2>
    """,
    unsafe_allow_html=True
)

reg = st.selectbox('Choose the location', data['region'].unique())
sqft = st.number_input('Enter the total sqft')
bhk = st.number_input('Enter no of bedrooms reqd')

input_df = pd.DataFrame([[bhk, sqft, reg]], columns=['bhk', 'area', 'region'])

if st.button("Predict Price"):
    output = model.predict(input_df)
    st.success(f'💰 Price of the House is ₹{float(output[0]):,.2f} Cr')

st.markdown("</div>", unsafe_allow_html=True)


