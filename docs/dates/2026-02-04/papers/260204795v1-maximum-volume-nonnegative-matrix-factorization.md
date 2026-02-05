---
layout: default
title: Maximum-Volume Nonnegative Matrix Factorization
---

# Maximum-Volume Nonnegative Matrix Factorization
**arXiv**：[2602.04795v1](https://arxiv.org/abs/2602.04795) · [PDF](https://arxiv.org/pdf/2602.04795.pdf)  
**作者**：Olivier Vu Thanh, Nicolas Gillis  

**一句话要点**：提出最大体积非负矩阵分解以增强稀疏分解和避免秩缺陷，应用于高光谱解混。

**关键词**：非负矩阵分解, 最大体积优化, 稀疏分解, 高光谱解混, 矩阵因子化, 可解释性分析

## 3 点简述
- 核心问题：非负矩阵分解中为提升可解释性和唯一性，传统最小体积方法在噪声下易产生秩缺陷。
- 方法要点：采用最大体积方法最大化因子H的体积，在无噪声下与最小体积同样可识别，但噪声下表现更优。
- 实验或效果：证明最大体积方法能提取稀疏分解、避免秩缺陷，并开发算法和归一化变体，在高光谱解混中验证性能。

## 摘要（原文）

> Nonnegative matrix factorization (NMF) is a popular data embedding technique. Given a nonnegative data matrix $X$, it aims at finding two lower dimensional matrices, $W$ and $H$, such that $X\approx WH$, where the factors $W$ and $H$ are constrained to be element-wise nonnegative. The factor $W$ serves as a basis for the columns of $X$. In order to obtain more interpretable and unique solutions, minimum-volume NMF (MinVol NMF) minimizes the volume of $W$. In this paper, we consider the dual approach, where the volume of $H$ is maximized instead; this is referred to as maximum-volume NMF (MaxVol NMF). MaxVol NMF is identifiable under the same conditions as MinVol NMF in the noiseless case, but it behaves rather differently in the presence of noise. In practice, MaxVol NMF is much more effective to extract a sparse decomposition and does not generate rank-deficient solutions. In fact, we prove that the solutions of MaxVol NMF with the largest volume correspond to clustering the columns of $X$ in disjoint clusters, while the solutions of MinVol NMF with smallest volume are rank deficient. We propose two algorithms to solve MaxVol NMF. We also present a normalized variant of MaxVol NMF that exhibits better performance than MinVol NMF and MaxVol NMF, and can be interpreted as a continuum between standard NMF and orthogonal NMF. We illustrate our results in the context of hyperspectral unmixing.

