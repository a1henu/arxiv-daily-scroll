---
layout: default
title: 3D CBCT Artefact Removal Using Perpendicular Score-Based Diffusion Models
---

# 3D CBCT Artefact Removal Using Perpendicular Score-Based Diffusion Models
**arXiv**：[2603.06300v1](https://arxiv.org/abs/2603.06300) · [PDF](https://arxiv.org/pdf/2603.06300.pdf)  
**作者**：Susanne Schaub, Florentin Bieder, Matheus L. Oliveira, Yulan Wang, Dorothea Dagassan-Berndt, Michael M. Bornstein, Philippe C. Cattin  

**一句话要点**：提出基于垂直分数扩散模型的3D CBCT植入物修复方法，以解决牙科成像中的伪影问题。

**关键词**：CBCT伪影去除, 3D植入物修复, 分数扩散模型, 牙科成像, 投影域处理

## 3 点简述
- 核心问题：CBCT成像中高密度植入物导致伪影，影响图像质量和诊断准确性。
- 方法要点：使用两个2D分数扩散模型在投影域训练，结合采样方案建模3D投影序列分布。
- 实验或效果：方法能生成高质量、伪影减少的3D CBCT图像，提升临床成像效果。

## 摘要（原文）

> Cone-beam computed tomography (CBCT) is a widely used 3D imaging technique in dentistry, offering high-resolution images while minimising radiation exposure for patients. However, CBCT is highly susceptible to artefacts arising from high-density objects such as dental implants, which can compromise image quality and diagnostic accuracy. To reduce artefacts, implant inpainting in the sequence of projections plays a crucial role in many artefact reduction approaches. Recently, diffusion models have achieved state-of-the-art results in image generation and have widely been applied to image inpainting tasks. However, to our knowledge, existing diffusion-based methods for implant inpainting operate on independent 2D projections. This approach neglects the correlations among individual projections, resulting in inconsistencies in the reconstructed images. To address this, we propose a 3D dental implant inpainting approach based on perpendicular score-based diffusion models, each trained in two different planes and operating in the projection domain. The 3D distribution of the projection series is modelled by combining the two 2D score-based diffusion models in the sampling scheme. Our results demonstrate the method's effectiveness in producing high-quality, artefact-reduced 3D CBCT images, making it a promising solution for improving clinical imaging.

