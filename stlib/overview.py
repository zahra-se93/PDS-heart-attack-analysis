def run():
    import streamlit as st
    from PIL import Image
    
    col1 , col2 = st.columns(2)
    with col1:
        st.markdown("# Overview Page")
        st.write(
        """
                Data mining is useful for studying and understanding a large amount of data. It is used for the extraction of data and to make the decision for further applications.Machine learning usage is growing vastly in the medical diagnosis industry, where the manual error can be reduced with computer analysis, and accuracy is improved. The diagnosis of a disease is highly reliable with machine learning techniques.

                Care and improvement of the unwellness by the help of identification, hindrance, and care of any kind of illness is HealthCare. Healthcare plays an important function in Big Data. But a major dispute is to render improved care and clinical services at an inexpensive value. By diverse predictive analysis, the expense will diminish and can get improved clinical care. 

                Heart disease causes a significant mortality rate around the world, and it has become a health threat for many people. Early prediction of heart disease may save many lives; detecting cardiovascular diseases like heart attacks, coronary artery diseases etc., isa critical challenge by the regular clinical data analysis. Machine learning can bring an effective solution for decision making and accurate predictions. The medical industry is showing enormous development in using machine learning techniques.

                Heart attack prediction model is suitable for all types of medical institutions to assist doctors in predicting heart disease and helping patients to better manage their heart disease. It can help doctors to better monitor their conditions and save patients' lives through prognosis, further improving the doctor-patient relationship and promoting the development of medical and healthcare in society.
        """
        )
    
    with col2:
        st.image(Image.open('assets/info_graph_1.png'))
            
    st.sidebar.header("Overview Sidebar")

# This code allows you to run the app standalone
# as well as part of a library of apps
if __name__ == "__main__":
    run()