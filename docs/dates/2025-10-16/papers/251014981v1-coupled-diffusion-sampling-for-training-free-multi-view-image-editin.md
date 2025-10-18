---
layout: default
title: Coupled Diffusion Sampling for Training-Free Multi-View Image Editing
---

# Coupled Diffusion Sampling for Training-Free Multi-View Image Editing
**arXiv**：[2510.14981v1](https://arxiv.org/abs/2510.14981) · [PDF](https://arxiv.org/pdf/2510.14981.pdf)  
**作者**：Hadi Alzayer, Yunzhi Zhang, Chen Geng, Jia-Bin Huang, Jiajun Wu  

**一句话要点**：提出耦合扩散采样方法，实现免训练的多视角图像编辑一致性

**关键词**：多视角图像编辑, 扩散采样, 免训练方法, 图像一致性, 隐式3D正则化

## 3 点简述
- 核心问题：预训练2D编辑模型在多视角图像中缺乏跨视角一致性
- 方法要点：通过耦合扩散采样，约束生成图像序列符合多视角分布
- 实验或效果：在三个多视角编辑任务中验证有效性和通用性

## 摘要（原文）

> We present an inference-time diffusion sampling method to perform multi-view
> consistent image editing using pre-trained 2D image editing models. These
> models can independently produce high-quality edits for each image in a set of
> multi-view images of a 3D scene or object, but they do not maintain consistency
> across views. Existing approaches typically address this by optimizing over
> explicit 3D representations, but they suffer from a lengthy optimization
> process and instability under sparse view settings. We propose an implicit 3D
> regularization approach by constraining the generated 2D image sequences to
> adhere to a pre-trained multi-view image distribution. This is achieved through
> coupled diffusion sampling, a simple diffusion sampling technique that
> concurrently samples two trajectories from both a multi-view image distribution
> and a 2D edited image distribution, using a coupling term to enforce the
> multi-view consistency among the generated images. We validate the
> effectiveness and generality of this framework on three distinct multi-view
> image editing tasks, demonstrating its applicability across various model
> architectures and highlighting its potential as a general solution for
> multi-view consistent editing.

