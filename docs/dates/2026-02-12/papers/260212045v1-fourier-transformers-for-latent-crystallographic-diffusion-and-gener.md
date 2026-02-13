---
layout: default
title: Fourier Transformers for Latent Crystallographic Diffusion and Generative Modeling
---

# Fourier Transformers for Latent Crystallographic Diffusion and Generative Modeling
**arXiv**：[2602.12045v1](https://arxiv.org/abs/2602.12045) · [PDF](https://arxiv.org/pdf/2602.12045.pdf)  
**作者**：Jed A. Duersch, Elohan Veillon, Astrid Klipfel, Adlane Sayede, Zied Bouraoui  

**一句话要点**：提出傅里叶变换器，通过倒易空间表示解决晶体材料生成中的周期性、对称性和原子多样性问题。

**关键词**：晶体材料生成, 傅里叶变换表示, 变压器变分自编码器, 潜在扩散模型, 倒易空间生成, 周期性边界条件

## 3 点简述
- 核心问题：晶体材料生成需处理周期性边界条件、对称性和物理约束，现有方法难以处理大单元细胞和原子多样性。
- 方法要点：使用截断傅里叶变换表示晶体密度，而非直接建模原子坐标，结合变压器变分自编码器和潜在扩散模型生成。
- 实验或效果：在LeMaterial基准上评估重建和潜在扩散，与小单元细胞坐标基线比较无条件生成效果。

## 摘要（原文）

> The discovery of new crystalline materials calls for generative models that handle periodic boundary conditions, crystallographic symmetries, and physical constraints, while scaling to large and structurally diverse unit cells. We propose a reciprocal-space generative pipeline that represents crystals through a truncated Fourier transform of the species-resolved unit-cell density, rather than modeling atomic coordinates directly. This representation is periodicity-native, admits simple algebraic actions of space-group symmetries, and naturally supports variable atomic multiplicities during generation, addressing a common limitation of particle-based approaches. Using only nine Fourier basis functions per spatial dimension, our approach reconstructs unit cells containing up to 108 atoms per chemical species. We instantiate this pipeline with a transformer variational autoencoder over complex-valued Fourier coefficients, and a latent diffusion model that generates in the compressed latent space. We evaluate reconstruction and latent diffusion on the LeMaterial benchmark and compare unconditional generation against coordinate-based baselines in the small-cell regime ($\leq 16$ atoms per unit cell).

