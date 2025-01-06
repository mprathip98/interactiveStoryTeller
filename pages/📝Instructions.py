#importing library
import streamlit as sl

#tab title and page title
sl.set_page_config(page_title="Instructions")

with ((sl.container(border=True))):
    sl.title("Instructions")
    sl.markdown("")
    sl.markdown("- The intro slide presents the **opening text**. Click the **continue button** to navigate to the next slide at your own pace.")
    sl.markdown("- The user is occasionally presented with two choices. Click on the either of the **two choices** to continue.")
    sl.markdown("- Click the **stop button** to quit and restart.")
    sl.markdown("- Click the **restart button**, which appears at the end, to reset and to navigate back to the inital slide.")
    sl.subheader("")
