---
layout: default
title: DeCo-VAE: Learning Compact Latents for Video Reconstruction via Decoupled Representation
---

# DeCo-VAE: Learning Compact Latents for Video Reconstruction via Decoupled Representation
**arXiv**：[2511.14530v1](https://arxiv.org/abs/2511.14530) · [PDF](https://arxiv.org/pdf/2511.14530.pdf)  
**作者**：Xiangchen Yin, Jiahui Yuan, Zhangchi Hu, Wenzhang Sun, Jie Chen, Xiaozhen Qiao, Hao Li, Xiaoyan Sun  

**一句话要点**：提出DeCo-VAE通过解耦表示学习紧凑潜在变量以改进视频重建

**关键词**：视频变分自编码器, 解耦表示学习, 紧凑潜在变量, 视频重建, 3D解码器

## 3 点简述
- 现有视频VAE忽略帧间相似性，导致潜在建模冗余
- 将视频解耦为关键帧、运动和残差组件，并学习专用潜在表示
- 实验显示DeCo-VAE在视频重建性能上优于现有方法

## 摘要（原文）

> Existing video Variational Autoencoders (VAEs) generally overlook the similarity between frame contents, leading to redundant latent modeling. In this paper, we propose decoupled VAE (DeCo-VAE) to achieve compact latent representation. Instead of encoding RGB pixels directly, we decompose video content into distinct components via explicit decoupling: keyframe, motion and residual, and learn dedicated latent representation for each. To avoid cross-component interference, we design dedicated encoders for each decoupled component and adopt a shared 3D decoder to maintain spatiotemporal consistency during reconstruction. We further utilize a decoupled adaptation strategy that freezes partial encoders while training the others sequentially, ensuring stable training and accurate learning of both static and dynamic features. Extensive quantitative and qualitative experiments demonstrate that DeCo-VAE achieves superior video reconstruction performance.

