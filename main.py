import streamlit as st
import pandas as pd
from PIL import Image
import os

st.title("🇰🇷 대한민국 역대 대통령 정보")

df = pd.read_csv("presidents.csv")

st.dataframe(df.drop(columns=["사진_url"]), use_container_width=True)

selected = st.selectbox("대통령 선택", df["이름"])
info = df[df["이름"] == selected].iloc[0]

st.markdown(f"""
### ✅ {info['이름']} 대통령
- **재임 기간:** {info['재임 기간']}
- **주요 특징:** {info['주요 특징']}
""")

# 이미지 경로가 그냥 파일명 (main.py와 같은 폴더)
image_path = info['사진_url']
st.write(f"이미지 경로: {image_path}")

if os.path.exists(image_path):
    img = Image.open(image_path)
    st.image(img, width=250)
else:
    st.error("❗ 이미지 파일을 찾을 수 없습니다. main.py와 같은 폴더에 이미지가 있는지 확인하세요.")
