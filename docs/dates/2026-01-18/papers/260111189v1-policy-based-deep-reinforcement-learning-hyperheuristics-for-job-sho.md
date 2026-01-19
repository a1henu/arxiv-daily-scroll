---
layout: default
title: Policy-Based Deep Reinforcement Learning Hyperheuristics for Job-Shop Scheduling Problems
---

# Policy-Based Deep Reinforcement Learning Hyperheuristics for Job-Shop Scheduling Problems
**arXiv**：[2601.11189v1](https://arxiv.org/abs/2601.11189) · [PDF](https://arxiv.org/pdf/2601.11189.pdf)  
**作者**：Sofiene Lassoued, Asrat Gobachew, Stefan Lier, Andreas Schwung  

**一句话要点**：提出基于策略的深度强化学习超启发式框架以解决作业车间调度问题

**关键词**：作业车间调度, 深度强化学习, 超启发式, 动作预过滤, 承诺机制, 调度规则

## 3 点简述
- 核心问题：作业车间调度问题，需动态切换调度规则以优化完工时间
- 方法要点：引入动作预过滤和承诺机制，评估不同承诺策略与动作选择策略
- 实验或效果：在标准基准上优于传统启发式、元启发式及近期神经网络方法

## 摘要（原文）

> This paper proposes a policy-based deep reinforcement learning hyper-heuristic framework for solving the Job Shop Scheduling Problem. The hyper-heuristic agent learns to switch scheduling rules based on the system state dynamically. We extend the hyper-heuristic framework with two key mechanisms. First, action prefiltering restricts decision-making to feasible low-level actions, enabling low-level heuristics to be evaluated independently of environmental constraints and providing an unbiased assessment. Second, a commitment mechanism regulates the frequency of heuristic switching. We investigate the impact of different commitment strategies, from step-wise switching to full-episode commitment, on both training behavior and makespan. Additionally, we compare two action selection strategies at the policy level: deterministic greedy selection and stochastic sampling. Computational experiments on standard JSSP benchmarks demonstrate that the proposed approach outperforms traditional heuristics, metaheuristics, and recent neural network-based scheduling methods

