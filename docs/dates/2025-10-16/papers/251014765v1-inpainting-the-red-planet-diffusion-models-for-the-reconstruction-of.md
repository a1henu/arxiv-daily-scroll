---
layout: default
title: Inpainting the Red Planet: Diffusion Models for the Reconstruction of Martian Environments in Virtual Reality
---

# Inpainting the Red Planet: Diffusion Models for the Reconstruction of Martian Environments in Virtual Reality
**arXiv**：[2510.14765v1](https://arxiv.org/abs/2510.14765) · [PDF](https://arxiv.org/pdf/2510.14765.pdf)  
**作者**：Giuseppe Lorenzo Catalano, Agata Marta Soccini  

**一句话要点**：提出无条件扩散模型以重建火星表面缺失数据

**关键词**：火星表面重建, 扩散模型, 高度图修复, 虚拟现实, 深度学习

## 3 点简述
- 火星高度图存在缺失值，传统插值方法难以保持几何一致性
- 使用无条件扩散模型，在12000张增强高度图上训练，多尺度特征提取
- 相比现有方法，重建精度和感知相似度显著提升

## 摘要（原文）

> Space exploration increasingly relies on Virtual Reality for several tasks,
> such as mission planning, multidisciplinary scientific analysis, and astronaut
> training. A key factor for the reliability of the simulations is having
> accurate 3D representations of planetary terrains. Extraterrestrial heightmaps
> derived from satellite imagery often contain missing values due to acquisition
> and transmission constraints. Mars is among the most studied planets beyond
> Earth, and its extensive terrain datasets make the Martian surface
> reconstruction a valuable task, although many areas remain unmapped. Deep
> learning algorithms can support void-filling tasks; however, whereas Earth's
> comprehensive datasets enables the use of conditional methods, such approaches
> cannot be applied to Mars. Current approaches rely on simpler interpolation
> techniques which, however, often fail to preserve geometric coherence. In this
> work, we propose a method for reconstructing the surface of Mars based on an
> unconditional diffusion model. Training was conducted on an augmented dataset
> of 12000 Martian heightmaps derived from NASA's HiRISE survey. A
> non-homogeneous rescaling strategy captures terrain features across multiple
> scales before resizing to a fixed 128x128 model resolution. We compared our
> method against established void-filling and inpainting techniques, including
> Inverse Distance Weighting, kriging, and Navier-Stokes algorithm, on an
> evaluation set of 1000 samples. Results show that our approach consistently
> outperforms these methods in terms of reconstruction accuracy (4-15% on RMSE)
> and perceptual similarity (29-81% on LPIPS) with the original data.

