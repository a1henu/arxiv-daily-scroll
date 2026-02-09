---
layout: default
title: Sample-Efficient Policy Space Response Oracles with Joint Experience Best Response
---

# Sample-Efficient Policy Space Response Oracles with Joint Experience Best Response
**arXiv**：[2602.06599v1](https://arxiv.org/abs/2602.06599) · [PDF](https://arxiv.org/pdf/2602.06599.pdf)  
**作者**：Ariyan Bighashdel, Thiago D. Simão, Frans A. Oliehoek  

**一句话要点**：提出联合经验最佳响应以提升策略空间响应预言机在多人强化学习中的样本效率

**关键词**：多人强化学习, 策略空间响应预言机, 样本效率, 离线强化学习, 最佳响应计算, 联合经验

## 3 点简述
- 核心问题：策略空间响应预言机在多人强化学习中因独立最佳响应训练导致样本成本过高
- 方法要点：通过收集联合轨迹数据集并复用，同时计算所有代理的最佳响应，转化为离线强化学习问题
- 实验或效果：在基准环境中，探索增强联合经验最佳响应实现最佳精度-效率权衡，混合最佳响应以低样本成本接近原方法性能

## 摘要（原文）

> Multi-agent reinforcement learning (MARL) offers a scalable alternative to exact game-theoretic analysis but suffers from non-stationarity and the need to maintain diverse populations of strategies that capture non-transitive interactions. Policy Space Response Oracles (PSRO) address these issues by iteratively expanding a restricted game with approximate best responses (BRs), yet per-agent BR training makes it prohibitively expensive in many-agent or simulator-expensive settings. We introduce Joint Experience Best Response (JBR), a drop-in modification to PSRO that collects trajectories once under the current meta-strategy profile and reuses this joint dataset to compute BRs for all agents simultaneously. This amortizes environment interaction and improves the sample efficiency of best-response computation. Because JBR converts BR computation into an offline RL problem, we propose three remedies for distribution-shift bias: (i) Conservative JBR with safe policy improvement, (ii) Exploration-Augmented JBR that perturbs data collection and admits theoretical guarantees, and (iii) Hybrid BR that interleaves JBR with periodic independent BR updates. Across benchmark multi-agent environments, Exploration-Augmented JBR achieves the best accuracy-efficiency trade-off, while Hybrid BR attains near-PSRO performance at a fraction of the sample cost. Overall, JBR makes PSRO substantially more practical for large-scale strategic learning while preserving equilibrium robustness.

