# app.py
import streamlit as st

def crawling():
    st.subheader("Crawling Data")
    # Add code for crawling here

def preprocessing():
    st.subheader("Analisis Kalimat")
    # Add code for preprocessing here

def analysis():
    st.subheader("Visualisasi")
    # Add code for analysis here

def display_data():
    st.subheader("Display Data")
    # Add code for displaying data here

def home():
    st.title("Selamat Datang Di Web Analisis Sentimen Lihut")
    st.write("Calon Potensial Presiden 2024")

def main():
    # st.title("My Streamlit App")

    # Create a sidebar with buttons for menu options
    home_button = st.sidebar.button("Home")
    crawling_button = st.sidebar.button("Crawling Data")
    preprocessing_button = st.sidebar.button("Analisis Kalimat")
    analysis_button = st.sidebar.button("Visualisasi")
    display_button = st.sidebar.button("Display Data")

    # Display content based on button click
    if home_button:
        home()
    elif crawling_button:
        crawling()
    elif preprocessing_button:
        preprocessing()
    elif analysis_button:
        analysis()
    elif display_button:
        display_data()
    else:
        # If no button is clicked, show the content for the "Home" page
        home()

if __name__ == "__main__":
    main()
