from funcs import *
from config import *
import pandas as pd
import os
import numpy as np

st.subheader('표준 내역 및 단가 등록')


@st.cache_data
def get_data():
    df = pd.DataFrame(
        np.random.randn(50, 20), columns=("col %d" % i for i in range(20))
    )
    return df

@st.cache_data
def convert_for_download(df):
    return df.to_csv().encode("utf-8")

df_down = get_data()
csv = convert_for_download(df_down)


tab1, tab2 = st.tabs(['표준내역 이력', '표준단가 이력'])

with tab1:
    # st.image('./images/표준내역 이력.png')
    file = os.path.join(DATA_FOLDER, '표준내역 이력.xlsx')
    df = pd.read_excel('./data/표준내역 이력.xlsx')
    df = df.fillna(" ")
    df['선택'] = False
    print(df)

    column_to_move = '선택'

    # 컬럼 재배치
    columns = list(df.columns) 
    columns.remove(column_to_move)  
    columns.insert(1, column_to_move)  # 두 번째 위치에 삽입
    df = df[columns]  # 새로운 순서로 DataFrame 재구성

    
    col1, col2, col3 = st.columns([2, 7, 2])
    with col1:
        st.button('표준내역 업로드')
    with col2:
        st.download_button(
            label="표준내역 다운로드",
             data=csv,
            file_name="data.csv",
            mime="text/csv",
            icon=":material/download:",
        )
    with col3:
        pass

    st.data_editor(df, height=1000, use_container_width=True, hide_index=True)
with tab2:
    # st.image('./images/표준내역 이력.png')
    file = os.path.join(DATA_FOLDER, '표준단가 이력.xlsx')
    df = pd.read_excel(file)
    df = df.fillna(" ")
    df['선택'] = False
    print(df)

    column_to_move = '선택'

    # 컬럼 재배치
    columns = list(df.columns) 
    columns.remove(column_to_move)  
    columns.insert(1, column_to_move)  # 두 번째 위치에 삽입
    df = df[columns]  # 새로운 순서로 DataFrame 재구성

    
    col1, col2, col3 = st.columns([2, 7, 2])
    with col1:
        st.button('표준단가 업로드', type="primary")
    with col2:
        st.download_button(
            label="표준단가 다운로드",
             data=csv,
            file_name="data.csv",
            mime="text/csv",
            icon=":material/download:",
        )
    with col3:
        pass

    st.data_editor(df, height=1000, use_container_width=True, hide_index=True)
    