---
layout: default
title: Forecast the Principal, Stabilize the Residual: Subspace-Aware Feature Caching for Efficient Diffusion Transformers
---

# Forecast the Principal, Stabilize the Residual: Subspace-Aware Feature Caching for Efficient Diffusion Transformers
**arXiv**：[2601.07396v1](https://arxiv.org/abs/2601.07396) · [PDF](https://arxiv.org/pdf/2601.07396.pdf)  
**作者**：Guantao Chen, Shikang Zheng, Yuqi Lin, Linfeng Zhang  

**一句话要点**：提出SVD-Cache以加速扩散Transformer推理，通过子空间感知特征缓存提升效率。

**关键词**：扩散Transformer, 特征缓存, 子空间分解, 推理加速, SVD预测

## 3 点简述
- 核心问题：扩散Transformer迭代采样计算成本高，现有特征缓存方法未区分特征子空间。
- 方法要点：基于SVD分解特征，对主成分子空间进行EMA预测，直接重用残差子空间。
- 实验或效果：在FLUX和HunyuanVideo上实现5.55倍加速，兼容蒸馏、量化等技术。

## 摘要（原文）

> Diffusion Transformer (DiT) models have achieved unprecedented quality in image and video generation, yet their iterative sampling process remains computationally prohibitive. To accelerate inference, feature caching methods have emerged by reusing intermediate representations across timesteps. However, existing caching approaches treat all feature components uniformly. We reveal that DiT feature spaces contain distinct principal and residual subspaces with divergent temporal behavior: the principal subspace evolves smoothly and predictably, while the residual subspace exhibits volatile, low-energy oscillations that resist accurate prediction. Building on this insight, we propose SVD-Cache, a subspace-aware caching framework that decomposes diffusion features via Singular Value Decomposition (SVD), applies exponential moving average (EMA) prediction to the dominant low-rank components, and directly reuses the residual subspace. Extensive experiments demonstrate that SVD-Cache achieves near-lossless across diverse models and methods, including 5.55$\times$ speedup on FLUX and HunyuanVideo, and compatibility with model acceleration techniques including distillation, quantization and sparse attention. Our code is in supplementary material and will be released on Github.

