---
layout: default
title: RAmmStein: Regime Adaptation in Mean-reverting Markets with Stein Thresholds -- Optimal Impulse Control in Concentrated AMMs
---

# RAmmStein: Regime Adaptation in Mean-reverting Markets with Stein Thresholds -- Optimal Impulse Control in Concentrated AMMs
**arXiv**：[2602.19419v1](https://arxiv.org/abs/2602.19419) · [PDF](https://arxiv.org/pdf/2602.19419.pdf)  
**作者**：Pranay Anchuri  

**一句话要点**：提出RAmmStein方法以解决去中心化交易所中集中流动性管理的脉冲控制问题

**关键词**：去中心化交易所, 集中流动性, 脉冲控制, 深度强化学习, 均值回归, 最优控制

## 3 点简述
- 核心问题：流动性提供者在最大化费用收益与最小化再平衡成本间存在权衡，现有方法未充分考虑市场动态
- 方法要点：将流动性管理建模为最优控制问题，基于HJB-QVI推导，采用深度强化学习并输入均值回归速度等特征
- 实验或效果：使用高频交易数据评估，RAmmStein实现0.72%净投资回报率，减少67%再平衡频率并保持88%活跃时间

## 摘要（原文）

> Concentrated liquidity provision in decentralized exchanges presents a fundamental Impulse Control problem. Liquidity Providers (LPs) face a non-trivial trade-off between maximizing fee accrual through tight price-range concentration and minimizing the friction costs of rebalancing, including gas fees and swap slippage. Existing methods typically employ heuristic or threshold strategies that fail to account for market dynamics. This paper formulates liquidity management as an optimal control problem and derives the corresponding Hamilton-Jacobi-Bellman quasi-variational inequality (HJB-QVI). We present an approximate solution RAmmStein, a Deep Reinforcement Learning method that incorporates the mean-reversion speed (theta) of an Ornstein-Uhlenbeck process among other features as input to the model. We demonstrate that the agent learns to separate the state space into regions of action and inaction. We evaluate the framework using high-frequency 1Hz Coinbase trade data comprising over 6.8M trades. Experimental results show that RAmmStein achieves a superior net ROI of 0.72% compared to both passive and aggressive strategies. Notably, the agent reduces rebalancing frequency by 67% compared to a greedy rebalancing strategy while maintaining 88% active time. Our results demonstrate that regime-aware laziness can significantly improve capital efficiency by preserving the returns that would otherwise be eroded by the operational costs.

