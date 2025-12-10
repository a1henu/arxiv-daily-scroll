---
layout: default
title: Geometry-Aware Sparse Depth Sampling for High-Fidelity RGB-D Depth Completion in Robotic Systems
---

# Geometry-Aware Sparse Depth Sampling for High-Fidelity RGB-D Depth Completion in Robotic Systems
**arXiv**：[2512.08229v1](https://arxiv.org/abs/2512.08229) · [PDF](https://arxiv.org/pdf/2512.08229.pdf)  
**作者**：Tony Salloom, Dandi Zhou, Xinhai Sun  

**一句话要点**：提出基于法线引导的稀疏深度采样策略，以提升机器人系统中RGB-D深度补全的精度与真实性。

**关键词**：深度补全, 稀疏深度采样, 法线估计, 机器人视觉, RGB-D感知, 扩散模型

## 3 点简述
- 核心问题：现有深度补全方法中稀疏深度采样忽略传感器几何依赖性和空间非均匀可靠性，导致训练条件不真实。
- 方法要点：利用RGB-D点云的PCA法线估计计算像素级深度可靠性，并据此采样稀疏深度，集成到扩散模型Marigold-DC中。
- 实验或效果：在NYU Depth v2上评估，几何感知采样提高精度、减少边缘伪影，并模拟更真实的传感器行为。

## 摘要（原文）

> Accurate three-dimensional perception is essential for modern industrial robotic systems that perform manipulation, inspection, and navigation tasks. RGB-D and stereo vision sensors are widely used for this purpose, but the depth maps they produce are often noisy, incomplete, or biased due to sensor limitations and environmental conditions. Depth completion methods aim to generate dense, reliable depth maps from RGB images and sparse depth input. However, a key limitation in current depth completion pipelines is the unrealistic generation of sparse depth: sparse pixels are typically selected uniformly at random from dense ground-truth depth, ignoring the fact that real sensors exhibit geometry-dependent and spatially nonuniform reliability. In this work, we propose a normal-guided sparse depth sampling strategy that leverages PCA-based surface normal estimation on the RGB-D point cloud to compute a per-pixel depth reliability measure. The sparse depth samples are then drawn according to this reliability distribution. We integrate this sampling method with the Marigold-DC diffusion-based depth completion model and evaluate it on NYU Depth v2 using the standard metrics. Experiments show that our geometry-aware sparse depth improves accuracy, reduces artifacts near edges and discontinuities, and produces more realistic training conditions that better reflect real sensor behavior.

