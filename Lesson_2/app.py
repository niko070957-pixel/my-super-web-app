import streamlit as st

st.set_page_config(page_title = "Мій Супер-Додаток", page_icon = "🚀", layout = "wide")

st.title("Ласково просимо до мого додатку 🤖")

tab_1, tab_2 = st.tabs(["Про мене", "Мій інструмент"])

with tab_1:
    st.header("Знайомство з автором")
    col_1, col_2 = st.columns([1, 2])
    with col_1:
        st.image("https://mamp.one/wp-content/uploads/2024/09/image-resources2.jpg")
    with col_2:
        st.subheader("Привіт, я майбутній Python Developer")
        st.write("Я навчаюсь в Малій Академії IT STEP")