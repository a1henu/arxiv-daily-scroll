---
layout: default
title: TT-FSI: Scalable Faithful Shapley Interactions via Tensor-Train
---

# TT-FSI: Scalable Faithful Shapley Interactions via Tensor-Train
**arXiv**：[2601.01903v1](https://arxiv.org/abs/2601.01903) · [PDF](https://arxiv.org/pdf/2601.01903.pdf)  
**作者**：Ungsik Kim, Suwon Lee  

**一句话要点**：提出TT-FSI以高效计算忠实Shapley交互指数，通过张量列车实现指数级加速与内存优化。

**关键词**：忠实Shapley交互指数, 张量列车分解, 可解释人工智能, 计算复杂度优化, 矩阵乘积算子

## 3 点简述
- 核心问题：忠实Shapley交互指数计算复杂度高，现有方法需O(4^d)内存，难以扩展到高维数据。
- 方法要点：利用矩阵乘积算子表示线性算子，证明TT秩为O(ℓd)，设计扫描算法实现O(ℓ²d³·2^d)时间和O(ℓd²)存储。
- 实验效果：在d=8至20数据集上，相比基线加速280倍，内存减少290倍，可扩展到d=20而竞争方法失败。

## 摘要（原文）

> The Faithful Shapley Interaction (FSI) index uniquely satisfies the faithfulness axiom among Shapley interaction indices, but computing FSI requires $O(d^\ell \cdot 2^d)$ time and existing implementations use $O(4^d)$ memory. We present TT-FSI, which exploits FSI's algebraic structure via Matrix Product Operators (MPO). Our main theoretical contribution is proving that the linear operator $v \mapsto \text{FSI}(v)$ admits an MPO representation with TT-rank $O(\ell d)$, enabling an efficient sweep algorithm with $O(\ell^2 d^3 \cdot 2^d)$ time and $O(\ell d^2)$ core storage an exponential improvement over existing methods. Experiments on six datasets ($d=8$ to $d=20$) demonstrate up to 280$\times$ speedup over baseline, 85$\times$ over SHAP-IQ, and 290$\times$ memory reduction. TT-FSI scales to $d=20$ (1M coalitions) where all competing methods fail.

