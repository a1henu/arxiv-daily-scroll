---
layout: default
title: Maximin Relative Improvement: Fair Learning as a Bargaining Problem
---

# Maximin Relative Improvement: Fair Learning as a Bargaining Problem
**arXiv**：[2602.04155v1](https://arxiv.org/abs/2602.04155) · [PDF](https://arxiv.org/pdf/2602.04155.pdf)  
**作者**：Jiwoo Han, Moulinath Banerjee, Yuekai Sun  

**一句话要点**：提出相对改进方法，将群体公平性建模为子群体间的讨价还价问题。

**关键词**：群体公平性, 讨价还价问题, 相对改进, Kalai-Smorodinsky解, 有限样本收敛

## 3 点简述
- 核心问题：在多个子群体上部署单一预测器时，如何公平分配预测性能提升。
- 方法要点：将公平性视为讨价还价问题，引入相对改进指标，对应Kalai-Smorodinsky解。
- 实验或效果：在温和条件下建立了有限样本收敛保证，提供公理合理性如尺度不变性。

## 摘要（原文）

> When deploying a single predictor across multiple subpopulations, we propose a fundamentally different approach: interpreting group fairness as a bargaining problem among subpopulations. This game-theoretic perspective reveals that existing robust optimization methods such as minimizing worst-group loss or regret correspond to classical bargaining solutions and embody different fairness principles. We propose relative improvement, the ratio of actual risk reduction to potential reduction from a baseline predictor, which recovers the Kalai-Smorodinsky solution. Unlike absolute-scale methods that may not be comparable when groups have different potential predictability, relative improvement provides axiomatic justification including scale invariance and individual monotonicity. We establish finite-sample convergence guarantees under mild conditions.

