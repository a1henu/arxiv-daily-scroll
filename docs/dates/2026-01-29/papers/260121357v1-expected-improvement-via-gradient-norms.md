---
layout: default
title: Expected Improvement via Gradient Norms
---

# Expected Improvement via Gradient Norms
**arXiv**：[2601.21357v1](https://arxiv.org/abs/2601.21357) · [PDF](https://arxiv.org/pdf/2601.21357.pdf)  
**作者**：Joshua Hang Sai Ip, Georgios Makrygiorgos, Ali Mesbah  

**一句话要点**：提出基于梯度范数的期望改进以增强贝叶斯优化的探索能力

**关键词**：贝叶斯优化, 期望改进, 梯度范数, 采集函数, 控制策略学习

## 3 点简述
- 核心问题：标准期望改进函数在贝叶斯优化中过于利用，易收敛至次优平稳点。
- 方法要点：通过梯度感知辅助目标应用改进原则，促进在高性能且接近一阶平稳区域采样。
- 实验或效果：在标准基准测试中表现优于基线，并适用于控制策略学习问题。

## 摘要（原文）

> Bayesian Optimization (BO) is a principled approach for optimizing expensive black-box functions, with Expected Improvement (EI) being one of the most widely used acquisition functions. Despite its empirical success, EI is known to be overly exploitative and can converge to suboptimal stationary points. We propose Expected Improvement via Gradient Norms (EI-GN), a novel acquisition function that applies the improvement principle to a gradient-aware auxiliary objective, thereby promoting sampling in regions that are both high-performing and approaching first-order stationarity. EI-GN relies on gradient observations used to learn gradient-enhanced surrogate models that enable principled gradient inference from function evaluations. We derive a tractable closed-form expression for EI-GN that allows efficient optimization and show that the proposed acquisition is consistent with the improvement-based acquisition framework. Empirical evaluations on standard BO benchmarks demonstrate that EI-GN yields consistent improvements against standard baselines. We further demonstrate applicability of EI-GN to control policy learning problems.

