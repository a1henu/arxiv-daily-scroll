---
layout: default
title: Fourier Transformers for Latent Crystallographic Diffusion and Generative Modeling
---

# Fourier Transformers for Latent Crystallographic Diffusion and Generative Modeling
**arXiv**：[2602.12045v1](https://arxiv.org/abs/2602.12045) · [PDF](https://arxiv.org/pdf/2602.12045.pdf)  
**作者**：Jed A. Duersch, Elohan Veillon, Astrid Klipfel, Adlane Sayede, Zied Bouraoui  

**一句话要点**：提出傅里叶变换器用于晶体材料的生成建模，通过倒易空间表示处理周期性边界条件和对称性。

**关键词**：晶体材料生成, 傅里叶变换, 潜在扩散模型, 周期性边界条件, 变压器变分自编码器

## 3 点简述
- 核心问题：晶体材料生成需处理周期性边界、对称性和物理约束，现有方法难以扩展到大型单元。
- 方法要点：使用截断傅里叶变换表示单元密度，基于复数傅里叶系数的变压器变分自编码器和潜在扩散模型。
- 实验或效果：在LeMaterial基准上评估重构和潜在扩散，小单元条件下与基于坐标的基线比较生成性能。

## 摘要（原文）

> The discovery of new crystalline materials calls for generative models that handle periodic boundary conditions, crystallographic symmetries, and physical constraints, while scaling to large and structurally diverse unit cells. We propose a reciprocal-space generative pipeline that represents crystals through a truncated Fourier transform of the species-resolved unit-cell density, rather than modeling atomic coordinates directly. This representation is periodicity-native, admits simple algebraic actions of space-group symmetries, and naturally supports variable atomic multiplicities during generation, addressing a common limitation of particle-based approaches. Using only nine Fourier basis functions per spatial dimension, our approach reconstructs unit cells containing up to 108 atoms per chemical species. We instantiate this pipeline with a transformer variational autoencoder over complex-valued Fourier coefficients, and a latent diffusion model that generates in the compressed latent space. We evaluate reconstruction and latent diffusion on the LeMaterial benchmark and compare unconditional generation against coordinate-based baselines in the small-cell regime ($\leq 16$ atoms per unit cell).

