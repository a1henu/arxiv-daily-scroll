---
layout: default
title: RANDSMAPs: Random-Feature/multi-Scale Neural Decoders with Mass Preservation
---

# RANDSMAPs: Random-Feature/multi-Scale Neural Decoders with Mass Preservation
**arXiv**：[2601.14794v1](https://arxiv.org/abs/2601.14794) · [PDF](https://arxiv.org/pdf/2601.14794.pdf)  
**作者**：Dimitrios G. Patsatzis, Alessandro Della Pia, Lucia Russo, Constantinos Siettos  

**一句话要点**：提出RANDSMAPs以在流形学习中解决病态原像问题并保持质量守恒

**关键词**：流形学习, 质量守恒, 随机特征神经网络, 多尺度解码, 病态原像问题, 约束优化

## 3 点简述
- 核心问题：流形学习中的病态原像问题，需在解码时显式遵守守恒定律
- 方法要点：基于随机傅里叶特征神经网络，结合多尺度变体，通过约束优化实现质量保持
- 实验或效果：在交通流、MRI图像和人群动力学基准上验证高重建精度和单机精度质量守恒

## 摘要（原文）

> We introduce RANDSMAPs (Random-feature/multi-scale neural decoders with Mass Preservation), numerical analysis-informed, explainable neural decoders designed to explicitly respect conservation laws when solving the challenging ill-posed pre-image problem in manifold learning. We start by proving the equivalence of vanilla random Fourier feature neural networks to Radial Basis Function interpolation and the double Diffusion Maps (based on Geometric Harmonics) decoders in the deterministic limit. We then establish the theoretical foundations for RANDSMAP and introduce its multiscale variant to capture structures across multiple scales. We formulate and derive the closed-form solution of the corresponding constrained optimization problem and prove the mass preservation property. Numerically, we assess the performance of RANDSMAP on three benchmark problems/datasets with mass preservation obtained by the Lighthill-Whitham-Richards traffic flow PDE with shock waves, 2D rotated MRI brain images, and the Hughes crowd dynamics PDEs. We demonstrate that RANDSMAPs yield high reconstruction accuracy at low computational cost and maintain mass conservation at single-machine precision. In its vanilla formulation, the scheme remains applicable to the classical pre-image problem, i.e., when mass-preservation constraints are not imposed.

