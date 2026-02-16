---
layout: default
title: FLAC: Maximum Entropy RL via Kinetic Energy Regularized Bridge Matching
---

# FLAC: Maximum Entropy RL via Kinetic Energy Regularized Bridge Matching
**arXiv**：[2602.12829v1](https://arxiv.org/abs/2602.12829) · [PDF](https://arxiv.org/pdf/2602.12829.pdf)  
**作者**：Lei Lv, Yunfei Li, Yu Luo, Fuchun Sun, Xiao Ma  

**一句话要点**：提出FLAC框架，通过动能正则化桥匹配解决迭代生成策略的最大熵强化学习问题。

**关键词**：最大熵强化学习, 动能正则化, 广义薛定谔桥, 迭代生成策略, 连续控制, 无似然框架

## 3 点简述
- 核心问题：迭代生成策略（如扩散模型）在连续控制中缺乏直接可访问的动作对数密度，阻碍最大熵强化学习。
- 方法要点：将策略优化视为广义薛定谔桥问题，以动能作为与高熵参考过程偏离的代理，避免显式密度估计。
- 实验或效果：在高维基准测试中表现优于或媲美强基线，自动通过拉格朗日对偶机制调节动能。

## 摘要（原文）

> Iterative generative policies, such as diffusion models and flow matching, offer superior expressivity for continuous control but complicate Maximum Entropy Reinforcement Learning because their action log-densities are not directly accessible. To address this, we propose Field Least-Energy Actor-Critic (FLAC), a likelihood-free framework that regulates policy stochasticity by penalizing the kinetic energy of the velocity field. Our key insight is to formulate policy optimization as a Generalized Schrödinger Bridge (GSB) problem relative to a high-entropy reference process (e.g., uniform). Under this view, the maximum-entropy principle emerges naturally as staying close to a high-entropy reference while optimizing return, without requiring explicit action densities. In this framework, kinetic energy serves as a physically grounded proxy for divergence from the reference: minimizing path-space energy bounds the deviation of the induced terminal action distribution. Building on this view, we derive an energy-regularized policy iteration scheme and a practical off-policy algorithm that automatically tunes the kinetic energy via a Lagrangian dual mechanism. Empirically, FLAC achieves superior or comparable performance on high-dimensional benchmarks relative to strong baselines, while avoiding explicit density estimation.

