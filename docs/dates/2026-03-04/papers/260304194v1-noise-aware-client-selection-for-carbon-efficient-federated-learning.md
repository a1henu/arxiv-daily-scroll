---
layout: default
title: Noise-aware Client Selection for carbon-efficient Federated Learning via Gradient Norm Thresholding
---

# Noise-aware Client Selection for carbon-efficient Federated Learning via Gradient Norm Thresholding
**arXiv**：[2603.04194v1](https://arxiv.org/abs/2603.04194) · [PDF](https://arxiv.org/pdf/2603.04194.pdf)  
**作者**：Patrick Wilhelm, Inese Yilmaz, Odej Kao  

**一句话要点**：提出基于梯度范数阈值的噪声感知客户端选择方法，以提升碳高效联邦学习的鲁棒性

**关键词**：联邦学习, 客户端选择, 噪声检测, 碳高效训练, 梯度范数阈值

## 3 点简述
- 联邦学习中客户端数据质量未知，影响模型性能与可持续性
- 在现有客户端选择策略上集成噪声过滤模块，通过探测轮次进行梯度范数阈值化
- 实验表明该方法能有效检测噪声数据，改善模型收敛与碳效率平衡

## 摘要（原文）

> Training large-scale Neural Networks requires substantial computational power and energy. Federated Learning enables distributed model training across geospatially distributed data centers, leveraging renewable energy sources to reduce the carbon footprint of AI training. Various client selection strategies have been developed to align the volatility of renewable energy with stable and fair model training in a federated system. However, due to the privacy-preserving nature of Federated Learning, the quality of data on client devices remains unknown, posing challenges for effective model training. In this paper, we introduce a modular approach on top to state-of-the-art client selection strategies for carbon-efficient Federated Learning. Our method enhances robustness by incorporating a noisy client data filtering, improving both model performance and sustainability in scenarios with unknown data quality. Additionally, we explore the impact of carbon budgets on model convergence, balancing efficiency and sustainability. Through extensive evaluations, we demonstrate that modern client selection strategies based on local client loss tend to select clients with noisy data, ultimately degrading model performance. To address this, we propose a gradient norm thresholding mechanism using probing rounds for more effective client selection and noise detection, contributing to the practical deployment of carbon-efficient Federated Learning.

