---
layout: default
title: Pixel-to-4D: Camera-Controlled Image-to-Video Generation with Dynamic 3D Gaussians
---

# Pixel-to-4D: Camera-Controlled Image-to-Video Generation with Dynamic 3D Gaussians
**arXiv**：[2601.00678v1](https://arxiv.org/abs/2601.00678) · [PDF](https://arxiv.org/pdf/2601.00678.pdf)  
**作者**：Melonie de Almeida, Daniela Ivanova, Tong Shi, John H. Williamson, Paul Henderson  

**一句话要点**：提出Pixel-to-4D框架，通过动态3D高斯实现单图像到可控相机路径的视频生成

**关键词**：图像到视频生成, 相机控制, 3D高斯表示, 时间一致性, 单图像条件

## 3 点简述
- 核心问题：现有方法在相机控制、时间一致性和几何完整性方面存在不足，限制实际应用
- 方法要点：使用单次前向传递构建3D高斯场景表示并采样物体运动，无需迭代去噪
- 实验或效果：在多个数据集上实现领先的视频质量和推理效率，支持快速相机引导生成

## 摘要（原文）

> Humans excel at forecasting the future dynamics of a scene given just a single image. Video generation models that can mimic this ability are an essential component for intelligent systems. Recent approaches have improved temporal coherence and 3D consistency in single-image-conditioned video generation. However, these methods often lack robust user controllability, such as modifying the camera path, limiting their applicability in real-world applications. Most existing camera-controlled image-to-video models struggle with accurately modeling camera motion, maintaining temporal consistency, and preserving geometric integrity. Leveraging explicit intermediate 3D representations offers a promising solution by enabling coherent video generation aligned with a given camera trajectory. Although these methods often use 3D point clouds to render scenes and introduce object motion in a later stage, this two-step process still falls short in achieving full temporal consistency, despite allowing precise control over camera movement. We propose a novel framework that constructs a 3D Gaussian scene representation and samples plausible object motion, given a single image in a single forward pass. This enables fast, camera-guided video generation without the need for iterative denoising to inject object motion into render frames. Extensive experiments on the KITTI, Waymo, RealEstate10K and DL3DV-10K datasets demonstrate that our method achieves state-of-the-art video quality and inference efficiency. The project page is available at https://melonienimasha.github.io/Pixel-to-4D-Website.

