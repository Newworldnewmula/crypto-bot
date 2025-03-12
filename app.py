import streamlit as st

st.title("Crypto Bot 🚀")
st.write("Scanning for new tokens on Solana...")

pairs = get_new_pairs()
for pair in pairs:
    if detect_rug_pull(pair):
        st.error(f"🚨 Rug pull detected: {pair['baseToken']['name']}")
    if find_high_potential(pair):
        st.success(f"🚀 High potential: {pair['baseToken']['name']}")
        