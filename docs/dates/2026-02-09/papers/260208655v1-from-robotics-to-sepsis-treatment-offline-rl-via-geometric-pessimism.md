---
layout: default
title: From Robotics to Sepsis Treatment: Offline RL via Geometric Pessimism
---

# From Robotics to Sepsis Treatment: Offline RL via Geometric Pessimism
**arXiv**：[2602.08655v1](https://arxiv.org/abs/2602.08655) · [PDF](https://arxiv.org/pdf/2602.08655.pdf)  
**作者**：Sarthak Wanjari  

**一句话要点**：提出几何悲观主义框架，通过密度惩罚增强离线强化学习在稀疏数据中的安全优化

**关键词**：离线强化学习, 分布外动作, 几何悲观主义, 奖励塑形, 稀疏数据, 医疗决策

## 3 点简述
- 离线强化学习易高估分布外动作，尤其在稀疏数据中，现有方法在计算效率与性能间需权衡。
- 方法基于IQL，在状态-动作嵌入空间使用k近邻距离计算密度惩罚，以奖励塑形注入保守性，训练开销为O(1)。
- 在D4RL MuJoCo基准上，Geo-IQL在敏感任务中性能提升超18点，方差降低4倍；在MIMIC-III脓毒症数据中，避免行为克隆，终端一致性达86.4%。

## 摘要（原文）

> Offline Reinforcement Learning (RL) promises the recovery of optimal policies from static datasets, yet it remains susceptible to the overestimation of out-of-distribution (OOD) actions, particularly in fractured and sparse data manifolds.Current solutions necessitates a trade off between computational efficiency and performance. Methods like CQL offers rigorous conservatism but require tremendous compute power while efficient expectile-based methods like IQL often fail to correct OOD errors on pathological datasets, collapsing to Behavioural Cloning. In this work, we propose Geometric Pessimism, a modular, compute-efficient framework that augments standard IQL with density-based penalty derived from k-nearest-neighbour distances in the state-action embedding space. By pre-computing the penalties applied to each state-action pair our method injects OOD conservatism via reward shaping with a O(1) training overhead. Evaluated on the D4Rl MuJoCo benchmark, our method, Geo-IQL outperforms standard IQL on sensitive and unstable medium-replay tasks by over 18 points, while reducing inter-seed variance by 4x. Furthermore, Geo-IQL does not degrade performance on stable manifolds. Crucially, we validate our algorithm on the MIMIC-III Sepsis critical care dataset. While standard IQL collapses to behaviour cloning, Geo-IQL demonstrates active policy improvement. Maintaining safety constraints, achieving 86.4% terminal agreement with clinicians compared to IQL's 75%. Our results suggest that geometric pessimism provides the necessary regularisation to safely overcome local optima in critical, real-world decision systems.

