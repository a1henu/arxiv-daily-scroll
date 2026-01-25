---
layout: default
title: On the Intrinsic Dimensions of Data in Kernel Learning
---

# On the Intrinsic Dimensions of Data in Kernel Learning
**arXiv**：[2601.16139v1](https://arxiv.org/abs/2601.16139) · [PDF](https://arxiv.org/pdf/2601.16139.pdf)  
**作者**：Rustem Takhanov  

**一句话要点**：提出基于核函数内蕴维度的核岭回归泛化误差分析，并设计算法估计维度上界。

**关键词**：核岭回归, 内蕴维度, 泛化误差, Kolmogorov n-宽度, 核学习, 分形集

## 3 点简述
- 研究核岭回归中数据内蕴维度对泛化性能的影响，定义Minkowski维度和有效维度。
- 分析Kolmogorov n-宽度与积分算子特征值的关系，推导出泛化误差上界为O(n^{-(2+d_K)/(2+2d_K)+ε})。
- 提出算法从有限样本估计n-宽度上界，并在分形集上计算有效维度，验证其小于Minkowski维度。

## 摘要（原文）

> The manifold hypothesis suggests that the generalization performance of machine learning methods improves significantly when the intrinsic dimension of the input distribution's support is low. In the context of KRR, we investigate two alternative notions of intrinsic dimension. The first, denoted $d_ρ$, is the upper Minkowski dimension defined with respect to the canonical metric induced by a kernel function $K$ on a domain $Ω$. The second, denoted $d_K$, is the effective dimension, derived from the decay rate of Kolmogorov $n$-widths associated with $K$ on $Ω$. Given a probability measure $μ$ on $Ω$, we analyze the relationship between these $n$-widths and eigenvalues of the integral operator $φ\to \int_ΩK(\cdot,x)φ(x)dμ(x)$. We show that, for a fixed domain $Ω$, the Kolmogorov $n$-widths characterize the worst-case eigenvalue decay across all probability measures $μ$ supported on $Ω$. These eigenvalues are central to understanding the generalization behavior of constrained KRR, enabling us to derive an excess error bound of order $O(n^{-\frac{2+d_K}{2+2d_K} + ε})$ for any $ε> 0$, when the training set size $n$ is large. We also propose an algorithm that estimates upper bounds on the $n$-widths using only a finite sample from $μ$. For distributions close to uniform, we prove that $ε$-accurate upper bounds on all $n$-widths can be computed with high probability using at most $O\left(ε^{-d_ρ}\log\frac{1}ε\right)$ samples, with fewer required for small $n$. Finally, we compute the effective dimension $d_K$ for various fractal sets and present additional numerical experiments. Our results show that, for kernels such as the Laplace kernel, the effective dimension $d_K$ can be significantly smaller than the Minkowski dimension $d_ρ$, even though $d_K = d_ρ$ provably holds on regular domains.

