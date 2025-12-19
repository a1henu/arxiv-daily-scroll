---
layout: default
title: Interpretable Deep Learning for Stock Returns: A Consensus-Bottleneck Asset Pricing Model
---

# Interpretable Deep Learning for Stock Returns: A Consensus-Bottleneck Asset Pricing Model
**arXiv**：[2512.16251v1](https://arxiv.org/abs/2512.16251) · [PDF](https://arxiv.org/pdf/2512.16251.pdf)  
**作者**：Bong-Gyu Jang, Younwoo Jeong, Changeun Kim  

**一句话要点**：提出共识瓶颈资产定价模型，以可解释深度学习预测股票收益并揭示信念驱动结构。

**关键词**：资产定价模型, 可解释深度学习, 共识形成, 股票收益预测, 信念驱动结构

## 3 点简述
- 核心问题：传统因子模型未充分捕捉信念驱动收益结构，需可解释方法预测股票风险溢价。
- 方法要点：设计部分可解释神经网络，模拟分析师共识形成过程，压缩分散信念为资产价格。
- 实验或效果：模型提升长期预测精度，优于标准深度学习，产生经济显著投资回报和可解释组件。

## 摘要（原文）

> We introduce the \textit{Consensus-Bottleneck Asset Pricing Model} (CB-APM), a partially interpretable neural network that replicates the reasoning processes of sell-side analysts by capturing how dispersed investor beliefs are compressed into asset prices through a consensus formation process. By modeling this ``bottleneck'' to summarize firm- and macro-level information, CB-APM not only predicts future risk premiums of U.S. equities but also links belief aggregation to expected returns in a structurally interpretable manner. The model improves long-horizon return forecasts and outperforms standard deep learning approaches in both predictive accuracy and explanatory power. Comprehensive portfolio analyses show that CB-APM's out-of-sample predictions translate into economically meaningful payoffs, with monotonic return differentials and stable long-short performance across regularization settings. Empirically, CB-APM leverages consensus as a regularizer to amplify long-horizon predictability and yields interpretable consensus-based components that clarify how information is priced in returns. Moreover, regression and GRS-based pricing diagnostics reveal that the learned consensus representations capture priced variation only partially spanned by traditional factor models, demonstrating that CB-APM uncovers belief-driven structure in expected returns beyond the canonical factor space. Overall, CB-APM provides an interpretable and empirically grounded framework for understanding belief-driven return dynamics.

