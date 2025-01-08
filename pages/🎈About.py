#importing library
import streamlit as sl

#tab title and page title
sl.set_page_config(page_title="Instructions")

with ((sl.container(border=True))):
    sl.title("About")
    sl.markdown("It has a total of three pages:")
    sl.markdown("- Home - All of the main content lies here")
    sl.markdown("- About - Quick facts about the project")
    sl.markdown("- Instructions - Simple instructions to use the app.")
    sl.markdown("This project also has a responsive design, adapting to any screen size")

    sl.title("Documentation")
    sl.markdown("This project uses Streamlit to cast the website and deploy it through the Streamlit Community Cloud.")
    sl.markdown("- Design Documentation: https://docs.streamlit.io/")
    sl.markdown("- Streamlit Community Cloud Deployment Documentation: https://docs.streamlit.io/deploy/streamlit-community-cloud")


