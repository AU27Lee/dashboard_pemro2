import streamlit as st
import pandas as pd
import plotly.express as px

def load_data():
    df= pd.read_csv("dataset/covid_19_indonesia_time_series_all.csv")
    return df

def filter_data(df, year=None):
    if year:
        df = df[df['Date'].astype(str).str.contains(str(year))]
    return df

def show_data(df):
    selected_columns = ['Location'] + list(df.loc[:, 'New Cases': "Total Recovered"].columns)
    df_selected = df[selected_columns]
    st.subheader("Data Covid-19 Indonesia ❤️🤍")
    st.dataframe(df_selected.head(10))
    
    #tampilkan statistika deskriptive
    st.subheader("Statistika Deskriptif")
    st.write(df.describe())
    
    #Ini gini kan, ya?

#total kasus
def total_case(df):
    total_kasus= df['New Cases'].sum()
    return total_kasus

#total death
def total_death(df):
    total_kematian = df["New Deaths"].sum()
    return total_kematian

#total sembuh
def total_recovery(df):
    total_sembuh = df['New Recovered'].sum()
    return total_sembuh

def kolom(df):
    kasus = total_case(df)
    kematian = total_death(df)
    sembuh = total_recovery(df)
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Total Kasus📊", value=kasus, border=True)
    col2.metric(label="Total Kematian⚰️", value=kematian, border=True)
    col3.metric(label="Total Sembuh❤️‍🩹", value=sembuh, border=True)
    
def select_year():
    # Gunakan list string agar tipe datanya seragam
    opsi_tahun = ["Semua Tahun", "2020", "2021", "2022"]
    
    pilihan = st.sidebar.selectbox(
        "Pilih Tahun📅",
        options=opsi_tahun
    )
    
    # Kembalikan None jika yang dipilih adalah "Semua Tahun" 
    # agar fungsi filter_data kamu tetap bekerja
    return None if pilihan == "Semua Tahun" else pilihan

def pie_chart(df):
    #pemanggil data
    total_mati= total_death(df)
    total_sembuh = total_recovery(df)
    
    #dataframe
    data = {
        'Status': ['Meninggal', 'Sembuh'],
        'Jumlah': [total_mati, total_sembuh]
    }
    
    fig = px.pie(
        data,
        names="Status",
        values="Jumlah",
        title="Perbandingan Total Kematian VS Total Kesembuhan",
        hole = 0.5,
        color_discrete_sequence=["#4de89f", "#ff6459"]
    )
    
    st.plotly_chart(fig, use_container_width=True)