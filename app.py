import streamlit as st
import random

st.title("🎋 おみくじアプリ")

st.write("今日の運せいは？")

if st.button("おみくじを引く"):
    omikuji = random.choice(["大吉", "中吉", "小吉", "吉", "凶"])
    
    if omikuji == "大吉":
        st.success(f"🎉 {omikuji}！！ さいこうだ！")
        st.balloons()
    elif omikuji == "中吉":
        st.success(f"😊 {omikuji}！ いいね！")
    elif omikuji == "小吉":
        st.info(f"🙂 {omikuji} まあまあだね")
    elif omikuji == "吉":
        st.info(f"😐 {omikuji} ふつうだね")
    else:
        st.error(f"😢 {omikuji}... 明日がんばろう！")
