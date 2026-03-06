---
layout: default
title: Timer-S1: A Billion-Scale Time Series Foundation Model with Serial Scaling
---

# Timer-S1: A Billion-Scale Time Series Foundation Model with Serial Scaling
**arXiv**：[2603.04791v1](https://arxiv.org/abs/2603.04791) · [PDF](https://arxiv.org/pdf/2603.04791.pdf)  
**作者**：Yong Liu, Xingjian Su, Shiyu Wang, Haoran Zhang, Haixuan Liu, Yuxuan Wang, Zhou Ye, Yang Xiang, Jianmin Wang, Mingsheng Long  

**一句话要点**：提出Timer-S1时间序列基础模型，通过串行缩放解决现有模型扩展瓶颈，实现高效长期预测。

**关键词**：时间序列基础模型, 混合专家模型, 串行缩放, 长期预测, 数据增强, 后训练优化

## 3 点简述
- 核心问题：现有时间序列基础模型存在扩展瓶颈，导致长期预测误差累积和推理成本高。
- 方法要点：采用串行缩放策略，结合稀疏TimeMoE块和通用TimeSTP块，通过串行令牌预测优化训练目标。
- 实验或效果：在GIFT-Eval排行榜上取得最佳MASE和CRPS分数，作为预训练模型实现最先进的预测性能。

## 摘要（原文）

> We introduce Timer-S1, a strong Mixture-of-Experts (MoE) time series foundation model with 8.3B total parameters, 0.75B activated parameters for each token, and a context length of 11.5K. To overcome the scalability bottleneck in existing pre-trained time series foundation models, we perform Serial Scaling in three dimensions: model architecture, dataset, and training pipeline. Timer-S1 integrates sparse TimeMoE blocks and generic TimeSTP blocks for Serial-Token Prediction (STP), a generic training objective that adheres to the serial nature of forecasting. The proposed paradigm introduces serial computations to improve long-term predictions while avoiding costly rolling-style inference and pronounced error accumulation in the standard next-token prediction. Pursuing a high-quality and unbiased training dataset, we curate TimeBench, a corpus with one trillion time points, and apply meticulous data augmentation to mitigate predictive bias. We further pioneer a post-training stage, including continued pre-training and long-context extension, to enhance short-term and long-context performance. Evaluated on the large-scale GIFT-Eval leaderboard, Timer-S1 achieves state-of-the-art forecasting performance, attaining the best MASE and CRPS scores as a pre-trained model. Timer-S1 will be released to facilitate further research.

