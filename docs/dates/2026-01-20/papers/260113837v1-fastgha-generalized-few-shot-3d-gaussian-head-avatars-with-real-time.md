---
layout: default
title: FastGHA: Generalized Few-Shot 3D Gaussian Head Avatars with Real-Time Animation
---

# FastGHA: Generalized Few-Shot 3D Gaussian Head Avatars with Real-Time Animation
**arXiv**：[2601.13837v1](https://arxiv.org/abs/2601.13837) · [PDF](https://arxiv.org/pdf/2601.13837.pdf)  
**作者**：Xinya Ji, Sebastian Weiss, Manuel Kansy, Jacek Naruniec, Xun Cao, Barbara Solenthaler, Derek Bradley  

**一句话要点**：提出FastGHA以从少量图像生成高质量3D高斯头化身并支持实时动画

**关键词**：3D高斯化身, 少样本学习, 实时动画, Transformer编码, 几何监督, 前馈生成

## 3 点简述
- 核心问题：现有3D高斯头化身方法依赖多视图捕获或单目视频优化，效率低且难以泛化到未见对象。
- 方法要点：使用前馈网络从输入图像学习像素级高斯表示，基于Transformer融合DINOv3和Stable Diffusion VAE特征，并引入轻量MLP网络预测高斯变形以实现动画。
- 实验或效果：在渲染质量和推理效率上显著优于现有方法，支持实时动态化身动画。

## 摘要（原文）

> Despite recent progress in 3D Gaussian-based head avatar modeling, efficiently generating high fidelity avatars remains a challenge. Current methods typically rely on extensive multi-view capture setups or monocular videos with per-identity optimization during inference, limiting their scalability and ease of use on unseen subjects. To overcome these efficiency drawbacks, we propose \OURS, a feed-forward method to generate high-quality Gaussian head avatars from only a few input images while supporting real-time animation. Our approach directly learns a per-pixel Gaussian representation from the input images, and aggregates multi-view information using a transformer-based encoder that fuses image features from both DINOv3 and Stable Diffusion VAE. For real-time animation, we extend the explicit Gaussian representations with per-Gaussian features and introduce a lightweight MLP-based dynamic network to predict 3D Gaussian deformations from expression codes. Furthermore, to enhance geometric smoothness of the 3D head, we employ point maps from a pre-trained large reconstruction model as geometry supervision. Experiments show that our approach significantly outperforms existing methods in both rendering quality and inference efficiency, while supporting real-time dynamic avatar animation.

