---
layout: default
title: Mesh4D: 4D Mesh Reconstruction and Tracking from Monocular Video
---

# Mesh4D: 4D Mesh Reconstruction and Tracking from Monocular Video
**arXiv**：[2601.05251v1](https://arxiv.org/abs/2601.05251) · [PDF](https://arxiv.org/pdf/2601.05251.pdf)  
**作者**：Zeren Jiang, Chuanxia Zheng, Iro Laina, Diane Larlus, Andrea Vedaldi  

**一句话要点**：提出Mesh4D模型，通过单目视频实现动态物体的4D网格重建与跟踪。

**关键词**：4D重建, 单目视频, 网格变形, 潜在空间, 时空注意力, 扩散模型

## 3 点简述
- 核心问题：从单目视频中重建动态物体的完整3D形状和运动，表示为变形场。
- 方法要点：使用编码器-解码器结构，结合骨骼结构先验和时空注意力，学习紧凑的潜在空间。
- 实验或效果：在重建和新视角合成基准测试中优于先前方法，准确恢复3D形状和变形。

## 摘要（原文）

> We propose Mesh4D, a feed-forward model for monocular 4D mesh reconstruction. Given a monocular video of a dynamic object, our model reconstructs the object's complete 3D shape and motion, represented as a deformation field. Our key contribution is a compact latent space that encodes the entire animation sequence in a single pass. This latent space is learned by an autoencoder that, during training, is guided by the skeletal structure of the training objects, providing strong priors on plausible deformations. Crucially, skeletal information is not required at inference time. The encoder employs spatio-temporal attention, yielding a more stable representation of the object's overall deformation. Building on this representation, we train a latent diffusion model that, conditioned on the input video and the mesh reconstructed from the first frame, predicts the full animation in one shot. We evaluate Mesh4D on reconstruction and novel view synthesis benchmarks, outperforming prior methods in recovering accurate 3D shape and deformation.

