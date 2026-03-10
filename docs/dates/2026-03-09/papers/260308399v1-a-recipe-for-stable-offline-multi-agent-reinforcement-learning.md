---
layout: default
title: A Recipe for Stable Offline Multi-agent Reinforcement Learning
---

# A Recipe for Stable Offline Multi-agent Reinforcement Learning
**arXiv**：[2603.08399v1](https://arxiv.org/abs/2603.08399) · [PDF](https://arxiv.org/pdf/2603.08399.pdf)  
**作者**：Dongsu Lee, Daehee Lee, Amy Zhang  

**一句话要点**：提出尺度不变值归一化以稳定离线多智能体强化学习中的非线性值分解

**关键词**：离线强化学习, 多智能体强化学习, 值分解, 稳定性优化, 演员-评论家训练

## 3 点简述
- 离线多智能体强化学习中非线性值分解导致值尺度放大和优化不稳定
- 引入尺度不变值归一化技术，稳定演员-评论家训练而不改变贝尔曼固定点
- 通过实验分析关键组件交互，提供实用配方以释放离线多智能体强化学习潜力

## 摘要（原文）

> Despite remarkable achievements in single-agent offline reinforcement learning (RL), multi-agent RL (MARL) has struggled to adopt this paradigm, largely persisting with on-policy training and self-play from scratch. One reason for this gap comes from the instability of non-linear value decomposition, leading prior works to avoid complex mixing networks in favor of linear value decomposition (e.g., VDN) with value regularization used in single-agent setups. In this work, we analyze the source of instability in non-linear value decomposition within the offline MARL setting. Our observations confirm that they induce value-scale amplification and unstable optimization. To alleviate this, we propose a simple technique, scale-invariant value normalization (SVN), that stabilizes actor-critic training without altering the Bellman fixed point. Empirically, we examine the interaction among key components of offline MARL (e.g., value decomposition, value learning, and policy extraction) and derive a practical recipe that unlocks its full potential.

