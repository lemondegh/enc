from funcs import *
from config import *
import pandas as pd
import os
import numpy as np

st.subheader('내역별 표준단가 산출')

tab1, tab2 = st.tabs(['외주 계약 조회', '표준단가 산출'])

with tab1:
    ret = st.button('외주계약 조회')

    if ret:
        file = os.path.join(DATA_FOLDER, '표준단가산출용 외주계약 정보.xlsx')
        df = pd.read_excel(file)
        df = df.fillna(" ")

        df['선택'] = True

        column_to_move = '선택'

        # 컬럼 재배치
        columns = list(df.columns) 
        columns.remove(column_to_move)  
        columns.insert(1, column_to_move)  # 두 번째 위치에 삽입
        df = df[columns]  # 새로운 순서로 DataFrame 재구성

        with st.expander('외주계약 정보', expanded=True):
            st.data_editor(df, hide_index=True, height=220, use_container_width=True)    

with tab2:
    calc_unit_price = st.button('표준단가 산출')

    if calc_unit_price:
        file = os.path.join(DATA_FOLDER, '표준단가 산출.xlsx')
        df = pd.read_excel(file)
        df = df.fillna(" ")

        df['단가(표준)'] = np.floor(df['단가(표준)']).astype(int)
        df['대비(표준)'] = np.floor(df['대비(표준)']).astype(int)

        # df['단가(외주1)'] = np.floor(df['단가(외주1)']).astype(int)
        df['대비(외주1)'] = np.floor(df['대비(외주1)']).astype(int)
        # df['단가(외주2)'] = np.floor(df['단가(외주2)']).astype(int)
        df['대비(외주2)'] = np.floor(df['대비(외주2)']).astype(int)
        # df['단가(외주3)'] = np.floor(df['단가(외주3)']).astype(int)
        df['대비(외주3)'] = np.floor(df['대비(외주3)']).astype(int)
        # df['단가(외주4)'] = np.floor(df['단가(외주4)']).astype(int)
        df['대비(외주4)'] = np.floor(df['대비(외주4)']).astype(int)
        # df['단가(외주5)'] = np.floor(df['단가(외주5)']).astype(int)
        df['대비(외주5)'] = np.floor(df['대비(외주5)']).astype(int)


        with st.expander('표준단가 산출', expanded=True):
            st.data_editor(df, hide_index=True, height=800, use_container_width=True)    


