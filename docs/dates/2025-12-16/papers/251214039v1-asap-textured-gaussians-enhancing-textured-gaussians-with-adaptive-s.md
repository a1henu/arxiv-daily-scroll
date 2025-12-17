---
layout: default
title: ASAP-Textured Gaussians: Enhancing Textured Gaussians with Adaptive Sampling and Anisotropic Parameterization
---

# ASAP-Textured Gaussians: Enhancing Textured Gaussians with Adaptive Sampling and Anisotropic Parameterization
**arXiv**：[2512.14039v1](https://arxiv.org/abs/2512.14039) · [PDF](https://arxiv.org/pdf/2512.14039.pdf)  
**作者**：Meng Wei, Cheng Zhang, Jianmin Zheng, Hamid Rezatofighi, Jianfei Cai  

**一句话要点**：提出自适应采样与各向异性参数化以优化纹理高斯方法的内存效率与渲染质量

**关键词**：3D高斯溅射, 纹理参数化, 自适应采样, 各向异性参数, 内存效率, 渲染质量

## 3 点简述
- 核心问题：纹理高斯方法存在采样效率低和参数分配不均，导致内存浪费和过参数化
- 方法要点：基于高斯密度分布进行自适应采样，并根据渲染误差分配各向异性纹理参数
- 实验或效果：显著提升质量效率权衡，以更少纹理参数实现高保真渲染

## 摘要（原文）

> Recent advances have equipped 3D Gaussian Splatting with texture parameterizations to capture spatially varying attributes, improving the performance of both appearance modeling and downstream tasks. However, the added texture parameters introduce significant memory efficiency challenges. Rather than proposing new texture formulations, we take a step back to examine the characteristics of existing textured Gaussian methods and identify two key limitations in common: (1) Textures are typically defined in canonical space, leading to inefficient sampling that wastes textures' capacity on low-contribution regions; and (2) texture parameterization is uniformly assigned across all Gaussians, regardless of their visual complexity, resulting in over-parameterization. In this work, we address these issues through two simple yet effective strategies: adaptive sampling based on the Gaussian density distribution and error-driven anisotropic parameterization that allocates texture resources according to rendering error. Our proposed ASAP Textured Gaussians, short for Adaptive Sampling and Anisotropic Parameterization, significantly improve the quality efficiency tradeoff, achieving high-fidelity rendering with far fewer texture parameters.

