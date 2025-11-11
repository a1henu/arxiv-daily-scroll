---
layout: default
title: YoNoSplat: You Only Need One Model for Feedforward 3D Gaussian Splatting
---

# YoNoSplat: You Only Need One Model for Feedforward 3D Gaussian Splatting
**arXiv**：[2511.07321v1](https://arxiv.org/abs/2511.07321) · [PDF](https://arxiv.org/pdf/2511.07321.pdf)  
**作者**：Botao Ye, Boqi Chen, Haofei Xu, Daniel Barath, Marc Pollefeys  

**一句话要点**：提出YoNoSplat前馈模型以从任意图像重建高质量3D高斯溅射表示

**关键词**：3D高斯溅射, 相机姿态估计, 前馈模型, 无标定输入, 场景重建

## 3 点简述
- 核心问题：从无结构图像集合快速灵活重建3D场景仍具挑战性
- 方法要点：使用混合训练策略联合学习3D高斯和相机参数，避免训练不稳定
- 实验或效果：在标准基准测试中实现最先进性能，重建100视图仅需2.69秒

## 摘要（原文）

> Fast and flexible 3D scene reconstruction from unstructured image collections
> remains a significant challenge. We present YoNoSplat, a feedforward model that
> reconstructs high-quality 3D Gaussian Splatting representations from an
> arbitrary number of images. Our model is highly versatile, operating
> effectively with both posed and unposed, calibrated and uncalibrated inputs.
> YoNoSplat predicts local Gaussians and camera poses for each view, which are
> aggregated into a global representation using either predicted or provided
> poses. To overcome the inherent difficulty of jointly learning 3D Gaussians and
> camera parameters, we introduce a novel mixing training strategy. This approach
> mitigates the entanglement between the two tasks by initially using
> ground-truth poses to aggregate local Gaussians and gradually transitioning to
> a mix of predicted and ground-truth poses, which prevents both training
> instability and exposure bias. We further resolve the scale ambiguity problem
> by a novel pairwise camera-distance normalization scheme and by embedding
> camera intrinsics into the network. Moreover, YoNoSplat also predicts intrinsic
> parameters, making it feasible for uncalibrated inputs. YoNoSplat demonstrates
> exceptional efficiency, reconstructing a scene from 100 views (at 280x518
> resolution) in just 2.69 seconds on an NVIDIA GH200 GPU. It achieves
> state-of-the-art performance on standard benchmarks in both pose-free and
> pose-dependent settings. Our project page is at
> https://botaoye.github.io/yonosplat/.

