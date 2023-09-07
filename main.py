import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forcast for The Next Days")
place = st.text_input("Place:")
days = st.slider("Forcast Days", max_value=1, min_value=5,
                 help="select the number of days")
option = st.selectbox("Select the date to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:

    filtered_data = get_data(place, days)

    if option == "Temperature":
        temperature = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]

        figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}
        sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
        image_path = [images[condition] for condition in sky_condition]
        st.image(image_path, width=100)
