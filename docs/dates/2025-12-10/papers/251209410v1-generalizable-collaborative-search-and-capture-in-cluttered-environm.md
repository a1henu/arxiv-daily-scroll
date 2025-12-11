---
layout: default
title: Generalizable Collaborative Search-and-Capture in Cluttered Environments via Path-Guided MAPPO and Directional Frontier Allocation
---

# Generalizable Collaborative Search-and-Capture in Cluttered Environments via Path-Guided MAPPO and Directional Frontier Allocation
**arXiv**：[2512.09410v1](https://arxiv.org/abs/2512.09410) · [PDF](https://arxiv.org/pdf/2512.09410.pdf)  
**作者**：Jialin Ying, Zhihao Li, Zicheng Dong, Guohua Wu, Yihuan Liao  

**一句话要点**：提出PGF-MAPPO框架，通过路径引导和方向性前沿分配解决杂乱环境中协作搜索与捕获的稀疏奖励问题。

**关键词**：多智能体强化学习, 协作搜索与捕获, 稀疏奖励塑形, 零样本泛化, 机器人集群控制

## 3 点简述
- 核心问题：杂乱环境中协作追逃面临稀疏奖励和受限视野，导致标准多智能体强化学习探索效率低且难以扩展。
- 方法要点：结合A*势场进行密集奖励塑形，并引入方向性前沿分配以强制空间分散，加速覆盖。
- 实验或效果：在10x10地图训练的策略能零样本泛化到20x20环境，捕获效率优于基线方法。

## 摘要（原文）

> Collaborative pursuit-evasion in cluttered environments presents significant challenges due to sparse rewards and constrained Fields of View (FOV). Standard Multi-Agent Reinforcement Learning (MARL) often suffers from inefficient exploration and fails to scale to large scenarios. We propose PGF-MAPPO (Path-Guided Frontier MAPPO), a hierarchical framework bridging topological planning with reactive control. To resolve local minima and sparse rewards, we integrate an A*-based potential field for dense reward shaping. Furthermore, we introduce Directional Frontier Allocation, combining Farthest Point Sampling (FPS) with geometric angle suppression to enforce spatial dispersion and accelerate coverage. The architecture employs a parameter-shared decentralized critic, maintaining O(1) model complexity suitable for robotic swarms. Experiments demonstrate that PGF-MAPPO achieves superior capture efficiency against faster evaders. Policies trained on 10x10 maps exhibit robust zero-shot generalization to unseen 20x20 environments, significantly outperforming rule-based and learning-based baselines.

