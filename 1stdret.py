from funcs import *
from config import *
import pandas as pd
import os
import time 

st.subheader('표준 내역 및 단가 조회', divider=True)
st.markdown(
    ":blue-badge[:material/star: ] :gray-badge[등록한 표준내역과 표준단가를 조회하는 화면]"
)

tab1, tab2 = st.tabs(['표준내역 조회','표준단가 조회'])

with tab1:
    with st.spinner('표준내역을 조회 중입니다.'):
        time.sleep(1)

    file = os.path.join(DATA_FOLDER, '표준내역 조회.xlsx')
    df = pd.read_excel(file)
    df = df.fillna(" ")


    st.dataframe(df, hide_index=True, height=1000, use_container_width=True)
with tab2:
    with st.spinner('표준단가를 조회 중입니다.'):
        time.sleep(1)

    file = os.path.join(DATA_FOLDER, '표준단가 조회.xlsx')
    df = pd.read_excel(file)
    df = df.fillna(" ")

    st.dataframe(df, hide_index=True, height=1000, use_container_width=True)