---
layout: default
title: Sequential Service Region Design with Capacity-Constrained Investment and Spillover Effect
---

# Sequential Service Region Design with Capacity-Constrained Investment and Spillover Effect
**arXiv**：[2603.08188v1](https://arxiv.org/abs/2603.08188) · [PDF](https://arxiv.org/pdf/2603.08188.pdf)  
**作者**：Tingting Chen, Feng Chu, Jiantong Zhang  

**一句话要点**：提出基于Transformer近端策略优化的序列服务区域设计框架，以解决容量约束和溢出效应下的投资决策问题。

**关键词**：序列服务区域设计, 实物期权分析, Transformer近端策略优化, 容量约束投资, 随机溢出效应, 深度强化学习

## 3 点简述
- 研究序列服务区域设计问题，考虑每期投资区域数量限制和随机溢出效应，需在不确定性下优化投资序列。
- 集成实物期权分析和Transformer近端策略优化算法，评估投资序列的跨期期权价值并学习生成高价值序列的策略。
- 数值实验表明，该方法在收敛速度和期权价值上优于基准深度强化学习方法，案例研究验证了其鲁棒性和适应性优势。

## 摘要（原文）

> Service region design determines the geographic coverage of service networks, shaping long-term operational performance. Capital and operational constraints preclude simultaneous large-scale deployment, requiring expansion to proceed sequentially. The resulting challenge is to determine when and where to invest under demand uncertainty, balancing intertemporal trade-offs between early and delayed investment and accounting for network effects whereby each deployment reshapes future demand through inter-regional connectivity. This study addresses a sequential service region design (SSRD) problem incorporating two practical yet underexplored factors: a $k$-region constraint that limits the number of regions investable per period and a stochastic spillover effect linking investment decisions to demand evolution. The resulting problem requires sequencing regional portfolios under uncertainty, leading to a combinatorial explosion in feasible investment sequences. To address this challenge, we propose a solution framework that integrates real options analysis (ROA) with a Transformer-based Proximal Policy Optimization (TPPO) algorithm. ROA evaluates the intertemporal option value of investment sequences, while TPPO learns sequential policies that directly generate high option-value sequences without exhaustive enumeration. Numerical experiments on realistic multi-region settings demonstrate that TPPO converges faster than benchmark DRL methods and consistently identifies sequences with superior option value. Case studies and sensitivity analyses further confirm robustness and provide insights on investment concurrency, regional prioritization, and the increasing benefits of adaptive expansion via our approach under stronger spillovers and dynamic market conditions.

