---
layout: default
title: Efficient Personalized Federated PCA with Manifold Optimization for IoT Anomaly Detection
---

# Efficient Personalized Federated PCA with Manifold Optimization for IoT Anomaly Detection
**arXiv**：[2602.12622v1](https://arxiv.org/abs/2602.12622) · [PDF](https://arxiv.org/pdf/2602.12622.pdf)  
**作者**：Xianchao Xiu, Chenyi Huang, Wei Zhang, Wanquan Liu  

**一句话要点**：提出高效个性化联邦PCA方法FedEP，用于物联网异常检测。

**关键词**：联邦学习, 主成分分析, 异常检测, 物联网安全, 流形优化, 个性化学习

## 3 点简述
- 核心问题：现有联邦PCA方法缺乏个性化和鲁棒性，影响物联网异常检测效果。
- 方法要点：引入ℓ₁范数实现个性化，ℓ₂,₁范数增强鲁棒性，基于流形优化和ADMM求解。
- 实验或效果：在多种物联网安全场景中，FedEP优于FedPG，获得高F1分数和准确率。

## 摘要（原文）

> Internet of things (IoT) networks face increasing security threats due to their distributed nature and resource constraints. Although federated learning (FL) has gained prominence as a privacy-preserving framework for distributed IoT environments, current federated principal component analysis (PCA) methods lack the integration of personalization and robustness, which are critical for effective anomaly detection. To address these limitations, we propose an efficient personalized federated PCA (FedEP) method for anomaly detection in IoT networks. The proposed model achieves personalization through introducing local representations with the $\ell_1$-norm for element-wise sparsity, while maintaining robustness via enforcing local models with the $\ell_{2,1}$-norm for row-wise sparsity. To solve this non-convex problem, we develop a manifold optimization algorithm based on the alternating direction method of multipliers (ADMM) with rigorous theoretical convergence guarantees. Experimental results confirm that the proposed FedEP outperforms the state-of-the-art FedPG, achieving excellent F1-scores and accuracy in various IoT security scenarios. Our code will be available at \href{https://github.com/xianchaoxiu/FedEP}{https://github.com/xianchaoxiu/FedEP}.

