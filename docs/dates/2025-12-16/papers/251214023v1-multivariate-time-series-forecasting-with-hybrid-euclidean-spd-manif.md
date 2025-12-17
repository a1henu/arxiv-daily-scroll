---
layout: default
title: Multivariate Time Series Forecasting with Hybrid Euclidean-SPD Manifold Graph Neural Networks
---

# Multivariate Time Series Forecasting with Hybrid Euclidean-SPD Manifold Graph Neural Networks
**arXiv**：[2512.14023v1](https://arxiv.org/abs/2512.14023) · [PDF](https://arxiv.org/pdf/2512.14023.pdf)  
**作者**：Yong Fang, Na Li, Hangguan Shan, Eryun Liu, Xinyu Li, Wei Ni, Er-Ping Li  

**一句话要点**：提出HSMGNN模型，通过混合欧几里得-黎曼几何框架提升多元时间序列预测精度。

**关键词**：多元时间序列预测, 图神经网络, 混合几何表示, 黎曼流形, 时空依赖建模

## 3 点简述
- 现有方法局限于单一几何空间，难以捕捉多元时间序列的复杂几何结构和时空依赖。
- HSMGNN引入SCS嵌入和ADB层，在混合空间中建模并降低计算成本，通过FGCN融合特征进行预测。
- 在三个基准数据集上实验，预测准确率最高提升13.8%，优于现有先进方法。

## 摘要（原文）

> Multivariate Time Series (MTS) forecasting plays a vital role in various real-world applications, such as traffic management and predictive maintenance. Existing approaches typically model MTS data in either Euclidean or Riemannian space, limiting their ability to capture the diverse geometric structures and complex spatio-temporal dependencies inherent in real-world data. To overcome this limitation, we propose the Hybrid Symmetric Positive-Definite Manifold Graph Neural Network (HSMGNN), a novel graph neural network-based model that captures data geometry within a hybrid Euclidean-Riemannian framework. To the best of our knowledge, this is the first work to leverage hybrid geometric representations for MTS forecasting, enabling expressive and comprehensive modeling of geometric properties. Specifically, we introduce a Submanifold-Cross-Segment (SCS) embedding to project input MTS into both Euclidean and Riemannian spaces, thereby capturing spatio-temporal variations across distinct geometric domains. To alleviate the high computational cost of Riemannian distance, we further design an Adaptive-Distance-Bank (ADB) layer with a trainable memory mechanism. Finally, a Fusion Graph Convolutional Network (FGCN) is devised to integrate features from the dual spaces via a learnable fusion operator for accurate prediction. Experiments on three benchmark datasets demonstrate that HSMGNN achieves up to a 13.8 percent improvement over state-of-the-art baselines in forecasting accuracy.

