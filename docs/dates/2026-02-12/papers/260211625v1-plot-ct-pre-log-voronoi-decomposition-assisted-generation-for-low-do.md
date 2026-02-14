---
layout: default
title: PLOT-CT: Pre-log Voronoi Decomposition Assisted Generation for Low-dose CT Reconstruction
---

# PLOT-CT: Pre-log Voronoi Decomposition Assisted Generation for Low-dose CT Reconstruction
**arXiv**：[2602.11625v1](https://arxiv.org/abs/2602.11625) · [PDF](https://arxiv.org/pdf/2602.11625.pdf)  
**作者**：Bin Huang, Xun Yu, Yikun Zhang, Yi Zhang, Yang Chen, Qiegen Liu  

**一句话要点**：提出PLOT-CT框架，通过预对数Voronoi分解辅助生成以解决低剂量CT重建中的噪声与数据保真度问题。

**关键词**：低剂量CT重建, 预对数域处理, Voronoi分解, 噪声抑制, 数据保真度, 生成模型

## 3 点简述
- 核心问题：低剂量CT重建面临严重噪声和数据保真度下降，传统方法在图像或后对数投影域操作易受噪声影响。
- 方法要点：在预对数正弦图上应用Voronoi分解，将数据解耦为不同潜在空间中的组件，以增强特征学习能力。
- 实验或效果：在预对数域1e4入射光子水平下，PSNR比传统方法提升2.36dB，达到先进性能。

## 摘要（原文）

> Low-dose computed tomography (LDCT) reconstruction is fundamentally challenged by severe noise and compromised data fidelity under reduced radiation exposure. Most existing methods operate either in the image or post-log projection domain, which fails to fully exploit the rich structural information in pre-log measurements while being highly susceptible to noise. The requisite logarithmic transformation critically amplifies noise within these data, imposing exceptional demands on reconstruction precision. To overcome these challenges, we propose PLOT-CT, a novel framework for Pre-Log vOronoi decomposiTion-assisted CT generation. Our method begins by applying Voronoi decomposition to pre-log sinograms, disentangling the data into distinct underlying components, which are embedded in separate latent spaces. This explicit decomposition significantly enhances the model's capacity to learn discriminative features, directly improving reconstruction accuracy by mitigating noise and preserving information inherent in the pre-log domain. Extensive experiments demonstrate that PLOT-CT achieves state-of-the-art performance, attaining a 2.36dB PSNR improvement over traditional methods at the 1e4 incident photon level in the pre-log domain.

