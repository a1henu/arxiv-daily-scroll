---
layout: default
title: Moving Light Adaptive Colonoscopy Reconstruction via Illumination-Attenuation-Aware 3D Gaussian Splatting
---

# Moving Light Adaptive Colonoscopy Reconstruction via Illumination-Attenuation-Aware 3D Gaussian Splatting
**arXiv**：[2510.18739v1](https://arxiv.org/abs/2510.18739) · [PDF](https://arxiv.org/pdf/2510.18739.pdf)  
**作者**：Hao Wang, Ying Zhou, Haoyu Zhao, Rui Wang, Qiang Hu, Xing Zhang, Qiang Li, Zhiwei Wang  

**一句话要点**：提出ColIAGS以解决结肠镜动态光照下的3D重建问题

**关键词**：3D高斯泼溅, 结肠镜重建, 光照衰减建模, 视图合成, 几何重建

## 3 点简述
- 核心问题：传统3DGS假设静态光照，不兼容结肠镜动态光源导致的亮度变化
- 方法要点：引入改进外观建模，结合光照衰减因子和高维视图嵌入
- 实验或效果：在标准基准上实现优越渲染保真度和深度MSE降低

## 摘要（原文）

> 3D Gaussian Splatting (3DGS) has emerged as a pivotal technique for real-time
> view synthesis in colonoscopy, enabling critical applications such as virtual
> colonoscopy and lesion tracking. However, the vanilla 3DGS assumes static
> illumination and that observed appearance depends solely on viewing angle,
> which causes incompatibility with the photometric variations in colonoscopic
> scenes induced by dynamic light source/camera. This mismatch forces most 3DGS
> methods to introduce structure-violating vaporous Gaussian blobs between the
> camera and tissues to compensate for illumination attenuation, ultimately
> degrading the quality of 3D reconstructions. Previous works only consider the
> illumination attenuation caused by light distance, ignoring the physical
> characters of light source and camera. In this paper, we propose ColIAGS, an
> improved 3DGS framework tailored for colonoscopy. To mimic realistic appearance
> under varying illumination, we introduce an Improved Appearance Modeling with
> two types of illumination attenuation factors, which enables Gaussians to adapt
> to photometric variations while preserving geometry accuracy. To ensure the
> geometry approximation condition of appearance modeling, we propose an Improved
> Geometry Modeling using high-dimensional view embedding to enhance Gaussian
> geometry attribute prediction. Furthermore, another cosine embedding input is
> leveraged to generate illumination attenuation solutions in an implicit manner.
> Comprehensive experimental results on standard benchmarks demonstrate that our
> proposed ColIAGS achieves the dual capabilities of novel view synthesis and
> accurate geometric reconstruction. It notably outperforms other
> state-of-the-art methods by achieving superior rendering fidelity while
> significantly reducing Depth MSE. Code will be available.

