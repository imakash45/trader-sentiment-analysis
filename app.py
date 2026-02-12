import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Trader Behaviour vs Market Sentiment Dashboard")

# load data
df = pd.read_csv("merged_dataset.csv")

st.sidebar.header("Filters")

sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment",
    options=df['classification'].unique(),
    default=df['classification'].unique()
)

filtered_df = df[df['classification'].isin(sentiment_filter)]

# ---- PnL Distribution ----
st.subheader("PnL Distribution by Sentiment")
fig1 = plt.figure()
sns.boxplot(data=filtered_df, x='classification', y='Closed PnL')
st.pyplot(fig1)

# ---- Trade Size ----
st.subheader("Trade Size by Sentiment")
fig2 = plt.figure()
sns.boxplot(data=filtered_df, x='classification', y='Size USD')
st.pyplot(fig2)

# ---- Long vs Short ----
st.subheader("Long vs Short Distribution")
direction = filtered_df.groupby(['classification','Direction']).size().unstack().fillna(0)
st.bar_chart(direction)

# ---- Trades per Day ----
st.subheader("Trades Per Day")
trades_per_day = filtered_df.groupby('date').size()
st.line_chart(trades_per_day)
