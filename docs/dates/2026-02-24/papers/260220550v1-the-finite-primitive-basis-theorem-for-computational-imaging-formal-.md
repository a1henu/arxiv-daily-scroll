---
layout: default
title: The Finite Primitive Basis Theorem for Computational Imaging: Formal Foundations of the OperatorGraph Representation
---

# The Finite Primitive Basis Theorem for Computational Imaging: Formal Foundations of the OperatorGraph Representation
**arXiv**：[2602.20550v1](https://arxiv.org/abs/2602.20550) · [PDF](https://arxiv.org/pdf/2602.20550.pdf)  
**作者**：Chengshuai Yang  

**一句话要点**：提出有限基元定理，将计算成像前向模型表示为11个基元构成的DAG，建立算子图表示形式基础。

**关键词**：计算成像, 算子图表示, 有限基元定理, 前向模型, DAG分解, 物理世界模型

## 3 点简述
- 核心问题：计算成像前向模型传统实现为单一、模态特定代码，缺乏统一表示。
- 方法要点：证明广泛算子类Cimg中任何模型可用11个基元DAG近似表示，并提供构造算法。
- 实验或效果：在31个线性模态上验证误差低于0.01，并为9个非线性模态提供分解示例。

## 摘要（原文）

> Computational imaging forward models, from coded aperture spectral cameras to MRI scanners, are traditionally implemented as monolithic, modality-specific codes. We prove that every forward model in a broad, precisely defined operator class Cimg (encompassing clinical, scientific, and industrial imaging modalities, both linear and nonlinear) admits an epsilon-approximate representation as a typed directed acyclic graph (DAG) whose nodes are drawn from a library of exactly 11 canonical primitives: Propagate, Modulate, Project, Encode, Convolve, Accumulate, Detect, Sample, Disperse, Scatter, and Transform. We call this the Finite Primitive Basis Theorem. The proof is constructive: we provide an algorithm that, given any H in Cimg, produces a DAG G with relative operator error at most epsilon and graph complexity within prescribed bounds. We further prove that the library is minimal: removing any single primitive causes at least one modality to lose its epsilon-approximate representation. A systematic analysis of nonlinearities in imaging physics shows they fall into two structural categories: pointwise scalar functions (handled by Transform) and self-consistent iterations (unrolled into existing linear primitives). Empirical validation on 31 linear modalities confirms eimg below 0.01 with at most 5 nodes and depth 5, and we provide constructive DAG decompositions for 9 additional nonlinear modalities. These results establish mathematical foundations for the Physics World Model (PWM) framework.

