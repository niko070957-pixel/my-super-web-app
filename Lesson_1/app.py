import streamlit as st

st.title("Мій перший веб-застосунок")
st.write("Привіт! Цей сайт був створено повністю на Python")

user_name = st.text_input("Як тебе звати?")

if st.button("Привітатися"):
    if user_name:
        st.success(f"Привіт, {user_name}! Радій тебе бачити на моєму сайті!")
    else:
        st.warning("Будь ласка, введи своє ім'я спочатку!")

st.subheader("Завантажте своє фото")
uploaded_file = st.file_uploader("Оберіть зображення...", type = ["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, use_container_width = True)