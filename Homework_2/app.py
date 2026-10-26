import streamlit as st, random

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


with tab_2:
    if 'secret_number' not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False

    st.subheader("Гра: Вгадай число від 1 до 100")

    user_guess = st.number_input("Tвiй Bapiaнт:", min_value=1, max_value=100, step=1)

    if st.button("Перевірити"):
        st.session_state.attempts += 1
        if user_guess < st.session_state.secret_number:
            st.info("Загадане число БІЛЬШЕ!")
        elif user_guess > st.session_state.secret_number:
            st.info("Задане число МЕНЬШЕ!")
        else:
            st.balloons()
            st.success(f"Перемога! Ти вгадав число {st.session_state.secret_number} зa {st.session_state.attempts} спроб!")
            st.session_state.game_over = True

    if st.button("Зіграти знову"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.rerun()