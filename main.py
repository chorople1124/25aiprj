import streamlit as st
import pandas as pd

# 타이틀
st.title("🇰🇷 대한민국 역대 대통령 정보")

# CSV 파일 불러오기
df = pd.read_csv("presidents.csv")

# 테이블 출력
st.dataframe(df, use_container_width=True)

# 선택한 대통령 상세 보기
selected = st.selectbox("대통령 선택", df["이름"])
info = df[df["이름"] == selected].iloc[0]

st.markdown(f"""
### ✅ {info["이름"]} 대통령
- **재임 기간:** {info["재임 기간"]}
- **주요 특징:** {info["주요 특징"]}
""")
