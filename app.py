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
elif menu == "Halaman Data":
    judul()
    show_data()
    jumlah_data()
    
st.caption("Copyright - Aulia- 184240010")