---
layout: default
title: TimeSliver : Symbolic-Linear Decomposition for Explainable Time Series Classification
---

# TimeSliver : Symbolic-Linear Decomposition for Explainable Time Series Classification
**arXiv**：[2601.21289v1](https://arxiv.org/abs/2601.21289) · [PDF](https://arxiv.org/pdf/2601.21289.pdf)  
**作者**：Akash Pandey, Payal Mohapatra, Wei Chen, Qi Zhu, Sinan Keten  

**一句话要点**：提出TimeSliver框架，通过符号-线性分解实现可解释的时间序列分类。

**关键词**：时间序列分类, 可解释性, 符号表示, 线性分解, 深度学习框架

## 3 点简述
- 核心问题：现有方法难以准确量化时间片段对模型预测的影响，且忽略序列依赖性。
- 方法要点：结合原始时间序列与符号抽象，构建保持时序结构的表示，线性编码各片段贡献。
- 实验或效果：在7个数据集上优于其他方法11%，在26个基准数据集上预测性能接近最优基线2%以内。

## 摘要（原文）

> Identifying the extent to which every temporal segment influences a model's predictions is essential for explaining model decisions and increasing transparency. While post-hoc explainable methods based on gradients and feature-based attributions have been popular, they suffer from reference state sensitivity and struggle to generalize across time-series datasets, as they treat time points independently and ignore sequential dependencies. Another perspective on explainable time-series classification is through interpretable components of the model, for instance, leveraging self-attention mechanisms to estimate temporal attribution; however, recent findings indicate that these attention weights often fail to provide faithful measures of temporal importance. In this work, we advance this perspective and present a novel explainability-driven deep learning framework, TimeSliver, which jointly utilizes raw time-series data and its symbolic abstraction to construct a representation that maintains the original temporal structure. Each element in this representation linearly encodes the contribution of each temporal segment to the final prediction, allowing us to assign a meaningful importance score to every time point. For time-series classification, TimeSliver outperforms other temporal attribution methods by 11% on 7 distinct synthetic and real-world multivariate time-series datasets. TimeSliver also achieves predictive performance within 2% of state-of-the-art baselines across 26 UEA benchmark datasets, positioning it as a strong and explainable framework for general time-series classification.

