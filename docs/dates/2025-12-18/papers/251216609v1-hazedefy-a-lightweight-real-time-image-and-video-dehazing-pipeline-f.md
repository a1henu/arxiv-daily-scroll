---
layout: default
title: Hazedefy: A Lightweight Real-Time Image and Video Dehazing Pipeline for Practical Deployment
---

# Hazedefy: A Lightweight Real-Time Image and Video Dehazing Pipeline for Practical Deployment
**arXiv**：[2512.16609v1](https://arxiv.org/abs/2512.16609) · [PDF](https://arxiv.org/pdf/2512.16609.pdf)  
**作者**：Ayush Bhavsar  

**一句话要点**：提出Hazedefy轻量级实时去雾管道，用于移动和嵌入式设备增强图像视频可见性。

**关键词**：图像去雾, 视频增强, 轻量级管道, 实时处理, 暗通道先验, 移动部署

## 3 点简述
- 核心问题：针对实时视频和相机流去雾，需在消费级硬件上实现轻量化和可部署性。
- 方法要点：基于暗通道先验和大气散射模型，采用伽马自适应重建、快速传输近似和稳定大气光估计。
- 实验或效果：在真实图像视频上展示，无需GPU加速即可提升可见度和对比度，适合移动应用。

## 摘要（原文）

> This paper introduces Hazedefy, a lightweight and application-focused dehazing pipeline intended for real-time video and live camera feed enhancement. Hazedefy prioritizes computational simplicity and practical deployability on consumer-grade hardware, building upon the Dark Channel Prior (DCP) concept and the atmospheric scattering model. Key elements include gamma-adaptive reconstruction, a fast transmission approximation with lower bounds for numerical stability, a stabilized atmospheric light estimator based on fractional top-pixel averaging, and an optional color balance stage. The pipeline is suitable for mobile and embedded applications, as experimental demonstrations on real-world images and videos show improved visibility and contrast without requiring GPU acceleration.

