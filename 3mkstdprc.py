from funcs import *
from config import *
import pandas as pd
import os
import numpy as np
import time 

st.subheader('내역별 표준단가 산출', divider=True)
st.markdown(
    ":blue-badge[:material/star: ] :gray-badge[외주계약 단가를 근거로 당분기 표준단가를 산출하는 화면(외주계약에서 조회되는 단가 활용)]"
)

tab1, tab2 = st.tabs(['외주 계약 조회', '표준단가 산출'])

def color_blue_column(col):
    return ['color: blue' for _ in col]

def color_red_column(col):
    return ['color: red' for _ in col]

def color_backgroubd_column(val):
    color = '#dee5d8' # if val else 'red'
    return f'background-color: {color}'

@st.dialog("외주계약 정보", width='large')
def show_dialog():
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

    st.data_editor(df, hide_index=True, height=220, use_container_width=True)
    selected = st.button('선택')

    if selected:
        st.rerun()

with tab1:
    ret = st.button('외주계약 조회')

    if ret:
        # dialog
        show_dialog()

with tab2:
    file = os.path.join(DATA_FOLDER, '표준단가 산출.xlsx')
    df = pd.read_excel(file)
    df = df.fillna(" ")

    # df['단가(표준)'] = np.floor(df['단가(표준)']).astype(int)
    # df['대비(표준,%)'] = np.floor(df['대비(표준,%)']).astype(int)

    # df['단가(외주1)'] = np.floor(df['단가(외주1)']).astype(int)
    # df['대비(외주1)]'] = np.floor(df['대비(외주1)]']).astype(int)
    # df['단가(외주2)'] = np.floor(df['단가(외주2)']).astype(int)
    # df['대비(외주2)]'] = np.floor(df['대비(외주2)]']).astype(int)
    # df['단가(외주3)'] = np.floor(df['단가(외주3)']).astype(int)
    # df['대비(외주3)]'] = np.floor(df['대비(외주3)]']).astype(int)
    # df['단가(외주4)'] = np.floor(df['단가(외주4)']).astype(int)
    # df['대비(외주4)]'] = np.floor(df['대비(외주4)]']).astype(int)
    # df['단가(외주5)'] = np.floor(df['단가(외주5)']).astype(int)
    # df['대비(외주5)]'] = np.floor(df['대비(외주5)]']).astype(int)


    # with st.expander('표준단가 산출', expanded=True):
    with st.spinner('표준단가를 산출하고 있습니다.'):
        time.sleep(2)

        styled_df = (df.style.applymap(color_backgroubd_column, subset=['단가(외주1)'])
              .applymap(color_backgroubd_column, subset=['단가(외주2)'])
              .applymap(color_backgroubd_column, subset=['단가(외주3)'])
              .applymap(color_backgroubd_column, subset=['단가(외주4)'])
              .applymap(color_backgroubd_column, subset=['단가(외주5)'])
              .applymap(color_backgroubd_column, subset=['단가(표준)'])
        )
        
        # st.data_editor(df, hide_index=True, height=800, use_container_width=True)    
        st.data_editor(styled_df, hide_index=True, height=800, use_container_width=True)    
        # st.dataframe(styled_df, hide_index=True, height=800, use_container_width=True)    

        print(styled_df)
