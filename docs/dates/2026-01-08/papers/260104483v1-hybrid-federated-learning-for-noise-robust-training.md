---
layout: default
title: Hybrid Federated Learning for Noise-Robust Training
---

# Hybrid Federated Learning for Noise-Robust Training
**arXiv**：[2601.04483v1](https://arxiv.org/abs/2601.04483) · [PDF](https://arxiv.org/pdf/2601.04483.pdf)  
**作者**：Yongjun Kim, Hyeongjun Park, Hwanjin Kim, Junil Choi  

**一句话要点**：提出混合联邦学习框架以在低信噪比下提升噪声鲁棒性训练效果

**关键词**：联邦学习, 噪声鲁棒性, 混合训练, 自适应优化, 分布式学习

## 3 点简述
- 核心问题：联邦学习和联邦蒸馏在噪声鲁棒性与学习速度间存在权衡
- 方法要点：结合梯度与logits传输，通过自适应聚类和权重选择优化框架
- 实验或效果：在低SNR下，利用自由度方法实现更优测试准确率

## 摘要（原文）

> Federated learning (FL) and federated distillation (FD) are distributed learning paradigms that train UE models with enhanced privacy, each offering different trade-offs between noise robustness and learning speed. To mitigate their respective weaknesses, we propose a hybrid federated learning (HFL) framework in which each user equipment (UE) transmits either gradients or logits, and the base station (BS) selects the per-round weights of FL and FD updates. We derive convergence of HFL framework and introduce two methods to exploit degrees of freedom (DoF) in HFL, which are (i) adaptive UE clustering via Jenks optimization and (ii) adaptive weight selection via a damped Newton method. Numerical results show that HFL achieves superior test accuracy at low SNR when both DoF are exploited.

