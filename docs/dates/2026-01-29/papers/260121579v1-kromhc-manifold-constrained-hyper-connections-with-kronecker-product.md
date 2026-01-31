---
layout: default
title: KromHC: Manifold-Constrained Hyper-Connections with Kronecker-Product Residual Matrices
---

# KromHC: Manifold-Constrained Hyper-Connections with Kronecker-Product Residual Matrices
**arXiv**：[2601.21579v1](https://arxiv.org/abs/2601.21579) · [PDF](https://arxiv.org/pdf/2601.21579.pdf)  
**作者**：Wuyang Zhou, Yuxuan Gu, Giorgos Iacovides, Danilo Mandic  

**一句话要点**：提出KromHC，利用Kronecker积构建双随机残差矩阵，解决超连接训练不稳定与参数爆炸问题。

**关键词**：超连接, 双随机矩阵, Kronecker积, 参数复杂度, 神经网络优化, 残差连接

## 3 点简述
- 超连接存在训练不稳定和参数复杂度高的问题，mHC通过Birkhoff多面体投影缓解但面临双随机性不精确和O(n^3C)复杂度。
- KromHC使用小双随机矩阵的Kronecker积参数化残差矩阵，保证精确双随机性，将参数复杂度降至O(n^2C)。
- 实验表明KromHC在性能上匹配或超越SOTA mHC变体，同时显著减少可训练参数。

## 摘要（原文）

> The success of Hyper-Connections (HC) in neural networks (NN) has also highlighted issues related to its training instability and restricted scalability. The Manifold-Constrained Hyper-Connections (mHC) mitigate these challenges by projecting the residual connection space onto a Birkhoff polytope, however, it faces two issues: 1) its iterative Sinkhorn-Knopp (SK) algorithm does not always yield exact doubly stochastic residual matrices; 2) mHC incurs a prohibitive $\mathcal{O}(n^3C)$ parameter complexity with $n$ as the width of the residual stream and $C$ as the feature dimension. The recently proposed mHC-lite reparametrizes the residual matrix via the Birkhoff-von-Neumann theorem to guarantee double stochasticity, but also faces a factorial explosion in its parameter complexity, $\mathcal{O} \left( nC \cdot n! \right)$. To address both challenges, we propose \textbf{KromHC}, which uses the \underline{Kro}necker products of smaller doubly stochastic matrices to parametrize the residual matrix in \underline{mHC}. By enforcing manifold constraints across the factor residual matrices along each mode of the tensorized residual stream, KromHC guarantees exact double stochasticity of the residual matrices while reducing parameter complexity to $\mathcal{O}(n^2C)$. Comprehensive experiments demonstrate that KromHC matches or even outperforms state-of-the-art (SOTA) mHC variants, while requiring significantly fewer trainable parameters. The code is available at \texttt{https://github.com/wz1119/KromHC}.

