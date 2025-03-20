import streamlit as st
import requests

# Streamlit UI Configuration
st.set_page_config(page_title="Side Hustles & Money Quotes", layout="wide")

# Custom CSS for Styling
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 36px;
        color: #4CAF50;
    }
    .quote-box, .hustle-box {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# FastAPI Backend URL
API_BASE_URL = "https://simple-apis-one.vercel.app/"

# Title
st.markdown("<h1 class='title'>💰 Side Hustles & Money Quotes 💡</h1>", unsafe_allow_html=True)

# Layout with Two Columns
col1, col2 = st.columns(2)

# Side Hustle Section
with col1:
    st.markdown("### 🚀 Side Hustle Idea")
    if st.button("Get a Side Hustle Idea"):
        response = requests.get(f"{API_BASE_URL}/side_hustles")
        if response.status_code == 200:
            hustle = response.json().get("side_hustle", "No hustle found")
            st.markdown(f"<div class='hustle-box'><h3>{hustle}</h3></div>", unsafe_allow_html=True)
        else:
            st.error("Failed to fetch side hustle idea")

# Money Quote Section
with col2:
    st.markdown("### 💸 Money Quote")
    if st.button("Get a Money Quote"):
        response = requests.get(f"{API_BASE_URL}/money_quotes")
        if response.status_code == 200:
            quote = response.json().get("money_quote", "No quote found")
            st.markdown(f"<div class='quote-box'><h3>📢 {quote}</h3></div>", unsafe_allow_html=True)
        else:
            st.error("Failed to fetch money quote")

# Footer
st.markdown("---")
st.markdown("### Built with ❤️ using FastAPI & Streamlit")
