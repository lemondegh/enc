from funcs import *
from config import *
import pandas as pd
import os
import time 

st.subheader('예산내역 결과 조회', divider=True)
st.markdown(
    ":blue-badge[:material/star: ] :gray-badge[표준 매핑 결과를 조회하는 화면]"
)

with st.spinner('예산내역 결과를 조회 중입니다.'):
    time.sleep(1.5)
    
file = os.path.join(DATA_FOLDER, '매핑결과 조회.xlsx')
df = pd.read_excel(file)
df = df.fillna(" ")

st.dataframe(df, hide_index=True, height=1000, use_container_width=True)