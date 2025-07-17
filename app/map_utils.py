

import folium
from folium.plugins import MarkerCluster

def create_map(df):
    avg_lat = df["Latitude"].mean()
    avg_lon = df["Longitude"].mean()
    
    m = folium.Map(location=[avg_lat, avg_lon], zoom_start=11)

    cluster = MarkerCluster().add_to(m)

    for _, row in df.iterrows():
        tooltip = f"{row['Name']} ({row['Type']})"
        popup = f"{row['Landmark']}<br>{row['Direction']}"
        folium.Marker(
            [row["Latitude"], row["Longitude"]],
            tooltip=tooltip,
            popup=popup,
            icon=folium.Icon(color="blue", icon="road", prefix="fa")
        ).add_to(cluster)

    return m

