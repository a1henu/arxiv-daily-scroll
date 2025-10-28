---
layout: default
title: UGAE: Unified Geometry and Attribute Enhancement for G-PCC Compressed Point Clouds
---

# UGAE: Unified Geometry and Attribute Enhancement for G-PCC Compressed Point Clouds
**arXiv**：[2510.23009v1](https://arxiv.org/abs/2510.23009) · [PDF](https://arxiv.org/pdf/2510.23009.pdf)  
**作者**：Pan Zhao, Hui Yuan, Chongzhen Tian, Tian Guo, Raouf Hamzaoui, Zhigeng Pan  

**一句话要点**：提出UGAE框架以增强G-PCC压缩点云的几何结构和属性质量

**关键词**：点云压缩, 几何增强, 属性增强, Transformer网络, G-PCC标准, 感知质量

## 3 点简述
- 点云有损压缩导致几何结构和属性信息不可逆失真
- UGAE包含PoGE、PAE和PoAE组件，分别处理几何重建、预属性增强和后属性增强
- 在8iVFB等数据集上，几何和属性质量显著提升，BD-PSNR增益和比特率节省突出

## 摘要（原文）

> Lossy compression of point clouds reduces storage and transmission costs;
> however, it inevitably leads to irreversible distortion in geometry structure
> and attribute information. To address these issues, we propose a unified
> geometry and attribute enhancement (UGAE) framework, which consists of three
> core components: post-geometry enhancement (PoGE), pre-attribute enhancement
> (PAE), and post-attribute enhancement (PoAE). In PoGE, a Transformer-based
> sparse convolutional U-Net is used to reconstruct the geometry structure with
> high precision by predicting voxel occupancy probabilities. Building on the
> refined geometry structure, PAE introduces an innovative enhanced
> geometry-guided recoloring strategy, which uses a detail-aware K-Nearest
> Neighbors (DA-KNN) method to achieve accurate recoloring and effectively
> preserve high-frequency details before attribute compression. Finally, at the
> decoder side, PoAE uses an attribute residual prediction network with a
> weighted mean squared error (W-MSE) loss to enhance the quality of
> high-frequency regions while maintaining the fidelity of low-frequency regions.
> UGAE significantly outperformed existing methods on three benchmark datasets:
> 8iVFB, Owlii, and MVUB. Compared to the latest G-PCC test model (TMC13v29),
> UGAE achieved an average BD-PSNR gain of 9.98 dB and 90.98% BD-bitrate savings
> for geometry under the D1 metric, as well as a 3.67 dB BD-PSNR improvement with
> 56.88% BD-bitrate savings for attributes on the Y component. Additionally, it
> improved perceptual quality significantly.

