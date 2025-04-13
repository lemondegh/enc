from funcs import *
from config import *
import pandas as pd
import os

st.subheader('표준 내역 및 단가 조회')

tab1, tab2 = st.tabs(['표준내역 조회','표준단가 조회'])

with tab1:

    file = os.path.join(DATA_FOLDER, '표준내역 조회.xlsx')
    df = pd.read_excel(file)
    df = df.fillna(" ")


    st.dataframe(df, hide_index=True, height=1000, use_container_width=True)
with tab2:

    file = os.path.join(DATA_FOLDER, '표준단가 조회.xlsx')
    df = pd.read_excel(file)
    df = df.fillna(" ")

    st.dataframe(df, hide_index=True, height=1000, use_container_width=True)