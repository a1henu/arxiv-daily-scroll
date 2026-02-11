---
layout: default
title: Optimistic World Models: Efficient Exploration in Model-Based Deep Reinforcement Learning
---

# Optimistic World Models: Efficient Exploration in Model-Based Deep Reinforcement Learning
**arXiv**：[2602.10044v1](https://arxiv.org/abs/2602.10044) · [PDF](https://arxiv.org/pdf/2602.10044.pdf)  
**作者**：Akshay Mete, Shahid Aamir Sheikh, Tzu-Hsiang Lin, Dileep Kalathil, P. R. Kumar  

**一句话要点**：提出乐观世界模型以解决稀疏奖励环境中的高效探索问题

**关键词**：强化学习, 世界模型, 高效探索, 稀疏奖励, 模型学习, 梯度优化

## 3 点简述
- 核心问题：强化学习在稀疏奖励环境中探索效率低，是主要挑战
- 方法要点：基于奖励偏置最大似然估计，通过乐观动态损失直接偏置模型学习，无需不确定性估计
- 实验或效果：在DreamerV3和STORM架构中实现，样本效率和累积回报显著提升

## 摘要（原文）

> Efficient exploration remains a central challenge in reinforcement learning (RL), particularly in sparse-reward environments. We introduce Optimistic World Models (OWMs), a principled and scalable framework for optimistic exploration that brings classical reward-biased maximum likelihood estimation (RBMLE) from adaptive control into deep RL. In contrast to upper confidence bound (UCB)-style exploration methods, OWMs incorporate optimism directly into model learning by augmentation with an optimistic dynamics loss that biases imagined transitions toward higher-reward outcomes. This fully gradient-based loss requires neither uncertainty estimates nor constrained optimization. Our approach is plug-and-play with existing world model frameworks, preserving scalability while requiring only minimal modifications to standard training procedures. We instantiate OWMs within two state-of-the-art world model architectures, leading to Optimistic DreamerV3 and Optimistic STORM, which demonstrate significant improvements in sample efficiency and cumulative return compared to their baseline counterparts.

