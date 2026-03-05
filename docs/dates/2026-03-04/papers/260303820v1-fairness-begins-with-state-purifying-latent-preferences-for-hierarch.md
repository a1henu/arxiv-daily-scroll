---
layout: default
title: Fairness Begins with State: Purifying Latent Preferences for Hierarchical Reinforcement Learning in Interactive Recommendation
---

# Fairness Begins with State: Purifying Latent Preferences for Hierarchical Reinforcement Learning in Interactive Recommendation
**arXiv**：[2603.03820v1](https://arxiv.org/abs/2603.03820) · [PDF](https://arxiv.org/pdf/2603.03820.pdf)  
**作者**：Yun Lu, Xiaoyu Shi, Hong Xie, Xiangyu Zhao, Mingsheng Shang  

**一句话要点**：提出DSRM-HRL框架，通过状态净化与分层决策解决交互推荐中的公平性问题

**关键词**：交互推荐系统, 公平性学习, 状态表示学习, 分层强化学习, 扩散模型

## 3 点简述
- 核心问题：交互推荐中观测状态受噪声和偏差污染，导致公平性与准确性冲突
- 方法要点：使用扩散模型净化潜在偏好状态，结合分层强化学习分离公平与短期目标
- 实验或效果：在高保真模拟器上验证，有效平衡推荐效用与曝光公平性

## 摘要（原文）

> Interactive recommender systems (IRS) are increasingly optimized with Reinforcement Learning (RL) to capture the sequential nature of user-system dynamics. However, existing fairness-aware methods often suffer from a fundamental oversight: they assume the observed user state is a faithful representation of true preferences. In reality, implicit feedback is contaminated by popularity-driven noise and exposure bias, creating a distorted state that misleads the RL agent. We argue that the persistent conflict between accuracy and fairness is not merely a reward-shaping issue, but a state estimation failure. In this work, we propose \textbf{DSRM-HRL}, a framework that reformulates fairness-aware recommendation as a latent state purification problem followed by decoupled hierarchical decision-making. We introduce a Denoising State Representation Module (DSRM) based on diffusion models to recover the low-entropy latent preference manifold from high-entropy, noisy interaction histories. Built upon this purified state, a Hierarchical Reinforcement Learning (HRL) agent is employed to decouple conflicting objectives: a high-level policy regulates long-term fairness trajectories, while a low-level policy optimizes short-term engagement under these dynamic constraints. Extensive experiments on high-fidelity simulators (KuaiRec, KuaiRand) demonstrate that DSRM-HRL effectively breaks the "rich-get-richer" feedback loop, achieving a superior Pareto frontier between recommendation utility and exposure equity.

