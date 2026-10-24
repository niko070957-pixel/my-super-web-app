import streamlit as st, time

score = 0

st.title("Python Knowledge Quiz")
st.write("Answer these three questions to test your Python knowledge!")

st.subheader("What is the output of the following code?")
st.code("print(2+2*3)")
answer_1 = st.radio("Choose one option:", ["8", "2+2*3", "syntax error", "other"])

st.subheader("Which type of data is:")
st.code('["hello", "world"]')
answer_2 = st.radio("Choose one option:", ["boolean", "string", "list", "class"])

st.subheader("What is the function of:")
st.code("input()")
answer_3 = st.radio("Choose one option:", ["outputs in terminal", "makes coffee", "creates a variable", "none of the above"])

if st.button("Submit answers"):
    if answer_1 == "8": score += 1
    if answer_2 == "list": score += 1
    if answer_3 == "none of the above": score += 1

    st.progress(score / 3)

    if score == 0:
        st.subheader("This... couldn't be correct.")
    elif score == 1:
        st.subheader("Not bad.")
    elif score == 2:
        st.subheader("Very close...")
    elif score == 3:
        st.balloons()
        st.subheader("You've hacked Python! Now you are a Python pro!")