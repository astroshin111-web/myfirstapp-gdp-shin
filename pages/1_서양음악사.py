import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(
    page_title="서양음악사",
    page_icon="🎼",
    layout="wide",
)

st.title("서양음악사")
st.caption("대표적인 음악가들의 이미지와 생몰연대를 정리한 페이지입니다.")

composers = [
    {
        "name": "요한 세바스티안 바흐",
        "birth": "1685",
        "death": "1750",
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/6a/Johann_Sebastian_Bach.jpg",
    },
    {
        "name": "볼프강 아마데우스 모차르트",
        "birth": "1756",
        "death": "1791",
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Mozart%28small%29.jpg",
    },
    {
        "name": "루트비히 판 베토벤",
        "birth": "1770",
        "death": "1827",
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Beethoven.jpg",
    },
    {
        "name": "요하네스 브람스",
        "birth": "1833",
        "death": "1897",
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/1f/Brahms.jpg",
    },
]

cols = st.columns(2)
for i, composer in enumerate(composers):
    with cols[i % 2]:
        st.image(composer["image"], width=220)
        st.subheader(composer["name"])
        st.write(f"생몰연대: {composer['birth']} ~ {composer['death']}")
        st.markdown("---")

st.markdown("---")
st.subheader("간단한 데이터 시각화 예시")

viz_df = pd.DataFrame(
    {
        "음악가": ["바흐", "모차르트", "베토벤", "브람스"],
        "출생년도": [1685, 1756, 1770, 1833],
        "사망년도": [1750, 1791, 1827, 1897],
    }
)

matplotlib_fig, ax = plt.subplots()
ax.bar(viz_df["음악가"], viz_df["출생년도"], color="skyblue", label="출생년도")
ax.set_title("음악가 출생년도 비교")
ax.set_ylabel("년도")
ax.set_xticklabels(viz_df["음악가"], rotation=20)
ax.legend()
plt.tight_layout()
st.pyplot(matplotlib_fig)

seaborn_fig = sns.relplot(
    data=viz_df,
    x="출생년도",
    y="사망년도",
    size="출생년도",
    hue="음악가",
    sizes=(50, 250),
)
seaborn_fig.fig.suptitle("출생년도와 사망년도 관계")
st.pyplot(seaborn_fig.fig)

plotly_fig = px.scatter(
    viz_df,
    x="출생년도",
    y="사망년도",
    text="음악가",
    size="출생년도",
    color="음악가",
)
plotly_fig.update_layout(title="음악가 생애 연도 분포")
st.plotly_chart(plotly_fig, use_container_width=True)