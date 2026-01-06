---
layout: default
title: Reinforcement Learning for Option Hedging: Static Implied-Volatility Fit versus Shortfall-Aware Performance
---

# Reinforcement Learning for Option Hedging: Static Implied-Volatility Fit versus Shortfall-Aware Performance
**arXiv**：[2601.01709v1](https://arxiv.org/abs/2601.01709) · [PDF](https://arxiv.org/pdf/2601.01709.pdf)  
**作者**：Ziheng Chen, Minxuan Hu, Jiayu Yi, Wenxi Sun  

**一句话要点**：提出风险厌恶与交易成本下的强化学习期权定价方法，提升动态对冲性能。

**关键词**：强化学习, 期权定价, 风险厌恶, 动态对冲, 市场摩擦

## 3 点简述
- 核心问题：期权定价模型在静态拟合与动态对冲性能间的权衡。
- 方法要点：扩展QLBS框架并引入RLOP方法，结合风险厌恶与市场摩擦。
- 实验或效果：基于SPY和XOP数据，Adaptive-QLBS静态精度高，RLOP动态对冲优。

## 摘要（原文）

> We extend the Q-learner in Black-Scholes (QLBS) framework by incorporating risk aversion and trading costs, and propose a novel Replication Learning of Option Pricing (RLOP) approach. Both methods are fully compatible with standard reinforcement learning algorithms and operate under market frictions. Using SPY and XOP option data, we evaluate performance along static and dynamic dimensions. Adaptive-QLBS achieves higher static pricing accuracy in implied volatility space, while RLOP delivers superior dynamic hedging performance by reducing shortfall probability. These results highlight the importance of evaluating option pricing models beyond static fit, emphasizing realized hedging outcomes.

