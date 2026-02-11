---
layout: default
title: Effectiveness of Binary Autoencoders for QUBO-Based Optimization Problems
---

# Effectiveness of Binary Autoencoders for QUBO-Based Optimization Problems
**arXiv**：[2602.10037v1](https://arxiv.org/abs/2602.10037) · [PDF](https://arxiv.org/pdf/2602.10037.pdf)  
**作者**：Tetsuro Abe, Masashi Yamashita, Shu Tanaka  

**一句话要点**：提出二进制自编码器以提升基于QUBO的黑盒组合优化效率

**关键词**：黑盒组合优化, 二进制自编码器, QUBO优化, 旅行商问题, 潜在表示学习

## 3 点简述
- 核心问题：黑盒组合优化中，二进制编码选择不当导致搜索效率低和不可行解浪费评估预算。
- 方法要点：结合二进制自编码器学习紧凑二进制潜在码，以更好地对齐原始解空间与潜在汉明距离。
- 实验或效果：在小旅行商问题中，该方法提高近似比速度，保持可行性，并减少局部最优。

## 摘要（原文）

> In black-box combinatorial optimization, objective evaluations are often expensive, so high quality solutions must be found under a limited budget. Factorization machine with quantum annealing (FMQA) builds a quadratic surrogate model from evaluated samples and optimizes it on an Ising machine. However, FMQA requires binary decision variables, and for nonbinary structures such as integer permutations, the choice of binary encoding strongly affects search efficiency. If the encoding fails to reflect the original neighborhood structure, small Hamming moves may not correspond to meaningful modifications in the original solution space, and constrained problems can yield many infeasible candidates that waste evaluations. Recent work combines FMQA with a binary autoencoder (bAE) that learns a compact binary latent code from feasible solutions, yet the mechanism behind its performance gains is unclear. Using a small traveling salesman problem as an interpretable testbed, we show that the bAE reconstructs feasible tours accurately and, compared with manually designed encodings at similar compression, better aligns tour distances with latent Hamming distances, yields smoother neighborhoods under small bit flips, and produces fewer local optima. These geometric properties explain why bAE+FMQA improves the approximation ratio faster while maintaining feasibility throughout optimization, and they provide guidance for designing latent representations for black-box optimization.

