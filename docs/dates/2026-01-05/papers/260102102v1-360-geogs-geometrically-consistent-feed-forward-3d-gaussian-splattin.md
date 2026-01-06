---
layout: default
title: 360-GeoGS: Geometrically Consistent Feed-Forward 3D Gaussian Splatting Reconstruction for 360 Images
---

# 360-GeoGS: Geometrically Consistent Feed-Forward 3D Gaussian Splatting Reconstruction for 360 Images
**arXiv**：[2601.02102v1](https://arxiv.org/abs/2601.02102) · [PDF](https://arxiv.org/pdf/2601.02102.pdf)  
**作者**：Jiaqi Yao, Zhongmiao Yan, Jingyi Xu, Songpengcheng Xia, Yan Xiang, Ling Pei  

**一句话要点**：提出360-GeoGS框架，通过深度-法向几何正则化提升360图像3D高斯溅射重建的几何一致性。

**关键词**：3D高斯溅射, 几何一致性, 360图像重建, 深度-法向正则化, 前馈框架

## 3 点简述
- 核心问题：现有前馈3D高斯溅射方法注重视觉质量，但几何一致性不足，影响表面重建精度。
- 方法要点：引入深度-法向几何正则化，耦合渲染深度梯度与法向信息，监督高斯旋转、尺度和位置。
- 实验或效果：实验显示，在保持高渲染质量的同时，显著提升几何一致性，适用于空间感知任务。

## 摘要（原文）

> 3D scene reconstruction is fundamental for spatial intelligence applications such as AR, robotics, and digital twins. Traditional multi-view stereo struggles with sparse viewpoints or low-texture regions, while neural rendering approaches, though capable of producing high-quality results, require per-scene optimization and lack real-time efficiency. Explicit 3D Gaussian Splatting (3DGS) enables efficient rendering, but most feed-forward variants focus on visual quality rather than geometric consistency, limiting accurate surface reconstruction and overall reliability in spatial perception tasks. This paper presents a novel feed-forward 3DGS framework for 360 images, capable of generating geometrically consistent Gaussian primitives while maintaining high rendering quality. A Depth-Normal geometric regularization is introduced to couple rendered depth gradients with normal information, supervising Gaussian rotation, scale, and position to improve point cloud and surface accuracy. Experimental results show that the proposed method maintains high rendering quality while significantly improving geometric consistency, providing an effective solution for 3D reconstruction in spatial perception tasks.

