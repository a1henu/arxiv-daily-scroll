---
layout: default
title: FLOWING: Implicit Neural Flows for Structure-Preserving Morphing
---

# FLOWING: Implicit Neural Flows for Structure-Preserving Morphing
**arXiv**：[2510.09537v1](https://arxiv.org/abs/2510.09537) · [PDF](https://arxiv.org/pdf/2510.09537.pdf)  
**作者**：Arthur Bizzi, Matias Grynberg, Vitor Matias, Daniel Perazzo, João Paulo Lima, Luiz Velho, Nuno Gonçalves, João Pereira, Guilherme Schardong, Tiago Novello  

**一句话要点**：提出FLOWING框架，通过微分向量流实现结构保持的2D图像和3D形状变形

**关键词**：隐式神经表示, 图像变形, 3D形状变形, 微分向量流, 结构保持变形

## 3 点简述
- 核心问题：传统多层感知机变形方法依赖昂贵正则化，导致训练不稳定和特征对齐困难
- 方法要点：将变形建模为微分向量流，确保连续性、可逆性和时间一致性
- 实验或效果：在面部和图像变形等应用中，实现最先进质量并加速收敛

## 摘要（原文）

> Morphing is a long-standing problem in vision and computer graphics,
> requiring a time-dependent warping for feature alignment and a blending for
> smooth interpolation. Recently, multilayer perceptrons (MLPs) have been
> explored as implicit neural representations (INRs) for modeling such
> deformations, due to their meshlessness and differentiability; however,
> extracting coherent and accurate morphings from standard MLPs typically relies
> on costly regularizations, which often lead to unstable training and prevent
> effective feature alignment. To overcome these limitations, we propose FLOWING
> (FLOW morphING), a framework that recasts warping as the construction of a
> differential vector flow, naturally ensuring continuity, invertibility, and
> temporal coherence by encoding structural flow properties directly into the
> network architectures. This flow-centric approach yields principled and stable
> transformations, enabling accurate and structure-preserving morphing of both 2D
> images and 3D shapes. Extensive experiments across a range of applications -
> including face and image morphing, as well as Gaussian Splatting morphing -
> show that FLOWING achieves state-of-the-art morphing quality with faster
> convergence. Code and pretrained models are available at
> http://schardong.github.io/flowing.

