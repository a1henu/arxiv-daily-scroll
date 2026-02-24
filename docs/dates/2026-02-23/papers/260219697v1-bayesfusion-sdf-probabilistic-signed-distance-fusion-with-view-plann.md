---
layout: default
title: BayesFusion-SDF: Probabilistic Signed Distance Fusion with View Planning on CPU
---

# BayesFusion-SDF: Probabilistic Signed Distance Fusion with View Planning on CPU
**arXiv**：[2602.19697v1](https://arxiv.org/abs/2602.19697) · [PDF](https://arxiv.org/pdf/2602.19697.pdf)  
**作者**：Soumya Mazumdar, Vineet Kumar Rakesh, Tapas Samanta  

**一句话要点**：提出BayesFusion-SDF，一种基于CPU的概率符号距离融合框架，用于机器人等场景的3D重建与不确定性估计。

**关键词**：概率3D重建, 符号距离函数, 贝叶斯融合, CPU计算, 不确定性估计, 主动感知

## 3 点简述
- 核心问题：传统TSDF方法依赖启发式权重，缺乏系统不确定性表达；神经方法计算成本高且可解释性差。
- 方法要点：将几何建模为稀疏高斯随机场，使用异方差贝叶斯公式融合深度观测，通过稀疏线性代数求解。
- 实验或效果：在控制场景和CO3D序列上验证，几何精度优于TSDF基线，并提供不确定性估计以支持主动感知。

## 摘要（原文）

> Key part of robotics, augmented reality, and digital inspection is dense 3D reconstruction from depth observations. Traditional volumetric fusion techniques, including truncated signed distance functions (TSDF), enable efficient and deterministic geometry reconstruction; however, they depend on heuristic weighting and fail to transparently convey uncertainty in a systematic way. Recent neural implicit methods, on the other hand, get very high fidelity but usually need a lot of GPU power for optimization and aren't very easy to understand for making decisions later on. This work presents BayesFusion-SDF, a CPU-centric probabilistic signed distance fusion framework that conceptualizes geometry as a sparse Gaussian random field with a defined posterior distribution over voxel distances. First, a rough TSDF reconstruction is used to create an adaptive narrow-band domain. Then, depth observations are combined using a heteroscedastic Bayesian formulation that is solved using sparse linear algebra and preconditioned conjugate gradients. Randomized diagonal estimators are a quick way to get an idea of posterior uncertainty. This makes it possible to extract surfaces and plan the next best view while taking into account uncertainty. Tests on a controlled ablation scene and a CO3D object sequence show that the new method is more accurate geometrically than TSDF baselines and gives useful estimates of uncertainty for active sensing. The proposed formulation provides a clear and easy-to-use alternative to GPU-heavy neural reconstruction methods while still being able to be understood in a probabilistic way and acting in a predictable way. GitHub: https://mazumdarsoumya.github.io/BayesFusionSDF

