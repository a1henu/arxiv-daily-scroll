---
layout: default
title: Taming the Monster Every Context: Complexity Measure and Unified Framework for Offline-Oracle Efficient Contextual Bandits
---

# Taming the Monster Every Context: Complexity Measure and Unified Framework for Offline-Oracle Efficient Contextual Bandits
**arXiv**：[2602.09456v1](https://arxiv.org/abs/2602.09456) · [PDF](https://arxiv.org/pdf/2602.09456.pdf)  
**作者**：Hao Qin, Chicheng Zhang  

**一句话要点**：提出OE2D框架，将上下文赌博机学习简化为离线回归，实现大动作空间下的近优遗憾。

**关键词**：上下文赌博机, 离线回归, 复杂度度量, 遗憾分析, 动作空间优化

## 3 点简述
- 核心问题：上下文赌博机在大动作空间中，如何高效平衡探索与利用，降低遗憾。
- 方法要点：设计OE2D算法，采用“开发性F设计”动作分布，减少离线回归调用次数。
- 实验或效果：引入DOEC复杂度度量，连接离线与在线高效算法，理论分析显示遗憾可控。

## 摘要（原文）

> We propose an algorithmic framework, Offline Estimation to Decisions (OE2D), that reduces contextual bandit learning with general reward function approximation to offline regression. The framework allows near-optimal regret for contextual bandits with large action spaces with $O(log(T))$ calls to an offline regression oracle over $T$ rounds, and makes $O(loglog(T))$ calls when $T$ is known. The design of OE2D algorithm generalizes Falcon~\citep{simchi2022bypassing} and its linear reward version~\citep[][Section 4]{xu2020upper} in that it chooses an action distribution that we term ``exploitative F-design'' that simultaneously guarantees low regret and good coverage that trades off exploration and exploitation. Central to our regret analysis is a new complexity measure, the Decision-Offline Estimation Coefficient (DOEC), which we show is bounded in bounded Eluder dimension per-context and smoothed regret settings. We also establish a relationship between DOEC and Decision Estimation Coefficient (DEC)~\citep{foster2021statistical}, bridging the design principles of offline- and online-oracle efficient contextual bandit algorithms for the first time.

