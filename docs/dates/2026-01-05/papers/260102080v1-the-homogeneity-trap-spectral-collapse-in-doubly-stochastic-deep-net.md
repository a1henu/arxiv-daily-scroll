---
layout: default
title: The Homogeneity Trap: Spectral Collapse in Doubly-Stochastic Deep Networks
---

# The Homogeneity Trap: Spectral Collapse in Doubly-Stochastic Deep Networks
**arXiv**：[2601.02080v1](https://arxiv.org/abs/2601.02080) · [PDF](https://arxiv.org/pdf/2601.02080.pdf)  
**作者**：Yizhi Liu  

**一句话要点**：揭示双随机深度网络中的谱崩溃现象，即同质性陷阱，分析其与熵稳定性的权衡。

**关键词**：双随机矩阵, 谱崩溃, 同质性陷阱, 熵稳定性, 深度网络, 特征变换

## 3 点简述
- 核心问题：双随机矩阵约束导致谱退化，抑制次主导奇异值，过滤高频特征。
- 方法要点：推导谱界，证明高熵约束限制有效感受野，层归一化在噪声主导下失效。
- 实验或效果：发现熵稳定性与谱表达性之间的基本权衡，结构在低信噪比下不可逆丢失。

## 摘要（原文）

> Doubly-stochastic matrices (DSM) are increasingly utilized in structure-preserving deep architectures -- such as Optimal Transport layers and Sinkhorn-based attention -- to enforce numerical stability and probabilistic interpretability. In this work, we identify a critical spectral degradation phenomenon inherent to these constraints, termed the Homogeneity Trap. We demonstrate that the maximum-entropy bias, typical of Sinkhorn-based projections, drives the mixing operator towards the uniform barycenter, thereby suppressing the subdominant singular value σ_2 and filtering out high-frequency feature components. We derive a spectral bound linking σ_2 to the network's effective depth, showing that high-entropy constraints restrict feature transformation to a shallow effective receptive field. Furthermore, we formally demonstrate that Layer Normalization fails to mitigate this collapse in noise-dominated regimes; specifically, when spectral filtering degrades the Signal-to-Noise Ratio (SNR) below a critical threshold, geometric structure is irreversibly lost to noise-induced orthogonal collapse. Our findings highlight a fundamental trade-off between entropic stability and spectral expressivity in DSM-constrained networks.

