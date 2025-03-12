import streamlit as st
import requests
from solana.rpc.api import Client

# Function to get new pairs
def get_new_pairs():
    try:
        url = "https://api.dexscreener.com/latest/dex/pairs/solana"
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        return data["pairs"]
    except Exception as e:
        st.error(f"Failed to fetch data: {e}")
        return []

# Function to detect rug pulls
def detect_rug_pull(pair):
    try:
        liquidity = float(pair["liquidity"]["usd"])
        if liquidity < 10000:  # Low liquidity = risky
            return True
        return False
    except Exception as e:
        st.error(f"Error analyzing pair: {e}")
        return False

# Function to find high potential gainers
def find_high_potential(pair):
    try:
        volume = float(pair["volume"]["h24"])
        liquidity = float(pair["liquidity"]["usd"])
        if volume > 100000 and liquidity > 50000:  # High volume and liquidity = good
            return True
        return False
    except Exception as e:
        st.error(f"Error analyzing pair: {e}")
        return False

# Streamlit app
st.title("Crypto Bot 🚀")
st.write("Scanning for new tokens on Solana...")

pairs = get_new_pairs()
if pairs:
    for pair in pairs:
        if detect_rug_pull(pair):
            st.error(f"🚨 Rug pull detected: {pair['baseToken']['name']}")
        if find_high_potential(pair):
            st.success(f"🚀 High potential: {pair['baseToken']['name']}")
else:
    st.warning("No data found. Please try again later.")