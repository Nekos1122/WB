import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Дэшборд Wildberries")

uploaded_file = st.file_uploader("Загрузите отчет (.csv или .xlsx)", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Определяем тип файла и читаем его
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success('Данные успешно загружены!')
    st.dataframe(df)  # Покажет таблицу полностью

    # Пусть в отчёте есть столбцы “Дата” и “Сумма продаж”
    if 'Дата' in df.columns and 'Сумма продаж' in df.columns:
        sales_by_date = df.groupby('Дата')['Сумма продаж'].sum().reset_index()
        # Построим график!
        fig, ax = plt.subplots(figsize=(10,5))
        ax.plot(sales_by_date['Дата'], sales_by_date['Сумма продаж'])
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.warning('В вашем файле не найдено нужных столбцов "Дата" и "Сумма продаж".')

else:
    st.info('Пожалуйста, загрузите файл для анализа.')