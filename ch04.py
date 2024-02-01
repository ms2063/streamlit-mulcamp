# _*_ coding:utf-8 _*_
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.graph_objects as go 
import plotly.express as px 
from plotly.subplots import make_subplots 
import plotly

@st.cache_data
def load_data():
    df = sns.load_dataset('tips')
    return df


def main():
    st.write(plotly.__version__)
    st.title("Streamlit with Matplotlib")
    tips = load_data()

    # 시각화 아무거나
     # 데이터가공
    m_tips = tips.loc[tips['sex'] == 'Male', :]
    f_tips = tips.loc[tips['sex'] == 'Female', :]
    # 시각화 차트
    fig, ax = plt.subplots(ncols=2, figsize=(10, 6), sharex=True, sharey=True)
    ax[0].scatter(x = m_tips['total_bill'], y = m_tips['tip'])
    ax[0].set_title('Male')
    ax[1].scatter(x = f_tips['total_bill'], y = f_tips['tip'])
    ax[1].set_title('Female')
    st.pyplot(fig)

    # seaborn으로 시각화 코드 아무거나 작성
    fig, ax = plt.subplots()
    #seaborn 코드 아무거나 작성
    #sns.barplot(x = m_tips['total_bill'], y = m_tips['tip'])
    fig, ax = plt.subplots(ncols=2, figsize=(10, 6), sharex=True, sharey=True)
    sns.scatterplot(data=m_tips, x = 'total_bill', y = 'tip', ax=ax[0])
    ax[0].set_title('Male')
    sns.scatterplot(data=f_tips, x = 'total_bill', y = 'tip', ax=ax[1])
    ax[0].set(xlabel=None, ylabel=None)
    ax[1].set_title('Female')
    ax[1].set(xlabel=None, ylabel=None)
    st.pyplot(fig)

    # plotly
    fig = px.scatter(tips, x = 'total_bill', y = 'tip')
    st.plotly_chart(fig, use_container_width=True)
if __name__ == "__main__":
    main()
