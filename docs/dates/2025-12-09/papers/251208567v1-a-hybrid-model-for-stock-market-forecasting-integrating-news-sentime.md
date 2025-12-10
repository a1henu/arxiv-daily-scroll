---
layout: default
title: A Hybrid Model for Stock Market Forecasting: Integrating News Sentiment and Time Series Data with Graph Neural Networks
---

# A Hybrid Model for Stock Market Forecasting: Integrating News Sentiment and Time Series Data with Graph Neural Networks
**arXiv**：[2512.08567v1](https://arxiv.org/abs/2512.08567) · [PDF](https://arxiv.org/pdf/2512.08567.pdf)  
**作者**：Nader Sadek, Mirette Moawad, Christina Naguib, Mariam Elzahaby  

**一句话要点**：提出融合新闻情感与时间序列数据的图神经网络混合模型以提升股市预测性能

**关键词**：股市预测, 图神经网络, 新闻情感分析, 多模态融合, 时间序列分析

## 3 点简述
- 核心问题：股市预测依赖历史价格，但外部新闻信号可提供补充信息。
- 方法要点：结合LSTM编码历史数据与语言模型嵌入新闻，构建异构图并使用GraphSAGE捕捉交互。
- 实验或效果：在美股和Bloomberg数据集上，GNN优于LSTM基线，准确率达53%，新闻量多的公司预测更准。

## 摘要（原文）

> Stock market prediction is a long-standing challenge in finance, as accurate forecasts support informed investment decisions. Traditional models rely mainly on historical prices, but recent work shows that financial news can provide useful external signals. This paper investigates a multimodal approach that integrates companies' news articles with their historical stock data to improve prediction performance. We compare a Graph Neural Network (GNN) model with a baseline LSTM model. Historical data for each company is encoded using an LSTM, while news titles are embedded with a language model. These embeddings form nodes in a heterogeneous graph, and GraphSAGE is used to capture interactions between articles, companies, and industries. We evaluate two targets: a binary direction-of-change label and a significance-based label. Experiments on the US equities and Bloomberg datasets show that the GNN outperforms the LSTM baseline, achieving 53% accuracy on the first target and a 4% precision gain on the second. Results also indicate that companies with more associated news yield higher prediction accuracy. Moreover, headlines contain stronger predictive signals than full articles, suggesting that concise news summaries play an important role in short-term market reactions.

