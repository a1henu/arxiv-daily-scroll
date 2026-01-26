---
layout: default
title: Reinforcement Learning-Based Energy-Aware Coverage Path Planning for Precision Agriculture
---

# Reinforcement Learning-Based Energy-Aware Coverage Path Planning for Precision Agriculture
**arXiv**：[2601.16405v1](https://arxiv.org/abs/2601.16405) · [PDF](https://arxiv.org/pdf/2601.16405.pdf)  
**作者**：Beining Wu, Zihao Ding, Leo Ostigaard, Jun Huang  

**一句话要点**：提出基于SAC强化学习的能量感知覆盖路径规划框架，用于农业机器人网格环境。

**关键词**：覆盖路径规划, 强化学习, 能量感知, 农业机器人, 卷积神经网络, 长短期记忆网络

## 3 点简述
- 核心问题：现有覆盖路径规划忽略能量约束，导致大规模或资源受限环境中操作不完整。
- 方法要点：结合CNN和LSTM，设计奖励函数优化覆盖效率、能耗和返航约束。
- 实验或效果：实验显示覆盖率达90%以上，优于传统启发式算法，减少约束违反59.9-88.3%。

## 摘要（原文）

> Coverage Path Planning (CPP) is a fundamental capability for agricultural robots; however, existing solutions often overlook energy constraints, resulting in incomplete operations in large-scale or resource-limited environments. This paper proposes an energy-aware CPP framework grounded in Soft Actor-Critic (SAC) reinforcement learning, designed for grid-based environments with obstacles and charging stations. To enable robust and adaptive decision-making under energy limitations, the framework integrates Convolutional Neural Networks (CNNs) for spatial feature extraction and Long Short-Term Memory (LSTM) networks for temporal dynamics. A dedicated reward function is designed to jointly optimize coverage efficiency, energy consumption, and return-to-base constraints. Experimental results demonstrate that the proposed approach consistently achieves over 90% coverage while ensuring energy safety, outperforming traditional heuristic algorithms such as Rapidly-exploring Random Tree (RRT), Particle Swarm Optimization (PSO), and Ant Colony Optimization (ACO) baselines by 13.4-19.5% in coverage and reducing constraint violations by 59.9-88.3%. These findings validate the proposed SAC-based framework as an effective and scalable solution for energy-constrained CPP in agricultural robotics.

