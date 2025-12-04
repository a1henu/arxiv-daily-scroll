---
layout: default
title: Tada-DIP: Input-adaptive Deep Image Prior for One-shot 3D Image Reconstruction
---

# Tada-DIP: Input-adaptive Deep Image Prior for One-shot 3D Image Reconstruction
**arXiv**：[2512.03962v1](https://arxiv.org/abs/2512.03962) · [PDF](https://arxiv.org/pdf/2512.03962.pdf)  
**作者**：Evan Bell, Shijun Liang, Ismail Alkhouri, Saiprasad Ravishankar  

**一句话要点**：提出Tada-DIP方法，通过输入自适应和去噪正则化解决3D图像重建中的过拟合问题。

**关键词**：3D图像重建, Deep Image Prior, 输入自适应, 去噪正则化, 稀疏视图CT

## 3 点简述
- 核心问题：Deep Image Prior在3D图像重建中应用有限，易过拟合。
- 方法要点：结合输入自适应和去噪正则化，提升3D重建质量。
- 实验或效果：在稀疏视图X射线CT重建中优于无训练数据基线，性能接近监督网络。

## 摘要（原文）

> Deep Image Prior (DIP) has recently emerged as a promising one-shot neural-network based image reconstruction method. However, DIP has seen limited application to 3D image reconstruction problems. In this work, we introduce Tada-DIP, a highly effective and fully 3D DIP method for solving 3D inverse problems. By combining input-adaptation and denoising regularization, Tada-DIP produces high-quality 3D reconstructions while avoiding the overfitting phenomenon that is common in DIP. Experiments on sparse-view X-ray computed tomography reconstruction validate the effectiveness of the proposed method, demonstrating that Tada-DIP produces much better reconstructions than training-data-free baselines and achieves reconstruction performance on par with a supervised network trained using a large dataset with fully-sampled volumes.

