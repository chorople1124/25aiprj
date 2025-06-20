
import streamlit as st

st.set_page_config(page_title="명언 모음집")

# 명언 사전
quotes = {
    "이승만": "나는 공산주의자와는 협상하지 않는다.",
    "박정희": "잘 살아보세, 우리도 한 번 잘 살아보세!",
    "김대중": "행동하지 않는 양심은 악의 편이다.",
    "노무현": "사람 사는 세상.",
    "문재인": "기회는 평등할 것입니다. 과정은 공정할 것입니다. 결과는 정의로울 것입니다.",
    "윤석열": "자유는 우리 헌법의 핵심 가치입니다.",
    "조 바이든": "America is an idea. An idea stronger than any army.",
    "버락 오바마": "Yes, we can.",
    "도널드 트럼프": "Make America Great Again.",
    "시진핑": "중화민족의 위대한 부흥은 반드시 실현될 것이다.",
    "아베 신조": "강한 일본을 만들겠습니다.",
    "스가 요시히데": "국민을 위해 성실히 일하겠습니다.",
    "기시다 후미오": "정치의 신뢰 회복이 중요합니다.",
    "김정은": "우리는 결심하면 무조건 합니다.",
    "김정일": "인민을 위한 정치가 진짜 정치다.",
    "김일성": "우리식 사회주의는 영원하다.",
}

st.title("💬 대통령/지도자 명언 모음집")

for name, quote in quotes.items():
    st.markdown(f"**{name}**: _\"{quote}\"_")
