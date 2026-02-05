---
layout: default
title: Topology-Aware Revival for Efficient Sparse Training
---

# Topology-Aware Revival for Efficient Sparse Training
**arXiv**：[2602.04166v1](https://arxiv.org/abs/2602.04166) · [PDF](https://arxiv.org/pdf/2602.04166.pdf)  
**作者**：Meiling Jin, Fei Wang, Xiaoyun Yuan, Chen Qian, Yuan Cheng  

**一句话要点**：提出拓扑感知复活方法以提升静态稀疏训练在深度强化学习中的效率与鲁棒性

**关键词**：静态稀疏训练, 深度强化学习, 拓扑感知, 剪枝优化, 连续控制任务

## 3 点简述
- 静态稀疏训练因固定掩码模式易导致结构脆弱，尤其在策略演变的深度强化学习中
- TAR通过一次性后剪枝步骤，基于拓扑需求分配预算并随机均匀复活部分连接
- 在连续控制任务中，TAR显著提升最终回报，优于静态和动态稀疏训练基线

## 摘要（原文）

> Static sparse training is a promising route to efficient learning by committing to a fixed mask pattern, yet the constrained structure reduces robustness. Early pruning decisions can lock the network into a brittle structure that is difficult to escape, especially in deep reinforcement learning (RL) where the evolving policy continually shifts the training distribution. We propose Topology-Aware Revival (TAR), a lightweight one-shot post-pruning procedure that improves static sparsity without dynamic rewiring. After static pruning, TAR performs a single revival step by allocating a small reserve budget across layers according to topology needs, randomly uniformly reactivating a few previously pruned connections within each layer, and then keeping the resulting connectivity fixed for the remainder of training. Across multiple continuous-control tasks with SAC and TD3, TAR improves final return over static sparse baselines by up to +37.9% and also outperforms dynamic sparse training baselines with a median gain of +13.5%.

