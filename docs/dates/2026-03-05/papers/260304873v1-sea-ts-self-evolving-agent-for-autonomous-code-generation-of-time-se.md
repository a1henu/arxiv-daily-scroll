---
layout: default
title: SEA-TS: Self-Evolving Agent for Autonomous Code Generation of Time Series Forecasting Algorithms
---

# SEA-TS: Self-Evolving Agent for Autonomous Code Generation of Time Series Forecasting Algorithms
**arXiv**：[2603.04873v1](https://arxiv.org/abs/2603.04873) · [PDF](https://arxiv.org/pdf/2603.04873.pdf)  
**作者**：Longkun Xu, Xiaochun Zhang, Qiantu Tuo, Rui Li  

**一句话要点**：提出SEA-TS框架以自主生成时间序列预测算法代码，解决数据稀缺和分布偏移问题。

**关键词**：时间序列预测, 自主代码生成, 自进化代理, 蒙特卡洛树搜索, 算法优化, 机器学习工程

## 3 点简述
- 核心问题：传统机器学习在时间序列预测中面临数据稀缺、分布偏移和手动迭代效率低的问题。
- 方法要点：引入MA-MCTS、代码审查与提示更新、全局可导推理，通过自进化循环生成和优化代码。
- 实验或效果：在Solar-Energy基准上MAE降低40%，在专有数据集上WAPE和MAPE优于基线方法，发现新颖架构模式。

## 摘要（原文）

> Accurate time series forecasting underpins decision-making across domains, yet conventional ML development suffers from data scarcity in new deployments, poor adaptability under distribution shift, and diminishing returns from manual iteration. We propose Self-Evolving Agent for Time Series Algorithms (SEA-TS), a framework that autonomously generates, validates, and optimizes forecasting code via an iterative self-evolution loop. Our framework introduces three key innovations: (1) Metric-Advantage Monte Carlo Tree Search (MA-MCTS), which replaces fixed rewards with a normalized advantage score for discriminative search guidance; (2) Code Review with running prompt refinement, where each executed solution undergoes automated review followed by prompt updates that encode corrective patterns, preventing recurrence of similar errors; and (3) Global Steerable Reasoning, which compares each node against global best and worst solutions, enabling cross-trajectory knowledge transfer. We adopt a MAP-Elites archive for architectural diversity. On the public Solar-Energy benchmark, SEA-TS generated code achieves a 40% MAE reduction relative to TimeMixer, surpassing state-of-the-art methods. On proprietary datasets, SEA-TS generated code reduces WAPE by 8.6% on solar PV forecasting and 7.7% on residential load forecasting compared to human-engineered baselines, and achieves 26.17% MAPE on load forecasting versus 29.34% by TimeMixer. Notably, the evolved models discover novel architectural patterns--including physics-informed monotonic decay heads encoding solar irradiance constraints, per-station learned diurnal cycle profiles, and learnable hourly bias correction--demonstrating that autonomous ML engineering can generate genuinely novel algorithmic ideas beyond manual design.

