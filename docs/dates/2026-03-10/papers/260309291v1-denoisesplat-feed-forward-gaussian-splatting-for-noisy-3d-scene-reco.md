---
layout: default
title: DenoiseSplat: Feed-Forward Gaussian Splatting for Noisy 3D Scene Reconstruction
---

# DenoiseSplat: Feed-Forward Gaussian Splatting for Noisy 3D Scene Reconstruction
**arXiv**：[2603.09291v1](https://arxiv.org/abs/2603.09291) · [PDF](https://arxiv.org/pdf/2603.09291.pdf)  
**作者**：Fuzhen Jiang, Zhuoran Li, Yinlin Zhang  

**一句话要点**：提出DenoiseSplat以解决噪声多视图图像下的3D场景重建问题

**关键词**：3D场景重建, 高斯泼溅, 噪声鲁棒性, 多视图图像, 前馈网络, 无3D真值训练

## 3 点简述
- 核心问题：现有NeRF和3D高斯泼溅方法在噪声输入下性能下降
- 方法要点：使用前馈式3D高斯泼溅，仅用干净2D渲染作为监督训练
- 实验或效果：在RE10K噪声基准上，PSNR/SSIM和LPIPS指标优于基线方法

## 摘要（原文）

> 3D scene reconstruction and novel-view synthesis are fundamental for VR, robotics, and content creation. However, most NeRF and 3D Gaussian Splatting pipelines assume clean inputs and degrade under real noise and artifacts. We therefore propose DenoiseSplat, a feed-forward 3D Gaussian splatting method for noisy multi-view images. We build a large-scale, scene-consistent noisy--clean benchmark on RE10K by injecting Gaussian, Poisson, speckle, and salt-and-pepper noise with controlled intensities. With a lightweight MVSplat-style feed-forward backbone, we train end-to-end using only clean 2D renderings as supervision and no 3D ground truth. On noisy RE10K, DenoiseSplat outperforms vanilla MVSplat and a strong two-stage baseline (IDF + MVSplat) in PSNR/SSIM and LPIPS across noise types and levels.

