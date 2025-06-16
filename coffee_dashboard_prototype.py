
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title='Coffee Price Dashboard', layout='wide')

st.title('📈 Coffee Export Price Dashboard (Prototype)')

# Fake data for demo
months = ['Jul 2025', 'Aug 2025', 'Sep 2025', 'Oct 2025', 'Nov 2025', 'Dec 2025',
          'Jan 2026', 'Feb 2026', 'Mar 2026', 'Apr 2026', 'May 2026', 'Jun 2026']

high = np.arange(6300, 7400+100, 100)
medium = np.arange(6300, 6850+50, 50)
low = np.arange(6200, 6420+20, 20)

df = pd.DataFrame({
    'Month': months,
    'High Scenario': high[:12],
    'Medium Scenario': medium[:12],
    'Low Scenario': low[:12]
})

st.subheader('📊 Price Scenarios')

fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Month'], y=df['High Scenario'],
                         mode='lines+markers', name='High Scenario'))
fig.add_trace(go.Scatter(x=df['Month'], y=df['Medium Scenario'],
                         mode='lines+markers', name='Medium Scenario'))
fig.add_trace(go.Scatter(x=df['Month'], y=df['Low Scenario'],
                         mode='lines+markers', name='Low Scenario'))

fig.update_layout(title='Coffee Price Forecast Scenarios',
                  xaxis_title='Month',
                  yaxis_title='Export Price (USD/ton)',
                  hovermode='x unified')

st.plotly_chart(fig, use_container_width=True)

st.subheader('📑 Forecast Table')
st.dataframe(df)
