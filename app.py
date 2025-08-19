# importing libraries
import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv

# setting up streamlit page
st.set_page_config(page_title="AI Travel Planner", page_icon="🌍", layout="centered")

# custom CSS for beautification
st.markdown("""
    <style>
        /* Page background */
        body {
            background-color: #0f1117; /* dark mode background */
        }

        /* Title */
        .title {
            font-size: 2.2rem;
            font-weight: 700;
            color: #4caf50;
            text-align: center;
            margin-bottom: 0.4rem;
        }

        /* Subtitle */
        .subtitle {
            font-size: 1rem;
            color: #bbb;
            text-align: center;
            margin-bottom: 2rem;
        }

        /* Transparent card-style form */
        .stForm {
            background-color: rgba(255, 255, 255, 0.0); /* fully transparent */
            padding: 2rem 2.5rem;
            border-radius: 12px;
            border: 1px solid rgba(200,200,200,0.2);
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            max-width: 600px;
            margin: auto;
        }

        /* Input fields transparent + white text */
        input, textarea {
            border-radius: 8px !important;
            border: 1px solid rgba(200,200,200,0.3) !important;
            padding: 0.6rem !important;
            background-color: rgba(255, 255, 255, 0.0) !important; /* transparent */
            color: #ffffff !important; /* white text */
        }
        input::placeholder, textarea::placeholder {
            color: rgba(255,255,255,0.5) !important; /* light placeholder */
        }

        /* Green button */
        div.stButton > button:first-child {
            background-color: #4caf50;
            color: white;
            font-size: 1rem;
            font-weight: 500;
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
            border: none;
            transition: background-color 0.2s ease, transform 0.1s ease;
        }
        div.stButton > button:first-child:hover {
            background-color: #388e3c;
            transform: translateY(-2px);
        }

        /* Transparent Output box with white text */
        .output-box {
            background-color: rgba(255, 255, 255, 0.0); /* transparent */
            padding: 1.2rem;
            border-radius: 10px;
            border: 1px solid rgba(200,200,200,0.3);
            margin-top: 1.5rem;
            box-shadow: 0 2px 6px rgba(0,0,0,0.2);
            color: #ffffff !important; /* white text */
        }
    </style>
""", unsafe_allow_html=True)


# app title
st.markdown("<h1 class='title'>AI Travel Itinerary Planner 🌍</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Plan your perfect day trip by entering your city and interests</p>", unsafe_allow_html=True)

# load env variables
load_dotenv()

# streamlit layout , input and output
with st.form("planner_form"):
    city = st.text_input(" Enter the city name for your trip")
    interests = st.text_input(" Enter your interests (comma-separated)")
    submitted = st.form_submit_button("✨ Generate Itinerary")

    if submitted:
        if city and interests:
            
            # sending input variables to our Travel planner method
            
            planner = TravelPlanner()
            
            # city input
            planner.set_city(city)
            
            # intrests input
            planner.set_interests(interests)
            
            # store the ai response in here
            itineary = planner.create_itineary()

            st.subheader("📄 Your Itinerary Plan")
            
            # printing response by groq
            st.markdown(f"<div class='output-box'>{itineary}</div>", unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please fill City or Interest to move forward")
