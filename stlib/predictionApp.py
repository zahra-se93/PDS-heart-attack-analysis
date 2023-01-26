def run():
    import streamlit as st
    import pandas as pd
    import pickle as pk
    from sklearn.preprocessing import RobustScaler
    import numpy as np

    col1 , col2, col3 = st.columns([1,1.5,1])
    
    st.sidebar.markdown("Fill Your Input Features Here:")
    
# Sidebar slider for user input features
    def user_input_features():
        age = st.sidebar.slider('**Age**', 18,100,30)
        
        sexCat = st.sidebar.selectbox('Sex',('Male','Female'))
        if sexCat == 'Male':
            sex = 1
        else:
            sex = 0
        
        cpSelect = st.sidebar.selectbox('**Chest Pain Type**',('Typical Angina','Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'))
        if cpSelect == 'Typical Angina':
            cp = 0
        elif cpSelect == 'Atypical Angina':
            cp = 1
        elif cpSelect == 'Non-Anginal Pain':
            cp = 2
        else:
            cp = 3
            
        trtbps = st.sidebar.slider('**Resting Blood Pressure (MM|HG)**', 100,200,125)
        chol = st.sidebar.slider('Cholestrol (MG|DL)', 100.0,450.0,130.0)
            
        fastBlood = st.sidebar.selectbox('**Fasting Blood Sugar > 120 MG/DL**',('False','True'))
        if fastBlood == 'False':
            fbs = 0
        else:
            fbs = 1
        
        restecgSelect = st.sidebar.selectbox('**Resting Electrocardiographic Results**',('Normal','Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)', 'Showing probable or definite left ventricular hypertrophy by Estes criteria'))
        if restecgSelect == 'Normal':
            restecg = 0
        elif restecgSelect == 'Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)':
            restecg = 1
        else:
            restecg = 2
        
        thalachh = st.sidebar.slider('**Maximum Heart Rate Achieved**', 90.0,210.0,153.0)
            
        exngSelect = st.sidebar.selectbox('**Exercise Induced Angina**',('False','True'))
        if exngSelect == 'False':
            exng = 0
        else:
            exng = 1
        
        oldpeak = st.sidebar.slider('**ST depression induced by exercise relative to rest**', 0.0,5.0,0.8)
        
        slpSelect = st.sidebar.selectbox('**Slope of the peak exercise ST segment**',('Unsloping','Flat', 'Downsloping'))
        if slpSelect == 'Unsloping':
            slp = 0
        elif slpSelect == 'Flat':
            slp = 1
        else:
            slp = 2
        
        caa = st.sidebar.slider('**Number Of Major Vessels**', 0,4,1)
        
        thallSelect = st.sidebar.selectbox('**Thalassemia**',('Null','Fixed Defect', 'Normal', 'Reversable Defect'))
        if thallSelect == 'Null':
            thall = 0
        elif thallSelect == 'Fixed Defect':
            thall = 1
        elif thallSelect == 'Normal':
            thall = 2
        else:
            thall = 3
            
        data = {'age': age,
                'sex': sex,
                'cp': cp,
                'trtbps': trtbps,
                'chol': chol,
                'fbs': fbs,
                'restecg': restecg,
                'thalachh': thalachh,
                'exng' : exng,
                'oldpeak': oldpeak,
                'slp': slp,
                'caa': caa,
                'thall': thall}
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()
    
    heart_raw = pd.read_csv('dataset/heart_cleaned.csv')
    heart = heart_raw.drop(columns=['output'])
    df = pd.concat([input_df,heart],axis=0)
    
    # define the columns to be encoded and scaled
    cat_cols = ['sex','exng','caa','cp','fbs','restecg','slp','thall']
    con_cols = ["age","trtbps","chol","thalachh","oldpeak"]
    
    # encoding the categorical columns
    df = pd.get_dummies(df, columns = cat_cols, drop_first = True)
    
    # instantiating the scaler
    scaler = RobustScaler()
    
    df[con_cols] = scaler.fit_transform(df[con_cols])
    df = df[:1]
    
    with col2:
        st.markdown("# Heart Disease Prediction")
        
        st.write("""
        This app predicts the **chances to have a heart disease** of a person based on medical features.
        The machine learning model was trained using [Heart Attack Dataset](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset).
        Use the slider on the left for each features to see the outcome. If you are a patient, please
        refer with an expert to obtain certain type of data for the prediction.
        """)
        
        # Displays the user input features
        st.subheader('Your Input Features')
        st.markdown('*Table below shows overall values of your input features from the sidebar*')
        st.write(input_df)
        
        # Reads in saved classification model
        load_clf = pk.load(open('stlib/models/lr.pkl', 'rb'))
        
        # Apply model to make predictions
        prediction = load_clf.predict(df)
        prediction_proba = load_clf.predict_proba(df)
        
        st.subheader('Prediction Outcome')
        if prediction == 0:
            st.success('Based on the input features prediction, you are **less likely** to have a Heart Disease. Congrats!', icon="✅")
            st.markdown("![Healthy heart](https://media.giphy.com/media/34uVCLrYC6vf7FxP2n/giphy.gif)")
        else:
            st.error('Based on the input features prediction, you are **more likely** to have a Heart Disease. Please refer to an expert.', icon="⚠️")
            st.markdown("![Sick heart](https://media.giphy.com/media/kIS1NBIphAbrmDwAva/giphy.gif)")
            
        # heart_output = np.array(['Based on the prediction, you are less likely to have a Heart Disease','Based on the prediction, you are more likely to have a Heart Disease. Please refer to an expert.'])
        # st.write(heart_output[prediction])
        
        st.subheader('Prediction Probability')
        st.markdown('*Table below shows the percentage of the prediction to be positive or negative as you select your input features. 1 indicates positive chances percentage, 0 negative chances percentage.*')
        st.write(prediction_proba)

        feedback = st.sidebar.slider('**How much would you rate this app?**',min_value=0,max_value=5,step=1)

        if feedback:
            st.header("Thank you for rating the app!")
            st.info("Caution: This is just a prediction and not doctoral advice. Kindly see a doctor if you feel the symptoms persist.")
            st.write("[Kaggle Link to Data Set](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset)")
    
# This code allows you to run the app standalone
# as well as part of a library of apps
if __name__ == "__main__":
    run()
