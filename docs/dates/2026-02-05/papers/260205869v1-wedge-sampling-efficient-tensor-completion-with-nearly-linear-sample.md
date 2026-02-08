---
layout: default
title: Wedge Sampling: Efficient Tensor Completion with Nearly-Linear Sample Complexity
---

# Wedge Sampling: Efficient Tensor Completion with Nearly-Linear Sample Complexity
**arXiv**：[2602.05869v1](https://arxiv.org/abs/2602.05869) · [PDF](https://arxiv.org/pdf/2602.05869.pdf)  
**作者**：Hengrui Luo, Anna Ma, Ludovic Stephan, Yizhe Zhu  

**一句话要点**：提出楔形采样以解决低秩张量补全中均匀采样样本复杂度高的问题

**关键词**：张量补全, 楔形采样, 低秩恢复, 谱初始化, 样本复杂度, 非自适应采样

## 3 点简述
- 研究低秩张量补全问题，传统均匀采样在稀疏时难以有效初始化
- 引入楔形采样，通过结构化长度二模式增强谱信号，实现近线性样本复杂度
- 结合现有细化方法，仅需额外少量均匀采样，显著提升效率

## 摘要（原文）

> We introduce Wedge Sampling, a new non-adaptive sampling scheme for low-rank tensor completion. We study recovery of an order-$k$ low-rank tensor of dimension $n \times \cdots \times n$ from a subset of its entries. Unlike the standard uniform entry model (i.e., i.i.d. samples from $[n]^k$), wedge sampling allocates observations to structured length-two patterns (wedges) in an associated bipartite sampling graph. By directly promoting these length-two connections, the sampling design strengthens the spectral signal that underlies efficient initialization, in regimes where uniform sampling is too sparse to generate enough informative correlations.
>   Our main result shows that this change in sampling paradigm enables polynomial-time algorithms to achieve both weak and exact recovery with nearly linear sample complexity in $n$. The approach is also plug-and-play: wedge-sampling-based spectral initialization can be combined with existing refinement procedures (e.g., spectral or gradient-based methods) using only an additional $\tilde{O}(n)$ uniformly sampled entries, substantially improving over the $\tilde{O}(n^{k/2})$ sample complexity typically required under uniform entry sampling for efficient methods. Overall, our results suggest that the statistical-to-computational gap highlighted in Barak and Moitra (2022) is, to a large extent, a consequence of the uniform entry sampling model for tensor completion, and that alternative non-adaptive measurement designs that guarantee a strong initialization can overcome this barrier.

