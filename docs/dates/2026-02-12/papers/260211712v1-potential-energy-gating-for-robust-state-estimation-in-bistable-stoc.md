---
layout: default
title: Potential-energy gating for robust state estimation in bistable stochastic systems
---

# Potential-energy gating for robust state estimation in bistable stochastic systems
**arXiv**：[2602.11712v1](https://arxiv.org/abs/2602.11712) · [PDF](https://arxiv.org/pdf/2602.11712.pdf)  
**作者**：Luigi Simeone  

**一句话要点**：提出势能门控方法，用于双阱随机系统中的鲁棒状态估计。

**关键词**：状态估计, 鲁棒滤波, 双阱系统, 势能门控, 卡尔曼滤波器, 粒子滤波器

## 3 点简述
- 核心问题：双阱随机系统在观测噪声下状态估计不鲁棒，传统滤波器对所有状态区域处理相同。
- 方法要点：基于已知或假设势能函数调制观测噪声协方差，在势能最小值附近信任观测，接近势垒时逐步折扣。
- 实验或效果：在合成基准测试中，相比标准扩展卡尔曼滤波器，均方根误差改进57-80%，且对势能参数误设鲁棒。

## 摘要（原文）

> We introduce potential-energy gating, a method for robust state estimation in systems governed by double-well stochastic dynamics. The observation noise covariance of a Bayesian filter is modulated by the local value of a known or assumed potential energy function: observations are trusted when the state is near a potential minimum and progressively discounted as it approaches the barrier separating metastable wells. This physics-based mechanism differs from purely statistical robust filters, which treat all regions of state space identically, and from constrained filters, which impose hard bounds on states rather than modulating observation trust. We implement the gating within Extended, Unscented, Ensemble, and Adaptive Kalman filters and particle filters, requiring only two additional hyperparameters. Synthetic benchmarks on a Ginzburg-Landau double-well process with 10% outlier contamination and Monte Carlo validation over 100 replications show 57-80% RMSE improvement over the standard Extended Kalman Filter, all statistically significant (p < 10^{-15}, Wilcoxon signed-rank test). A naive topological baseline using only distance to the nearest well achieves 57%, confirming that the continuous energy landscape adds an additional ~21 percentage points. The method is robust to misspecification: even when assumed potential parameters deviate by 50% from their true values, improvement never falls below 47%. Comparing externally forced and spontaneous Kramers-type transitions, gating retains 68% improvement under noise-induced transitions whereas the naive baseline degrades to 30%. As an empirical illustration, we apply the framework to Dansgaard-Oeschger events in the NGRIP delta-18O ice-core record, estimating asymmetry parameter gamma = -0.109 (bootstrap 95% CI: [-0.220, -0.011], excluding zero) and demonstrating that outlier fraction explains 91% of the variance in filter improvement.

