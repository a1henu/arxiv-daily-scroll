---
layout: default
title: A Short and Unified Convergence Analysis of the SAG, SAGA, and IAG Algorithms
---

# A Short and Unified Convergence Analysis of the SAG, SAGA, and IAG Algorithms
**arXiv**：[2602.05304v1](https://arxiv.org/abs/2602.05304) · [PDF](https://arxiv.org/pdf/2602.05304.pdf)  
**作者**：Feng Zhu, Robert W. Heath, Aritra Mitra  

**一句话要点**：提出统一收敛分析框架，适用于SAG、SAGA和IAG算法，针对光滑强凸有限和优化问题。

**关键词**：随机方差缩减算法, 有限和优化, 收敛分析, Lyapunov函数, 强凸目标函数

## 3 点简述
- 现有SAG、SAGA和IAG算法分析分散且复杂，缺乏统一理论框架。
- 通过延迟边界和新Lyapunov函数设计，提供简短模块化收敛证明。
- 获得SAG和SAGA的高概率界，并改进IAG算法的最佳已知收敛率。

## 摘要（原文）

> Stochastic variance-reduced algorithms such as Stochastic Average Gradient (SAG) and SAGA, and their deterministic counterparts like the Incremental Aggregated Gradient (IAG) method, have been extensively studied in large-scale machine learning. Despite their popularity, existing analyses for these algorithms are disparate, relying on different proof techniques tailored to each method. Furthermore, the original proof of SAG is known to be notoriously involved, requiring computer-aided analysis. Focusing on finite-sum optimization with smooth and strongly convex objective functions, our main contribution is to develop a single unified convergence analysis that applies to all three algorithms: SAG, SAGA, and IAG. Our analysis features two key steps: (i) establishing a bound on delays due to stochastic sub-sampling using simple concentration tools, and (ii) carefully designing a novel Lyapunov function that accounts for such delays. The resulting proof is short and modular, providing the first high-probability bounds for SAG and SAGA that can be seamlessly extended to non-convex objectives and Markov sampling. As an immediate byproduct of our new analysis technique, we obtain the best known rates for the IAG algorithm, significantly improving upon prior bounds.

