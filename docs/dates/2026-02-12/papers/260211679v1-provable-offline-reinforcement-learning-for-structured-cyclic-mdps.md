---
layout: default
title: Provable Offline Reinforcement Learning for Structured Cyclic MDPs
---

# Provable Offline Reinforcement Learning for Structured Cyclic MDPs
**arXiv**：[2602.11679v1](https://arxiv.org/abs/2602.11679) · [PDF](https://arxiv.org/pdf/2602.11679.pdf)  
**作者**：Kyungbok Lee, Angelica Cristello Sarteau, Michael R. Kosorok  

**一句话要点**：提出CycleFQI以解决结构化循环MDP中的离线强化学习挑战

**关键词**：离线强化学习, 循环马尔可夫决策过程, 模块化结构, 拟合Q迭代, 理论分析, 医疗决策

## 3 点简述
- 针对循环MDP中阶段异质性和策略优化传播不匹配的核心问题
- 采用模块化结构分解循环过程，扩展FQI为阶段特定Q函数以支持部分控制
- 理论分析显示缓解维度诅咒，实验在模拟和真实糖尿病数据中验证有效性

## 摘要（原文）

> We introduce a novel cyclic Markov decision process (MDP) framework for multi-step decision problems with heterogeneous stage-specific dynamics, transitions, and discount factors across the cycle. In this setting, offline learning is challenging: optimizing a policy at any stage shifts the state distributions of subsequent stages, propagating mismatch across the cycle. To address this, we propose a modular structural framework that decomposes the cyclic process into stage-wise sub-problems. While generally applicable, we instantiate this principle as CycleFQI, an extension of fitted Q-iteration enabling theoretical analysis and interpretation. It uses a vector of stage-specific Q-functions, tailored to each stage, to capture within-stage sequences and transitions between stages. This modular design enables partial control, allowing some stages to be optimized while others follow predefined policies. We establish finite-sample suboptimality error bounds and derive global convergence rates under Besov regularity, demonstrating that CycleFQI mitigates the curse of dimensionality compared to monolithic baselines. Additionally, we propose a sieve-based method for asymptotic inference of optimal policy values under a margin condition. Experiments on simulated and real-world Type 1 Diabetes data sets demonstrate CycleFQI's effectiveness.

