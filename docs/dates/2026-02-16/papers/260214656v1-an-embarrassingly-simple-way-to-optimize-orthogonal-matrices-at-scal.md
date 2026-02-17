---
layout: default
title: An Embarrassingly Simple Way to Optimize Orthogonal Matrices at Scale
---

# An Embarrassingly Simple Way to Optimize Orthogonal Matrices at Scale
**arXiv**：[2602.14656v1](https://arxiv.org/abs/2602.14656) · [PDF](https://arxiv.org/pdf/2602.14656.pdf)  
**作者**：Adrián Javaloy, Antonio Vergari  

**一句话要点**：提出POGO算法以高效优化大规模正交矩阵，确保约束满足并兼容自适应优化器。

**关键词**：正交矩阵优化, 大规模优化, 自适应优化器, GPU加速, 机器学习约束

## 3 点简述
- 正交约束在机器学习中常见，但现有优化器计算昂贵且难以扩展到数百或数千约束。
- POGO基于Landing算法改进，仅需5次矩阵乘法，GPU友好，实时保持正交性。
- 在多个基准测试中，POGO显著优于近期优化器，能在几分钟内处理数千正交矩阵。

## 摘要（原文）

> Orthogonality constraints are ubiquitous in robust and probabilistic machine learning. Unfortunately, current optimizers are computationally expensive and do not scale to problems with hundreds or thousands of constraints. One notable exception is the Landing algorithm (Ablin et al., 2024) which, however comes at the expense of temporarily relaxing orthogonality. In this work, we revisit and improve on the ideas behind Landing, enabling the inclusion of modern adaptive optimizers while ensuring that orthogonal constraints are effectively met. Remarkably, these improvements come at little to no cost, and reduce the number of required hyperparemeters. Our algorithm POGO is fast and GPU-friendly, consisting of only 5 matrix products, and in practice maintains orthogonality at all times. On several challenging benchmarks, POGO greatly outperforms recent optimizers and shows it can optimize problems with thousands of orthogonal matrices in minutes while alternatives would take hours. As such, POGO sets a milestone to finally exploit orthogonality constraints in ML at scale. A PyTorch implementation of POGO is publicly available at https://github.com/adrianjav/pogo.

