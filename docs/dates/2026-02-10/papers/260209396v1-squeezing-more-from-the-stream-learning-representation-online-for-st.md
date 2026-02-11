---
layout: default
title: Squeezing More from the Stream : Learning Representation Online for Streaming Reinforcement Learning
---

# Squeezing More from the Stream : Learning Representation Online for Streaming Reinforcement Learning
**arXiv**：[2602.09396v1](https://arxiv.org/abs/2602.09396) · [PDF](https://arxiv.org/pdf/2602.09396.pdf)  
**作者**：Nilaksh, Antoine Clavaud, Mathieu Reymond, François Rivest, Sarath Chandar  

**一句话要点**：提出在线自预测表示方法以解决流式强化学习中的样本效率低下问题

**关键词**：流式强化学习, 自预测表示, 样本效率, 梯度冲突, 在线学习, 表示学习

## 3 点简述
- 核心问题：流式强化学习中单次更新后丢弃样本导致样本效率低下，仅依赖价值损失难以从瞬态数据学习有效表示
- 方法要点：扩展自预测表示至流式管道，引入正交梯度更新以缓解相关样本导致的训练不稳定
- 实验或效果：在Atari等基准上超越现有流式基线，潜在空间分析证实学习到更丰富的表示，弥补无回放缓冲区的性能差距

## 摘要（原文）

> In streaming Reinforcement Learning (RL), transitions are observed and discarded immediately after a single update. While this minimizes resource usage for on-device applications, it makes agents notoriously sample-inefficient, since value-based losses alone struggle to extract meaningful representations from transient data. We propose extending Self-Predictive Representations (SPR) to the streaming pipeline to maximize the utility of every observed frame. However, due to the highly correlated samples induced by the streaming regime, naively applying this auxiliary loss results in training instabilities. Thus, we introduce orthogonal gradient updates relative to the momentum target and resolve gradient conflicts arising from streaming-specific optimizers. Validated across the Atari, MinAtar, and Octax suites, our approach systematically outperforms existing streaming baselines. Latent-space analysis, including t-SNE visualizations and effective-rank measurements, confirms that our method learns significantly richer representations, bridging the performance gap caused by the absence of a replay buffer, while remaining efficient enough to train on just a few CPU cores.

