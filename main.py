import streamlit as st
import pandas as pd
from PIL import Image
import os

st.title("🇰🇷 대한민국 역대 대통령 정보")

# CSV 읽기
df = pd.read_csv("presidents.csv")

# 사진_url 컬럼 빼고 데이터프레임 출력
st.dataframe(df.drop(columns=["사진_url"]), use_container_width=True)

# 대통령 선택박스
selected = st.selectbox("대통령 선택", df["이름"])
info = df[df["이름"] == selected].iloc[0]

# 대통령 정보 출력
st.markdown(f"""
### ✅ {info['이름']} 대통령
- **재임 기간:** {info['재임 기간']}
- **주요 특징:** {info['주요 특징']}
""")

# 이미지 경로 생성 및 존재 여부 확인
image_path = os.path.join("images", info['사진_url'])
st.write(f"이미지 경로: {image_path}")  # 경로 확인용

if os.path.exists(image_path):
    img = Image.open(image_path)
    st.image(img, width=250)
else:
    st.error("❗ 이미지 파일을 찾을 수 없습니다. 'images' 폴더에 사진 파일을 넣었는지 확인하세요.")
