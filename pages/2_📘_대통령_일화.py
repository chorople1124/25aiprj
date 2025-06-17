import streamlit as st
import pandas as pd

st.set_page_config(page_title="대통령 일화 모음", layout="centered")
st.title("📘 대통령/지도자 일화 모음")

# CSV 파일 불러오기
try:
    df = pd.read_csv("anecdotes.csv")
except FileNotFoundError:
    st.error("❗ 'anecdotes.csv' 파일이 프로젝트 루트에 존재해야 합니다.")
    st.stop()

# 국가 선택
countries = df["국가"].unique()
selected_country = st.selectbox("국가 선택", countries)

# 선택된 국가에 따른 인물 필터링
filtered_df = df[df["국가"] == selected_country]
selected_name = st.selectbox("인물 선택", filtered_df["이름"])

# 선택된 인물의 일화 출력
anecdote = filtered_df[filtered_df["이름"] == selected_name]["일화"].values[0]

st.markdown(f"""
### ✅ {selected_name} ({selected_country})
> {anecdote}
""")

# 구분선
st.markdown("---")
st.info("👈 왼쪽 사이드바에서 다른 페이지로 이동할 수 있습니다.")
