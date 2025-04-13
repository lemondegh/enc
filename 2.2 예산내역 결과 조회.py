from funcs import *
from config import *
import pandas as pd
import os

st.subheader('예산내역 결과 조회')

# st.image('./images/운영예산 내역 결과 조회.jpg')
    
file = os.path.join(DATA_FOLDER, '매핑결과 조회.xlsx')
df = pd.read_excel(file)
df = df.fillna(" ")

st.dataframe(df, hide_index=True, height=1000, use_container_width=True)