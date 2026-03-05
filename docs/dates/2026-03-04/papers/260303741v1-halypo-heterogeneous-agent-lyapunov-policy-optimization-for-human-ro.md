---
layout: default
title: HALyPO: Heterogeneous-Agent Lyapunov Policy Optimization for Human-Robot Collaboration
---

# HALyPO: Heterogeneous-Agent Lyapunov Policy Optimization for Human-Robot Collaboration
**arXiv**：[2603.03741v1](https://arxiv.org/abs/2603.03741) · [PDF](https://arxiv.org/pdf/2603.03741.pdf)  
**作者**：Hao Zhang, Yaru Niu, Yikai Wang, Ding Zhao, H. Eric Tseng  

**一句话要点**：提出HALyPO以稳定人机协作中的异构多智能体强化学习

**关键词**：人机协作, 多智能体强化学习, 李雅普诺夫稳定性, 异构智能体, 策略优化

## 3 点简述
- 核心问题：人机异构性导致理性差距，使分散策略梯度学习不稳定
- 方法要点：在策略参数空间施加李雅普诺夫下降条件，通过二次投影稳定梯度
- 实验或效果：仿真和真实人形机器人实验显示提升泛化性和鲁棒性

## 摘要（原文）

> To improve generalization and resilience in human-robot collaboration (HRC), robots must handle the combinatorial diversity of human behaviors and contexts, motivating multi-agent reinforcement learning (MARL). However, inherent heterogeneity between robots and humans creates a rationality gap (RG) in the learning process-a variational mismatch between decentralized best-response dynamics and centralized cooperative ascent. The resulting learning problem is a general-sum differentiable game, so independent policy-gradient updates can oscillate or diverge without added structure. We propose heterogeneous-agent Lyapunov policy optimization (HALyPO), which establishes formal stability directly in the policy-parameter space by enforcing a per-step Lyapunov decrease condition on a parameter-space disagreement metric. Unlike Lyapunov-based safe RL, which targets state/trajectory constraints in constrained Markov decision processes, HALyPO uses Lyapunov certification to stabilize decentralized policy learning. HALyPO rectifies decentralized gradients via optimal quadratic projections, ensuring monotonic contraction of RG and enabling effective exploration of open-ended interaction spaces. Extensive simulations and real-world humanoid-robot experiments show that this certified stability improves generalization and robustness in collaborative corner cases.

