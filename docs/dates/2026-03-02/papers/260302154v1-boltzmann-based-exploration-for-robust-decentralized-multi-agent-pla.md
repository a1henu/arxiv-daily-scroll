---
layout: default
title: Boltzmann-based Exploration for Robust Decentralized Multi-Agent Planning
---

# Boltzmann-based Exploration for Robust Decentralized Multi-Agent Planning
**arXiv**：[2603.02154v1](https://arxiv.org/abs/2603.02154) · [PDF](https://arxiv.org/pdf/2603.02154.pdf)  
**作者**：Nhat Nguyen, Duong Nguyen, Gianluca Rizzo, Hung Nguyen  

**一句话要点**：提出协调玻尔兹曼MCTS以解决多智能体规划在稀疏或偏斜奖励环境中的探索问题

**关键词**：多智能体规划, 蒙特卡洛树搜索, 玻尔兹曼探索, 分散式决策, 稀疏奖励环境

## 3 点简述
- 核心问题：分散式蒙特卡洛树搜索在稀疏或偏斜奖励环境中探索不足，影响多智能体规划效果
- 方法要点：用随机玻尔兹曼策略和衰减熵奖励替代确定性UCT，实现持续且聚焦的探索
- 实验或效果：在欺骗性场景中优于Dec-MCTS，在标准基准测试中保持竞争力，提供鲁棒解决方案

## 摘要（原文）

> Decentralized Monte Carlo Tree Search (Dec-MCTS) is widely used for cooperative multi-agent planning but struggles in sparse or skewed reward environments. We introduce Coordinated Boltzmann MCTS (CB-MCTS), which replaces deterministic UCT with a stochastic Boltzmann policy and a decaying entropy bonus for sustained yet focused exploration. While Boltzmann exploration has been studied in single-agent MCTS, applying it in multi-agent systems poses unique challenges. CB-MCTS is the first to address this. We analyze CB-MCTS in the simple-regret setting and show in simulations that it outperforms Dec-MCTS in deceptive scenarios and remains competitive on standard benchmarks, providing a robust solution for multi-agent planning.

