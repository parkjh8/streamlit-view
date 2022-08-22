import streamlit as st
view =[100,150,30]
st.write('# your view')
st.write('## raw')
view
st.write('## bar Chart')
st.bar_chart(view)
import pandas as pd
sview = pd.Series(view)
sview