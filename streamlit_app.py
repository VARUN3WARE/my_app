import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import base64


# Example image URL or path
image_url = "https://img.freepik.com/premium-vector/dragon-logo-icon-design-illustration_586739-384.jpg"  # Replace with your image URL or local path
# Inject custom CSS for the background color
st.markdown("""
    <style>
        /* Apply background color to the main content area */
        .css-1d391kg {
            background-color: white;
        }
        /* Apply background color to the sidebar */
        .css-1d391kg:nth-child(2) {
            background-color: white;
        }
        /* Optional: Change text color for contrast */
        .css-1y4p1t1, .css-1cm7oa0, .css-1s6ln3p {
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

# Custom HTML with text and image
html_content = """


<img src="{image_url}" alt="Your Image Alt Text" style="display: block; margin: 0 auto; width: 50%;"/>

""".format(image_url=image_url)

# Render the HTML
st.markdown(html_content, unsafe_allow_html=True)

# st.image("WhatsApp Image 2024-07-31 at 09.40.50_257fb7f3.jpg", caption="Sunrise by the mountains")
st.header("Dragon04 :blue[Hospital Prediction Prototype]", divider=True)
# Load your data
st.markdown(':grey[This code will be printed')
data = pd.read_csv('merge.csv')  # Replace with your actual data source
data.dropna(inplace=True)
# Create a Folium map
m = folium.Map(location=[data['lat'].mean(), data['lon'].mean()], zoom_start=10)
image_path = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Fpremium-vector%2Fdragon-logo-icon-design-illustration_34736272.htm&psig=AOvVaw0f-nbBfGRQELq82IIMbmay&ust=1722602318682000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLC1wOzn04cDFQAAAAAdAAAAABAE'  # Replace with your image file path

# Read the image and encode it in base64
with open(image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()

    
# Add hospital markers
for _, row in data.iterrows():
    folium.Marker(
        location=[row['lat'], row['lon']],
        popup=row['name'],  # Assuming your DataFrame has a 'name' column for hospital names
        #now using our own custom icon
        # icon=custom_icon
        # icon=folium.Icon(icon='plus', prefix='fa', color='blue')
        # icon =iconm
    ).add_to(m)

# Display the map in Streamlit
folium_static(m)
