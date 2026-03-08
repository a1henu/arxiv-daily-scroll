---
layout: default
title: Towards 3D Scene Understanding of Gas Plumes in LWIR Hyperspectral Images Using Neural Radiance Fields
---

# Towards 3D Scene Understanding of Gas Plumes in LWIR Hyperspectral Images Using Neural Radiance Fields
**arXiv**：[2603.05473v1](https://arxiv.org/abs/2603.05473) · [PDF](https://arxiv.org/pdf/2603.05473.pdf)  
**作者**：Scout Jarman, Zigfried Hampel-Arias, Adra Carr, Kevin R. Moon  

**一句话要点**：提出基于NeRF的3D场景重建方法，用于LWIR高光谱图像中的气体羽流检测与分析。

**关键词**：神经辐射场, 长波红外高光谱图像, 气体羽流检测, 3D场景重建, 稀疏视图重建, 自适应损失函数

## 3 点简述
- 核心问题：LWIR高光谱图像中气体羽流的3D场景理解，通常图像数量有限且分析孤立。
- 方法要点：结合高光谱NeRF和稀疏视图NeRF技术，引入自适应加权MSE损失，减少训练图像需求。
- 实验或效果：在合成数据集上，使用30张训练图像实现平均PSNR 39.8 dB，气体检测AUC达0.821。

## 摘要（原文）

> Hyperspectral images (HSI) have many applications, ranging from environmental monitoring to national security, and can be used for material detection and identification. Longwave infrared (LWIR) HSI can be used for gas plume detection and analysis. Oftentimes, only a few images of a scene of interest are available and are analyzed individually. The ability to combine information from multiple images into a single, cohesive representation could enhance analysis by providing more context on the scene's geometry and spectral properties. Neural radiance fields (NeRFs) create a latent neural representation of volumetric scene properties that enable novel-view rendering and geometry reconstruction, offering a promising avenue for hyperspectral 3D scene reconstruction. We explore the possibility of using NeRFs to create 3D scene reconstructions from LWIR HSI and demonstrate that the model can be used for the basic downstream analysis task of gas plume detection. The physics-based DIRSIG software suite was used to generate a synthetic multi-view LWIR HSI dataset of a simple facility with a strong sulfur hexafluoride gas plume. Our method, built on the standard Mip-NeRF architecture, combines state-of-the-art methods for hyperspectral NeRFs and sparse-view NeRFs, along with a novel adaptive weighted MSE loss. Our final NeRF method requires around 50% fewer training images than the standard Mip-NeRF and achieves an average PSNR of 39.8 dB with as few as 30 training images. Gas plume detection applied to NeRF-rendered test images using the adaptive coherence estimator achieves an average AUC of 0.821 when compared with detection masks generated from ground-truth test images.

