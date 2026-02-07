---
layout: default
title: A Data Driven Structural Decomposition of Dynamic Games via Best Response Maps
---

# A Data Driven Structural Decomposition of Dynamic Games via Best Response Maps
**arXiv**：[2602.05324v1](https://arxiv.org/abs/2602.05324) · [PDF](https://arxiv.org/pdf/2602.05324.pdf)  
**作者**：Mahdis Rabbani, Navid Mojahed, Shima Nazari  

**一句话要点**：提出基于离线最佳响应映射的数据驱动结构分解方法，以解决动态博弈中纳什均衡计算复杂性问题。

**关键词**：动态博弈, 纳什均衡计算, 最佳响应映射, 结构分解, 数据驱动方法, 自动驾驶赛车

## 3 点简述
- 动态博弈中纳什均衡计算因耦合优化和数值条件差而复杂，现有方法或直接求解或牺牲均衡一致性。
- 通过离线编译最佳响应映射作为可行性约束，移除嵌套优化层和导数耦合，实现结构简化。
- 在标准条件下，精确映射对应局部纳什均衡；蒙特卡洛实验验证了在自动驾驶赛车场景中的效果。

## 摘要（原文）

> Dynamic games are powerful tools to model multi-agent decision-making, yet computing Nash (generalized Nash) equilibria remains a central challenge in such settings. Complexity arises from tightly coupled optimality conditions, nested optimization structures, and poor numerical conditioning. Existing game-theoretic solvers address these challenges by directly solving the joint game, typically requiring explicit modeling of all agents' objective functions and constraints, while learning-based approaches often decouple interaction through prediction or policy approximation, sacrificing equilibrium consistency. This paper introduces a conceptually novel formulation for dynamic games by restructuring the equilibrium computation. Rather than solving a fully coupled game or decoupling agents through prediction or policy approximation, a data-driven structural reduction of the game is proposed that removes nested optimization layers and derivative coupling by embedding an offline-compiled best-response map as a feasibility constraint. Under standard regularity conditions, when the best-response operator is exact, any converged solution of the reduced problem corresponds to a local open-loop Nash (GNE) equilibrium of the original game; with a learned surrogate, the solution is approximately equilibrium-consistent up to the best-response approximation error. The proposed formulation is supported by mathematical proofs, accompanying a large-scale Monte Carlo study in a two-player open-loop dynamic game motivated by the autonomous racing problem. Comparisons are made against state-of-the-art joint game solvers, and results are reported on solution quality, computational cost, and constraint satisfaction.

