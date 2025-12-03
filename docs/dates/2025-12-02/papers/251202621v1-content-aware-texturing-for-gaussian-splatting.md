---
layout: default
title: Content-Aware Texturing for Gaussian Splatting
---

# Content-Aware Texturing for Gaussian Splatting
**arXiv**：[2512.02621v1](https://arxiv.org/abs/2512.02621) · [PDF](https://arxiv.org/pdf/2512.02621.pdf)  
**作者**：Panagiotis Papantonakis, Georgios Kopanas, Fredo Durand, George Drettakis  

**一句话要点**：提出内容感知纹理映射方法，以优化高斯泼溅中的外观表示效率。

**关键词**：高斯泼溅, 纹理映射, 3D重建, 实时渲染, 自适应优化

## 3 点简述
- 核心问题：高斯泼溅中细节外观需大量小高斯基元，导致参数浪费。
- 方法要点：引入自适应纹理映射，根据图像采样频率和内容调整纹理分辨率。
- 实验或效果：在图像质量和参数数量上优于其他纹理化高斯基元方案。

## 摘要（原文）

> Gaussian Splatting has become the method of choice for 3D reconstruction and real-time rendering of captured real scenes. However, fine appearance details need to be represented as a large number of small Gaussian primitives, which can be wasteful when geometry and appearance exhibit different frequency characteristics.
>   Inspired by the long tradition of texture mapping, we propose to use texture to represent detailed appearance where possible. Our main focus is to incorporate per-primitive texture maps that adapt to the scene in a principled manner during Gaussian Splatting optimization. We do this by proposing a new appearance representation for 2D Gaussian primitives with textures where the size of a texel is bounded by the image sampling frequency and adapted to the content of the input images. We achieve this by adaptively upscaling or downscaling the texture resolution during optimization. In addition, our approach enables control of the number of primitives during optimization based on texture resolution. We show that our approach performs favorably in image quality and total number of parameters used compared to alternative solutions for textured Gaussian primitives. Project page: https://repo-sam.inria.fr/nerphys/gs-texturing/

