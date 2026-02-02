---
layout: default
title: Sparse Attention as Compact Kernel Regression
---

# Sparse Attention as Compact Kernel Regression
**arXiv**：[2601.22766v1](https://arxiv.org/abs/2601.22766) · [PDF](https://arxiv.org/pdf/2601.22766.pdf)  
**作者**：Saul Santos, Nuno Gonçalves, Daniel C. McNamee, André F. T Martins  

**一句话要点**：建立稀疏注意力与紧致核回归的对应关系，为Transformer设计提供理论框架

**关键词**：稀疏注意力, 核回归, Transformer, 紧致核, α-entmax, 语言建模

## 3 点简述
- 核心问题：缺乏稀疏注意力机制的核理论理解，现有方法多基于启发式设计
- 方法要点：证明稀疏注意力（如归一化ReLU、sparsemax）对应Epanechnikov等紧致核回归，统一α-entmax与核密度估计
- 实验或效果：基于核回归的Memory Mosaics在语言建模、上下文学习和长度泛化任务中表现竞争性

## 摘要（原文）

> Recent work has revealed a link between self-attention mechanisms in transformers and test-time kernel regression via the Nadaraya-Watson estimator, with standard softmax attention corresponding to a Gaussian kernel. However, a kernel-theoretic understanding of sparse attention mechanisms is currently missing. In this paper, we establish a formal correspondence between sparse attention and compact (bounded support) kernels. We show that normalized ReLU and sparsemax attention arise from Epanechnikov kernel regression under fixed and adaptive normalizations, respectively. More generally, we demonstrate that widely used kernels in nonparametric density estimation -- including Epanechnikov, biweight, and triweight -- correspond to $α$-entmax attention with $α= 1 + \frac{1}{n}$ for $n \in \mathbb{N}$, while the softmax/Gaussian relationship emerges in the limit $n \to \infty$. This unified perspective explains how sparsity naturally emerges from kernel design and provides principled alternatives to heuristic top-$k$ attention and other associative memory mechanisms. Experiments with a kernel-regression-based variant of transformers -- Memory Mosaics -- show that kernel-based sparse attention achieves competitive performance on language modeling, in-context learning, and length generalization tasks, offering a principled framework for designing attention mechanisms.

