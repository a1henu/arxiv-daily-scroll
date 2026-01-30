---
layout: default
title: The Surprising Difficulty of Search in Model-Based Reinforcement Learning
---

# The Surprising Difficulty of Search in Model-Based Reinforcement Learning
**arXiv**：[2601.21306v1](https://arxiv.org/abs/2601.21306) · [PDF](https://arxiv.org/pdf/2601.21306.pdf)  
**作者**：Wei-Di Chang, Mikael Henaff, Brandon Amos, Gregory Dudek, Scott Fujimoto  

**一句话要点**：揭示模型强化学习中搜索的意外困难，强调缓解分布偏移的重要性

**关键词**：模型强化学习, 搜索算法, 分布偏移, 强化学习基准, 性能优化

## 3 点简述
- 挑战传统观点，指出搜索并非学习策略的即插即用替代品
- 发现即使模型高度准确，搜索也可能损害性能，而非仅由长期预测和误差累积导致
- 提出缓解分布偏移是关键，并识别有效搜索技术，在多个基准领域实现先进性能

## 摘要（原文）

> This paper investigates search in model-based reinforcement learning (RL). Conventional wisdom holds that long-term predictions and compounding errors are the primary obstacles for model-based RL. We challenge this view, showing that search is not a plug-and-play replacement for a learned policy. Surprisingly, we find that search can harm performance even when the model is highly accurate. Instead, we show that mitigating distribution shift matters more than improving model or value function accuracy. Building on this insight, we identify key techniques for enabling effective search, achieving state-of-the-art performance across multiple popular benchmark domains.

