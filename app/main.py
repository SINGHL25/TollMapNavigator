import os
import sys
import streamlit as st

# Ensure the current file's directory is in sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "app")))




sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.file_loader import load_site_data



from app.file_loader import load_site_data
from app.map_utils import create_map
from streamlit_folium import folium_static

st.set_page_config(page_title="TollMap Navigator", layout="wide")

st.title("🚧 TollMap Navigator - Queensland")
st.markdown("Visualize tolling gantries, shelters, ramps by location")

# Upload or load file
uploaded = st.file_uploader("Upload Toll Site CSV", type=["csv"])
if uploaded:
    df = load_site_data(uploaded)
else:
    df = load_site_data()

st.success(f"Loaded {len(df)} locations.")

# Filter options
site_type = st.multiselect("Filter by Type", options=df["Type"].unique(), default=df["Type"].unique())
direction = st.multiselect("Direction", options=df["Direction"].unique(), default=df["Direction"].unique())

filtered_df = df[(df["Type"].isin(site_type)) & (df["Direction"].isin(direction))]

# Show Map
st.subheader("📍 Map View")
folium_map = create_map(filtered_df)
folium_static(folium_map, width=1100, height=600)

# Show Table
st.subheader("📄 Location Data")
st.dataframe(filtered_df.reset_index(drop=True))
