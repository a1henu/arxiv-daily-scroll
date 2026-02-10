---
layout: default
title: When and How Much to Imagine: Adaptive Test-Time Scaling with World Models for Visual Spatial Reasoning
---

# When and How Much to Imagine: Adaptive Test-Time Scaling with World Models for Visual Spatial Reasoning
**arXiv**：[2602.08236v1](https://arxiv.org/abs/2602.08236) · [PDF](https://arxiv.org/pdf/2602.08236.pdf)  
**作者**：Shoubin Yu, Yue Zhang, Zun Wang, Jaehong Yoon, Huaxiu Yao, Mingyu Ding, Mohit Bansal  

**一句话要点**：提出自适应测试时框架AVIC，通过选择性调用世界模型解决视觉空间推理中想象资源的优化问题

**关键词**：视觉空间推理, 世界模型, 自适应测试时框架, 多模态大语言模型, 计算效率优化

## 3 点简述
- 核心问题：视觉空间推理中何时及如何调用世界模型进行想象，以避免计算浪费和性能下降
- 方法要点：引入AVIC框架，动态评估视觉证据充分性，选择性缩放想象资源
- 实验或效果：在SAT、MMSI和R2R基准上，AVIC以更少调用和令牌匹配或超越固定想象策略

## 摘要（原文）

> Despite rapid progress in Multimodal Large Language Models (MLLMs), visual spatial reasoning remains unreliable when correct answers depend on how a scene would appear under unseen or alternative viewpoints. Recent work addresses this by augmenting reasoning with world models for visual imagination, but questions such as when imagination is actually necessary, how much of it is beneficial, and when it becomes harmful, remain poorly understood. In practice, indiscriminate imagination can increase computation and even degrade performance by introducing misleading evidence. In this work, we present an in-depth analysis of test-time visual imagination as a controllable resource for spatial reasoning. We study when static visual evidence is sufficient, when imagination improves reasoning, and how excessive or unnecessary imagination affects accuracy and efficiency. To support this analysis, we introduce AVIC, an adaptive test-time framework with world models that explicitly reasons about the sufficiency of current visual evidence before selectively invoking and scaling visual imagination. Across spatial reasoning benchmarks (SAT, MMSI) and an embodied navigation benchmark (R2R), our results reveal clear scenarios where imagination is critical, marginal, or detrimental, and show that selective control can match or outperform fixed imagination strategies with substantially fewer world-model calls and language tokens. Overall, our findings highlight the importance of analyzing and controlling test-time imagination for efficient and reliable spatial reasoning.

