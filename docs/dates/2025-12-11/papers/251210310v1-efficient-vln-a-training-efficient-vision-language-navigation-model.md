---
layout: default
title: Efficient-VLN: A Training-Efficient Vision-Language Navigation Model
---

# Efficient-VLN: A Training-Efficient Vision-Language Navigation Model
**arXiv**：[2512.10310v1](https://arxiv.org/abs/2512.10310) · [PDF](https://arxiv.org/pdf/2512.10310.pdf)  
**作者**：Duo Zheng, Shijia Huang, Yanyang Li, Liwei Wang  

**一句话要点**：提出Efficient-VLN以解决视觉语言导航中训练开销大的问题

**关键词**：视觉语言导航, 训练效率, 记忆机制, 动态策略, 多模态大语言模型

## 3 点简述
- 核心问题：MLLMs在VLN中面临长历史观察的二次计算负担和DAgger中探索与效率的权衡。
- 方法要点：设计渐进式记忆和可学习递归记忆机制，并引入动态混合策略以平衡探索与效率。
- 实验或效果：在R2R-CE和RxR-CE上达到SOTA性能，训练开销显著降低至282 H800 GPU小时。

## 摘要（原文）

> Multimodal large language models (MLLMs) have shown promising potential in Vision-Language Navigation (VLN). However, their practical development is severely hindered by the substantial training overhead. We recognize two key issues that contribute to the overhead: (1) the quadratic computational burden from processing long-horizon historical observations as massive sequences of tokens, and (2) the exploration-efficiency trade-off in DAgger, i.e., a data aggregation process of collecting agent-explored trajectories. While more exploration yields effective error-recovery trajectories for handling test-time distribution shifts, it comes at the cost of longer trajectory lengths for both training and inference. To address these challenges, we propose Efficient-VLN, a training-efficient VLN model. Specifically, to mitigate the token processing burden, we design two efficient memory mechanisms: a progressive memory that dynamically allocates more tokens to recent observations, and a learnable recursive memory that utilizes the key-value cache of learnable tokens as the memory state. Moreover, we introduce a dynamic mixed policy to balance the exploration-efficiency trade-off. Extensive experiments show that Efficient-VLN achieves state-of-the-art performance on R2R-CE (64.2% SR) and RxR-CE (67.0% SR). Critically, our model consumes merely 282 H800 GPU hours, demonstrating a dramatic reduction in training overhead compared to state-of-the-art methods.

