---
layout: default
title: Not All Candidates are Created Equal: A Heterogeneity-Aware Approach to Pre-ranking in Recommender Systems
---

# Not All Candidates are Created Equal: A Heterogeneity-Aware Approach to Pre-ranking in Recommender Systems
**arXiv**：[2603.03770v1](https://arxiv.org/abs/2603.03770) · [PDF](https://arxiv.org/pdf/2603.03770.pdf)  
**作者**：Pengfei Tong, Siyuan Chen, Chenwei Zhang, Bo Wang, Qi Pi, Pixun Li, Zuotao Liu  

**一句话要点**：提出异构感知自适应预排序框架以解决推荐系统中预排序阶段的梯度冲突与计算效率问题

**关键词**：推荐系统预排序, 异构样本处理, 梯度冲突缓解, 自适应计算分配, 工业部署优化

## 3 点简述
- 核心问题：预排序阶段训练样本异构性导致梯度冲突，硬样本主导训练而简单样本利用不足
- 方法要点：通过冲突敏感采样与定制损失设计分离简单与硬样本，并自适应分配计算预算
- 实验或效果：在头条生产系统部署9个月，用户应用使用时长提升0.4%，无额外计算成本

## 摘要（原文）

> Most large-scale recommender systems follow a multi-stage cascade of retrieval, pre-ranking, ranking, and re-ranking. A key challenge at the pre-ranking stage arises from the heterogeneity of training instances sampled from coarse-grained retrieval results, fine-grained ranking signals, and exposure feedback. Our analysis reveals that prevailing pre-ranking methods, which indiscriminately mix heterogeneous samples, suffer from gradient conflicts: hard samples dominate training while easy ones remain underutilized, leading to suboptimal performance. We further show that the common practice of uniformly scaling model complexity across all samples is inefficient, as it overspends computation on easy cases and slows training without proportional gains. To address these limitations, this paper presents Heterogeneity-Aware Adaptive Pre-ranking (HAP), a unified framework that mitigates gradient conflicts through conflict-sensitive sampling coupled with tailored loss design, while adaptively allocating computational budgets across candidates. Specifically, HAP disentangles easy and hard samples, directing each subset along dedicated optimization paths. Building on this separation, it first applies lightweight models to all candidates for efficient coverage, and further engages stronger models on the hard ones, maintaining accuracy while reducing cost. This approach not only improves pre-ranking effectiveness but also provides a practical perspective on scaling strategies in industrial recommender systems. HAP has been deployed in the Toutiao production system for 9 months, yielding up to 0.4% improvement in user app usage duration and 0.05% in active days, without additional computational cost. We also release a large-scale industrial hybrid-sample dataset to enable the systematic study of source-driven candidate heterogeneity in pre-ranking.

