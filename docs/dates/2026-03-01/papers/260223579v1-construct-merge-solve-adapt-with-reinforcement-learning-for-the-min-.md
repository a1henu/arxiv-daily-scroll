---
layout: default
title: Construct, Merge, Solve & Adapt with Reinforcement Learning for the min-max Multiple Traveling Salesman Problem
---

# Construct, Merge, Solve & Adapt with Reinforcement Learning for the min-max Multiple Traveling Salesman Problem
**arXiv**：[2602.23579v1](https://arxiv.org/abs/2602.23579) · [PDF](https://arxiv.org/pdf/2602.23579.pdf)  
**作者**：Guillem Rodríguez-Corominas, Maria J. Blesa, Christian Blum  

**一句话要点**：提出RL-CMSA方法以解决对称单仓库最小最大多旅行商问题

**关键词**：多旅行商问题, 强化学习, 混合优化算法, 最小最大目标, 精确优化, 局部搜索

## 3 点简述
- 核心问题：最小最大多旅行商问题，旨在平衡多个旅行商的工作负载。
- 方法要点：结合强化学习引导概率聚类、精确优化和局部搜索的混合算法。
- 实验效果：在随机和TSPLIB实例上优于先进混合遗传算法，尤其在大规模问题中表现突出。

## 摘要（原文）

> The Multiple Traveling Salesman Problem (mTSP) extends the Traveling Salesman Problem to m tours that start and end at a common depot and jointly visit all customers exactly once. In the min-max variant, the objective is to minimize the longest tour, reflecting workload balance. We propose a hybrid approach, Construct, Merge, Solve & Adapt with Reinforcement Learning (RL-CMSA), for the symmetric single-depot min-max mTSP. The method iteratively constructs diverse solutions using probabilistic clustering guided by learned pairwise q-values, merges routes into a compact pool, solves a restricted set-covering MILP, and refines solutions via inter-route remove, shift, and swap moves. The q-values are updated by reinforcing city-pair co-occurrences in high-quality solutions, while the pool is adapted through ageing and pruning. This combination of exact optimization and reinforcement-guided construction balances exploration and exploitation. Computational results on random and TSPLIB instances show that RL-CMSA consistently finds (near-)best solutions and outperforms a state-of-the-art hybrid genetic algorithm under comparable time limits, especially as instance size and the number of salesmen increase.

