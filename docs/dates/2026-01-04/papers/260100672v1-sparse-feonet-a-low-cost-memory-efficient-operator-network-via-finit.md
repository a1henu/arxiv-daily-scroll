---
layout: default
title: Sparse FEONet: A Low-Cost, Memory-Efficient Operator Network via Finite-Element Local Sparsity for Parametric PDEs
---

# Sparse FEONet: A Low-Cost, Memory-Efficient Operator Network via Finite-Element Local Sparsity for Parametric PDEs
**arXiv**：[2601.00672v1](https://arxiv.org/abs/2601.00672) · [PDF](https://arxiv.org/pdf/2601.00672.pdf)  
**作者**：Seungchan Ko, Jiyeon Kim, Dongwook Shin  

**一句话要点**：提出稀疏有限元算子网络，通过有限元局部稀疏性降低计算成本与内存需求，用于参数偏微分方程求解。

**关键词**：有限元算子网络, 稀疏网络架构, 参数偏微分方程, 计算效率, 算子学习

## 3 点简述
- 原FEONet在大规模问题中计算成本高且精度可能下降，需改进扩展性。
- 新网络基于有限元结构设计稀疏架构，减少参数并保持近似能力。
- 实验显示稀疏网络显著提升计算效率，理论分析支持其有效性与稳定性。

## 摘要（原文）

> In this paper, we study the finite element operator network (FEONet), an operator-learning method for parametric problems, originally introduced in J. Y. Lee, S. Ko, and Y. Hong, Finite Element Operator Network for Solving Elliptic-Type Parametric PDEs, SIAM J. Sci. Comput., 47(2), C501-C528, 2025. FEONet realizes the parameter-to-solution map on a finite element space and admits a training procedure that does not require training data, while exhibiting high accuracy and robustness across a broad class of problems. However, its computational cost increases and accuracy may deteriorate as the number of elements grows, posing notable challenges for large-scale problems. In this paper, we propose a new sparse network architecture motivated by the structure of the finite elements to address this issue. Throughout extensive numerical experiments, we show that the proposed sparse network achieves substantial improvements in computational cost and efficiency while maintaining comparable accuracy. We also establish theoretical results demonstrating that the sparse architecture can approximate the target operator effectively and provide a stability analysis ensuring reliable training and prediction.

