# Trader Behaviour vs Market Sentiment Analysis

This project analyzes how Bitcoin market sentiment (Fear vs Greed) influences trader behavior and performance on Hyperliquid.   
The goal is to uncover patterns that can inform better trading and risk management strategies.

# How to Run
Install requirements: 
pandas, 
numpy, 
matplotlib, 
seaborn, 
scikit-learn, 
streamlit,

Run dashboard:  
streamlit run app/app.py

# Methodology

Cleaned and aligned sentiment and trade datasets on daily level, 
Engineered key metrics:, 
Daily PnL, 
Win rate, 
Trade frequency, 
Trade size, 
Long vs Short ratio, 
Compared trader performance and behavior during Fear vs Greed periods, 
Segmented traders into behavioral groups, 
Built a simple predictive model and clustering analysis.

# Key Insights

## Performance differs by sentiment  
Larger losses and lower win rates occur during Fear periods, 
Greed periods show more stable profitability.

## Behavior changes with sentiment  
Trading activity increases during Fear, 
Traders take larger positions during Greed, 
Long bias dominates Greed, Short bias dominates Fear

## Trader segmentation  
Frequent traders show higher risk and wider PnL distribution, 
Consistent winners exhibit more disciplined trading

# Strategy Recommendations  

## 1. Reduce risk during Fear markets  
Smaller position sizes, 
Avoid over-trading, 
Focus on high-confidence trades

## 2. Increase exposure during Greed markets  
Slightly larger position sizes, 
Favor trend-following strategies 
Maintain trading discipline

# Bonus Work

Random Forest model predicting next-day profitability
Trader clustering into behavioral archetypes
Interactive Streamlit dashboard
