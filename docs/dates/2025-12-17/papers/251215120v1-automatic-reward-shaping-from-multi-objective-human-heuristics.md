---
layout: default
title: Automatic Reward Shaping from Multi-Objective Human Heuristics
---

# Automatic Reward Shaping from Multi-Objective Human Heuristics
**arXiv**：[2512.15120v1](https://arxiv.org/abs/2512.15120) · [PDF](https://arxiv.org/pdf/2512.15120.pdf)  
**作者**：Yuqing Xie, Jiayu Chen, Wenhao Tang, Ya Zhang, Chao Yu, Yu Wang  

**一句话要点**：提出MORSE框架以自动组合多目标启发式奖励，解决强化学习中奖励函数设计难题。

**关键词**：强化学习, 多目标优化, 奖励塑形, 机器人任务, 双层优化, 探索策略

## 3 点简述
- 核心问题：多目标环境中手动设计有效奖励函数困难，需平衡多个目标。
- 方法要点：采用双层优化，内层训练策略，外层更新奖励函数，并引入随机性促进探索。
- 实验或效果：在MuJoCo和Isaac Sim环境中验证，任务性能接近手动调优奖励函数。

## 摘要（原文）

> Designing effective reward functions remains a central challenge in reinforcement learning, especially in multi-objective environments. In this work, we propose Multi-Objective Reward Shaping with Exploration (MORSE), a general framework that automatically combines multiple human-designed heuristic rewards into a unified reward function. MORSE formulates the shaping process as a bi-level optimization problem: the inner loop trains a policy to maximize the current shaped reward, while the outer loop updates the reward function to optimize task performance. To encourage exploration in the reward space and avoid suboptimal local minima, MORSE introduces stochasticity into the shaping process, injecting noise guided by task performance and the prediction error of a fixed, randomly initialized neural network. Experimental results in MuJoCo and Isaac Sim environments show that MORSE effectively balances multiple objectives across various robotic tasks, achieving task performance comparable to those obtained with manually tuned reward functions.

