import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Мини WB-дэшборд")

# Загрузка файла
wb_file = st.file_uploader("Загрузите отчёт Wildberries (.csv или .xlsx)")

if wb_file is not None:
    if wb_file.name.endswith(".csv"):
        df = pd.read_csv(wb_file, sep=';', encoding='utf-8')
    elif wb_file.name.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(wb_file)
    else:
        st.warning("Формат не поддерживается.")
        st.stop()
    st.success("Данные успешно загружены!")
    st.dataframe(df.head())

    # Простейшие показатели
    if "Кол-во" in df.columns:
        st.metric("Общее количество", int(df["Кол-во"].sum()))
    if "Сумма" in df.columns:
        st.metric("Общая сумма", float(df["Сумма"].sum()))

    # Пример графика
    if "Дата" in df.columns and "Сумма" in df.columns:
        df['Дата'] = pd.to_datetime(df['Дата'], errors='coerce')
        df2 = df.groupby('Дата')["Сумма"].sum().reset_index()
        plt.plot(df2['Дата'], df2['Сумма'])
        plt.xlabel('Дата')
        plt.ylabel('Сумма продаж')
        st.pyplot(plt)
else:
    st.info("Пожалуйста, загрузите файл для анализа!")