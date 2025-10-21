---
layout: default
title: Raindrop GS: A Benchmark for 3D Gaussian Splatting under Raindrop Conditions
---

# Raindrop GS: A Benchmark for 3D Gaussian Splatting under Raindrop Conditions
**arXiv**：[2510.17719v1](https://arxiv.org/abs/2510.17719) · [PDF](https://arxiv.org/pdf/2510.17719.pdf)  
**作者**：Zhiqiang Teng, Beibei Lin, Tingting Chen, Zifeng Yuan, Xuanyi Li, Xuanyu Zhang, Shunli Zhang  

**一句话要点**：提出RaindropGS基准以评估雨滴条件下3D高斯泼溅重建性能

**关键词**：3D高斯泼溅, 雨滴干扰, 基准评估, 相机姿态估计, 点云初始化, 图像去雨

## 3 点简述
- 核心问题：雨滴导致遮挡和光学畸变，影响3D高斯泼溅重建质量与相机姿态估计
- 方法要点：构建真实雨滴数据集，包含多焦点图像集，支持全流程评估
- 实验或效果：揭示相机焦点位置和姿态初始化对重建性能的关键影响

## 摘要（原文）

> 3D Gaussian Splatting (3DGS) under raindrop conditions suffers from severe
> occlusions and optical distortions caused by raindrop contamination on the
> camera lens, substantially degrading reconstruction quality. Existing
> benchmarks typically evaluate 3DGS using synthetic raindrop images with known
> camera poses (constrained images), assuming ideal conditions. However, in
> real-world scenarios, raindrops often interfere with accurate camera pose
> estimation and point cloud initialization. Moreover, a significant domain gap
> between synthetic and real raindrops further impairs generalization. To tackle
> these issues, we introduce RaindropGS, a comprehensive benchmark designed to
> evaluate the full 3DGS pipeline-from unconstrained, raindrop-corrupted images
> to clear 3DGS reconstructions. Specifically, the whole benchmark pipeline
> consists of three parts: data preparation, data processing, and raindrop-aware
> 3DGS evaluation, including types of raindrop interference, camera pose
> estimation and point cloud initialization, single image rain removal
> comparison, and 3D Gaussian training comparison. First, we collect a real-world
> raindrop reconstruction dataset, in which each scene contains three aligned
> image sets: raindrop-focused, background-focused, and rain-free ground truth,
> enabling a comprehensive evaluation of reconstruction quality under different
> focus conditions. Through comprehensive experiments and analyses, we reveal
> critical insights into the performance limitations of existing 3DGS methods on
> unconstrained raindrop images and the varying impact of different pipeline
> components: the impact of camera focus position on 3DGS reconstruction
> performance, and the interference caused by inaccurate pose and point cloud
> initialization on reconstruction. These insights establish clear directions for
> developing more robust 3DGS methods under raindrop conditions.

