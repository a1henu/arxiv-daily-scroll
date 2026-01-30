---
layout: default
title: A block-coordinate descent framework for non-convex composite optimization. Application to sparse precision matrix estimation
---

# A block-coordinate descent framework for non-convex composite optimization. Application to sparse precision matrix estimation
**arXiv**：[2601.21467v1](https://arxiv.org/abs/2601.21467) · [PDF](https://arxiv.org/pdf/2601.21467.pdf)  
**作者**：Guillaume Lauga  

**一句话要点**：提出块坐标下降框架以解决非凸复合优化问题，应用于稀疏精度矩阵估计

**关键词**：块坐标下降, 非凸优化, 复合优化, 稀疏精度矩阵估计, 图形套索

## 3 点简述
- 核心问题：非凸复合优化在块坐标下降中的理论分析不足，影响大规模应用。
- 方法要点：新框架支持变量度量近端梯度、近端牛顿和交替最小化更新，确保目标函数下降和收敛。
- 实验或效果：在稀疏精度矩阵估计中，迭代次数减少高达100倍，达到先进估计质量。

## 摘要（原文）

> Block-coordinate descent (BCD) is the method of choice to solve numerous large scale optimization problems, however their theoretical study for non-convex optimization, has received less attention. In this paper, we present a new block-coordinate descent (BCD) framework to tackle non-convex composite optimization problems, ensuring decrease of the objective function and convergence to a solution. This framework is general enough to include variable metric proximal gradient updates, proximal Newton updates, and alternated minimization updates. This generality allows to encompass three versions of the most used solvers in the sparse precision matrix estimation problem, deemed Graphical Lasso: graphical ISTA, Primal GLasso, and QUIC. We demonstrate the value of this new framework on non-convex sparse precision matrix estimation problems, providing convergence guarantees and up to a $100$-fold reduction in the number of iterations required to reach state-of-the-art estimation quality.

