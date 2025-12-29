---
layout: default
title: Hybrid Combinatorial Multi-armed Bandits with Probabilistically Triggered Arms
---

# Hybrid Combinatorial Multi-armed Bandits with Probabilistically Triggered Arms
**arXiv**：[2512.21925v1](https://arxiv.org/abs/2512.21925) · [PDF](https://arxiv.org/pdf/2512.21925.pdf)  
**作者**：Kongchang Zhou, Tingyu Zhang, Wei Chen, Fang Kong  

**一句话要点**：提出混合组合多臂老虎机框架，结合离线数据与在线交互以优化学习效率。

**关键词**：组合多臂老虎机, 概率触发臂, 混合学习, 离线数据, 在线交互, 遗憾分析

## 3 点简述
- 核心问题：在线组合多臂老虎机成本高，离线方法受数据质量限制，缺乏互补性。
- 方法要点：设计混合CUCB算法，利用离线数据引导探索，在线交互纠正偏差，加速收敛。
- 实验或效果：理论证明降低遗憾，实证显示优于纯在线或离线方法，尤其在高质量数据下。

## 摘要（原文）

> The problem of combinatorial multi-armed bandits with probabilistically triggered arms (CMAB-T) has been extensively studied. Prior work primarily focuses on either the online setting where an agent learns about the unknown environment through iterative interactions, or the offline setting where a policy is learned solely from logged data. However, each of these paradigms has inherent limitations: online algorithms suffer from high interaction costs and slow adaptation, while offline methods are constrained by dataset quality and lack of exploration capabilities. To address these complementary weaknesses, we propose hybrid CMAB-T, a new framework that integrates offline data with online interaction in a principled manner. Our proposed hybrid CUCB algorithm leverages offline data to guide exploration and accelerate convergence, while strategically incorporating online interactions to mitigate the insufficient coverage or distributional bias of the offline dataset. We provide theoretical guarantees on the algorithm's regret, demonstrating that hybrid CUCB significantly outperforms purely online approaches when high-quality offline data is available, and effectively corrects the bias inherent in offline-only methods when the data is limited or misaligned. Empirical results further demonstrate the consistent advantage of our algorithm.

