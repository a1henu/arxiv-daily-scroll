---
layout: default
title: Ranking-aware Reinforcement Learning for Ordinal Ranking
---

# Ranking-aware Reinforcement Learning for Ordinal Ranking
**arXiv**：[2601.20585v1](https://arxiv.org/abs/2601.20585) · [PDF](https://arxiv.org/pdf/2601.20585.pdf)  
**作者**：Aiming Hao, Chen Zhu, Jiashu Zhu, Jiahong Wu, Xiangxiang Chu  

**一句话要点**：提出排名感知强化学习框架以解决序数回归与排序中的依赖建模问题

**关键词**：序数回归, 强化学习, 排名感知奖励, 策略优化, 基准测试

## 3 点简述
- 核心问题：传统方法难以建模序数依赖关系，影响回归与排序性能
- 方法要点：通过统一目标整合回归与排序，利用排名感知奖励进行策略优化
- 实验或效果：在三个基准测试中验证了框架的有效性，提升模型性能

## 摘要（原文）

> Ordinal regression and ranking are challenging due to inherent ordinal dependencies that conventional methods struggle to model. We propose Ranking-Aware Reinforcement Learning (RARL), a novel RL framework that explicitly learns these relationships. At its core, RARL features a unified objective that synergistically integrates regression and Learning-to-Rank (L2R), enabling mutual improvement between the two tasks. This is driven by a ranking-aware verifiable reward that jointly assesses regression precision and ranking accuracy, facilitating direct model updates via policy optimization. To further enhance training, we introduce Response Mutation Operations (RMO), which inject controlled noise to improve exploration and prevent stagnation at saddle points. The effectiveness of RARL is validated through extensive experiments on three distinct benchmarks.

