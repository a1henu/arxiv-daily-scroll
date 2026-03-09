---
layout: default
title: Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis
---

# Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis
**arXiv**：[2603.05917v1](https://arxiv.org/abs/2603.05917) · [PDF](https://arxiv.org/pdf/2603.05917.pdf)  
**作者**：Mohammad Al Ridhawi, Mahtab Haj Ali, Hussein Al Osman  

**一句话要点**：提出结合节点Transformer与BERT情感分析的集成框架以提升股票市场预测精度

**关键词**：股票市场预测, 节点Transformer, BERT情感分析, 图神经网络, 跨截面依赖, 时序建模

## 3 点简述
- 核心问题：传统方法难以捕捉金融市场中的复杂模式和跨股票依赖关系。
- 方法要点：将市场建模为图结构，集成BERT情感分析和节点Transformer处理时序与跨截面数据。
- 实验效果：在S&P 500数据上，集成模型MAPE为0.80%，优于基准模型，情感分析在财报期提升25%精度。

## 摘要（原文）

> Stock market prediction presents considerable challenges for investors, financial institutions, and policymakers operating in complex market environments characterized by noise, non-stationarity, and behavioral dynamics. Traditional forecasting methods often fail to capture the intricate patterns and cross-sectional dependencies inherent in financial markets. This paper presents an integrated framework combining a node transformer architecture with BERT-based sentiment analysis for stock price forecasting. The proposed model represents the stock market as a graph structure where individual stocks form nodes and edges capture relationships including sectoral affiliations, correlated price movements, and supply chain connections. A fine-tuned BERT model extracts sentiment from social media posts and combines it with quantitative market features through attention-based fusion. The node transformer processes historical market data while capturing both temporal evolution and cross-sectional dependencies among stocks. Experiments on 20 S&P 500 stocks spanning January 1982 to March 2025 demonstrate that the integrated model achieves a mean absolute percentage error (MAPE) of 0.80% for one-day-ahead predictions, compared to 1.20% for ARIMA and 1.00% for LSTM. Sentiment analysis reduces prediction error by 10% overall and 25% during earnings announcements, while graph-based modeling contributes an additional 15% improvement by capturing inter-stock dependencies. Directional accuracy reaches 65% for one-day forecasts. Statistical validation through paired t-tests confirms these improvements (p < 0.05 for all comparisons). The model maintains MAPE below 1.5% during high-volatility periods where baseline models exceed 2%.

