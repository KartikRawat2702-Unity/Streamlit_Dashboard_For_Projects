import streamlit as st
import pandas as pd
import pyttsx3
import random
from openai import OpenAI
st.set_page_config(page_title="Final Project Dashboard", layout="centered")
st.title("🚀 Final Certificate Project Dashboard")
OPENAI_API_KEY = "put your key here"
client = OpenAI(api_key=OPENAI_API_KEY)
project = st.selectbox(
    "Select Your Project",
    [
        "Calculator",
        "ATM PIN System",
        "Unit Converter",
        "Movie Ticket Booking",
        "Positive/Negative Checker",
        "File Transfer App",
        "Improved Streamlit Dashboard",
        "OpenAI Chat App",
        "Text-to-Speech Tool",
        "XO Game",
        "Flask API Project (Demo)"
    ]
)
st.divider()

if project == "Calculator":
    st.header("🧮 Calculator")
    a = st.number_input("Enter First Number")
    b = st.number_input("Enter Second Number")
    op = st.selectbox("Operation", ["+", "-", "*", "/"])
    if st.button("Calculate"):
        if op == "+":
            st.success(a + b)
        elif op == "-":
            st.success(a - b)
        elif op == "*":
            st.success(a * b)
        elif op == "/":
            st.success(a / b if b != 0 else "Cannot divide by zero")

elif project == "ATM PIN System":
    st.header("🏧 Advanced ATM System")
    if "balance" not in st.session_state:
        st.session_state.balance = 5000
    if "atm_logged" not in st.session_state:
        st.session_state.atm_logged = False
    correct_pin = "1234"
    pin = st.text_input("Enter Your ATM PIN", type="password")
    if st.button("Login"):
        if pin == correct_pin:
            st.session_state.atm_logged = True
            st.success("✅ Login Done")
        else:
            st.error("❌ Wrong PIN")
    if st.session_state.atm_logged:
        st.subheader("💰 Balance")
        st.info(f"₹ {st.session_state.balance}")
        action = st.selectbox("Select Action", ["Deposit", "Withdraw"])
        amount = st.number_input("Enter Amount", min_value=0)
        if st.button("Submit"):
            if action == "Deposit":
                st.session_state.balance += amount
                st.success(f"₹{amount} Deposited Successfully")
            elif action == "Withdraw":
                if amount > st.session_state.balance:
                    st.error("❌ Insufficient Balance")
                else:
                    st.session_state.balance -= amount
                    st.success(f"₹{amount} Withdrawn Complete")
            st.info(f"Updated Balance: ₹ {st.session_state.balance}")
        if st.button("Logout"):
            st.session_state.atm_logged = False
            st.success("🔒 Logged Out Done")

elif project == "Unit Converter":
    st.header("📏 Unit Converter (KM → M)")
    km = st.number_input("Enter KM")
    if st.button("Convert"):
        st.success(f"{km} KM = {km * 1000} meters")

elif project == "Movie Ticket Booking":
    st.header("🎬 Movie Ticket Booking")
    name = st.text_input("Customer Name")
    movie = st.selectbox("Select Movie", ["Avengers", "Pathaan", "Jawan"])
    seats = st.number_input("Seats", min_value=1, max_value=10)
    if st.button("Book Ticket"):
        st.success(f"🎟 Ticket booked for {name} - {movie}")

elif project == "Positive/Negative Checker":
    st.header("➕➖ Positive / Negative Checker")
    num = st.number_input("Enter a Number")
    if st.button("Check"):
        if num > 0:
            st.success("Positive Number")
        elif num < 0:
            st.warning("Negative Number")
        else:
            st.info("Zero")

elif project == "File Transfer App":
    st.header("📁 File Transfer App")
    file = st.file_uploader("Upload File")
    if file:
        st.success("File uploaded successfully")
        st.download_button("Download File", file.read(), file.name)

elif project == "Streamlit Dashboard":
    st.header("📊 Analytics Dashboard")
    df = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Users": [120, 150, 200, 260, 350],
        "Revenue": [2000, 3500, 5000, 6500, 9000]
    })
    col1, col2 = st.columns(2)
    col1.metric("Total Users", df["Users"].sum())
    col2.metric("Total Revenue", f"₹ {df['Revenue'].sum()}")
    st.subheader("User Growth")
    st.line_chart(df.set_index("Month")["Users"])
    st.subheader("Monthly Revenue")
    st.bar_chart(df.set_index("Month")["Revenue"])
    st.subheader("Data Table")
    st.dataframe(df)

elif project == "OpenAI Chat App":
    st.header("🤖 OpenAI Chat Application")
    if "chat" not in st.session_state:
        st.session_state.chat = []
    msg = st.text_input("Type your message")
    if st.button("Send") and msg:
        st.session_state.chat.append(("You", msg))
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": msg}
            ]
        )
        reply = response.choices[0].message.content
        st.session_state.chat.append(("Bot", reply))
    for who, text in st.session_state.chat:
        st.write(f"**{who}:** {text}")

elif project == "Text-to-Speech Tool":
    st.header("🔊 Text to Speech")
    text = st.text_input("Enter Text")
    if st.button("Speak"):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        st.success("Speaking...")

elif project == "XO Game":
    st.header("🎮 XO (Tic Tac Toe) Game")
    if "board" not in st.session_state:
        st.session_state.board = [""] * 9
        st.session_state.turn = "X"
    def winner():
        b = st.session_state.board
        combos = [(0,1,2),(3,4,5),(6,7,8),
                  (0,3,6),(1,4,7),(2,5,8),
                  (0,4,8),(2,4,6)]
        for i, j, k in combos:
            if b[i] == b[j] == b[k] and b[i] != "":
                return b[i]
        if "" not in b:
            return "Draw"
        return None
    cols = st.columns(3)
    for i in range(9):
        with cols[i % 3]:
            if st.button(st.session_state.board[i] or " ", key=i):
                if st.session_state.board[i] == "":
                    st.session_state.board[i] = st.session_state.turn
                    st.session_state.turn = "O" if st.session_state.turn == "X" else "X"
    result = winner()
    if result:
        if result == "Draw":
            st.info("🤝 Match Draw")
        else:
            st.success(f"🏆 Player {result} Wins!")

        if st.button("Restart Game"):
            st.session_state.board = [""] * 9
            st.session_state.turn = "X"

elif project == "Flask API Project (Demo)":
    st.header("🌐 Flask API Demo")
    if st.button("Fetch API Data"):
        st.success("✅ API Data Fetched Successfully")
        st.json({"status": "success", "data": [10, 20, 30, 40]})
