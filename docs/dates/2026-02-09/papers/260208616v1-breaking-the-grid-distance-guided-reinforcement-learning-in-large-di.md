---
layout: default
title: Breaking the Grid: Distance-Guided Reinforcement Learning in Large Discrete and Hybrid Action Spaces
---

# Breaking the Grid: Distance-Guided Reinforcement Learning in Large Discrete and Hybrid Action Spaces
**arXiv**：[2602.08616v1](https://arxiv.org/abs/2602.08616) · [PDF](https://arxiv.org/pdf/2602.08616.pdf)  
**作者**：Heiko Hoppe, Fabian Akkerman, Wouter van Heeswijk, Maximilian Schiffer  

**一句话要点**：提出距离引导强化学习以解决大规模离散和混合动作空间中的维度诅咒问题

**关键词**：强化学习, 大规模动作空间, 距离引导学习, 混合动作空间, 策略优化, 语义嵌入

## 3 点简述
- 核心问题：标准强化学习算法在大规模离散动作空间中面临维度诅咒，现有方法依赖网格结构或高成本搜索，限制高维或不规则领域应用。
- 方法要点：结合采样动态邻域和基于距离的更新，利用语义嵌入空间进行随机体积探索，将策略优化转化为稳定回归任务，保证单调改进。
- 实验或效果：在规则和不规则结构环境中，性能提升高达66%，同时提高收敛速度和计算效率，并自然泛化到混合连续-离散动作空间。

## 摘要（原文）

> Reinforcement Learning is increasingly applied to logistics, scheduling, and recommender systems, but standard algorithms struggle with the curse of dimensionality in such large discrete action spaces. Existing algorithms typically rely on restrictive grid-based structures or computationally expensive nearest-neighbor searches, limiting their effectiveness in high-dimensional or irregularly structured domains. We propose Distance-Guided Reinforcement Learning (DGRL), combining Sampled Dynamic Neighborhoods (SDN) and Distance-Based Updates (DBU) to enable efficient RL in spaces with up to 10$^\text{20}$ actions. Unlike prior methods, SDN leverages a semantic embedding space to perform stochastic volumetric exploration, provably providing full support over a local trust region. Complementing this, DBU transforms policy optimization into a stable regression task, decoupling gradient variance from action space cardinality and guaranteeing monotonic policy improvement. DGRL naturally generalizes to hybrid continuous-discrete action spaces without requiring hierarchical dependencies. We demonstrate performance improvements of up to 66% against state-of-the-art benchmarks across regularly and irregularly structured environments, while simultaneously improving convergence speed and computational complexity.

