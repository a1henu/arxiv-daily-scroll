---
layout: default
title: Not All News Is Equal: Topic- and Event-Conditional Sentiment from Finetuned LLMs for Aluminum Price Forecasting
---

# Not All News Is Equal: Topic- and Event-Conditional Sentiment from Finetuned LLMs for Aluminum Price Forecasting
**arXiv**：[2603.09085v1](https://arxiv.org/abs/2603.09085) · [PDF](https://arxiv.org/pdf/2603.09085.pdf)  
**作者**：Alvaro Paredes Amorin, Andre Python, Christoph Weisser  

**一句话要点**：提出基于微调大语言模型的主题与事件条件情感分析，以提升铝价预测性能。

**关键词**：铝价预测, 情感分析, 大语言模型微调, 长短期记忆网络, 新闻数据集成

## 3 点简述
- 核心问题：探究微调大语言模型在铝价预测中提取情感信号的有效性及适用市场条件。
- 方法要点：从英中新闻标题生成月度情感分数，结合传统表格数据，使用LSTM模型进行预测。
- 实验或效果：在高波动期，结合Qwen3模型情感数据的LSTM模型（夏普比率1.04）显著优于仅用表格数据的基线（夏普比率0.23）。

## 摘要（原文）

> By capturing the prevailing sentiment and market mood, textual data has become increasingly vital for forecasting commodity prices, particularly in metal markets. However, the effectiveness of lightweight, finetuned large language models (LLMs) in extracting predictive signals for aluminum prices, and the specific market conditions under which these signals are most informative, remains under-explored. This study generates monthly sentiment scores from English and Chinese news headlines (Reuters, Dow Jones Newswires, and China News Service) and integrates them with traditional tabular data, including base metal indices, exchange rates, inflation rates, and energy prices. We evaluate the predictive performance and economic utility of these models through long-short simulations on the Shanghai Metal Exchange from 2007 to 2024. Our results demonstrate that during periods of high volatility, Long Short-Term Memory (LSTM) models incorporating sentiment data from a finetuned Qwen3 model (Sharpe ratio 1.04) significantly outperform baseline models using tabular data alone (Sharpe ratio 0.23). Subsequent analysis elucidates the nuanced roles of news sources, topics, and event types in aluminum price forecasting.

