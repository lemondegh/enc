import streamlit as st

st.set_page_config(layout="wide")

st.sidebar.markdown('''
    :ballot_box_with_check: **표준내역 매핑 시스템**
''')

pages = {
    "1. 표준 관리": [
        st.Page("1.1 표준 내역 및 단가 등록.py", title="표준 내역 및 단가 등록"),
        st.Page("1.2 표준 내역 및 단가 조회.py", title="표준 내역 및 단가 조회"),
    ],
    "2. 매핑 관리": [
        st.Page("2.1 매핑 요청.py", title="매핑 요청"),
        st.Page("2.2 예산내역 결과 조회.py", title="예산내역 결과 조회"),
    ],
    "3. 단가 관리": [
        st.Page("3.1 내역별 표준단가 산출.py", title="내역별 표준단가 산출"),
    ],
}

pg = st.navigation(pages)
pg.run()