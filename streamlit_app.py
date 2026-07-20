import streamlit as st

st.set_page_config(
    page_title="자기소개 페이지",
    page_icon="🎵",
    layout="wide",
)

st.title("안녕하세요! 저는 음악을 가르치는 교사입니다.")
st.caption("학생들의 음악성을 키우기 위한 동기부여를 만드는 것을 좋아합니다.")

image_col, text_col = st.columns([0.9, 1.1])

with image_col:
    st.image(
        "https://images.unsplash.com/photo-1516280440614-37939bbacd81?auto=format&fit=crop&w=1200&q=80",
        caption="음악과 함께하는 순간",
        width=500,
    )

with text_col:
    st.subheader("소개")
    st.write("""
    - 이름: 신옥찬
    - 직업: 중학교음악교사 / 앱 개발 꿈나무
    - 관심 분야: Python, Streamlit, 데이터 시각화, 웹 서비스
    - 목표: 사용자에게 실용적이고 깔끔한 경험을 제공하는 앱을 만드는 것
    """)

st.markdown("---")

st.subheader("기술 스택")
tech_skills = ["Python", "Streamlit", "Pandas", "HTML/CSS", "Git"]
st.progress(0.85, text="기술 역량 성장 중")
st.write(tech_skills)

st.markdown("---")

st.subheader("관심사")
interest_options = ["데이터 시각화", "자동화", "AI 서비스", "사용자 경험 개선"]
selected_interests = st.multiselect(
    "제가 관심 있는 주제를 선택해보세요",
    interest_options,
    default=["데이터 시각화", "AI 서비스"],
)
st.write(f"선택한 관심사: {', '.join(selected_interests) if selected_interests else '없음'}")

st.markdown("---")

st.subheader("연락처")
contact_col1, contact_col2 = st.columns(2)
with contact_col1:
    st.link_button("GitHub", "https://github.com")
with contact_col2:
    st.link_button("Email", "mailto:example@email.com")
