---
layout: default
title: Decentralized Fairness Aware Multi Task Federated Learning for VR Network
---

# Decentralized Fairness Aware Multi Task Federated Learning for VR Network
**arXiv**：[2512.02513v1](https://arxiv.org/abs/2512.02513) · [PDF](https://arxiv.org/pdf/2512.02513.pdf)  
**作者**：Krishnendu S. Tharakan, Carlo Fischione  

**一句话要点**：提出去中心化公平感知多任务联邦学习算法，以优化VR网络中的基站缓存与预取。

**关键词**：联邦学习, 虚拟现实网络, 缓存优化, 去中心化学习, 公平性, 多任务学习

## 3 点简述
- 核心问题：无线VR视频传输面临低延迟、高体验质量要求与设备能力限制，传统联邦学习易偏置且忽略统计异质性。
- 方法要点：设计DMTFL算法，在基站学习个性化缓存模型，通过Rademacher复杂度和PAC界提供理论保证。
- 实验或效果：基于真实VR头部追踪数据集模拟，DMTFL算法在性能上优于基线算法。

## 摘要（原文）

> Wireless connectivity promises to unshackle virtual reality (VR) experiences, allowing users to engage from anywhere, anytime. However, delivering seamless, high-quality, real-time VR video wirelessly is challenging due to the stringent quality of experience requirements, low latency constraints, and limited VR device capabilities. This paper addresses these challenges by introducing a novel decentralized multi task fair federated learning (DMTFL) based caching that caches and prefetches each VR user's field of view (FOV) at base stations (BSs) based on the caching strategies tailored to each BS. In federated learning (FL) in its naive form, often biases toward certain users, and a single global model fails to capture the statistical heterogeneity across users and BSs. In contrast, the proposed DMTFL algorithm personalizes content delivery by learning individual caching models at each BS. These models are further optimized to perform well under any target distribution, while providing theoretical guarantees via Rademacher complexity and a probably approximately correct (PAC) bound on the loss. Using a realistic VR head-tracking dataset, our simulations demonstrate the superiority of our proposed DMTFL algorithm compared to baseline algorithms.

