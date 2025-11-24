---
layout: default
title: OmniLens++: Blind Lens Aberration Correction via Large LensLib Pre-Training and Latent PSF Representation
---

# OmniLens++: Blind Lens Aberration Correction via Large LensLib Pre-Training and Latent PSF Representation
**arXiv**：[2511.17126v1](https://arxiv.org/abs/2511.17126) · [PDF](https://arxiv.org/pdf/2511.17126.pdf)  
**作者**：Qi Jiang, Xiaolong Qian, Yao Gao, Lei Sun, Kailun Yang, Zhonghua Yi, Wenyong Li, Ming-Hsuan Yang, Luc Van Gool, Kaiwei Wang  

**一句话要点**：提出OmniLens++框架以解决盲镜头像差校正的泛化问题

**关键词**：盲镜头像差校正, 镜头库预训练, 潜在PSF表示, 光学退化建模, 泛化能力提升

## 3 点简述
- 核心问题：现有方法在数据扩展和光学退化先验利用上泛化能力不足
- 方法要点：扩展镜头库数据多样性并引入潜在PSF表示作为先验指导
- 实验或效果：在真实和合成镜头库上展示领先的盲像差校正性能

## 摘要（原文）

> Emerging deep-learning-based lens library pre-training (LensLib-PT) pipeline offers a new avenue for blind lens aberration correction by training a universal neural network, demonstrating strong capability in handling diverse unknown optical degradations. This work proposes the OmniLens++ framework, which resolves two challenges that hinder the generalization ability of existing pipelines: the difficulty of scaling data and the absence of prior guidance characterizing optical degradation. To improve data scalability, we expand the design specifications to increase the degradation diversity of the lens source, and we sample a more uniform distribution by quantifying the spatial-variation patterns and severity of optical degradation. In terms of model design, to leverage the Point Spread Functions (PSFs), which intuitively describe optical degradation, as guidance in a blind paradigm, we propose the Latent PSF Representation (LPR). The VQVAE framework is introduced to learn latent features of LensLib's PSFs, which is assisted by modeling the optical degradation process to constrain the learning of degradation priors. Experiments on diverse aberrations of real-world lenses and synthetic LensLib show that OmniLens++ exhibits state-of-the-art generalization capacity in blind aberration correction. Beyond performance, the AODLibpro is verified as a scalable foundation for more effective training across diverse aberrations, and LPR can further tap the potential of large-scale LensLib. The source code and datasets will be made publicly available at https://github.com/zju-jiangqi/OmniLens2.

