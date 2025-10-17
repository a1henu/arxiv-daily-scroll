---
layout: default
title: Virtually Being: Customizing Camera-Controllable Video Diffusion Models with Multi-View Performance Captures
---

# Virtually Being: Customizing Camera-Controllable Video Diffusion Models with Multi-View Performance Captures
**arXiv**：[2510.14179v1](https://arxiv.org/abs/2510.14179) · [PDF](https://arxiv.org/pdf/2510.14179.pdf)  
**作者**：Yuancheng Xu, Wenqi Xian, Li Ma, Julien Philip, Ahmet Levent Taşel, Yiwei Zhao, Ryan Burgert, Mingming He, Oliver Hermann, Oliver Pilarski, Rahul Garg, Paul Debevec, Ning Yu  

**一句话要点**：提出定制化视频扩散模型框架，实现多视角角色一致性和3D相机控制，用于虚拟制作。

**关键词**：视频扩散模型, 多视角一致性, 3D相机控制, 虚拟制作, 高斯溅射, 视频重光照

## 3 点简述
- 核心问题：视频扩散模型在多视角角色一致性和3D相机控制方面存在不足。
- 方法要点：使用4D高斯溅射和视频重光照模型构建定制数据管道，微调模型。
- 实验或效果：实验显示视频质量、个性化精度、相机控制和光照适应性均提升。

## 摘要（原文）

> We introduce a framework that enables both multi-view character consistency
> and 3D camera control in video diffusion models through a novel customization
> data pipeline. We train the character consistency component with recorded
> volumetric capture performances re-rendered with diverse camera trajectories
> via 4D Gaussian Splatting (4DGS), lighting variability obtained with a video
> relighting model. We fine-tune state-of-the-art open-source video diffusion
> models on this data to provide strong multi-view identity preservation, precise
> camera control, and lighting adaptability. Our framework also supports core
> capabilities for virtual production, including multi-subject generation using
> two approaches: joint training and noise blending, the latter enabling
> efficient composition of independently customized models at inference time; it
> also achieves scene and real-life video customization as well as control over
> motion and spatial layout during customization. Extensive experiments show
> improved video quality, higher personalization accuracy, and enhanced camera
> control and lighting adaptability, advancing the integration of video
> generation into virtual production. Our project page is available at:
> https://eyeline-labs.github.io/Virtually-Being.

