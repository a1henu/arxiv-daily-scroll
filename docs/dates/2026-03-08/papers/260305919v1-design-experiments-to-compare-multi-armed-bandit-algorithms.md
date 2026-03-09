---
layout: default
title: Design Experiments to Compare Multi-armed Bandit Algorithms
---

# Design Experiments to Compare Multi-armed Bandit Algorithms
**arXiv**：[2603.05919v1](https://arxiv.org/abs/2603.05919) · [PDF](https://arxiv.org/pdf/2603.05919.pdf)  
**作者**：Huiling Meng, Ningyuan Chen, Xuefeng Gao  

**一句话要点**：提出Artificial Replay实验设计，以低成本比较多臂老虎机算法

**关键词**：多臂老虎机, 实验设计, 在线平台, 算法比较, Artificial Replay, 无偏估计

## 3 点简述
- 核心问题：多臂老虎机算法比较需多次独立重启，成本高且延迟部署决策
- 方法要点：通过记录轨迹和重用奖励，减少用户交互次数，实现无偏估计
- 实验或效果：理论证明方差增长次线性，数值实验验证UCB、Thompson Sampling等算法的性能提升

## 摘要（原文）

> Online platforms routinely compare multi-armed bandit algorithms, such as UCB and Thompson Sampling, to select the best-performing policy. Unlike standard A/B tests for static treatments, each run of a bandit algorithm over $T$ users produces only one dependent trajectory, because the algorithm's decisions depend on all past interactions. Reliable inference therefore demands many independent restarts of the algorithm, making experimentation costly and delaying deployment decisions. We propose Artificial Replay (AR) as a new experimental design for this problem. AR first runs one policy and records its trajectory. When the second policy is executed, it reuses a recorded reward whenever it selects an action the first policy already took, and queries the real environment only otherwise. We develop a new analytical framework for this design and prove three key properties of the resulting estimator: it is unbiased; it requires only $T + o(T)$ user interactions instead of $2T$ for a run of the treatment and control policies, nearly halving the experimental cost when both policies have sub-linear regret; and its variance grows sub-linearly in $T$, whereas the estimator from a naïve design has a linearly-growing variance. Numerical experiments with UCB, Thompson Sampling, and $ε$-greedy policies confirm these theoretical gains.

