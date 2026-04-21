import streamlit as st
import pandas as pd

def load_data():
    df= pd.read_csv("dataset\covid_19_indonesia_time_series_all.csv")
    return df

def show_data():
    df = load_data()
    st.subheader("🦠Data Kasus Covid-19🦠")
    cols = ['Location'] + list(df.loc[:, 'New Cases':'Total Recovered'].columns)
    st.dataframe(df[cols].head(10))
    
    #tampilkan statistika deskriptive
    st.subheader("Statistika Deskriptif")
    st.write(df.describe())
    
    #Ini gini kan, ya?
    
def jumlah_data():
    df = load_data()
    total = df['Total Cases'].sum()
    st.subheader("Jumlah Kasus")
    st.write(f"Total Kasus: {total}")
    
