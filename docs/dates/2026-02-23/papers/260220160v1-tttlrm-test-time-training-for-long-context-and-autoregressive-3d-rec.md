---
layout: default
title: tttLRM: Test-Time Training for Long Context and Autoregressive 3D Reconstruction
---

# tttLRM: Test-Time Training for Long Context and Autoregressive 3D Reconstruction
**arXiv**：[2602.20160v1](https://arxiv.org/abs/2602.20160) · [PDF](https://arxiv.org/pdf/2602.20160.pdf)  
**作者**：Chen Wang, Hao Tan, Wang Yifan, Zhiqin Chen, Yuheng Liu, Kalyan Sunkavalli, Sai Bi, Lingjie Liu, Yiwei Hu  

**一句话要点**：提出tttLRM，通过测试时训练层实现长上下文自回归3D重建，计算复杂度线性。

**关键词**：3D重建, 测试时训练, 长上下文处理, 自回归模型, 高斯溅射, 在线学习

## 3 点简述
- 核心问题：传统3D重建模型在处理长上下文图像序列时计算复杂度高，难以实现高效自回归重建。
- 方法要点：引入测试时训练层，将多图像观测压缩为快速权重，形成隐式3D表示，可解码为高斯溅射等显式格式。
- 实验或效果：在物体和场景上优于现有方法，支持在线渐进重建，预训练视图合成任务提升重建质量和收敛速度。

## 摘要（原文）

> We propose tttLRM, a novel large 3D reconstruction model that leverages a Test-Time Training (TTT) layer to enable long-context, autoregressive 3D reconstruction with linear computational complexity, further scaling the model's capability. Our framework efficiently compresses multiple image observations into the fast weights of the TTT layer, forming an implicit 3D representation in the latent space that can be decoded into various explicit formats, such as Gaussian Splats (GS) for downstream applications. The online learning variant of our model supports progressive 3D reconstruction and refinement from streaming observations. We demonstrate that pretraining on novel view synthesis tasks effectively transfers to explicit 3D modeling, resulting in improved reconstruction quality and faster convergence. Extensive experiments show that our method achieves superior performance in feedforward 3D Gaussian reconstruction compared to state-of-the-art approaches on both objects and scenes.

