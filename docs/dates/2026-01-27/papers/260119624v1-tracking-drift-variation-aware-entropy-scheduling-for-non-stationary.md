---
layout: default
title: Tracking Drift: Variation-Aware Entropy Scheduling for Non-Stationary Reinforcement Learning
---

# Tracking Drift: Variation-Aware Entropy Scheduling for Non-Stationary Reinforcement Learning
**arXiv**：[2601.19624v1](https://arxiv.org/abs/2601.19624) · [PDF](https://arxiv.org/pdf/2601.19624.pdf)  
**作者**：Tongxi Wang, Zhuoyang Xia, Xinran Chen, Shan Liu  

**一句话要点**：提出自适应熵调度方法以解决非平稳强化学习中的环境漂移问题

**关键词**：非平稳强化学习, 环境漂移, 熵调度, 自适应探索, 在线学习

## 3 点简述
- 核心问题：现有方法使用静态熵系数，导致稳定期过度探索、漂移后探索不足和恢复缓慢
- 方法要点：基于可观测漂移信号在线调整熵系数，实现快速跟踪与避免随机性的权衡
- 实验或效果：在多种算法、任务和漂移模式下显著减少性能下降并加速恢复

## 摘要（原文）

> Real-world reinforcement learning often faces environment drift, but most existing methods rely on static entropy coefficients/target entropy, causing over-exploration during stable periods and under-exploration after drift (thus slow recovery), and leaving unanswered the principled question of how exploration intensity should scale with drift magnitude. We prove that entropy scheduling under non-stationarity can be reduced to a one-dimensional, round-by-round trade-off, faster tracking of the optimal solution after drift vs. avoiding gratuitous randomness when the environment is stable, so exploration strength can be driven by measurable online drift signals. Building on this, we propose AES (Adaptive Entropy Scheduling), which adaptively adjusts the entropy coefficient/temperature online using observable drift proxies during training, requiring almost no structural changes and incurring minimal overhead. Across 4 algorithm variants, 12 tasks, and 4 drift modes, AES significantly reduces the fraction of performance degradation caused by drift and accelerates recovery after abrupt changes.

