---
layout: default
title: Function-Space Decoupled Diffusion for Forward and Inverse Modeling in Carbon Capture and Storage
---

# Function-Space Decoupled Diffusion for Forward and Inverse Modeling in Carbon Capture and Storage
**arXiv**：[2602.12274v1](https://arxiv.org/abs/2602.12274) · [PDF](https://arxiv.org/pdf/2602.12274.pdf)  
**作者**：Xin Ju, Jiachen Yao, Anima Anandkumar, Sally M. Benson, Gege Wen  

**一句话要点**：提出Fun-DDPS框架，结合函数空间扩散模型与可微神经算子代理，用于碳捕集与封存的正反演建模。

**关键词**：碳捕集与封存, 函数空间扩散模型, 神经算子代理, 正反演建模, 数据同化, 地质参数恢复

## 3 点简述
- 核心问题：碳捕集与封存中地下流反演问题因观测稀疏而病态，传统方法在极端数据稀疏下失效。
- 方法要点：通过单通道扩散模型学习地质参数先验分布，利用局部神经算子代理提供物理一致指导，实现参数与动态场的解耦建模。
- 实验或效果：在合成数据集上，正演建模相对误差降至7.7%，反演结果与真实后验Jensen-Shannon散度小于0.06，样本效率提升4倍。

## 摘要（原文）

> Accurate characterization of subsurface flow is critical for Carbon Capture and Storage (CCS) but remains challenged by the ill-posed nature of inverse problems with sparse observations. We present Fun-DDPS, a generative framework that combines function-space diffusion models with differentiable neural operator surrogates for both forward and inverse modeling. Our approach learns a prior distribution over geological parameters (geomodel) using a single-channel diffusion model, then leverages a Local Neural Operator (LNO) surrogate to provide physics-consistent guidance for cross-field conditioning on the dynamics field. This decoupling allows the diffusion prior to robustly recover missing information in parameter space, while the surrogate provides efficient gradient-based guidance for data assimilation. We demonstrate Fun-DDPS on synthetic CCS modeling datasets, achieving two key results: (1) For forward modeling with only 25% observations, Fun-DDPS achieves 7.7% relative error compared to 86.9% for standard surrogates (an 11x improvement), proving its capability to handle extreme data sparsity where deterministic methods fail. (2) We provide the first rigorous validation of diffusion-based inverse solvers against asymptotically exact Rejection Sampling (RS) posteriors. Both Fun-DDPS and the joint-state baseline (Fun-DPS) achieve Jensen-Shannon divergence less than 0.06 against the ground truth. Crucially, Fun-DDPS produces physically consistent realizations free from the high-frequency artifacts observed in joint-state baselines, achieving this with 4x improved sample efficiency compared to rejection sampling.

