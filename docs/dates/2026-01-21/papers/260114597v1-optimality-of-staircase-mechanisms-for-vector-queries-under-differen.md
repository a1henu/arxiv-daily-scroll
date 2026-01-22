---
layout: default
title: Optimality of Staircase Mechanisms for Vector Queries under Differential Privacy
---

# Optimality of Staircase Mechanisms for Vector Queries under Differential Privacy
**arXiv**：[2601.14597v1](https://arxiv.org/abs/2601.14597) · [PDF](https://arxiv.org/pdf/2601.14597.pdf)  
**作者**：James Melbourne, Mario Diaz, Shahab Asoodeh  

**一句话要点**：证明向量查询下差分隐私加性机制的最优性由阶梯机制实现

**关键词**：差分隐私, 加性机制, 阶梯机制, 最优设计, 凸重排理论, 向量查询

## 3 点简述
- 研究向量查询在ε-差分隐私下加性机制的最优设计问题
- 利用凸重排理论将无限维优化简化为径向对称分布的一维凸族
- 证明阶梯机制在所有加性机制中对于任意维度、范数和范数单调成本函数均最优

## 摘要（原文）

> We study the optimal design of additive mechanisms for vector-valued queries under $ε$-differential privacy (DP). Given only the sensitivity of a query and a norm-monotone cost function measuring utility loss, we ask which noise distribution minimizes expected cost among all additive $ε$-DP mechanisms. Using convex rearrangement theory, we show that this infinite-dimensional optimization problem admits a reduction to a one-dimensional compact and convex family of radially symmetric distributions whose extreme points are the staircase distributions. As a consequence, we prove that for any dimension, any norm, and any norm-monotone cost function, there exists an $ε$-DP staircase mechanism that is optimal among all additive mechanisms. This result resolves a conjecture of Geng, Kairouz, Oh, and Viswanath, and provides a geometric explanation for the emergence of staircase mechanisms as extremal solutions in differential privacy.

