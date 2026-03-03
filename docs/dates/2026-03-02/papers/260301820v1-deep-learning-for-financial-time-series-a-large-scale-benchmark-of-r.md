---
layout: default
title: Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance
---

# Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance
**arXiv**：[2603.01820v1](https://arxiv.org/abs/2603.01820) · [PDF](https://arxiv.org/pdf/2603.01820.pdf)  
**作者**：Adir Saly-Kaufmann, Kieran Wood, Jan Peter-Calliess, Stefan Zohren  

**一句话要点**：提出大规模深度学习基准以优化金融时间序列的夏普比率

**关键词**：金融时间序列预测, 深度学习基准, 夏普比率优化, 风险调整性能, 混合模型, 交易成本分析

## 3 点简述
- 核心问题：评估深度学习模型在金融时间序列预测和头寸调整中的风险调整性能，超越平均回报。
- 方法要点：比较线性模型、循环网络、Transformer、状态空间模型和序列表示方法，包括VSN与LSTM等混合模型。
- 实验或效果：VSN与LSTM混合模型获得最高夏普比率，xLSTM在交易成本缓冲方面表现最佳，模型在统计显著性和稳健性上得到验证。

## 摘要（原文）

> We present a large scale benchmark of modern deep learning architectures for a financial time series prediction and position sizing task, with a primary focus on Sharpe ratio optimization. Evaluating linear models, recurrent networks, transformer based architectures, state space models, and recent sequence representation approaches, we assess out of sample performance on a daily futures dataset spanning commodities, equity indices, bonds, and FX spanning 2010 to 2025. Our evaluation goes beyond average returns and includes statistical significance, downside and tail risk measures, breakeven transaction cost analysis, robustness to random seed selection, and computational efficiency. We find that models explicitly designed to learn rich temporal representations consistently outperform linear benchmarks and generic deep learning models, which often lead the ranking in standard time series benchmarks. Hybrid models such as VSN with LSTM, a combination of Variable Selection Networks (VSN) and LSTMs, achieves the highest overall Sharpe ratio, while VSN with xLSTM and LSTM with PatchTST exhibit superior downside adjusted characteristics. xLSTM demonstrates the largest breakeven transaction cost buffer, indicating improved robustness to trading frictions.

