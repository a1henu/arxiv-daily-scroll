---
layout: default
title: On the Robustness of Age for Learning-Based Wireless Scheduling in Unknown Environments
---

# On the Robustness of Age for Learning-Based Wireless Scheduling in Unknown Environments
**arXiv**：[2601.05956v1](https://arxiv.org/abs/2601.05956) · [PDF](https://arxiv.org/pdf/2601.05956.pdf)  
**作者**：Juaren Steiger, Bin Li  

**一句话要点**：提出基于队首年龄的无线调度策略，提升未知环境下的鲁棒性

**关键词**：无线调度, 多臂老虎机, 鲁棒性学习, 队首年龄, 虚拟队列, 未知环境

## 3 点简述
- 核心问题：无线调度中虚拟队列长度在信道突变时可能无限增长，导致系统不稳定
- 方法要点：用队首年龄替代虚拟队列长度设计学习算法，增强对约束不可行性的适应
- 实验或效果：在独立同分布条件下性能匹配最优，信道突变时系统稳定且快速恢复

## 摘要（原文）

> The constrained combinatorial multi-armed bandit model has been widely employed to solve problems in wireless networking and related areas, including the problem of wireless scheduling for throughput optimization under unknown channel conditions. Most work in this area uses an algorithm design strategy that combines a bandit learning algorithm with the virtual queue technique to track the throughput constraint violation. These algorithms seek to minimize the virtual queue length in their algorithm design. However, in networks where channel conditions change abruptly, the resulting constraints may become infeasible, leading to unbounded growth in virtual queue lengths. In this paper, we make the key observation that the dynamics of the head-of-line age, i.e. the age of the oldest packet in the virtual queue, make it more robust when used in algorithm design compared to the virtual queue length. We therefore design a learning-based scheduling policy that uses the head-of-line age in place of the virtual queue length. We show that our policy matches state-of-the-art performance under i.i.d. network conditions. Crucially, we also show that the system remains stable even under abrupt changes in channel conditions and can rapidly recover from periods of constraint infeasibility.

