---
layout: default
title: ECHO: Entropy-Confidence Hybrid Optimization for Test-Time Reinforcement Learning
---

# ECHO: Entropy-Confidence Hybrid Optimization for Test-Time Reinforcement Learning
**arXiv**：[2602.02150v1](https://arxiv.org/abs/2602.02150) · [PDF](https://arxiv.org/pdf/2602.02150.pdf)  
**作者**：Chu Zhao, Enneng Yang, Yuting Liu, Jianzhe Zhao, Guibing Guo  

**一句话要点**：提出ECHO方法以解决测试时强化学习中分支崩溃和早期伪标签噪声问题

**关键词**：测试时强化学习, 树状rollout, 熵置信度混合优化, 分支崩溃缓解, 伪标签噪声处理, 在线策略更新

## 3 点简述
- 核心问题：树状rollout中高熵分支导致崩溃，早期伪标签噪声引发过早过拟合
- 方法要点：结合局部熵和组置信度自适应控制分支宽度，引入置信度剪枝和混合优势塑形
- 实验或效果：在数学和视觉推理基准上取得一致提升，有限rollout预算下泛化更有效

## 摘要（原文）

> Test-time reinforcement learning generates multiple candidate answers via repeated rollouts and performs online updates using pseudo-labels constructed by majority voting. To reduce overhead and improve exploration, prior work introduces tree structured rollouts, which share reasoning prefixes and branch at key nodes to improve sampling efficiency. However, this paradigm still faces two challenges: (1) high entropy branching can trigger rollout collapse, where the branching budget concentrates on a few trajectories with consecutive high-entropy segments, rapidly reducing the number of effective branches; (2) early pseudo-labels are noisy and biased, which can induce self-reinforcing overfitting, causing the policy to sharpen prematurely and suppress exploration. To address these issues, we propose Entropy Confidence Hybrid Group Relative Policy Optimization (ECHO). During rollout, ECHO jointly leverages local entropy and group level confidence to adaptively control branch width, and further introduces online confidence-based pruning to terminate persistently low confidence branches, avoiding high entropy traps and mitigating collapse. During policy updates, ECHO employs confidence adaptive clipping and an entropy confidence hybrid advantage shaping approach to enhance training robustness and mitigate early stage bias. Experiments demonstrate that ECHO achieves consistent gains on multiple mathematical and visual reasoning benchmarks, and generalizes more effectively under a limited rollout budget.

