---
layout: default
title: LAGO: A Local-Global Optimization Framework Combining Trust Region Methods and Bayesian Optimization
---

# LAGO: A Local-Global Optimization Framework Combining Trust Region Methods and Bayesian Optimization
**arXiv**：[2603.02970v1](https://arxiv.org/abs/2603.02970) · [PDF](https://arxiv.org/pdf/2603.02970.pdf)  
**作者**：Eliott Van Dieren, Tommaso Vanzan, Fabio Nobile  

**一句话要点**：提出LAGO算法，结合贝叶斯优化与信赖域方法，实现全局探索与局部精化的高效优化。

**关键词**：贝叶斯优化, 信赖域方法, 全局优化, 局部精化, 梯度增强, 自适应竞争

## 3 点简述
- 核心问题：全局优化算法在局部收敛时可能牺牲全局探索，而局部优化算法缺乏全局搜索能力。
- 方法要点：通过自适应竞争机制，独立生成全局和局部候选点，基于预测改进选择评估点。
- 实验或效果：相比标准非线性局部优化算法，在平滑函数上实现更优全局探索，同时保持局部快速收敛。

## 摘要（原文）

> We introduce LAGO, a LocAl-Global Optimization algorithm that combines gradient-enhanced Bayesian Optimization (BO) with gradient-based trust region local refinement through an adaptive competition mechanism. At each iteration, global and local optimization strategies independently propose candidate points, and the next evaluation is selected based on predicted improvement. LAGO separates global exploration from local refinement at the proposal level: the BO acquisition function is optimized outside the active trust region, while local function and gradient evaluations are incorporated into the global gradient-enhanced Gaussian process only when they satisfy a lengthscale-based minimum-distance criterion, reducing the risk of numerical instability during the local exploitation. This enables efficient local refinement when reaching promising regions, without sacrificing a global search of the design space. As a result, the method achieves an improved exploration of the full design space compared to standard non-linear local optimization algorithms for smooth functions, while maintaining fast local convergence in regions of interest.

