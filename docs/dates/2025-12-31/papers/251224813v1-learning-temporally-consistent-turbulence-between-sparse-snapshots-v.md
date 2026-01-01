---
layout: default
title: Learning Temporally Consistent Turbulence Between Sparse Snapshots via Diffusion Models
---

# Learning Temporally Consistent Turbulence Between Sparse Snapshots via Diffusion Models
**arXiv**：[2512.24813v1](https://arxiv.org/abs/2512.24813) · [PDF](https://arxiv.org/pdf/2512.24813.pdf)  
**作者**：Mohammed Sardar, Małgorzata J. Zimoń, Samuel Draycott, Alistair Revell, Alex Skillen  

**一句话要点**：提出基于条件DDPM的生成模型，用于稀疏快照间湍流的时间一致插值

**关键词**：湍流插值, 扩散模型, 时间一致性, 生成代理, 统计分析

## 3 点简述
- 研究稀疏、去相关湍流快照间时空序列的时间插值统计准确性
- 采用条件去噪扩散概率模型作为生成代理，重建湍流动态
- 在2D Kolmogorov流和3D Kelvin-Helmholtz不稳定性上验证，分析湍动能谱和结构衰减

## 摘要（原文）

> We investigate the statistical accuracy of temporally interpolated spatiotemporal flow sequences between sparse, decorrelated snapshots of turbulent flow fields using conditional Denoising Diffusion Probabilistic Models (DDPMs). The developed method is presented as a proof-of-concept generative surrogate for reconstructing coherent turbulent dynamics between sparse snapshots, demonstrated on a 2D Kolmogorov Flow, and a 3D Kelvin-Helmholtz Instability (KHI). We analyse the generated flow sequences through the lens of statistical turbulence, examining the time-averaged turbulent kinetic energy spectra over generated sequences, and temporal decay of turbulent structures. For the non-stationary Kelvin-Helmholtz Instability, we assess the ability of the proposed method to capture evolving flow statistics across the most strongly time-varying flow regime. We additionally examine instantaneous fields and physically motivated metrics at key stages of the KHI flow evolution.

