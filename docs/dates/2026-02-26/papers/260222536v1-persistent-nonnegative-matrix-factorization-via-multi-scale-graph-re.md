---
layout: default
title: Persistent Nonnegative Matrix Factorization via Multi-Scale Graph Regularization
---

# Persistent Nonnegative Matrix Factorization via Multi-Scale Graph Regularization
**arXiv**：[2602.22536v1](https://arxiv.org/abs/2602.22536) · [PDF](https://arxiv.org/pdf/2602.22536.pdf)  
**作者**：Jichao Zhang, Ran Miao, Limin Li  

**一句话要点**：提出持久非负矩阵分解以解决单尺度NMF无法捕捉多尺度连通性演化的问题

**关键词**：非负矩阵分解, 多尺度分析, 持久同调, 图正则化, 低秩嵌入, 单细胞RNA测序

## 3 点简述
- 现有NMF方法为单尺度，无法捕获跨分辨率连通性结构演化
- 通过持久同调识别典型尺度，引入图拉普拉斯正则化和跨尺度一致性约束
- 在合成和单细胞RNA测序数据集上验证多尺度低秩嵌入的有效性

## 摘要（原文）

> Matrix factorization techniques, especially Nonnegative Matrix Factorization (NMF), have been widely used for dimensionality reduction and interpretable data representation. However, existing NMF-based methods are inherently single-scale and fail to capture the evolution of connectivity structures across resolutions. In this work, we propose persistent nonnegative matrix factorization (pNMF), a scale-parameterized family of NMF problems, that produces a sequence of persistence-aligned embeddings rather than a single one. By leveraging persistent homology, we identify a canonical minimal sufficient scale set at which the underlying connectivity undergoes qualitative changes. These canonical scales induce a sequence of graph Laplacians, leading to a coupled NMF formulation with scale-wise geometric regularization and explicit cross-scale consistency constraint. We analyze the structural properties of the embeddings along the scale parameter and establish bounds on their increments between consecutive scales. The resulting model defines a nontrivial solution path across scales, rather than a single factorization, which poses new computational challenges. We develop a sequential alternating optimization algorithm with guaranteed convergence. Numerical experiments on synthetic and single-cell RNA sequencing datasets demonstrate the effectiveness of the proposed approach in multi-scale low-rank embeddings.

