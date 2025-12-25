---
layout: default
title: BALLAST: Bandit-Assisted Learning for Latency-Aware Stable Timeouts in Raft
---

# BALLAST: Bandit-Assisted Learning for Latency-Aware Stable Timeouts in Raft
**arXiv**：[2512.21165v1](https://arxiv.org/abs/2512.21165) · [PDF](https://arxiv.org/pdf/2512.21165.pdf)  
**作者**：Qizhi Wang  

**一句话要点**：提出BALLAST，利用上下文赌博机优化Raft选举超时，以应对长尾延迟和分区恢复场景。

**关键词**：Raft共识算法, 选举超时优化, 上下文赌博机, 长尾延迟, 分区恢复, 在线学习

## 3 点简述
- 核心问题：Raft随机选举超时在长尾延迟、抖动和分区恢复下易导致分裂投票，增加不可用性。
- 方法要点：采用轻量级在线自适应机制，基于线性上下文赌博机（LinUCB变体）从离散超时选项中选择，并加入安全探索以限制风险。
- 实验或效果：在模拟长尾延迟、损失、突发相关性和节点异质性的环境中，BALLAST显著减少恢复时间和不可写时间，优于标准随机超时和常见启发式方法。

## 摘要（原文）

> Randomized election timeouts are a simple and effective liveness heuristic for Raft, but they become brittle under long-tail latency, jitter, and partition recovery, where repeated split votes can inflate unavailability. This paper presents BALLAST, a lightweight online adaptation mechanism that replaces static timeout heuristics with contextual bandits. BALLAST selects from a discrete set of timeout "arms" using efficient linear contextual bandits (LinUCB variants), and augments learning with safe exploration to cap risk during unstable periods. We evaluate BALLAST on a reproducible discrete-event simulation with long-tail delay, loss, correlated bursts, node heterogeneity, and partition/recovery turbulence. Across challenging WAN regimes, BALLAST substantially reduces recovery time and unwritable time compared to standard randomized timeouts and common heuristics, while remaining competitive on stable LAN/WAN settings.

