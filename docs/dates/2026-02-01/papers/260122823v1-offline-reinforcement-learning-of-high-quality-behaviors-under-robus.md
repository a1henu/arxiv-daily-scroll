---
layout: default
title: Offline Reinforcement Learning of High-Quality Behaviors Under Robust Style Alignment
---

# Offline Reinforcement Learning of High-Quality Behaviors Under Robust Style Alignment
**arXiv**：[2601.22823v1](https://arxiv.org/abs/2601.22823) · [PDF](https://arxiv.org/pdf/2601.22823.pdf)  
**作者**：Mathieu Petitbois, Rémy Portelas, Sylvain Lamprier  

**一句话要点**：提出SCIQL框架以解决离线强化学习中风格对齐与任务性能的冲突问题

**关键词**：离线强化学习, 风格对齐, 目标条件强化学习, 门控优势加权回归, 离线策略优化

## 3 点简述
- 核心问题：离线强化学习中风格对齐与任务性能因分布偏移和内在冲突而难以兼顾
- 方法要点：基于统一风格定义，结合目标条件RL技术和门控优势加权回归机制优化性能与风格
- 实验或效果：SCIQL在风格对齐和任务性能上优于现有离线方法，提供代码和数据集

## 摘要（原文）

> We study offline reinforcement learning of style-conditioned policies using explicit style supervision via subtrajectory labeling functions. In this setting, aligning style with high task performance is particularly challenging due to distribution shift and inherent conflicts between style and reward. Existing methods, despite introducing numerous definitions of style, often fail to reconcile these objectives effectively. To address these challenges, we propose a unified definition of behavior style and instantiate it into a practical framework. Building on this, we introduce Style-Conditioned Implicit Q-Learning (SCIQL), which leverages offline goal-conditioned RL techniques, such as hindsight relabeling and value learning, and combine it with a new Gated Advantage Weighted Regression mechanism to efficiently optimize task performance while preserving style alignment. Experiments demonstrate that SCIQL achieves superior performance on both objectives compared to prior offline methods. Code, datasets and visuals are available in: https://sciql-iclr-2026.github.io/.

