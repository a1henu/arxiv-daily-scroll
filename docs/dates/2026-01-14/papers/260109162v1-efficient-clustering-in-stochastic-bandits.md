---
layout: default
title: Efficient Clustering in Stochastic Bandits
---

# Efficient Clustering in Stochastic Bandits
**arXiv**：[2601.09162v1](https://arxiv.org/abs/2601.09162) · [PDF](https://arxiv.org/pdf/2601.09162.pdf)  
**作者**：G Dhinesh Chandran, Kota Srinivas Reddy, Srikrishna Bhashyam  

**一句话要点**：提出高效赌博机聚类算法EBC，在固定置信度下实现渐近最优且计算高效

**关键词**：赌博机聚类, 固定置信度, 渐近最优, 计算效率, 向量参数分布, 顺序采样

## 3 点简述
- 研究赌博机聚类问题，允许聚类内臂分布不同，扩展至满足正则条件的向量参数分布
- 提出EBC算法，通过单步逼近优化问题，避免每步完全求解，提升计算效率
- 通过合成和真实数据集模拟验证EBC的渐近最优性和性能优势

## 摘要（原文）

> We study the Bandit Clustering (BC) problem under the fixed confidence setting, where the objective is to group a collection of data sequences (arms) into clusters through sequential sampling from adaptively selected arms at each time step while ensuring a fixed error probability at the stopping time. We consider a setting where arms in a cluster may have different distributions. Unlike existing results in this setting, which assume Gaussian-distributed arms, we study a broader class of vector-parametric distributions that satisfy mild regularity conditions. Existing asymptotically optimal BC algorithms require solving an optimization problem as part of their sampling rule at each step, which is computationally costly. We propose an Efficient Bandit Clustering algorithm (EBC), which, instead of solving the full optimization problem, takes a single step toward the optimal value at each time step, making it computationally efficient while remaining asymptotically optimal. We also propose a heuristic variant of EBC, called EBC-H, which further simplifies the sampling rule, with arm selection based on quantities computed as part of the stopping rule. We highlight the computational efficiency of EBC and EBC-H by comparing their per-sample run time with that of existing algorithms. The asymptotic optimality of EBC is supported through simulations on the synthetic datasets. Through simulations on both synthetic and real-world datasets, we show the performance gain of EBC and EBC-H over existing approaches.

