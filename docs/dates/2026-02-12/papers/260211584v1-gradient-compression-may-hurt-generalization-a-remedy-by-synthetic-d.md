---
layout: default
title: Gradient Compression May Hurt Generalization: A Remedy by Synthetic Data Guided Sharpness Aware Minimization
---

# Gradient Compression May Hurt Generalization: A Remedy by Synthetic Data Guided Sharpness Aware Minimization
**arXiv**：[2602.11584v1](https://arxiv.org/abs/2602.11584) · [PDF](https://arxiv.org/pdf/2602.11584.pdf)  
**作者**：Yujie Gu, Richeng Jin, Zhaoyang Zhang, Huaiyu Dai  

**一句话要点**：提出FedSynSAM以解决联邦学习中梯度压缩损害泛化的问题

**关键词**：联邦学习, 梯度压缩, 泛化能力, 锐度感知最小化, 合成数据, 非独立同分布数据

## 3 点简述
- 发现梯度压缩在非独立同分布数据下导致损失景观更尖锐，损害泛化能力
- 利用全局模型轨迹构建合成数据，精确估计全局扰动以改进SAM应用
- 理论证明收敛性，实验验证FedSynSAM在通信效率和泛化上的有效性

## 摘要（原文）

> It is commonly believed that gradient compression in federated learning (FL) enjoys significant improvement in communication efficiency with negligible performance degradation. In this paper, we find that gradient compression induces sharper loss landscapes in federated learning, particularly under non-IID data distributions, which suggests hindered generalization capability. The recently emerging Sharpness Aware Minimization (SAM) effectively searches for a flat minima by incorporating a gradient ascent step (i.e., perturbing the model with gradients) before the celebrated stochastic gradient descent. Nonetheless, the direct application of SAM in FL suffers from inaccurate estimation of the global perturbation due to data heterogeneity. Existing approaches propose to utilize the model update from the previous communication round as a rough estimate. However, its effectiveness is hindered when model update compression is incorporated. In this paper, we propose FedSynSAM, which leverages the global model trajectory to construct synthetic data and facilitates an accurate estimation of the global perturbation. The convergence of the proposed algorithm is established, and extensive experiments are conducted to validate its effectiveness.

