---
layout: default
title: Efficient Incremental SLAM via Information-Guided and Selective Optimization
---

# Efficient Incremental SLAM via Information-Guided and Selective Optimization
**arXiv**：[2601.08110v1](https://arxiv.org/abs/2601.08110) · [PDF](https://arxiv.org/pdf/2601.08110.pdf)  
**作者**：Reza Arablouei  

**一句话要点**：提出信息引导门控与选择性优化以提升增量SLAM效率，在动态数据丰富环境中实现实时操作。

**关键词**：增量SLAM, 信息引导门控, 选择性优化, 实时操作, 计算效率

## 3 点简述
- 核心问题：增量SLAM后端计算成本高，需在保持全局一致性的同时减少不必要的优化。
- 方法要点：结合信息引导门控（IGG）和选择性部分优化（SPO），基于信息增益触发全局优化并动态聚焦计算。
- 实验或效果：在基准数据集上匹配批量求解器精度，相比传统增量方法显著节省计算资源。

## 摘要（原文）

> We present an efficient incremental SLAM back-end that achieves the accuracy of full batch optimization while substantially reducing computational cost. The proposed approach combines two complementary ideas: information-guided gating (IGG) and selective partial optimization (SPO). IGG employs an information-theoretic criterion based on the log-determinant of the information matrix to quantify the contribution of new measurements, triggering global optimization only when a significant information gain is observed. This avoids unnecessary relinearization and factorization when incoming data provide little additional information. SPO executes multi-iteration Gauss-Newton (GN) updates but restricts each iteration to the subset of variables most affected by the new measurements, dynamically refining this active set until convergence. Together, these mechanisms retain all measurements to preserve global consistency while focusing computation on parts of the graph where it yields the greatest benefit. We provide theoretical analysis showing that the proposed approach maintains the convergence guarantees of full GN. Extensive experiments on benchmark SLAM datasets show that our approach consistently matches the estimation accuracy of batch solvers, while achieving significant computational savings compared to conventional incremental approaches. The results indicate that the proposed approach offers a principled balance between accuracy and efficiency, making it a robust and scalable solution for real-time operation in dynamic data-rich environments.

