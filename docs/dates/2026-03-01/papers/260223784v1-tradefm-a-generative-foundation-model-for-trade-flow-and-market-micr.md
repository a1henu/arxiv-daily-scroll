---
layout: default
title: TradeFM: A Generative Foundation Model for Trade-flow and Market Microstructure
---

# TradeFM: A Generative Foundation Model for Trade-flow and Market Microstructure
**arXiv**：[2602.23784v1](https://arxiv.org/abs/2602.23784) · [PDF](https://arxiv.org/pdf/2602.23784.pdf)  
**作者**：Maxime Kawawa-Beaudan, Srijan Sood, Kassiani Papasotiriou, Daniel Borrajo, Manuela Veloso  

**一句话要点**：提出TradeFM生成式基础模型，以统一表征市场微观结构，用于合成数据生成和交易代理学习。

**关键词**：市场微观结构, 生成式基础模型, 尺度不变特征, 通用分词, 合成数据生成, 零样本泛化

## 3 点简述
- 核心问题：市场微观结构数据异构且资产特定，难以实现跨资产泛化。
- 方法要点：开发尺度不变特征和通用分词方案，将订单流事件映射为统一离散序列。
- 实验或效果：在模拟中重现金融回报关键特征，分布误差低于基线，零样本泛化至APAC市场。

## 摘要（原文）

> Foundation models have transformed domains from language to genomics by learning general-purpose representations from large-scale, heterogeneous data. We introduce TradeFM, a 524M-parameter generative Transformer that brings this paradigm to market microstructure, learning directly from billions of trade events across >9K equities. To enable cross-asset generalization, we develop scale-invariant features and a universal tokenization scheme that map the heterogeneous, multi-modal event stream of order flow into a unified discrete sequence -- eliminating asset-specific calibration. Integrated with a deterministic market simulator, TradeFM-generated rollouts reproduce key stylized facts of financial returns, including heavy tails, volatility clustering, and absence of return autocorrelation. Quantitatively, TradeFM achieves 2-3x lower distributional error than Compound Hawkes baselines and generalizes zero-shot to geographically out-of-distribution APAC markets with moderate perplexity degradation. Together, these results suggest that scale-invariant trade representations capture transferable structure in market microstructure, opening a path toward synthetic data generation, stress testing, and learning-based trading agents.

