---
layout: default
title: MoTDiff: High-resolution Motion Trajectory estimation from a single blurred image using Diffusion models
---

# MoTDiff: High-resolution Motion Trajectory estimation from a single blurred image using Diffusion models
**arXiv**：[2510.26173v1](https://arxiv.org/abs/2510.26173) · [PDF](https://arxiv.org/pdf/2510.26173.pdf)  
**作者**：Wontae Choi, Jaelin Lee, Hyung Sup Yun, Byeungwoo Jeon, Il Yong Chun  

**一句话要点**：提出MoTDiff框架，使用扩散模型从单张模糊图像估计高分辨率运动轨迹。

**关键词**：运动轨迹估计, 扩散模型, 盲图像去模糊, 编码曝光摄影, 高分辨率估计

## 3 点简述
- 核心问题：现有从单张模糊图像提取运动信息的方法质量低，轨迹粗糙且不准确。
- 方法要点：采用条件扩散框架，以多尺度特征图为条件，结合新训练方法提升轨迹精度。
- 实验或效果：在盲图像去模糊和编码曝光摄影应用中优于现有先进方法。

## 摘要（原文）

> Accurate estimation of motion information is crucial in diverse computational
> imaging and computer vision applications. Researchers have investigated various
> methods to extract motion information from a single blurred image, including
> blur kernels and optical flow. However, existing motion representations are
> often of low quality, i.e., coarse-grained and inaccurate. In this paper, we
> propose the first high-resolution (HR) Motion Trajectory estimation framework
> using Diffusion models (MoTDiff). Different from existing motion
> representations, we aim to estimate an HR motion trajectory with high-quality
> from a single motion-blurred image. The proposed MoTDiff consists of two key
> components: 1) a new conditional diffusion framework that uses multi-scale
> feature maps extracted from a single blurred image as a condition, and 2) a new
> training method that can promote precise identification of a fine-grained
> motion trajectory, consistent estimation of overall shape and position of a
> motion path, and pixel connectivity along a motion trajectory. Our experiments
> demonstrate that the proposed MoTDiff can outperform state-of-the-art methods
> in both blind image deblurring and coded exposure photography applications.

