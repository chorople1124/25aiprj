import streamlit as st
import pandas as pd
from PIL import Image
import os

st.set_page_config(page_title="🌏 세계 대통령 정보", layout="centered")

st.title("🌏 세계 주요 국가 대통령/지도자 정보")

# CSV 읽기
df = pd.read_csv("presidents.csv")

# 국가 선택
countries = df["국가"].unique()
selected_country = st.selectbox("국가 선택", countries)

# 선택한 국가 필터링
country_df = df[df["국가"] == selected_country]

# 테이블 출력
st.dataframe(country_df.drop(columns=["사진_url"]), use_container_width=True)

# 지도자 선택
selected = st.selectbox(f"{selected_country} 대통령/지도자 선택", country_df["이름"])
info = country_df[country_df["이름"] == selected].iloc[0]

# 정보 출력
st.markdown(f"""
### ✅ {info['이름']} ({selected_country})
- **재임 기간:** {info['재임 기간']}
- **주요 특징:** {info['주요 특징']}
""")

# 이미지 출력
image_path = info["사진_url"]
if os.path.exists(image_path):
    st.image(Image.open(image_path), width=250)
else:
    st.error("❗ 이미지가 없습니다.")

# 명언 페이지로 이동 안내
st.markdown("---")
st.markdown("👉 아래 버튼을 눌러 **명언 페이지로 이동**하세요.")

# 버튼 클릭 시 유저에게 페이지 전환 안내
if st.button("💬 명언 페이지로 이동"):
    st.success("좌측 상단 사이드바에서 **💬 명언 모음** 페이지를 클릭하세요!")
