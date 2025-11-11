---
layout: default
title: Sparse4DGS: 4D Gaussian Splatting for Sparse-Frame Dynamic Scene Reconstruction
---

# Sparse4DGS: 4D Gaussian Splatting for Sparse-Frame Dynamic Scene Reconstruction
**arXiv**：[2511.07122v1](https://arxiv.org/abs/2511.07122) · [PDF](https://arxiv.org/pdf/2511.07122.pdf)  
**作者**：Changyue Shi, Chuxiao Yang, Xinyuan Hu, Minghao Chen, Wenwen Pan, Yan Yang, Jiajun Ding, Zhou Yu, Jun Yu  

**一句话要点**：提出Sparse4DGS以解决稀疏帧动态场景重建问题

**关键词**：动态场景重建, 高斯溅射, 稀疏帧处理, 纹理感知优化, 4D重建

## 3 点简述
- 核心问题：现有动态重建方法依赖密集帧，稀疏帧下在规范与变形空间失效，尤其在纹理丰富区域。
- 方法要点：引入纹理感知变形正则化和规范优化，通过纹理引导高斯变形与梯度下降。
- 实验或效果：在多个数据集上优于现有动态或少量帧技术，验证稀疏帧重建有效性。

## 摘要（原文）

> Dynamic Gaussian Splatting approaches have achieved remarkable performance
> for 4D scene reconstruction. However, these approaches rely on dense-frame
> video sequences for photorealistic reconstruction. In real-world scenarios, due
> to equipment constraints, sometimes only sparse frames are accessible. In this
> paper, we propose Sparse4DGS, the first method for sparse-frame dynamic scene
> reconstruction. We observe that dynamic reconstruction methods fail in both
> canonical and deformed spaces under sparse-frame settings, especially in areas
> with high texture richness. Sparse4DGS tackles this challenge by focusing on
> texture-rich areas. For the deformation network, we propose Texture-Aware
> Deformation Regularization, which introduces a texture-based depth alignment
> loss to regulate Gaussian deformation. For the canonical Gaussian field, we
> introduce Texture-Aware Canonical Optimization, which incorporates
> texture-based noise into the gradient descent process of canonical Gaussians.
> Extensive experiments show that when taking sparse frames as inputs, our method
> outperforms existing dynamic or few-shot techniques on NeRF-Synthetic,
> HyperNeRF, NeRF-DS, and our iPhone-4D datasets.

