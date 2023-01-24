def run():
    import streamlit as st
    import pandas as pd
    import pickle as pk
    from sklearn.preprocessing import RobustScaler
    import numpy as np

    col1 , col2, col3 = st.columns([1,1.5,1])
    
    st.sidebar.markdown("Use Slider Below For Input")
    
# Sidebar slider for user input features
    def user_input_features():
        age = st.sidebar.slider('Age', 18,100,30)
        
        sexCat = st.sidebar.selectbox('Sex',('male','female'))
        if sexCat == 'male':
            sex = 1
        else:
            sex = 0
            
        cp = st.sidebar.slider('Chest Pain Type', 0,3,2)
        trtbps = st.sidebar.slider('RESTING BLOOD PRESSURE IN (MM|HG)', 100,200,125)
        chol = st.sidebar.slider('CHOLESTROL IN (MG|DL)', 100.0,450.0,130.0)
        fbs = st.sidebar.slider('FASTING BLOOD SUGAR > 120 MG/DL', 0,1,1)
        restecg = st.sidebar.slider('RESTING ELECTROCARDIOGRAPHIC RESULTS)', 0,2,1)
        thalachh = st.sidebar.slider('MAXIMUM HEART RATE ACHIEVED', 90.0,210.0,153.0)
        exng = st.sidebar.slider('exercise induced angina ', 0,1,0)
        oldpeak = st.sidebar.slider('ST depression induced by exercise relative to rest', 0.0,5.0,0.8)
        slp = st.sidebar.slider('slope of the peak exercise ST segment', 0,2,1) 
        caa = st.sidebar.slider('number of major vessels', 0,4,1)
        thall = st.sidebar.slider('thalassemia', 0,3,1)
            
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
        st.markdown("# Chance of Heart Attack Prediction App")
        
        st.write("""
        This app predicts the **chances of heart attack** of a person based on medical features.
        Use the slider on the left for each features to see the outcome.
        """)
        
        # Displays the user input features
        st.subheader('Your Input Features')
        
        st.write(input_df)
        
        # Reads in saved classification model
        load_clf = pk.load(open('stlib/models/rf.pkl', 'rb'))
        
        # Apply model to make predictions
        prediction = load_clf.predict(df)
        prediction_proba = load_clf.predict_proba(df)
        
        st.subheader('Prediction Outcome')
        heart_output = np.array(['< 50%% diameter narrowing. less chance of heart disease ','> 50%% diameter narrowing. more chance of heart disease'])
        st.write(heart_output[prediction])
        
        st.subheader('Prediction Probability')
        st.write(prediction_proba)
    
# This code allows you to run the app standalone
# as well as part of a library of apps
if __name__ == "__main__":
    run()