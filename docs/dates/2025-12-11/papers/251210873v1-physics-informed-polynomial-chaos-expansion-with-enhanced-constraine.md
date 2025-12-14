---
layout: default
title: Physics-informed Polynomial Chaos Expansion with Enhanced Constrained Optimization Solver and D-optimal Sampling
---

# Physics-informed Polynomial Chaos Expansion with Enhanced Constrained Optimization Solver and D-optimal Sampling
**arXiv**：[2512.10873v1](https://arxiv.org/abs/2512.10873) · [PDF](https://arxiv.org/pdf/2512.10873.pdf)  
**作者**：Qitian Lu, Himanshu Sharma, Michael D. Shields, Lukáš Novák  

**一句话要点**：提出SULM优化求解器与D-最优采样以增强物理信息多项式混沌展开在高维不确定性量化中的性能

**关键词**：物理信息多项式混沌展开, 约束优化求解器, D-最优采样, 不确定性量化, 高维参数空间, 虚拟点选择

## 3 点简述
- PC²框架在高维参数空间或数据不足时性能下降，需改进求解效率与数据代表性
- 采用SULM求解器降低计算成本，结合D-最优采样选择虚拟点以平衡精度与效率
- 通过微分方程数值实验验证增强PC²在综合能力上优于标准PC²，适用于高维任务

## 摘要（原文）

> Physics-informed polynomial chaos expansions (PC$^2$) provide an efficient physically constrained surrogate modeling framework by embedding governing equations and other physical constraints into the standard data-driven polynomial chaos expansions (PCE) and solving via the Karush-Kuhn-Tucker (KKT) conditions. This approach improves the physical interpretability of surrogate models while achieving high computational efficiency and accuracy. However, the performance and efficiency of PC$^2$ can still be degraded with high-dimensional parameter spaces, limited data availability, or unrepresentative training data. To address this problem, this study explores two complementary enhancements to the PC$^2$ framework. First, a numerically efficient constrained optimization solver, straightforward updating of Lagrange multipliers (SULM), is adopted as an alternative to the conventional KKT solver. The SULM method significantly reduces computational cost when solving physically constrained problems with high-dimensionality and derivative boundary conditions that require a large number of virtual points. Second, a D-optimal sampling strategy is utilized to select informative virtual points to improve the stability and achieve the balance of accuracy and efficiency of the PC$^2$. The proposed methods are integrated into the PC$^2$ framework and evaluated through numerical examples of representative physical systems governed by ordinary or partial differential equations. The results demonstrate that the enhanced PC$^2$ has better comprehensive capability than standard PC$^2$, and is well-suited for high-dimensional uncertainty quantification tasks.

