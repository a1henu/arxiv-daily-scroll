---
layout: default
title: Multi-Agent Monocular Dense SLAM With 3D Reconstruction Priors
---

# Multi-Agent Monocular Dense SLAM With 3D Reconstruction Priors
**arXiv**：[2511.19031v1](https://arxiv.org/abs/2511.19031) · [PDF](https://arxiv.org/pdf/2511.19031.pdf)  
**作者**：Haihang Wu, Yuchen Zhou  

**一句话要点**：提出多智能体单目稠密SLAM系统，利用3D重建先验提升计算效率与地图一致性

**关键词**：多智能体SLAM, 单目稠密SLAM, 3D重建先验, 地图融合, 计算效率优化

## 3 点简述
- 核心问题：单目稠密SLAM计算成本高，且现有方法仅支持单智能体操作
- 方法要点：每个智能体使用3D重建先验进行局部SLAM，通过闭环机制融合全局地图
- 实验效果：在真实数据集上保持类似精度，计算效率优于现有方法

## 摘要（原文）

> Monocular Simultaneous Localization and Mapping (SLAM) aims to estimate a robot's pose while simultaneously reconstructing an unknown 3D scene using a single camera. While existing monocular SLAM systems generate detailed 3D geometry through dense scene representations, they are computationally expensive due to the need for iterative optimization. To address this challenge, MASt3R-SLAM utilizes learned 3D reconstruction priors, enabling more efficient and accurate estimation of both 3D structures and camera poses. However, MASt3R-SLAM is limited to single-agent operation. In this paper, we extend MASt3R-SLAM to introduce the first multi-agent monocular dense SLAM system. Each agent performs local SLAM using a 3D reconstruction prior, and their individual maps are fused into a globally consistent map through a loop-closure-based map fusion mechanism. Our approach improves computational efficiency compared to state-of-the-art methods, while maintaining similar mapping accuracy when evaluated on real-world datasets.

