import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="음악교사 소개 앱",
    page_icon="🎵",
    layout="wide",
)

st.sidebar.title("메뉴")
page = st.sidebar.radio(
    "페이지 선택",
    ["홈", "출석", "수업자료", "질문"],
    index=0,
)


def show_home():
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


def show_attendance():
    st.title("출석")
    st.write("오늘의 출석 현황을 확인해보세요.")

    attendance_data = pd.DataFrame(
        {
            "학생": ["김민수", "이서연", "박지훈", "최유진"],
            "상태": ["출석", "결석", "지각", "출석"],
            "메모": ["좋은 참여", "보강 필요", "조용히 참여", "정상"],
        }
    )
    st.dataframe(attendance_data, use_container_width=True)


def show_materials():
    st.title("수업자료")
    st.write("이번 수업에 필요한 자료를 정리해두었습니다.")

    st.success("1. 음악 이론 요약 자료")
    st.success("2. 리듬 연습 시트")
    st.success("3. 합주 안내문")

    with st.expander("추가 자료 보기"):
        st.write("- 악보 예시")
        st.write("- 연습 동영상 링크")
        st.write("- 평가 기준표")


def show_questions():
    st.title("질문")
    st.write("학생들이 궁금한 점을 남겨주세요.")

    with st.form("question_form"):
        name = st.text_input("이름")
        question = st.text_area("질문 내용")
        submitted = st.form_submit_button("제출")

        if submitted:
            st.success(f"질문이 접수되었습니다. {name}님 감사합니다.")


if page == "홈":
    show_home()
elif page == "출석":
    show_attendance()
elif page == "수업자료":
    show_materials()
else:
    show_questions()
