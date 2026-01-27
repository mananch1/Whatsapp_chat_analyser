import streamlit as st
import preprocessor

st.sidebar.title('Whatsapp chat analyser')

uploaded_file = st.sidebar.file_uploader("Select a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode('utf-8')
    df = preprocessor.preprocessor(data)
    
    st.dataframe(df)

