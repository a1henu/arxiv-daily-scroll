---
layout: default
title: Physics Encoded Spatial and Temporal Generative Adversarial Network for Tropical Cyclone Image Super-resolution
---

# Physics Encoded Spatial and Temporal Generative Adversarial Network for Tropical Cyclone Image Super-resolution
**arXiv**：[2602.17277v1](https://arxiv.org/abs/2602.17277) · [PDF](https://arxiv.org/pdf/2602.17277.pdf)  
**作者**：Ruoyi Zhang, Jiawei Yuan, Lujia Ye, Runling Yu, Liling Zhao  

**一句话要点**：提出物理编码时空生成对抗网络以提升热带气旋图像超分辨率，增强物理保真度。

**关键词**：热带气旋图像超分辨率, 物理编码生成对抗网络, 时空生成模型, 涡度方程近似, 双判别器框架

## 3 点简述
- 现有超分辨率方法忽略云运动物理规律，导致重建图像缺乏气象合理性。
- 设计解耦生成器，通过PhyCell模块编码涡度方程近似物理动态，分离物理动态与视觉纹理。
- 在Digital Typhoon数据集上实验，4倍上采样显示结构保真度和感知质量优于现有方法。

## 摘要（原文）

> High-resolution satellite imagery is indispensable for tracking the genesis, intensification, and trajectory of tropical cyclones (TCs). However, existing deep learning-based super-resolution (SR) methods often treat satellite image sequences as generic videos, neglecting the underlying atmospheric physical laws governing cloud motion. To address this, we propose a Physics Encoded Spatial and Temporal Generative Adversarial Network (PESTGAN) for TC image super-resolution. Specifically, we design a disentangled generator architecture incorporating a PhyCell module, which approximates the vorticity equation via constrained convolutions and encodes the resulting approximate physical dynamics as implicit latent representations to separate physical dynamics from visual textures. Furthermore, a dual-discriminator framework is introduced, employing a temporal discriminator to enforce motion consistency alongside spatial realism. Experiments on the Digital Typhoon dataset for 4$\times$ upscaling demonstrate that PESTGAN establishes a better performance in structural fidelity and perceptual quality. While maintaining competitive pixel-wise accuracy compared to existing approaches, our method significantly excels in reconstructing meteorologically plausible cloud structures with superior physical fidelity.

