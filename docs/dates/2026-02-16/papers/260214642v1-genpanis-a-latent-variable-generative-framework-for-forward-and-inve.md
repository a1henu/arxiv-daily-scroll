---
layout: default
title: GenPANIS: A Latent-Variable Generative Framework for Forward and Inverse PDE Problems in Multiphase Media
---

# GenPANIS: A Latent-Variable Generative Framework for Forward and Inverse PDE Problems in Multiphase Media
**arXiv**：[2602.14642v1](https://arxiv.org/abs/2602.14642) · [PDF](https://arxiv.org/pdf/2602.14642.pdf)  
**作者**：Matthaios Chatzopoulos, Phaedon-Stelios Koutsourelakis  

**一句话要点**：提出GenPANIS生成框架以解决多相介质中离散微结构的前向与反问题

**关键词**：多相介质, 生成模型, 反问题求解, PDE求解, 不确定性量化, 潜在变量模型

## 3 点简述
- 多相介质中离散微结构的反问题与反设计因非可微性难以应用梯度方法
- GenPANIS通过连续潜在嵌入保持离散微结构，支持单架构内双向推理
- 在Darcy流和Helmholtz方程上验证，性能优于现有方法且参数更少

## 摘要（原文）

> Inverse problems and inverse design in multiphase media, i.e., recovering or engineering microstructures to achieve target macroscopic responses, require operating on discrete-valued material fields, rendering the problem non-differentiable and incompatible with gradient-based methods. Existing approaches either relax to continuous approximations, compromising physical fidelity, or employ separate heavyweight models for forward and inverse tasks. We propose GenPANIS, a unified generative framework that preserves exact discrete microstructures while enabling gradient-based inference through continuous latent embeddings. The model learns a joint distribution over microstructures and PDE solutions, supporting bidirectional inference (forward prediction and inverse recovery) within a single architecture. The generative formulation enables training with unlabeled data, physics residuals, and minimal labeled pairs. A physics-aware decoder incorporating a differentiable coarse-grained PDE solver preserves governing equation structure, enabling extrapolation to varying boundary conditions and microstructural statistics. A learnable normalizing flow prior captures complex posterior structure for inverse problems. Demonstrated on Darcy flow and Helmholtz equations, GenPANIS maintains accuracy on challenging extrapolative scenarios - including unseen boundary conditions, volume fractions, and microstructural morphologies, with sparse, noisy observations. It outperforms state-of-the-art methods while using 10 - 100 times fewer parameters and providing principled uncertainty quantification.

