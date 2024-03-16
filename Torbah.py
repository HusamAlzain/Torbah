import streamlit as st
import pandas as pd

import pickle
from pathlib import Path

import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# -- User authentication --

names = ["Ali", "Ahemd"]
usernames = ["Ali01", "Ahemd1"]

# Load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

# 'afj' is a random code for encruption, cookie_expairy_days => after 30 days the cookies will be removed
# authenticator = stauth.Authenticate (names, usernames, hashed_passwords,
# "sales_dashboard", "abcdef")

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login("main", "Login")

if authentication_status == False:
    st.error("كلمة المرور او اسم المستخدم خاطئة")

if authentication_status == None:
    st.error("الرجاء ادخال كلمة المرور واسم المستخدم")


if authentication_status:
    authenticator.logout("Logout", "Sidebar")
    st.sidebar(f"اهلا {name}")
    st.set_page_config(page_title="AgriTech Dashboard", layout="wide")
    st.sidebar.success('Select a page above')

    # Creating an empty DataFrame
    df = pd.DataFrame()

    # Set the background color of the page


    # Add a title to the page
    st.title("اهلا بكم في ُتربة")

    # Display farm information
    st.header("Farm Information")

    # You can add components here to display information about the farm using st.write or st.text

    # Display climate data (you can replace this with your actual data and visualizations)
    st.header("Climate Data")

    # You can add components here to display climate data using st.line_chart, st.bar_chart, etc.

    # Display crop yield data (you can replace this with your actual data and visualizations)
    st.header("Crop Yield Data")

    # You can add components here to display crop yield data using st.bar_chart, st.line_chart, etc.

    # Display the DataFrame
    st.header("DataFrame Display")
    st.write(df)
