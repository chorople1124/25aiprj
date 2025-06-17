import streamlit as st
import pandas as pd
from PIL import Image
import os

st.title("🌏 세계 주요 국가 대통령/지도자 정보")

# CSV 읽기
df = pd.read_csv("presidents.csv")

# 국가 선택
countries = df["국가"].unique()
selected_country = st.selectbox("국가 선택", countries)

# 선택한 국가 필터링
country_df = df[df["국가"] == selected_country]

# 사진_url 컬럼 제외한 테이블 출력
st.dataframe(country_df.drop(columns=["사진_url"]), use_container_width=True)

# 대통령/지도자 선택
selected = st.selectbox(f"{selected_country} 대통령/지도자 선택", country_df["이름"])
info = country_df[country_df["이름"] == selected].iloc[0]

# 상세 정보 출력
st.markdown(f"""
### ✅ {info['이름']} ({selected_country})
- **재임 기간:** {info['재임 기간']}
- **주요 특징:** {info['주요 특징']}
""")

# 이미지 경로
image_path = info['사진_url']

# 이미지 존재 여부 확인 후 출력
if os.path.exists(image_path):
    img = Image.open(image_path)
    st.image(img, width=250)
else:
    st.error("❗ 이미지 파일을 찾을 수 없습니다. 이미지가 올바른 경로에 있는지 확인하세요.")
