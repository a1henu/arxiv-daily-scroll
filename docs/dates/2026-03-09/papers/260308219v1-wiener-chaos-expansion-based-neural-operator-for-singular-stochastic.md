---
layout: default
title: Wiener Chaos Expansion based Neural Operator for Singular Stochastic Partial Differential Equations
---

# Wiener Chaos Expansion based Neural Operator for Singular Stochastic Partial Differential Equations
**arXiv**：[2603.08219v1](https://arxiv.org/abs/2603.08219) · [PDF](https://arxiv.org/pdf/2603.08219.pdf)  
**作者**：Dai Shi, Luke Thompson, Andi Han, Peiyan Hu, Junbin Gao, José Miguel Hernández-Lobato  

**一句话要点**：提出基于Wiener混沌展开与特征线性调制的神经算子，用于求解奇异随机偏微分方程。

**关键词**：奇异随机偏微分方程, Wiener混沌展开, 神经算子, 特征线性调制, 统计量子场论

## 3 点简述
- 核心问题：求解奇异随机偏微分方程，如动态Φ^4_2模型，传统方法依赖重整化因子。
- 方法要点：结合Wiener混沌展开与特征线性调制，捕捉解与平滑余项的依赖关系。
- 实验效果：在Φ^4_2上表现优异，无需重整化因子，并探索了Φ^4_3的模拟潜力。

## 摘要（原文）

> In this paper, we explore how our recently developed Wiener Chaos Expansion (WCE)-based neural operator (NO) can be applied to singular stochastic partial differential equations, e.g., the dynamic $\boldsymbolΦ^4_2$ model simulated in the recent works. Unlike the previous WCE-NO which solves SPDEs by simply inserting Wick-Hermite features into the backbone NO model, we leverage feature-wise linear modulation (FiLM) to appropriately capture the dependency between the solution of singular SPDE and its smooth remainder. The resulting WCE-FiLM-NO shows excellent performance on $\boldsymbolΦ^4_2$, as measured by relative $L_2$ loss, out-of-distribution $L_2$ loss, and autocorrelation score; all without the help of renormalisation factor. In addition, we also show the potential of simulating $\boldsymbolΦ^4_3$ data, which is more aligned with real scientific practice in statistical quantum field theory. To the best of our knowledge, this is among the first works to develop an efficient data-driven surrogate for the dynamical $\boldsymbolΦ^4_3$ model.

