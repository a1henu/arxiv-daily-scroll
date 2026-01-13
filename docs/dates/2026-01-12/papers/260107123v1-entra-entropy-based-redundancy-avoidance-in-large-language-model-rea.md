---
layout: default
title: ENTRA: Entropy-Based Redundancy Avoidance in Large Language Model Reasoning
---

# ENTRA: Entropy-Based Redundancy Avoidance in Large Language Model Reasoning
**arXiv**：[2601.07123v1](https://arxiv.org/abs/2601.07123) · [PDF](https://arxiv.org/pdf/2601.07123.pdf)  
**作者**：Ruichu Cai, Haopeng Du, Qingwen Lin, Yutong Chen, Zijian Li, Boyan Xu  

**一句话要点**：提出ENTRA框架，基于熵抑制大语言模型推理中的冗余生成以降低计算开销。

**关键词**：大语言模型推理, 冗余避免, 熵优化, 强化学习, 数学推理

## 3 点简述
- 核心问题：大推理模型常因过度思考生成冗长推理链，导致计算开销大而性能增益有限。
- 方法要点：使用双向重要性估计和基于熵的冗余奖励，通过强化学习优化推理简洁性。
- 实验或效果：在数学推理基准上，输出长度减少37%至53%，准确率无损失或有提升。

## 摘要（原文）

> Large Reasoning Models (LRMs) often suffer from overthinking, generating unnecessarily long reasoning chains even for simple tasks. This leads to substantial computational overhead with limited performance gain, primarily due to redundant verification and repetitive generation. While prior work typically constrains output length or optimizes correctness, such coarse supervision fails to guide models toward concise yet accurate inference. In this paper, we propose ENTRA, an entropy-based training framework that suppresses redundant reasoning while preserving performance. ENTRA first estimates the token-level importance using a lightweight Bidirectional Importance Estimation (BIE) method, which accounts for both prediction confidence and forward influence. It then computes a redundancy reward based on the entropy of low-importance tokens, normalized by its theoretical upper bound, and optimizes this reward via reinforcement learning. Experiments on mathematical reasoning benchmarks demonstrate that ENTRA reduces output length by 37% to 53% with no loss-and in some cases, gains-in accuracy. Our approach offers a principled and efficient solution to reduce overthinking in LRMs, and provides a generalizable path toward redundancy-aware reasoning optimization.

