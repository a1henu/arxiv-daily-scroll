---
layout: default
title: NeuraLSP: An Efficient and Rigorous Neural Left Singular Subspace Preconditioner for Conjugate Gradient Methods
---

# NeuraLSP: An Efficient and Rigorous Neural Left Singular Subspace Preconditioner for Conjugate Gradient Methods
**arXiv**：[2601.20174v1](https://arxiv.org/abs/2601.20174) · [PDF](https://arxiv.org/pdf/2601.20174.pdf)  
**作者**：Alexander Benanti, Xi Han, Hong Qin  

**一句话要点**：提出NeuraLSP神经左奇异子空间预处理器，以解决PDE求解中图神经网络预处理器秩膨胀和收敛率不佳问题。

**关键词**：偏微分方程求解, 神经预处理器, 左奇异子空间, 共轭梯度法, 图神经网络, 秩膨胀

## 3 点简述
- 核心问题：现有GNN预处理器因图聚合导致秩膨胀和收敛率不优。
- 方法要点：利用系统矩阵近零空间向量的左奇异子空间，设计新损失函数压缩谱信息为低秩算子。
- 实验或效果：理论保证和实证稳健性，在多种PDE上实现最高53%加速。

## 摘要（原文）

> Numerical techniques for solving partial differential equations (PDEs) are integral for many fields across science and engineering. Such techniques usually involve solving large, sparse linear systems, where preconditioning methods are critical. In recent years, neural methods, particularly graph neural networks (GNNs), have demonstrated their potential through accelerated convergence. Nonetheless, to extract connective structures, existing techniques aggregate discretized system matrices into graphs, and suffer from rank inflation and a suboptimal convergence rate. In this paper, we articulate NeuraLSP, a novel neural preconditioner combined with a novel loss metric that leverages the left singular subspace of the system matrix's near-nullspace vectors. By compressing spectral information into a fixed low-rank operator, our method exhibits both theoretical guarantees and empirical robustness to rank inflation, affording up to a 53% speedup. Besides the theoretical guarantees for our newly-formulated loss function, our comprehensive experimental results across diverse families of PDEs also substantiate the aforementioned theoretical advances.

