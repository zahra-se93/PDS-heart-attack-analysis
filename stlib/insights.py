def run():
    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import warnings
    warnings.filterwarnings("ignore")

    st.markdown("# Heart Attack Insights")
    st.write("""
            Based on this dataset: [Kaggle](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset), our
            Data Scientist team have conducted several exploratory analysis. Below are our findings.
            """
    )
    
    tab1,tab2,tab3,tab4 = st.tabs(['Kernel Distribution Estimation Plot','Box Plot', 'Count Plot', 'Correlation Heatmap'])
    
    heart_raw = pd.read_csv('dataset/heart_cleaned.csv')
    
    with tab1:
        st.subheader('Based on the observed Kernel Distribution Estimation Plot, those with higher chances of heart attack are:')
        st.write('Aged 40-60 years old')
        st.write('With resting blood sugar between 120-140 (mm Hg)')
        st.write('With cholesterol between 200-250 (mg/dl)')
        st.write('With maximum achieved heart rate between 150-175')
        st.write('With ST depression induced by exercise relative to rest (oldpeak) between 0-1')
        fig = plt.figure(figsize=(16,16))
        gs = fig.add_gridspec(5,2)
        gs.update(wspace=0.5, hspace=0.5)
        ax0 = fig.add_subplot(gs[0,0])
        ax1 = fig.add_subplot(gs[0,1])
        ax2 = fig.add_subplot(gs[1,0])
        ax3 = fig.add_subplot(gs[1,1])
        ax4 = fig.add_subplot(gs[2,0])
        ax5 = fig.add_subplot(gs[2,1])
        ax6 = fig.add_subplot(gs[3,0])
        ax7 = fig.add_subplot(gs[3,1])
        ax8 = fig.add_subplot(gs[4,0])
        ax9 = fig.add_subplot(gs[4,1])

        background_color = "#FFFFFF"
        color_palette = ["#5833ff","#8000ff","#6aac90","#5833ff","#da8829"]
        fig.patch.set_facecolor(background_color) 
        ax0.set_facecolor(background_color) 
        ax1.set_facecolor(background_color) 
        ax2.set_facecolor(background_color)
        ax3.set_facecolor(background_color)
        ax4.set_facecolor(background_color)
        ax5.set_facecolor(background_color) 
        ax6.set_facecolor(background_color) 
        ax7.set_facecolor(background_color)
        ax8.set_facecolor(background_color)
        ax9.set_facecolor(background_color)

        # Age title
        ax0.text(0.5,0.5,"Distribution of age\naccording to\n target variable\n___________",
                horizontalalignment = 'center',
                verticalalignment = 'center',
                fontsize = 18,
                fontweight='bold',
                fontfamily='serif',
                color='#000000')
        ax0.spines["bottom"].set_visible(False)
        ax0.set_xticklabels([])
        ax0.set_yticklabels([])
        ax0.tick_params(left=False, bottom=False)

        # Age
        ax1.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
        sns.kdeplot(ax=ax1, data=heart_raw, x='age',hue="output", fill=True,palette=["#800000","#9370DB"], alpha=.5, linewidth=0)
        ax1.set_xlabel("")
        ax1.set_ylabel("")
        # TrTbps title pressure
        ax2.text(0.5,0.5,"Distribution of pressure\naccording to\n target variable\n___________",
                horizontalalignment = 'center',
                verticalalignment = 'center',
                fontsize = 18,
                fontweight='bold',
                fontfamily='serif',
                color='#000000')
        ax2.spines["bottom"].set_visible(False)
        ax2.set_xticklabels([])
        ax2.set_yticklabels([])
        ax2.tick_params(left=False, bottom=False)

        # TrTbps
        ax3.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
        sns.kdeplot(ax=ax3, data=heart_raw, x='trtbps',hue="output", fill=True,palette=["#800000","#9370DB"], alpha=.5, linewidth=0)
        ax3.set_xlabel("")
        ax3.set_ylabel("")
        # Chol title
        ax4.text(0.5,0.5,"Distribution of cholesterol\naccording to\n target variable\n___________",
                horizontalalignment = 'center',
                verticalalignment = 'center',
                fontsize = 18,
                fontweight='bold',
                fontfamily='serif',
                color='#000000')
        ax4.spines["bottom"].set_visible(False)
        ax4.set_xticklabels([])
        ax4.set_yticklabels([])
        ax4.tick_params(left=False, bottom=False)

        # Chol
        ax5.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
        sns.kdeplot(ax=ax5, data=heart_raw, x='chol',hue="output", fill=True,palette=["#800000","#9370DB"], alpha=.5, linewidth=0)
        ax5.set_xlabel("")
        ax5.set_ylabel("")
        # Thalachh title
        ax6.text(0.5,0.5,"Distribution of rate\naccording to\n target variable\n___________",
                horizontalalignment = 'center',
                verticalalignment = 'center',
                fontsize = 18,
                fontweight='bold',
                fontfamily='serif',
                color='#000000')
        ax6.spines["bottom"].set_visible(False)
        ax6.set_xticklabels([])
        ax6.set_yticklabels([])
        ax6.tick_params(left=False, bottom=False)

        # rate 
        ax7.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
        sns.kdeplot(ax=ax7, data=heart_raw, x='thalachh',hue="output", fill=True,palette=["#800000","#9370DB"], alpha=.5, linewidth=0)
        ax7.set_xlabel("")
        ax7.set_ylabel("")

        # Oldpeak title
        ax8.text(0.5,0.5,"Distribution of oldpeak\naccording to\n target variable\n___________",
                horizontalalignment = 'center',
                verticalalignment = 'center',
                fontsize = 18,
                fontweight='bold',
                fontfamily='serif',
                color='#000000')
        ax8.spines["bottom"].set_visible(False)
        ax8.set_xticklabels([])
        ax8.set_yticklabels([])
        ax8.tick_params(left=False, bottom=False)

        # Oldpeak
        ax9.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
        sns.kdeplot(ax=ax9, data=heart_raw, x='oldpeak',hue="output", fill=True,palette=["#800000","#9370DB"], alpha=.5, linewidth=0)
        ax9.set_xlabel("")
        ax9.set_ylabel("")

        for i in ["top","left","right"]:
            ax0.spines[i].set_visible(False)
            ax1.spines[i].set_visible(False)
            ax2.spines[i].set_visible(False)
            ax3.spines[i].set_visible(False)
            ax4.spines[i].set_visible(False)
            ax5.spines[i].set_visible(False)
            ax6.spines[i].set_visible(False)
            ax7.spines[i].set_visible(False)
            ax8.spines[i].set_visible(False)
            ax9.spines[i].set_visible(False)

        st.pyplot(fig)
    
    with tab2:
        st.subheader('Based on the observed Box Plot, those with higher chances of heart attack are:')
        st.write('Aged 45-60 years old')
        st.write('With resting blood sugar between 120-140 (mm Hg)')
        st.write('With cholesterol between 200-250 (mg/dl)')
        st.write('With maximum achieved heart rate between 150-170')
        st.write('With ST depression induced by exercise relative to rest (oldpeak) between 0-1')
        fig = plt.figure(figsize=(18,16))
        gs = fig.add_gridspec(2,3)
        gs.update(wspace=0.3, hspace=0.15)
        ax0 = fig.add_subplot(gs[0,0])
        ax1 = fig.add_subplot(gs[0,1])
        ax2 = fig.add_subplot(gs[0,2])
        ax3 = fig.add_subplot(gs[1,0])
        ax4 = fig.add_subplot(gs[1,1])
        ax5 = fig.add_subplot(gs[1,2])

        background_color = "#FFFFFF"
        color_palette = ["#800000","#9370DB","#6aac90","#4169E1","#da8829"]
        fig.patch.set_facecolor(background_color) 
        ax0.set_facecolor(background_color) 
        ax1.set_facecolor(background_color) 
        ax2.set_facecolor(background_color) 
        ax3.set_facecolor(background_color) 
        ax4.set_facecolor(background_color) 
        ax5.set_facecolor(background_color) 

        # Title of the plot
        ax0.spines["bottom"].set_visible(False)
        ax0.spines["left"].set_visible(False)
        ax0.spines["top"].set_visible(False)
        ax0.spines["right"].set_visible(False)
        ax0.tick_params(left=False, bottom=False)
        ax0.set_xticklabels([])
        ax0.set_yticklabels([])
        ax0.text(0.5,0.5,
                'Box plot for various\n continuous features\n_________________',
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=18, fontweight='bold',
                fontfamily='serif',
                color="#000000")

        # Age 
        ax1.text(-0.05, 81, 'Age', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
        ax1.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
        sns.boxplot(ax=ax1,x='output',y='age',data=heart_raw,hue=heart_raw['output'],palette=["#800000"],width=0.6)
        ax1.set_xlabel("")
        ax1.set_ylabel("")

        # Trtbps 
        ax2.text(-0.05, 208, 'pressure', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
        ax2.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
        sns.boxplot(ax=ax2,x='output',y='trtbps',data=heart_raw,hue=heart_raw['output'],palette=["#9370DB"],width=0.6)
        ax2.set_xlabel("")
        ax2.set_ylabel("")

        # Chol 
        ax3.text(-0.05, 600, 'cholestral', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
        ax3.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
        sns.boxplot(ax=ax3,x='output',y='chol',data=heart_raw,hue=heart_raw['output'],palette=["#6aac90"],width=0.6)
        ax3.set_xlabel("")
        ax3.set_ylabel("")

        # rate  
        ax4.text(-0.09, 210, 'rate', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
        ax4.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
        sns.boxplot(ax=ax4,x='output',y='thalachh',data=heart_raw,hue=heart_raw['output'],palette=["#4169E1"],width=0.6)
        ax4.set_xlabel("")
        ax4.set_ylabel("")
        # oldpeak 
        ax5.text(-0.1, 6.6, 'Oldpeak', fontsize=14, fontweight='bold', fontfamily='serif', color="#000000")
        ax5.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
        sns.boxplot(ax=ax5,x='output',y='oldpeak',data=heart_raw,hue=heart_raw['output'],palette=["#da8829"],width=0.6)
        ax5.set_xlabel("")
        ax5.set_ylabel("")

        for s in ["top","right","left"]:
            ax0.spines[s].set_visible(False)
            ax1.spines[s].set_visible(False)
            ax2.spines[s].set_visible(False)
            ax3.spines[s].set_visible(False)
            ax4.spines[s].set_visible(False)
            ax5.spines[s].set_visible(False)
    
        st.pyplot(fig)
    
    with tab3:
        st.subheader('Based on the observed Count Plot, those with higher chances of heart attack are:')   
        st.write('Male')
        st.write('Not having exercise induced angina')
        st.write('People with 0 major vessels') 
        st.write('having non-Anginal chest pain')
        st.write('having fasting blood sugar < 120 mg/dl') 
        st.write('with resting electrocardiographic results, re=1, which is having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)')
        st.write('with slope=2, which refers to flat slope')
        st.write('with Thalassemia rate, thall = 2')
        fig = plt.figure(figsize=(20,15))
        gs = fig.add_gridspec(3,3)
        gs.update(wspace=0.5, hspace=0.25)
        ax0 = fig.add_subplot(gs[0,0])
        ax1 = fig.add_subplot(gs[0,1])
        ax2 = fig.add_subplot(gs[0,2])
        ax3 = fig.add_subplot(gs[1,0])
        ax4 = fig.add_subplot(gs[1,1])
        ax5 = fig.add_subplot(gs[1,2])
        ax6 = fig.add_subplot(gs[2,0])
        ax7 = fig.add_subplot(gs[2,1])
        ax8 = fig.add_subplot(gs[2,2])

        background_color = "#FFFFFF"
        color_palette = ["#800000","#9370DB","#6aac90","#4169E1","#da8829"]
        fig.patch.set_facecolor(background_color) 
        ax0.set_facecolor(background_color) 
        ax1.set_facecolor(background_color) 
        ax2.set_facecolor(background_color) 
        ax3.set_facecolor(background_color) 
        ax4.set_facecolor(background_color) 
        ax5.set_facecolor(background_color) 
        ax6.set_facecolor(background_color) 
        ax7.set_facecolor(background_color) 
        ax8.set_facecolor(background_color) 

        # Title of the plot
        ax0.spines["bottom"].set_visible(False)
        ax0.spines["left"].set_visible(False)
        ax0.spines["top"].set_visible(False)
        ax0.spines["right"].set_visible(False)
        ax0.spines["right"].set_visible(False)
        ax0.tick_params(left=False, bottom=False)
        ax0.set_xticklabels([])
        ax0.set_yticklabels([])
        ax0.text(0.5,0.5,
                'Count plot for various\n categorical features\n_________________',
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=18, fontweight='bold',
                fontfamily='serif',
                color="#000000")

        # Sex count
        ax1.text(-0.1, 130, 'Sex: 0-Female 1-Male', fontsize=15, fontweight='bold', fontfamily='serif', color="#000000")
        ax1.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
        sns.countplot(ax=ax1,data=heart_raw,x='sex',hue='output',fill= True,palette=color_palette)
        ax1.set_xlabel("")
        ax1.set_ylabel("")

        # Exng count
        ax2.text(-1, 160, 'Exng: exercise induced angina (1 = yes; 0 = no)', fontsize=15, fontweight='bold', fontfamily='serif', color="#000000")
        ax2.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
        sns.countplot(ax=ax2,data=heart_raw,x='exng',hue='output',fill= True,palette=color_palette)
        ax2.set_xlabel("")
        ax2.set_ylabel("")

        # Caa count
        ax3.text(-1.0, 150, 'Caa: number of major vessels (0-3)', fontsize=15, fontweight='bold', fontfamily='serif', color="#000000")
        ax3.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
        sns.countplot(ax=ax3,data=heart_raw,x='caa',hue='output',fill= True,palette=color_palette)
        ax3.set_xlabel("")
        ax3.set_ylabel("")

        # Cp count,
        ax4.text(-0.8, 120, 'Cp: Chest Pain type chest pain type(1-4)', fontsize=15, fontweight='bold', fontfamily='serif', color="#000000")
        ax4.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
        sns.countplot(ax=ax4,data=heart_raw,x='cp',hue='output',fill= True,palette=color_palette)
        ax4.set_xlabel("")
        ax4.set_ylabel("")

        # Fbs count
        ax5.text(-0.8, 165, 'Fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)', fontsize=15, fontweight='bold', fontfamily='serif', color="#000000")
        ax5.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
        sns.countplot(ax=ax5,data=heart_raw,x='fbs',hue='output',fill= True,palette=color_palette)
        ax5.set_xlabel("")
        ax5.set_ylabel("")

        # Restecg count
        ax6.text(-1.0, 110, 're: resting electrocardiographic results(0-2)', fontsize=15, fontweight='bold', fontfamily='serif', color="#000000")
        ax6.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
        sns.countplot(ax=ax6,data=heart_raw,x='restecg',hue='output',fill= True,palette=color_palette)
        ax6.set_xlabel("")
        ax6.set_ylabel("")

        # Slp count
        ax7.text(0.85, 120, 'Slp: Slope', fontsize=15, fontweight='bold', fontfamily='serif', color="#000000")
        ax7.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
        sns.countplot(ax=ax7,data=heart_raw,x='slp',hue='output',fill= True,palette=color_palette)
        ax7.set_xlabel("")
        ax7.set_ylabel("")

        # Thall count
        ax8.text(-0.6, 150, 'Thall: Thalium Stress Test result ~ (0,3)', fontsize=15, fontweight='bold', fontfamily='serif', color="#000000")
        ax8.grid(color='#000000', linestyle=':', axis='y', zorder=0,  dashes=(1,5))
        sns.countplot(ax=ax8,data=heart_raw,x='thall',hue='output',fill= True,palette=color_palette)
        ax8.set_xlabel("")
        ax8.set_ylabel("")

        for s in ["top","right","left"]:
            ax0.spines[s].set_visible(False)
            ax1.spines[s].set_visible(False)
            ax2.spines[s].set_visible(False)
            ax3.spines[s].set_visible(False)
            ax4.spines[s].set_visible(False)
            ax5.spines[s].set_visible(False)
            ax6.spines[s].set_visible(False)
            ax7.spines[s].set_visible(False)
            ax8.spines[s].set_visible(False)
    
        st.pyplot(fig)
        
    with tab4:
        st.subheader('Based on the Correlation HeatMap, the features that have high impact in resulting in heart attack are:')
        st.write('Chest Pain type (cp)')
        st.write('Maximum heart rate achieved (thalach)')
        st.write('Slope of the peak exercise ST segment (slp)')
        st.write('____________')
        st.write('Note: Based on the colours of the below features in the heatmap, indicate that there is a strong negative correlation between these features and the target output:') 
        st.write('Exercise induced angina (exng)') 
        st.write('ST depression induced by exercise relative to rest (oldpeak)')
        st.write('Number of major vessels (caa)')
        st.write('Thalassemia rate (thall)')
        cor_mat=heart_raw.corr()
        fig,ax=plt.subplots(figsize=(15,10))
        sns.heatmap(cor_mat,annot=True,linewidths=0.5,fmt=".3f")

        st.write(fig)
              
    st.sidebar.header("WebApp by Data Alliance:")
    st.sidebar.write("""
                     * Azzim
                     * Kelvin
                     * Ruobing
                     * Jiangmeng
                     """)

# This code allows you to run the app standalone
# as well as part of a library of apps
if __name__ == "__main__":
    run()
