---
layout: default
title: Smooth, Sparse, and Stable: Finite-Time Exact Skeleton Recovery via Smoothed Proximal Gradients
---

# Smooth, Sparse, and Stable: Finite-Time Exact Skeleton Recovery via Smoothed Proximal Gradients
**arXiv**：[2601.18189v1](https://arxiv.org/abs/2601.18189) · [PDF](https://arxiv.org/pdf/2601.18189.pdf)  
**作者**：Rui Wu, Yongjun Li  

**一句话要点**：提出平滑近端梯度方法，在有限迭代内精确恢复因果图骨架

**关键词**：因果发现, 连续优化, 无环约束, 近端梯度, 有限时间收敛, 图结构恢复

## 3 点简述
- 现有连续优化方法仅保证渐近收敛，导致稠密权重矩阵需后处理阈值化
- 引入混合阶无环约束，通过平滑近端梯度优化，理论证明有限时间精确恢复图结构
- 实验验证算法达到最先进精度，支持有限时间识别理论

## 摘要（原文）

> Continuous optimization has significantly advanced causal discovery, yet existing methods (e.g., NOTEARS) generally guarantee only asymptotic convergence to a stationary point. This often yields dense weighted matrices that require arbitrary post-hoc thresholding to recover a DAG. This gap between continuous optimization and discrete graph structures remains a fundamental challenge. In this paper, we bridge this gap by proposing the Hybrid-Order Acyclicity Constraint (AHOC) and optimizing it via the Smoothed Proximal Gradient (SPG-AHOC). Leveraging the Manifold Identification Property of proximal algorithms, we provide a rigorous theoretical guarantee: the Finite-Time Oracle Property. We prove that under standard identifiability assumptions, SPG-AHOC recovers the exact DAG support (structure) in finite iterations, even when optimizing a smoothed approximation. This result eliminates structural ambiguity, as our algorithm returns graphs with exact zero entries without heuristic truncation. Empirically, SPG-AHOC achieves state-of-the-art accuracy and strongly corroborates the finite-time identification theory.

