---
layout: default
title: One Operator to Rule Them All? On Boundary-Indexed Operator Families in Neural PDE Solvers
---

# One Operator to Rule Them All? On Boundary-Indexed Operator Families in Neural PDE Solvers
**arXiv**：[2603.01406v1](https://arxiv.org/abs/2603.01406) · [PDF](https://arxiv.org/pdf/2603.01406.pdf)  
**作者**：Lennon J. Shikhman  

**一句话要点**：揭示神经PDE求解器在边界条件变化时学习边界索引算子族而非单一算子

**关键词**：神经PDE求解器, 算子学习, 边界条件, 泛化分析, 泊松方程, 条件风险最小化

## 3 点简述
- 核心问题：标准神经算子训练隐含学习边界索引算子族，而非边界无关算子，导致泛化受限
- 方法要点：形式化算子学习为边界条件上的条件风险最小化，得出训练边界分布外不可识别性
- 实验或效果：泊松方程实验显示边界条件偏移下性能急剧下降，移除边界信息时收敛到条件期望

## 摘要（原文）

> Neural PDE solvers are often described as learning solution operators that map problem data to PDE solutions. In this work, we argue that this interpretation is generally incorrect when boundary conditions vary. We show that standard neural operator training implicitly learns a boundary-indexed family of operators, rather than a single boundary-agnostic operator, with the learned mapping fundamentally conditioned on the boundary-condition distribution seen during training. We formalize this perspective by framing operator learning as conditional risk minimization over boundary conditions, which leads to a non-identifiability result outside the support of the training boundary distribution. As a consequence, generalization in forcing terms or resolution does not imply generalization across boundary conditions. We support our theoretical analysis with controlled experiments on the Poisson equation, demonstrating sharp degradation under boundary-condition shifts, cross-distribution failures between distinct boundary ensembles, and convergence to conditional expectations when boundary information is removed. Our results clarify a core limitation of current neural PDE solvers and highlight the need for explicit boundary-aware modeling in the pursuit of foundation models for PDEs.

