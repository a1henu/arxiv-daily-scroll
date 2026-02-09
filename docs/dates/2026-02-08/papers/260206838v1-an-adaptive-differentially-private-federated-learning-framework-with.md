---
layout: default
title: An Adaptive Differentially Private Federated Learning Framework with Bi-level Optimization
---

# An Adaptive Differentially Private Federated Learning Framework with Bi-level Optimization
**arXiv**：[2602.06838v1](https://arxiv.org/abs/2602.06838) · [PDF](https://arxiv.org/pdf/2602.06838.pdf)  
**作者**：Jin Wang, Hui Ma, Fei Xing, Ming Yan  

**一句话要点**：提出自适应差分隐私联邦学习框架，以解决异构与隐私约束下的模型效率问题。

**关键词**：联邦学习, 差分隐私, 异构数据, 梯度优化, 自适应裁剪, 模型聚合

## 3 点简述
- 核心问题：设备异构与非独立同分布数据导致梯度不稳定，差分隐私加剧扰动，影响训练性能。
- 方法要点：客户端引入轻量压缩模块正则化表示，服务器自适应梯度裁剪与约束感知聚合机制。
- 实验或效果：在CIFAR-10和SVHN上实验，显示收敛稳定性和分类准确性提升。

## 摘要（原文）

> Federated learning enables collaborative model training across distributed clients while preserving data privacy. However, in practical deployments, device heterogeneity, non-independent, and identically distributed (Non-IID) data often lead to highly unstable and biased gradient updates. When differential privacy is enforced, conventional fixed gradient clipping and Gaussian noise injection may further amplify gradient perturbations, resulting in training oscillation and performance degradation and degraded model performance. To address these challenges, we propose an adaptive differentially private federated learning framework that explicitly targets model efficiency under heterogeneous and privacy-constrained settings. On the client side, a lightweight local compressed module is introduced to regularize intermediate representations and constrain gradient variability, thereby mitigating noise amplification during local optimization. On the server side, an adaptive gradient clipping strategy dynamically adjusts clipping thresholds based on historical update statistics to avoid over-clipping and noise domination. Furthermore, a constraint-aware aggregation mechanism is designed to suppress unreliable or noise-dominated client updates and stabilize global optimization. Extensive experiments on CIFAR-10 and SVHN demonstrate improved convergence stability and classification accuracy.

