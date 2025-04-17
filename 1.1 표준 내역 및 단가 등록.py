from funcs import *
from config import *
import pandas as pd
import os
import numpy as np
import io
import time 

buffer = io.BytesIO()

st.subheader('표준 내역 및 단가 등록', divider=True)
st.markdown(
    ":blue-badge[:material/star: ] :gray-badge[표준내역과 표준단가를 등록하고 이력을 조회하는 화면]"
)

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

@st.dialog("표준내역 업로드", width='large')
def show_dialog_items():
    file = os.path.join(DATA_FOLDER, '표준내역_업로드용.xlsx')
    df = pd.read_excel(file)
    df = df.fillna(" ")

    st.data_editor(df, hide_index=True, height=400, width=100,use_container_width=True)
    col1, col2, col3 = st.columns([2, 7, 2])
    with col1:
        selected = st.button('업로드')
    with col3:
        cancel = st.button('취소')
    with col2:
        pass 

    if selected:
        with st.spinner('표준내역을 업로드 중입니다.'):
            time.sleep(2)
        st.rerun()
    if cancel:
        st.rerun()

@st.dialog("표준단가 업로드", width='large')
def show_dialog_unit_price():
    file = os.path.join(DATA_FOLDER, '표준단가_업로드용.xlsx')
    df = pd.read_excel(file)
    df = df.fillna(" ")

    st.data_editor(df, hide_index=True, height=400, width=100,use_container_width=True)
    col1, col2, col3 = st.columns([2, 7, 2])
    with col1:
        selected = st.button('업로드')
    with col3:
        cancel = st.button('취소')
    with col2:
        pass 

    if selected:
        with st.spinner('표준단가를 업로드 중입니다.'):
            time.sleep(2)
        st.rerun()
    if cancel:
        st.rerun()

tab1, tab2 = st.tabs(['표준내역 이력', '표준단가 이력'])

with tab1:
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

    
    col1, col2, col3 = st.columns([3, 7, 3])
    with col1:
        upload = st.button('표준내역 업로드')
    with col3:
        file = os.path.join(DATA_FOLDER, '표준내역_업로드용.xlsx')
        df_down = df.fillna(" ")
        df_down = pd.read_excel(file)

        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            # Write each dataframe to a different worksheet.
            df_down.to_excel(writer, sheet_name='Sheet1', index=False)

        st.download_button(
            label="표준내역 다운로드",
            data=buffer,
            file_name="표준내역.xlsx",
            mime="application/vnd.ms-excel",
            icon=":material/download:",
            help='목록에서 대상 선택 후 다운로드하세요.'
        )
    with col2:
        pass

    st.data_editor(df, height=400, use_container_width=True, hide_index=True)

    if upload:
        show_dialog_items()


with tab2:
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

    
    col1, col2, col3 = st.columns([3, 7, 3])
    with col1:
        upload = st.button('표준단가 업로드')
    with col3:
        file = os.path.join(DATA_FOLDER, '표준단가_업로드용.xlsx')
        df_down = df.fillna(" ")
        df_down = pd.read_excel(file)

        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            # Write each dataframe to a different worksheet.
            df_down.to_excel(writer, sheet_name='Sheet1', index=False)

        st.download_button(
            label="표준단가 다운로드",
            data=buffer,
            file_name="표준단가.xlsx",
            mime="application/vnd.ms-excel",
            icon=":material/download:",
            help='목록에서 대상 선택 후 다운로드하세요.'
        )
    with col2:
        pass

    st.data_editor(df, height=400, use_container_width=True, hide_index=True)
    
    if upload:  
        show_dialog_unit_price()