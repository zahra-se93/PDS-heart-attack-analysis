message = """
        __Select a page from the list below__
        """

import streamlit as st
st.set_page_config(layout = "wide") # optional

from stlib import overview
from stlib import findings
from stlib import predictionApp

with st.sidebar:
    st.markdown('''# Data Alliance''')
    page = st.selectbox('Pages:',['Overview','Findings', 'Heart Attack Prediction']) 

if page == 'Overview':
    overview.run()
elif page == 'Findings':
    findings.run()
else:
    predictionApp.run()