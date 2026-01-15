---
layout: default
title: A$^2$TG: Adaptive Anisotropic Textured Gaussians for Efficient 3D Scene Representation
---

# A$^2$TG: Adaptive Anisotropic Textured Gaussians for Efficient 3D Scene Representation
**arXiv**：[2601.09243v1](https://arxiv.org/abs/2601.09243) · [PDF](https://arxiv.org/pdf/2601.09243.pdf)  
**作者**：Sheng-Chi Hsu, Ting-Yu Yen, Shih-Hsuan Hung, Hung-Kuo Chu  

**一句话要点**：提出自适应各向异性纹理高斯以高效表示3D场景

**关键词**：3D场景表示, 高斯泼溅, 纹理优化, 自适应分配, 内存效率

## 3 点简述
- 问题：现有纹理高斯方法使用固定方形纹理，导致内存效率低且适应性有限。
- 方法：引入各向异性纹理，通过梯度引导自适应规则动态确定纹理分辨率和长宽比。
- 效果：在多个基准数据集上验证，显著降低内存消耗并提升图像质量。

## 摘要（原文）

> Gaussian Splatting has emerged as a powerful representation for high-quality, real-time 3D scene rendering. While recent works extend Gaussians with learnable textures to enrich visual appearance, existing approaches allocate a fixed square texture per primitive, leading to inefficient memory usage and limited adaptability to scene variability. In this paper, we introduce adaptive anisotropic textured Gaussians (A$^2$TG), a novel representation that generalizes textured Gaussians by equipping each primitive with an anisotropic texture. Our method employs a gradient-guided adaptive rule to jointly determine texture resolution and aspect ratio, enabling non-uniform, detail-aware allocation that aligns with the anisotropic nature of Gaussian splats. This design significantly improves texture efficiency, reducing memory consumption while enhancing image quality. Experiments on multiple benchmark datasets demonstrate that A TG consistently outperforms fixed-texture Gaussian Splatting methods, achieving comparable rendering fidelity with substantially lower memory requirements.

