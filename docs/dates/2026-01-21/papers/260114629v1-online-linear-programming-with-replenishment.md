---
layout: default
title: Online Linear Programming with Replenishment
---

# Online Linear Programming with Replenishment
**arXiv**：[2601.14629v1](https://arxiv.org/abs/2601.14629) · [PDF](https://arxiv.org/pdf/2601.14629.pdf)  
**作者**：Yuze Chen, Yuan Zhou, Baichuan Mo, Jie Ying, Yufei Ruan, Zhou Ye  

**一句话要点**：提出在线线性规划补货模型，针对资源逐步累积场景，实现不同分布下的最优遗憾界。

**关键词**：在线线性规划, 补货模型, 遗憾分析, 随机过程, 算法设计, 资源管理

## 3 点简述
- 研究在线线性规划中库存通过随机补货逐步累积的问题，消除初始库存假设。
- 针对有界、有限支撑和连续支撑分布，设计算法分别达到√T、log T和log² T遗憾界。
- 实验验证算法在补货设置中优于经典方法，提供近乎完整的遗憾界刻画。

## 摘要（原文）

> We study an online linear programming (OLP) model in which inventory is not provided upfront but instead arrives gradually through an exogenous stochastic replenishment process. This replenishment-based formulation captures operational settings, such as e-commerce fulfillment, perishable supply chains, and renewable-powered systems, where resources are accumulated gradually and initial inventories are small or zero. The introduction of dispersed, uncertain replenishment fundamentally alters the structure of classical OLPs, creating persistent stockout risk and eliminating advance knowledge of the total budget.
>   We develop new algorithms and regret analyses for three major distributional regimes studied in the OLP literature: bounded distributions, finite-support distributions, and continuous-support distributions with a non-degeneracy condition. For bounded distributions, we design an algorithm that achieves $\widetilde{\mathcal{O}}(\sqrt{T})$ regret. For finite-support distributions with a non-degenerate induced LP, we obtain $\mathcal{O}(\log T)$ regret, and we establish an $Ω(\sqrt{T})$ lower bound for degenerate instances, demonstrating a sharp separation from the classical setting where $\mathcal{O}(1)$ regret is achievable. For continuous-support, non-degenerate distributions, we develop a two-stage accumulate-then-convert algorithm that achieves $\mathcal{O}(\log^2 T)$ regret, comparable to the $\mathcal{O}(\log T)$ regret in classical OLPs. Together, these results provide a near-complete characterization of the optimal regret achievable in OLP with replenishment. Finally, we empirically evaluate our algorithms and demonstrate their advantages over natural adaptations of classical OLP methods in the replenishment setting.

