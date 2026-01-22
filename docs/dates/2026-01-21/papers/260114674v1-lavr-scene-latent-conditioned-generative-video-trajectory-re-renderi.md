---
layout: default
title: LaVR: Scene Latent Conditioned Generative Video Trajectory Re-Rendering using Large 4D Reconstruction Models
---

# LaVR: Scene Latent Conditioned Generative Video Trajectory Re-Rendering using Large 4D Reconstruction Models
**arXiv**：[2601.14674v1](https://arxiv.org/abs/2601.14674) · [PDF](https://arxiv.org/pdf/2601.14674.pdf)  
**作者**：Mingyang Xie, Numair Khan, Tianfu Wang, Naina Dhingra, Seonghyeon Nam, Haitao Yang, Zhuo Hui, Christopher Metzler, Andrea Vedaldi, Hamed Pirsiavash, Lei Luo  

**一句话要点**：提出LaVR方法，利用大型4D重建模型的隐式几何知识进行视频重渲染，以解决几何条件不足或依赖显式重建的问题。

**关键词**：视频重渲染, 4D重建模型, 隐式几何知识, 扩散模型, 相机轨迹生成, 潜在空间条件化

## 3 点简述
- 核心问题：现有视频重渲染方法在几何无条件模型中缺乏空间感知，导致视角变化下的漂移和变形；几何条件模型则依赖估计深度和显式重建，易受深度不准确和校准误差影响。
- 方法要点：通过大型4D重建模型的隐式几何知识嵌入潜在空间，结合源相机姿态，条件化视频生成过程，提供灵活表示以正则化误差。
- 实验或效果：在视频重渲染任务上实现未知性能，项目网页已公开。

## 摘要（原文）

> Given a monocular video, the goal of video re-rendering is to generate views of the scene from a novel camera trajectory. Existing methods face two distinct challenges. Geometrically unconditioned models lack spatial awareness, leading to drift and deformation under viewpoint changes. On the other hand, geometrically-conditioned models depend on estimated depth and explicit reconstruction, making them susceptible to depth inaccuracies and calibration errors.
>   We propose to address these challenges by using the implicit geometric knowledge embedded in the latent space of a large 4D reconstruction model to condition the video generation process. These latents capture scene structure in a continuous space without explicit reconstruction. Therefore, they provide a flexible representation that allows the pretrained diffusion prior to regularize errors more effectively. By jointly conditioning on these latents and source camera poses, we demonstrate that our model achieves state-of-the-art results on the video re-rendering task. Project webpage is https://lavr-4d-scene-rerender.github.io/

