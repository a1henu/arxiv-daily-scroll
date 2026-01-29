---
layout: default
title: CPiRi: Channel Permutation-Invariant Relational Interaction for Multivariate Time Series Forecasting
---

# CPiRi: Channel Permutation-Invariant Relational Interaction for Multivariate Time Series Forecasting
**arXiv**：[2601.20318v1](https://arxiv.org/abs/2601.20318) · [PDF](https://arxiv.org/pdf/2601.20318.pdf)  
**作者**：Jiyuan Xu, Wenyu Zhang, Xin Jing, Shuai Chen, Shuai Zhang, Jiahao Nie  

**一句话要点**：提出CPiRi框架以解决多变量时间序列预测中通道依赖与独立模型的局限性，实现通道排列不变性。

**关键词**：多变量时间序列预测, 通道排列不变性, 时空解耦架构, 排列不变正则化, 泛化能力, 高效部署

## 3 点简述
- 核心问题：现有通道依赖模型易过拟合通道顺序，通道独立模型忽略通道间依赖，限制泛化与性能。
- 方法要点：结合时空解耦架构与排列不变正则化训练，通过冻结时间编码器和轻量空间模块学习数据驱动的通道关系。
- 实验或效果：在多个基准测试中达到先进水平，对通道重排稳定，仅用一半通道训练即可泛化到未见通道，保持高效。

## 摘要（原文）

> Current methods for multivariate time series forecasting can be classified into channel-dependent and channel-independent models. Channel-dependent models learn cross-channel features but often overfit the channel ordering, which hampers adaptation when channels are added or reordered. Channel-independent models treat each channel in isolation to increase flexibility, yet this neglects inter-channel dependencies and limits performance. To address these limitations, we propose \textbf{CPiRi}, a \textbf{channel permutation invariant (CPI)} framework that infers cross-channel structure from data rather than memorizing a fixed ordering, enabling deployment in settings with structural and distributional co-drift without retraining. CPiRi couples \textbf{spatio-temporal decoupling architecture} with \textbf{permutation-invariant regularization training strategy}: a frozen pretrained temporal encoder extracts high-quality temporal features, a lightweight spatial module learns content-driven inter-channel relations, while a channel shuffling strategy enforces CPI during training. We further \textbf{ground CPiRi in theory} by analyzing permutation equivariance in multivariate time series forecasting. Experiments on multiple benchmarks show state-of-the-art results. CPiRi remains stable when channel orders are shuffled and exhibits strong \textbf{inductive generalization} to unseen channels even when trained on \textbf{only half} of the channels, while maintaining \textbf{practical efficiency} on large-scale datasets. The source code is released at https://github.com/JasonStraka/CPiRi.

