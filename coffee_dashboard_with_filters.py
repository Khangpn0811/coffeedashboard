import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title='Vietnam Coffee Market Dashboard', layout='wide')

st.title('🇻🇳 Vietnam Coffee Market Dashboard (Upgraded)')

# ------------------------
# Sidebar
# ------------------------
st.sidebar.header('⚙️ Settings')

# Bộ lọc: chọn kịch bản
scenario = st.sidebar.selectbox('Chọn kịch bản:', ['High', 'Medium', 'Low'])

# Bộ lọc: chọn khoảng thời gian
months_full = ['Jul 2025', 'Aug 2025', 'Sep 2025', 'Oct 2025', 'Nov 2025', 'Dec 2025',
               'Jan 2026', 'Feb 2026', 'Mar 2026', 'Apr 2026', 'May 2026', 'Jun 2026']
months_selected = st.sidebar.multiselect('Chọn các tháng:', months_full, default=months_full)

# Bộ lọc: bật/tắt module
show_map = st.sidebar.checkbox('Hiển thị bản đồ thị phần', True)
show_alert = st.sidebar.checkbox('Hiển thị cảnh báo rủi ro', True)

# ------------------------
# Giả lập dữ liệu giá
# ------------------------
high = np.arange(6300, 7400+100, 100)
medium = np.arange(6300, 6850+50, 50)
low = np.arange(6200, 6420+20, 20)

df = pd.DataFrame({
    'Month': months_full,
    'High': high[:12],
    'Medium': medium[:12],
    'Low': low[:12]
})
