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

# 로컬 이미지 경로 생성 후 출력
image_path = os.path.join("images", info['사진_url'])
img = Image.open(image_path)
st.image(img, width=250)
