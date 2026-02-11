---
layout: default
title: Statistical-Computational Trade-offs in Learning Multi-Index Models via Harmonic Analysis
---

# Statistical-Computational Trade-offs in Learning Multi-Index Models via Harmonic Analysis
**arXiv**：[2602.09959v1](https://arxiv.org/abs/2602.09959) · [PDF](https://arxiv.org/pdf/2602.09959.pdf)  
**作者**：Hugo Latourelle-Vigeant, Theodor Misiakiewicz  

**一句话要点**：利用调和分析推导多索引模型学习中的统计-计算权衡，并提出谱算法实现最优复杂度。

**关键词**：多索引模型, 调和分析, 统计查询框架, 低阶多项式框架, 谱算法, 复杂度权衡

## 3 点简述
- 研究多索引模型学习问题，标签仅依赖于未知低维投影。
- 基于正交群等变性，在球对称输入下通过调和分析推导SQ和LDP框架的复杂度下界。
- 设计基于调和张量展开的谱算法，实现样本与运行时间的权衡，接近理论下界。

## 摘要（原文）

> We study the problem of learning multi-index models (MIMs), where the label depends on the input $\boldsymbol{x} \in \mathbb{R}^d$ only through an unknown $\mathsf{s}$-dimensional projection $\boldsymbol{W}_*^\mathsf{T} \boldsymbol{x} \in \mathbb{R}^\mathsf{s}$. Exploiting the equivariance of this problem under the orthogonal group $\mathcal{O}_d$, we obtain a sharp harmonic-analytic characterization of the learning complexity for MIMs with spherically symmetric inputs -- which refines and generalizes previous Gaussian-specific analyses. Specifically, we derive statistical and computational complexity lower bounds within the Statistical Query (SQ) and Low-Degree Polynomial (LDP) frameworks. These bounds decompose naturally across spherical harmonic subspaces. Guided by this decomposition, we construct a family of spectral algorithms based on harmonic tensor unfolding that sequentially recover the latent directions and (nearly) achieve these SQ and LDP lower bounds. Depending on the choice of harmonic degree sequence, these estimators can realize a broad range of trade-offs between sample and runtime complexity. From a technical standpoint, our results build on the semisimple decomposition of the $\mathcal{O}_d$-action on $L^2 (\mathbb{S}^{d-1})$ and the intertwining isomorphism between spherical harmonics and traceless symmetric tensors.

