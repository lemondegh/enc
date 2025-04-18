from funcs import *
from config import *
import pandas as pd
import os
import time

st.subheader('매핑 요청청', divider=True)
st.markdown(
    ":blue-badge[:material/star: ] :gray-badge[표준 매핑 요청 후 진행상황 확인을 위한 모니터링 화면]"
)

# with st.spinner('매핑요청 목록을 조회 중입니다.'):
#     time.sleep(1.5)
    
file = os.path.join(DATA_FOLDER, '요청 모니터링.xlsx')
df = pd.read_excel(file)
df = df.fillna(" ")
df.drop(['선택', '구분', '상세'], inplace=True, axis=1)
df['선택'] = False

column_to_move = '선택'

# 컬럼 재배치
columns = list(df.columns) 
columns.remove(column_to_move)  
columns.insert(1, column_to_move)  # 두 번째 위치에 삽입
df = df[columns]  # 새로운 순서로 DataFrame 재구성

df["현장코드"] = df["현장코드"].astype(str)

col1, col2 = st.columns([1,9])

req = None
exp = True
with col1:
    req = st.button('매핑 요청')
with col2:

    document = '''
        <p style='padding-top:6px'> 행을 선택 후 매핑을 요청하시기 바랍니다. </p>
    '''
    st.markdown(document, unsafe_allow_html=True)

with st.expander('조회 목록', expanded=exp):
    st.data_editor(df, height=600, use_container_width=True, hide_index=True)

if req:
    with st.spinner("SmartTA에 내역 매핑을 요청하고 있습니다...", show_time=True):
        st.image('./images/nginx.jpg', use_column_width=True)
        time.sleep(5)

        # file = os.path.join(DATA_FOLDER, '요청 모니터링_RES.xlsx')
        # df = pd.read_excel(file)
        # df = df.fillna(" ")

        # st.data_editor(df, height=800, use_container_width=True, hide_index=True)
        
        st.info(
            ":blue-badge[:material/star: ] :gray-badge[예산내역결과 조회를 통해 확인할 수 있습니다.]"
        )