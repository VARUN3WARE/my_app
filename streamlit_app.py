import streamlit as st 
import plotly.express as px
st.title("hello packy poinet")
st.header("this is my app",divider="gray")
st.header("This is a header with a divider", divider="rainbow")

with st.sidebar:
  st.header("About app")

df = px.data.iris()
fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="species",
    size="petal_length",
    hover_data=["petal_width"],
)

event = st.plotly_chart(fig, key="iris", on_select="rerun")

event.selection
