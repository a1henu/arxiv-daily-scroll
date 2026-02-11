---
layout: default
title: Statistical benchmarking of transformer models in low signal-to-noise time-series forecasting
---

# Statistical benchmarking of transformer models in low signal-to-noise time-series forecasting
**arXiv**：[2602.09869v1](https://arxiv.org/abs/2602.09869) · [PDF](https://arxiv.org/pdf/2602.09869.pdf)  
**作者**：Cyril Garcia, Guillaume Remy  

**一句话要点**：提出动态稀疏化注意力机制，提升Transformer在低信噪比时间序列预测中的性能

**关键词**：时间序列预测, Transformer模型, 低信噪比, 注意力机制, 动态稀疏化, 多变量分析

## 3 点简述
- 研究Transformer在低数据量、低信噪比多变量时间序列预测中的表现
- 引入双向注意力Transformer和动态稀疏化训练方法，优于传统基线模型
- 通过合成数据实验和注意力模式分析，验证模型在噪声环境下的泛化能力

## 摘要（原文）

> We study the performance of transformer architectures for multivariate time-series forecasting in low-data regimes consisting of only a few years of daily observations. Using synthetically generated processes with known temporal and cross-sectional dependency structures and varying signal-to-noise ratios, we conduct bootstrapped experiments that enable direct evaluation via out-of-sample correlations with the optimal ground-truth predictor. We show that two-way attention transformers, which alternate between temporal and cross-sectional self-attention, can outperform standard baselines-Lasso, boosting methods, and fully connected multilayer perceptrons-across a wide range of settings, including low signal-to-noise regimes. We further introduce a dynamic sparsification procedure for attention matrices applied during training, and demonstrate that it becomes significantly effective in noisy environments, where the correlation between the target variable and the optimal predictor is on the order of a few percent. Analysis of the learned attention patterns reveals interpretable structure and suggests connections to sparsity-inducing regularization in classical regression, providing insight into why these models generalize effectively under noise.

