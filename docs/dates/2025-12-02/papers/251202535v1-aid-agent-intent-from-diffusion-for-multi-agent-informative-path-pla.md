---
layout: default
title: AID: Agent Intent from Diffusion for Multi-Agent Informative Path Planning
---

# AID: Agent Intent from Diffusion for Multi-Agent Informative Path Planning
**arXiv**：[2512.02535v1](https://arxiv.org/abs/2512.02535) · [PDF](https://arxiv.org/pdf/2512.02535.pdf)  
**作者**：Jeric Lew, Yuhong Cao, Derek Ming Siang Tan, Guillaume Sartoretti  

**一句话要点**：提出AID框架，利用扩散模型解决多智能体信息路径规划中的协调问题

**关键词**：多智能体信息路径规划, 扩散模型, 非自回归轨迹生成, 行为克隆, 强化学习优化, 去中心化协调

## 3 点简述
- 核心问题：多智能体信息路径规划中，协调困难且现有意图预测方法计算成本高、易出错
- 方法要点：采用扩散模型非自回归生成长期轨迹，结合行为克隆与强化学习优化策略
- 实验或效果：相比基线，执行速度提升高达4倍，信息增益增加17%，可扩展至更多智能体

## 摘要（原文）

> Information gathering in large-scale or time-critical scenarios (e.g., environmental monitoring, search and rescue) requires broad coverage within limited time budgets, motivating the use of multi-agent systems. These scenarios are commonly formulated as multi-agent informative path planning (MAIPP), where multiple agents must coordinate to maximize information gain while operating under budget constraints. A central challenge in MAIPP is ensuring effective coordination while the belief over the environment evolves with incoming measurements. Recent learning-based approaches address this by using distributions over future positions as "intent" to support coordination. However, these autoregressive intent predictors are computationally expensive and prone to compounding errors. Inspired by the effectiveness of diffusion models as expressive, long-horizon policies, we propose AID, a fully decentralized MAIPP framework that leverages diffusion models to generate long-term trajectories in a non-autoregressive manner. AID first performs behavior cloning on trajectories produced by existing MAIPP planners and then fine-tunes the policy using reinforcement learning via Diffusion Policy Policy Optimization (DPPO). This two-stage pipeline enables the policy to inherit expert behavior while learning improved coordination through online reward feedback. Experiments demonstrate that AID consistently improves upon the MAIPP planners it is trained from, achieving up to 4x faster execution and 17% increased information gain, while scaling effectively to larger numbers of agents. Our implementation is publicly available at https://github.com/marmotlab/AID.

