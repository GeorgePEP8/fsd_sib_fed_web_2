import io
import streamlit as st



st.title('Предсказание уровня заражения вирусом COVID-19 в городах России')


uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
     bytes_data = uploaded_file.read()
     file_name = uploaded_file.name
     st.write("filename:", file_name)
     st.write(bytes_data)

