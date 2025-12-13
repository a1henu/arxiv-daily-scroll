---
layout: default
title: Adaptive Replay Buffer for Offline-to-Online Reinforcement Learning
---

# Adaptive Replay Buffer for Offline-to-Online Reinforcement Learning
**arXiv**：[2512.10510v1](https://arxiv.org/abs/2512.10510) · [PDF](https://arxiv.org/pdf/2512.10510.pdf)  
**作者**：Chihyeon Song, Jaewoo Lee, Jinkyoo Park  

**一句话要点**：提出自适应回放缓冲区以解决离线到在线强化学习中的数据平衡问题

**关键词**：离线到在线强化学习, 自适应回放缓冲区, 数据采样策略, 学习稳定性, 渐进性能优化

## 3 点简述
- 核心问题：离线到在线强化学习中，固定数据混合比例难以平衡早期学习稳定性与渐进性能。
- 方法要点：基于轻量级指标'on-policyness'动态优先采样数据，无需复杂学习过程，易于集成现有算法。
- 实验或效果：在D4RL基准测试中，有效缓解早期性能下降，显著提升多种算法的最终性能。

## 摘要（原文）

> Offline-to-Online Reinforcement Learning (O2O RL) faces a critical dilemma in balancing the use of a fixed offline dataset with newly collected online experiences. Standard methods, often relying on a fixed data-mixing ratio, struggle to manage the trade-off between early learning stability and asymptotic performance. To overcome this, we introduce the Adaptive Replay Buffer (ARB), a novel approach that dynamically prioritizes data sampling based on a lightweight metric we call 'on-policyness'. Unlike prior methods that rely on complex learning procedures or fixed ratios, ARB is designed to be learning-free and simple to implement, seamlessly integrating into existing O2O RL algorithms. It assesses how closely collected trajectories align with the current policy's behavior and assigns a proportional sampling weight to each transition within that trajectory. This strategy effectively leverages offline data for initial stability while progressively focusing learning on the most relevant, high-rewarding online experiences. Our extensive experiments on D4RL benchmarks demonstrate that ARB consistently mitigates early performance degradation and significantly improves the final performance of various O2O RL algorithms, highlighting the importance of an adaptive, behavior-aware replay buffer design.

