---
layout: default
title: PUL-SLAM: Path-Uncertainty Co-Optimization with Lightweight Stagnation Detection for Efficient Robotic Exploration
---

# PUL-SLAM: Path-Uncertainty Co-Optimization with Lightweight Stagnation Detection for Efficient Robotic Exploration
**arXiv**：[2511.04180v1](https://arxiv.org/abs/2511.04180) · [PDF](https://arxiv.org/pdf/2511.04180.pdf)  
**作者**：Yizhen Yin, Dapeng Feng, Hongbo Chen, Yuhua Qi  

**一句话要点**：提出路径-不确定性协同优化与轻量停滞检测框架，以提升机器人探索效率

**关键词**：主动SLAM, 路径优化, 不确定性建模, 强化学习, 机器人探索, 停滞检测

## 3 点简述
- 现有主动SLAM方法存在探索速度慢和路径次优问题
- 结合路径-不确定性协同优化DRL和轻量停滞检测机制，平衡探索与利用
- 实验显示探索时间缩短65%，路径距离减少42%，验证实际适用性

## 摘要（原文）

> Existing Active SLAM methodologies face issues such as slow exploration speed
> and suboptimal paths. To address these limitations, we propose a hybrid
> framework combining a Path-Uncertainty Co-Optimization Deep Reinforcement
> Learning framework and a Lightweight Stagnation Detection mechanism. The
> Path-Uncertainty Co-Optimization framework jointly optimizes travel distance
> and map uncertainty through a dual-objective reward function, balancing
> exploration and exploitation. The Lightweight Stagnation Detection reduces
> redundant exploration through Lidar Static Anomaly Detection and Map Update
> Stagnation Detection, terminating episodes on low expansion rates. Experimental
> results show that compared with the frontier-based method and RRT method, our
> approach shortens exploration time by up to 65% and reduces path distance by up
> to 42%, significantly improving exploration efficiency in complex environments
> while maintaining reliable map completeness. Ablation studies confirm that the
> collaborative mechanism accelerates training convergence. Empirical validation
> on a physical robotic platform demonstrates the algorithm's practical
> applicability and its successful transferability from simulation to real-world
> environments.

