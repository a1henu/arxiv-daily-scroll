---
layout: default
title: SAGS: Self-Adaptive Alias-Free Gaussian Splatting for Dynamic Surgical Endoscopic Reconstruction
---

# SAGS: Self-Adaptive Alias-Free Gaussian Splatting for Dynamic Surgical Endoscopic Reconstruction
**arXiv**：[2510.27318v1](https://arxiv.org/abs/2510.27318) · [PDF](https://arxiv.org/pdf/2510.27318.pdf)  
**作者**：Wenfeng Huang, Xiangyun Liao, Yinling Qian, Hao Liu, Yongming Yang, Wenjing Jia, Qiong Wang  

**一句话要点**：提出自适应性无混叠高斯溅射框架以解决动态内窥镜重建中的混叠和伪影问题

**关键词**：动态内窥镜重建, 高斯溅射, 无混叠渲染, 变形组织建模, 4D变形解码器, 手术可视化

## 3 点简述
- 核心问题：动态内窥镜重建中组织运动导致混叠和伪影，降低可视化质量
- 方法要点：引入注意力驱动动态加权4D变形解码器，结合3D平滑和2D Mip滤波器
- 实验或效果：在EndoNeRF和SCARED基准上，PSNR、SSIM和LPIPS指标优于现有方法

## 摘要（原文）

> Surgical reconstruction of dynamic tissues from endoscopic videos is a
> crucial technology in robot-assisted surgery. The development of Neural
> Radiance Fields (NeRFs) has greatly advanced deformable tissue reconstruction,
> achieving high-quality results from video and image sequences. However,
> reconstructing deformable endoscopic scenes remains challenging due to aliasing
> and artifacts caused by tissue movement, which can significantly degrade
> visualization quality. The introduction of 3D Gaussian Splatting (3DGS) has
> improved reconstruction efficiency by enabling a faster rendering pipeline.
> Nevertheless, existing 3DGS methods often prioritize rendering speed while
> neglecting these critical issues. To address these challenges, we propose SAGS,
> a self-adaptive alias-free Gaussian splatting framework. We introduce an
> attention-driven, dynamically weighted 4D deformation decoder, leveraging 3D
> smoothing filters and 2D Mip filters to mitigate artifacts in deformable tissue
> reconstruction and better capture the fine details of tissue movement.
> Experimental results on two public benchmarks, EndoNeRF and SCARED, demonstrate
> that our method achieves superior performance in all metrics of PSNR, SSIM, and
> LPIPS compared to the state of the art while also delivering better
> visualization quality.

