---
layout: default
title: Denoising Particle Filters: Learning State Estimation with Single-Step Objectives
---

# Denoising Particle Filters: Learning State Estimation with Single-Step Objectives
**arXiv**：[2602.19651v1](https://arxiv.org/abs/2602.19651) · [PDF](https://arxiv.org/pdf/2602.19651.pdf)  
**作者**：Lennart Röstel, Berthold Bäuml  

**一句话要点**：提出基于去噪粒子滤波的机器人状态估计方法，通过单步目标学习提升效率与可解释性。

**关键词**：粒子滤波, 状态估计, 去噪分数匹配, 机器人学习, 单步学习, 贝叶斯滤波

## 3 点简述
- 针对基于学习的机器人状态估计中序列建模训练成本高、模型难解释的问题。
- 提出粒子滤波算法，利用马尔可夫性从单步状态转移学习，通过去噪分数匹配隐式学习测量模型。
- 在仿真机器人任务中验证，性能媲美端到端基线，并保持经典滤波的可组合性优势。

## 摘要（原文）

> Learning-based methods commonly treat state estimation in robotics as a sequence modeling problem. While this paradigm can be effective at maximizing end-to-end performance, models are often difficult to interpret and expensive to train, since training requires unrolling sequences of predictions in time. As an alternative to end-to-end trained state estimation, we propose a novel particle filtering algorithm in which models are trained from individual state transitions, fully exploiting the Markov property in robotic systems. In this framework, measurement models are learned implicitly by minimizing a denoising score matching objective. At inference, the learned denoiser is used alongside a (learned) dynamics model to approximately solve the Bayesian filtering equation at each time step, effectively guiding predicted states toward the data manifold informed by measurements. We evaluate the proposed method on challenging robotic state estimation tasks in simulation, demonstrating competitive performance compared to tuned end-to-end trained baselines. Importantly, our method offers the desirable composability of classical filtering algorithms, allowing prior information and external sensor models to be incorporated without retraining.

