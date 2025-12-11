---
layout: default
title: Gaussian Process Aggregation for Root-Parallel Monte Carlo Tree Search with Continuous Actions
---

# Gaussian Process Aggregation for Root-Parallel Monte Carlo Tree Search with Continuous Actions
**arXiv**：[2512.09727v1](https://arxiv.org/abs/2512.09727) · [PDF](https://arxiv.org/pdf/2512.09727.pdf)  
**作者**：Junlin Xiao, Victor-Alexandru Darvariu, Bruno Lacerda, Nick Hawes  

**一句话要点**：提出高斯过程聚合方法以提升根并行蒙特卡洛树搜索在连续动作空间中的性能

**关键词**：蒙特卡洛树搜索, 连续动作空间, 高斯过程回归, 根并行规划, 在线规划, 统计聚合

## 3 点简述
- 核心问题：连续动作空间中根并行蒙特卡洛树搜索的线程统计聚合策略未充分探索
- 方法要点：使用高斯过程回归估计未尝试动作的价值，优化聚合过程
- 实验或效果：在6个领域系统评估，显示方法优于现有策略，推理时间略有增加

## 摘要（原文）

> Monte Carlo Tree Search is a cornerstone algorithm for online planning, and its root-parallel variant is widely used when wall clock time is limited but best performance is desired. In environments with continuous action spaces, how to best aggregate statistics from different threads is an important yet underexplored question. In this work, we introduce a method that uses Gaussian Process Regression to obtain value estimates for promising actions that were not trialed in the environment. We perform a systematic evaluation across 6 different domains, demonstrating that our approach outperforms existing aggregation strategies while requiring a modest increase in inference time.

