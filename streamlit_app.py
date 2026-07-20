import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Streamlit 요소 예시",
    page_icon="✨",
    layout="wide",
)

st.title("🎉 Streamlit 요소 예시 페이지")
st.caption("한 페이지 안에서 다양한 Streamlit 위젯과 레이아웃을 보여주는 샘플입니다.")

st.markdown("이 페이지는 텍스트, 버튼, 입력창, 선택 위젯, 탭, 아코디언, 차트, 테이블, 폼까지 한 번에 확인할 수 있도록 구성했습니다.")

with st.sidebar:
    st.header("사이드바 위젯")
    name = st.text_input("이름을 입력하세요", placeholder="홍길동")
    color = st.selectbox("좋아하는 색상", ["파란색", "초록색", "노란색"])
    interests = st.multiselect(
        "관심 있는 분야",
        ["데이터 분석", "AI", "웹 앱", "자동화"],
        default=["데이터 분석", "웹 앱"],
    )
    is_subscribed = st.checkbox("뉴스레터 구독")
    difficulty = st.slider("난이도", 1, 10, 5)

    st.markdown("---")
    st.info(f"입력값 요약: {name} / {color} / {', '.join(interests) or '없음'}")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("조회수", "1,234", "+12%")
with col2:
    st.metric("사용자", "89", "+4%")
with col3:
    st.metric("완료율", "76%", "-2%")
with col4:
    st.metric("평균 응답시간", "1.2s", "-0.1s")

st.markdown("---")

if st.button("클릭해 보세요"):
    st.success("버튼이 눌렸습니다!")

st.subheader("탭으로 섹션 나누기")

tab1, tab2, tab3 = st.tabs(["텍스트", "테이블", "차트"])

with tab1:
    st.write("이곳은 기본 텍스트와 코드 블록을 보여주는 영역입니다.")
    st.code("import streamlit as st\nst.write('Hello, Streamlit!')", language="python")
    st.json({"name": name, "color": color, "difficulty": difficulty})

with tab2:
    sample_df = pd.DataFrame(
        {
            "이름": ["Alice", "Bob", "Charlie"],
            "점수": [90, 85, 88],
            "등급": ["A", "B", "B"],
        }
    )
    st.dataframe(sample_df, use_container_width=True)
    st.download_button(
        label="CSV로 다운로드",
        data=sample_df.to_csv(index=False),
        file_name="sample_data.csv",
        mime="text/csv",
    )

with tab3:
    chart_df = pd.DataFrame(
        {
            "월": ["1월", "2월", "3월", "4월", "5월"],
            "매출": [20, 35, 28, 40, 55],
            "목표": [25, 30, 30, 35, 50],
        }
    )
    st.line_chart(chart_df.set_index("월"))

st.markdown("---")

with st.expander("추가 정보 보기"):
    st.write("아코디언 안에 설명, 참고 링크, 또는 작은 예제를 넣을 수 있습니다.")
    st.link_button("Streamlit 공식 문서", "https://docs.streamlit.io/")

st.subheader("폼 예제")
with st.form("demo_form"):
    feedback = st.text_area("의견을 남겨주세요", placeholder="예: 페이지 구성이 깔끔합니다.")
    submitted = st.form_submit_button("제출")

    if submitted:
        st.success(f"제출 완료: {feedback}")

st.markdown("---")

st.warning("이 페이지는 예시용으로 구성된 샘플입니다.")
st.success("필요하면 이 예시를 바탕으로 실제 앱으로 확장할 수 있습니다.")
