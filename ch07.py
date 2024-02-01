# -*- coding:utf-8 -*-

import streamlit as st
import pandas as pd
import yfinance as yf

def main():
    st.sidebar.title("Stock Chart")

# ticker 텍스트 구현
    ticker = st.sidebar.text_input("Enter a ticker (e.g. AAPL)", value="AAPL")
    st.sidebar.markdown('Tickers Link : [All Stock Symbols](https://stockanalysis.com/stocks/)')

# 날짜 입력 구현
    start_date = st.sidebar.date_input("검색 시작일", value = pd.to_datetime("2023-01-01"))
    end_date = st.sidebar.date_input("검색 종료일", value = pd.to_datetime("today"))

# 데이터 다운로드
    data = yf.download(ticker, start = start_date, end = end_date)
    st.table(data)

if __name__ == "__main__":
    main()
