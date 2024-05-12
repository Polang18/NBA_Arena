import streamlit as st
import pandas as pd
import folium
import streamlit_folium as sf
df = pd.read_csv("nba_team_arena.csv")
map = folium.Map(location=[39.8,-98.5],zoom_start=4)
for i,row in df.iterrows():
  lat,long = row["latitude"],row["longitude"]
  folium.Marker([lat,long],tooltip=row["stadium"]).add_to(map)
sf.st_folium(map)