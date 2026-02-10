---
layout: default
title: Is Flow Matching Just Trajectory Replay for Sequential Data?
---

# Is Flow Matching Just Trajectory Replay for Sequential Data?
**arXiv**：[2602.08318v1](https://arxiv.org/abs/2602.08318) · [PDF](https://arxiv.org/pdf/2602.08318.pdf)  
**作者**：Soon Hoe Lim, Shizheng Lin, Michael W. Mahoney, N. Benjamin Erichson  

**一句话要点**：揭示流匹配在序列数据中本质为轨迹重放，并推导出最优速度场的闭式解

**关键词**：流匹配, 序列数据生成, 最优速度场, 轨迹重放, 非参数动力学系统, ODE采样

## 3 点简述
- 核心问题：流匹配是否学习通用动力学结构，还是仅进行轨迹重放
- 方法要点：在完美函数逼近极限下，推导出高斯条件路径对应的最优速度场闭式表达式
- 实验或效果：基于最优场结构改进采样方案，在非线性动力系统基准上实现无需训练的强概率预测

## 摘要（原文）

> Flow matching (FM) is increasingly used for time-series generation, but it is not well understood whether it learns a general dynamical structure or simply performs an effective "trajectory replay". We study this question by deriving the velocity field targeted by the empirical FM objective on sequential data, in the limit of perfect function approximation. For the Gaussian conditional paths commonly used in practice, we show that the implied sampler is an ODE whose dynamics constitutes a nonparametric, memory-augmented continuous-time dynamical system. The optimal field admits a closed-form expression as a similarity-weighted mixture of instantaneous velocities induced by past transitions, making the dataset dependence explicit and interpretable. This perspective positions neural FM models trained by stochastic optimization as parametric surrogates of an ideal nonparametric solution. Using the structure of the optimal field, we study sampling and approximation schemes that improve the efficiency and numerical robustness of ODE-based generation. On nonlinear dynamical system benchmarks, the resulting closed-form sampler yields strong probabilistic forecasts directly from historical transitions, without training.

