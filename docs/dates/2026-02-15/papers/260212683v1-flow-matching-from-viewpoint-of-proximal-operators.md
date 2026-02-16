---
layout: default
title: Flow Matching from Viewpoint of Proximal Operators
---

# Flow Matching from Viewpoint of Proximal Operators
**arXiv**：[2602.12683v1](https://arxiv.org/abs/2602.12683) · [PDF](https://arxiv.org/pdf/2602.12683.pdf)  
**作者**：Kenji Fukumizu, Wei Huang, Han Bao, Shuntuo Xu, Nisha Chandramoothy  

**一句话要点**：从近端算子视角重新表述最优传输条件流匹配，证明其具有精确近端形式，并分析流形目标下的动力学性质。

**关键词**：最优传输, 条件流匹配, 近端算子, Brenier势, 流形学习, 动力学系统

## 3 点简述
- 核心问题：最优传输条件流匹配（OT-CFM）的数学基础，特别是目标分布无密度假设下的精确表述。
- 方法要点：通过扩展Brenier势，将OT-CFM重新表述为近端算子，提供向量场的显式近端表达式。
- 实验或效果：证明对于流形支持的目标，OT-CFM在时间重标度后具有终端法向双曲性，法向指数收缩而切向中性。

## 摘要（原文）

> We reformulate Optimal Transport Conditional Flow Matching (OT-CFM), a class of dynamical generative models, showing that it admits an exact proximal formulation via an extended Brenier potential, without assuming that the target distribution has a density. In particular, the mapping to recover the target point is exactly given by a proximal operator, which yields an explicit proximal expression of the vector field. We also discuss the convergence of minibatch OT-CFM to the population formulation as the batch size increases. Finally, using second epi-derivatives of convex potentials, we prove that, for manifold-supported targets, OT-CFM is terminally normally hyperbolic: after time rescaling, the dynamics contracts exponentially in directions normal to the data manifold while remaining neutral along tangential directions.

