---
layout: default
title: Piece of CAKE: Adaptive Execution Engines via Microsecond-Scale Learning
---

# Piece of CAKE: Adaptive Execution Engines via Microsecond-Scale Learning
**arXiv**：[2602.04181v1](https://arxiv.org/abs/2602.04181) · [PDF](https://arxiv.org/pdf/2602.04181.pdf)  
**作者**：Zijie Zhao, Ryan Marcus  

**一句话要点**：提出CAKE系统，通过微秒级学习自适应选择数据库内核以优化性能

**关键词**：数据库内核选择, 自适应执行引擎, 微秒级学习, 上下文多臂老虎机, 反事实反馈, 后悔树

## 3 点简述
- 核心问题：数据库内核选择依赖静态启发式，无法适应数据分布变化，导致性能损失
- 方法要点：利用反事实反馈和上下文多臂老虎机，编译低延迟后悔树实现微秒级学习
- 实验或效果：相比先进静态启发式，CAKE可将端到端工作负载延迟降低高达2倍

## 摘要（原文）

> Low-level database operators often admit multiple physical implementations ("kernels") that are semantically equivalent but have vastly different performance characteristics depending on the input data distribution. Existing database systems typically rely on static heuristics or worst-case optimal defaults to select these kernels, often missing significant performance opportunities. In this work, we propose CAKE (Counterfactual Adaptive Kernel Execution), a system that learns to select the optimal kernel for each data "morsel" using a microsecond-scale contextual multi-armed bandit. CAKE circumvents the high latency of traditional reinforcement learning by exploiting the cheapness of counterfactuals -- selectively running multiple kernels to obtain full feedback -- and compiling policies into low-latency regret trees. Experimentally, we show that CAKE can reduce end-to-end workload latency by up to 2x compared to state-of-the-art static heuristics.

