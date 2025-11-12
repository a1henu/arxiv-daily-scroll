---
layout: default
title: SkelSplat: Robust Multi-view 3D Human Pose Estimation with Differentiable Gaussian Rendering
---

# SkelSplat: Robust Multi-view 3D Human Pose Estimation with Differentiable Gaussian Rendering
**arXiv**：[2511.08294v1](https://arxiv.org/abs/2511.08294) · [PDF](https://arxiv.org/pdf/2511.08294.pdf)  
**作者**：Laura Bragagnolo, Leonardo Barcellona, Stefano Ghidoni  

**一句话要点**：提出SkelSplat框架，基于可微高斯渲染解决多视角3D人体姿态估计泛化问题

**关键词**：多视角3D人体姿态估计, 可微高斯渲染, 骨架建模, 无监督学习, 泛化性提升

## 3 点简述
- 核心问题：多视角3D人体姿态估计方法依赖标注数据，泛化性差
- 方法要点：使用3D高斯骨架建模姿态，通过可微渲染融合任意视角，无需3D真值监督
- 实验效果：在Human3.6M和CMU数据集上优于无3D真值方法，跨数据集误差降低达47.8%

## 摘要（原文）

> Accurate 3D human pose estimation is fundamental for applications such as augmented reality and human-robot interaction. State-of-the-art multi-view methods learn to fuse predictions across views by training on large annotated datasets, leading to poor generalization when the test scenario differs. To overcome these limitations, we propose SkelSplat, a novel framework for multi-view 3D human pose estimation based on differentiable Gaussian rendering. Human pose is modeled as a skeleton of 3D Gaussians, one per joint, optimized via differentiable rendering to enable seamless fusion of arbitrary camera views without 3D ground-truth supervision. Since Gaussian Splatting was originally designed for dense scene reconstruction, we propose a novel one-hot encoding scheme that enables independent optimization of human joints. SkelSplat outperforms approaches that do not rely on 3D ground truth in Human3.6M and CMU, while reducing the cross-dataset error up to 47.8% compared to learning-based methods. Experiments on Human3.6M-Occ and Occlusion-Person demonstrate robustness to occlusions, without scenario-specific fine-tuning. Our project page is available here: https://skelsplat.github.io.

