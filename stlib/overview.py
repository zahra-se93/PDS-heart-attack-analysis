def run():
    import streamlit as st
    from PIL import Image
    import time
    
    # st.markdown("# Overview")
        
    x,y,z = st.columns([1,0.9,1])
    col1 , col2, col3 = st.columns([1,2,1])
    
    
    with y:
        st.markdown("![Alt Text](https://media.giphy.com/media/8cBhJBU2wlq6H6qY4W/giphy.gif)")
    with col2:
        
        st.write(
        """
            Cardiovascular diseases (CVDs) are the number 1 cause of death globally, taking an estimated 17.9 million lives each year, which accounts for 31% of all deaths worldwide. Four out of 5CVD deaths are due to heart attacks and strokes, and one-third of these deaths occur prematurely in people under 70 years of age. Heart failure is a common event caused by CVDs and this dataset contains 11 features that can be used to predict a possible heart disease.

            People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need early detection and management wherein a machine learning model can be of great help.

        """
        )
        st.image(Image.open('assets/info_graph_1.png'))
    
            
    st.sidebar.header("Overview Sidebar")

# This code allows you to run the app standalone
# as well as part of a library of apps
if __name__ == "__main__":
    run()