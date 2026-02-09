---
layout: default
title: Optimal Abstractions for Verifying Properties of Kolmogorov-Arnold Networks (KANs)
---

# Optimal Abstractions for Verifying Properties of Kolmogorov-Arnold Networks (KANs)
**arXiv**：[2602.06737v1](https://arxiv.org/abs/2602.06737) · [PDF](https://arxiv.org/pdf/2602.06737.pdf)  
**作者**：Noah Schwartz, Chandra Kanth Nagesh, Sriram Sankaranarayanan, Ramneet Kaur, Tuhin Sahai, Susmit Jha  

**一句话要点**：提出基于动态规划和背包优化的最优抽象框架，以验证Kolmogorov-Arnold网络（KANs）的属性。

**关键词**：Kolmogorov-Arnold网络验证, 分段仿射近似, 混合整数线性规划, 动态规划优化, 误差界限保证, 神经网络属性验证

## 3 点简述
- 核心问题：验证KANs属性时，分段仿射（PWA）近似中分段数量需平衡计算可处理性与误差界限。
- 方法要点：结合单元级动态规划和网络级背包优化，最小化分段数同时保证误差界限，生成最优抽象。
- 实验或效果：在多个KAN基准测试中，前期分析成本被优越的验证结果所证明。

## 摘要（原文）

> We present a novel approach for verifying properties of Kolmogorov-Arnold Networks (KANs), a class of neural networks characterized by nonlinear, univariate activation functions typically implemented as piecewise polynomial splines or Gaussian processes. Our method creates mathematical ``abstractions'' by replacing each KAN unit with a piecewise affine (PWA) function, providing both local and global error estimates between the original network and its approximation. These abstractions enable property verification by encoding the problem as a Mixed Integer Linear Program (MILP), determining whether outputs satisfy specified properties when inputs belong to a given set. A critical challenge lies in balancing the number of pieces in the PWA approximation: too many pieces add binary variables that make verification computationally intractable, while too few pieces create excessive error margins that yield uninformative bounds. Our key contribution is a systematic framework that exploits KAN structure to find optimal abstractions. By combining dynamic programming at the unit level with a knapsack optimization across the network, we minimize the total number of pieces while guaranteeing specified error bounds. This approach determines the optimal approximation strategy for each unit while maintaining overall accuracy requirements. Empirical evaluation across multiple KAN benchmarks demonstrates that the upfront analysis costs of our method are justified by superior verification results.

