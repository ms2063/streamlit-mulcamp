# _*_ coding:utf-8 _*_

import streamlit as st
import seaborn as sns
import pandas as pd

@st.cache_data # decorator, 함수의 중급 레벨 사용법
def load_data():
    #df = sns.load_dataset("iris")
    df = sns.load_dataset("tips")
    return df


def main():
    st.write(st.__version__)
    st.write(sns.__version__)
    st.write(pd.__version__)

    tips = load_data()
    st.dataframe(tips, use_container_width = True)

    st.write("-" * 50)
    st.title("st.metric()")
    tip_max = tips['tip'].max() # 최대값
    tip_min = tips['tip'].min() # 최소값

    st.metric(label = "팁 최고금액", value = tip_max, delta = tip_max - tip_min)
    st.metric(label = "팁 최소금액", value = tip_min, delta = tip_min - tip_max)

    st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

    st.write("This is some text.")

    st.slider("This is a slider", 0, 100, (25, 75))

    st.divider()  # 👈 Draws a horizontal rule

    st.write("This text is between the horizontal rules.")

    st.divider()  # 👈 Another horizontal rule

    df1 = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
    edited_df = st.data_editor(df1)

    favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
    st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

    st.markdown('''
    $$\mathbb{N} = \{ a \in \mathbb{Z} : a > 0 \}$$
''')

if __name__ == "__main__":
    main()
#ch02.py 파일 생성
