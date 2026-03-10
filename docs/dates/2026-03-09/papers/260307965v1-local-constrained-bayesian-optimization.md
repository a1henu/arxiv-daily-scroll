---
layout: default
title: Local Constrained Bayesian Optimization
---

# Local Constrained Bayesian Optimization
**arXiv**：[2603.07965v1](https://arxiv.org/abs/2603.07965) · [PDF](https://arxiv.org/pdf/2603.07965.pdf)  
**作者**：Jing Jingzhe, Fan Zheyi, Szu Hui Ng, Qingpei Hu  

**一句话要点**：提出局部约束贝叶斯优化以解决高维约束优化问题

**关键词**：贝叶斯优化, 高维优化, 约束优化, 局部优化, 收敛分析

## 3 点简述
- 高维约束贝叶斯优化面临维度灾难挑战
- 利用约束惩罚代理模型的可微性，交替进行局部下降和不确定性探索
- 在高达100维的基准测试中优于现有方法

## 摘要（原文）

> Bayesian optimization (BO) for high-dimensional constrained problems remains a significant challenge due to the curse of dimensionality. We propose Local Constrained Bayesian Optimization (LCBO), a novel framework tailored for such settings. Unlike trust-region methods that are prone to premature shrinking when confronting tight or complex constraints, LCBO leverages the differentiable landscape of constraint-penalized surrogates to alternate between rapid local descent and uncertainty-driven exploration. Theoretically, we prove that LCBO achieves a convergence rate for the Karush-Kuhn-Tucker (KKT) residual that depends polynomially on the dimension $d$ for common kernels under mild assumptions, offering a rigorous alternative to global BO where regret bounds typically scale exponentially. Extensive evaluations on high-dimensional benchmarks (up to 100D) demonstrate that LCBO consistently outperforms state-of-the-art baselines.

