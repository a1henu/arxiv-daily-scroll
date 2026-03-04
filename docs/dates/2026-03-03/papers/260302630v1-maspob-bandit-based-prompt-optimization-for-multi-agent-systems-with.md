---
layout: default
title: MASPOB: Bandit-Based Prompt Optimization for Multi-Agent Systems with Graph Neural Networks
---

# MASPOB: Bandit-Based Prompt Optimization for Multi-Agent Systems with Graph Neural Networks
**arXiv**：[2603.02630v1](https://arxiv.org/abs/2603.02630) · [PDF](https://arxiv.org/pdf/2603.02630.pdf)  
**作者**：Zhi Hong, Qian Zhang, Jiahang Sun, Zhiwei Shang, Mingze Kong, Xiangyi Wang, Yao Shu, Zhongxiang Dai  

**一句话要点**：提出MASPOB框架，基于多臂老虎机和图神经网络，解决多智能体系统提示优化的样本效率与耦合问题。

**关键词**：多智能体系统, 提示优化, 多臂老虎机, 图神经网络, 样本效率, 坐标上升

## 3 点简述
- 核心问题：多智能体系统提示优化面临高评估成本、拓扑耦合和搜索空间组合爆炸三大挑战。
- 方法要点：结合UCB老虎机平衡探索与利用，利用GNN捕获拓扑先验，采用坐标上升降低搜索复杂度。
- 实验或效果：在多个基准测试中实现最优性能，显著超越现有基线方法。

## 摘要（原文）

> Large Language Models (LLMs) have achieved great success in many real-world applications, especially the one serving as the cognitive backbone of Multi-Agent Systems (MAS) to orchestrate complex workflows in practice. Since many deployment scenarios preclude MAS workflow modifications and its performance is highly sensitive to the input prompts, prompt optimization emerges as a more natural approach to improve its performance. However, real-world prompt optimization for MAS is impeded by three key challenges: (1) the need of sample efficiency due to prohibitive evaluation costs, (2) topology-induced coupling among prompts, and (3) the combinatorial explosion of the search space. To address these challenges, we introduce MASPOB (Multi-Agent System Prompt Optimization via Bandits), a novel sample-efficient framework based on bandits. By leveraging Upper Confidence Bound (UCB) to quantify uncertainty, the bandit framework balances exploration and exploitation, maximizing gains within a strictly limited budget. To handle topology-induced coupling, MASPOB integrates Graph Neural Networks (GNNs) to capture structural priors, learning topology-aware representations of prompt semantics. Furthermore, it employs coordinate ascent to decompose the optimization into univariate sub-problems, reducing search complexity from exponential to linear. Extensive experiments across diverse benchmarks demonstrate that MASPOB achieves state-of-the-art performance, consistently outperforming existing baselines.

