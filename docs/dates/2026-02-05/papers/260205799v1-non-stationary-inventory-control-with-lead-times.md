---
layout: default
title: Non-Stationary Inventory Control with Lead Times
---

# Non-Stationary Inventory Control with Lead Times
**arXiv**：[2602.05799v1](https://arxiv.org/abs/2602.05799) · [PDF](https://arxiv.org/pdf/2602.05799.pdf)  
**作者**：Nele H. Amiri, Sean R. Sinclair, Maximiliano Udenio  

**一句话要点**：提出自适应在线算法以解决非平稳需求下库存控制问题，涵盖不同库存模型与提前期。

**关键词**：非平稳库存控制, 在线学习算法, 动态遗憾分析, 需求滞后, 销售损失模型, 提前期影响

## 3 点简述
- 研究非平稳需求分布未知且可能变化的单物品周期性库存控制问题。
- 提出基于基库存策略的自适应在线算法，并建立动态遗憾性能保证。
- 模拟结果显示算法显著优于现有基准，揭示不同库存模型间的性能差异。

## 摘要（原文）

> We study non-stationary single-item, periodic-review inventory control problems in which the demand distribution is unknown and may change over time. We analyze how demand non-stationarity affects learning performance across inventory models, including systems with demand backlogging or lost-sales, both with and without lead times. For each setting, we propose an adaptive online algorithm that optimizes over the class of base-stock policies and establish performance guarantees in terms of dynamic regret relative to the optimal base-stock policy at each time step. Our results reveal a sharp separation across inventory models. In backlogging systems and lost-sales models with zero lead time, we show that it is possible to adapt to demand changes without incurring additional performance loss in stationary environments, even without prior knowledge of the demand distributions or the number of demand shifts. In contrast, for lost-sales systems with positive lead times, we establish weaker guarantees that reflect fundamental limitations imposed by delayed replenishment in combination with censored feedback. Our algorithms leverage the convexity and one-sided feedback structure of inventory costs to enable counterfactual policy evaluation despite demand censoring. We complement the theoretical analysis with simulation results showing that our methods significantly outperform existing benchmarks.

