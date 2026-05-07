import streamlit as st
from data import *

#judul dashboard
def judul():
    st.title("📊Dashboard Covid-19")
    st.write("Jadi, ini merupakan dashboard telat dari kejadian Covid-19.")
    
st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Home", "Halaman Data"])

if menu == "Home":
    judul()
    #Pilih tahun
    year = select_year()
    lokasi = select_location(load_data())
    #Load & filter data
    df = load_data()
    df_filtered = filter_data(df,year)
    kolom(df_filtered)
    pie_chart(df_filtered)
elif menu == "Halaman Data":
    judul()
    year = select_year()
    lokasi = select_location(load_data())
    #Load & filter data
    df = load_data()
    df_filtered = filter_data(df, year)
    show_data(df_filtered)
    
st.caption("Copyright - Aulia- 184240010")