---
layout: default
title: pathsig: A GPU-Accelerated Library for Truncated and Projected Path Signatures
---

# pathsig: A GPU-Accelerated Library for Truncated and Projected Path Signatures
**arXiv**：[2602.24066v1](https://arxiv.org/abs/2602.24066) · [PDF](https://arxiv.org/pdf/2602.24066.pdf)  
**作者**：Tobias Nygaard  

**一句话要点**：提出pathsig库以解决路径签名在大规模梯度学习中的可扩展性问题

**关键词**：路径签名, GPU加速, PyTorch库, 并行计算, 机器学习模型

## 3 点简述
- 核心问题：现有路径签名库在大规模梯度学习中缺乏可扩展性
- 方法要点：基于PyTorch原生实现，使用CUDA内核并行更新签名系数
- 实验或效果：相比其他库，在截断签名计算中实现10-30倍加速

## 摘要（原文）

> Path signatures provide a rich representation of sequential data, with strong theoretical guarantees and good performance in a variety of machine-learning tasks. While signatures have progressed from fixed feature extractors to trainable components of machine-learning models, existing libraries often lack the required scalability for large-scale, gradient-based learning. To address this gap, this paper introduces pathsig, a PyTorch-native library that computes path signatures directly in the word basis. By using CUDA kernels to update signature coefficients in parallel over prefix-closed word sets, pathsig achieves high GPU throughput and near-minimal peak memory. Compared with other libraries, pathsig achieves 10-30x speedups for computation of truncated signatures and up to 4-10x speedups in training that require backpropagation through the signature. Beyond regular truncation, pathsig supports projections of the (infinite-dimensional) signature onto user-specified sets of words and anisotropic truncation motivated by inhomogeneous path regularity, enabling more compact representations that can reduce dimensionality, redundancy, and computational cost.

