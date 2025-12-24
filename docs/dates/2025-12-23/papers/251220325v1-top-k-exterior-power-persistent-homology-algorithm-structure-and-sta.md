---
layout: default
title: Top-K Exterior Power Persistent Homology: Algorithm, Structure, and Stability
---

# Top-K Exterior Power Persistent Homology: Algorithm, Structure, and Stability
**arXiv**：[2512.20325v1](https://arxiv.org/abs/2512.20325) · [PDF](https://arxiv.org/pdf/2512.20325.pdf)  
**作者**：Yoshihiro Maruyama  

**一句话要点**：提出Top-K外幂持久同调算法，高效提取高阶特征以支持大规模数据分析。

**关键词**：持久同调, 外幂层, Top-K算法, 结构分解, 稳定性分析, 大规模数据处理

## 3 点简述
- 研究从持久模的外幂层中提取K个最长区间的问题。
- 证明结构分解定理，实现基于优先队列的最佳优先算法。
- 实验验证算法在高度重叠情况下优于完全枚举，加速特征提取。

## 摘要（原文）

> Exterior powers play important roles in persistent homology in computational geometry. In the present paper we study the problem of extracting the $K$ longest intervals of the exterior-power layers of a tame persistence module. We prove a structural decomposition theorem that organizes the exterior-power layers into monotone per-anchor streams with explicit multiplicities, enabling a best-first algorithm. We also show that the Top-$K$ length vector is $2$-Lipschitz under bottleneck perturbations of the input barcode, and prove a comparison-model lower bound. Our experiments confirm the theory, showing speedups over full enumeration in high overlap cases. By enabling efficient extraction of the most prominent features, our approach makes higher-order persistence feasible for large datasets and thus broadly applicable to machine learning, data science, and scientific computing.

