---
layout: default
title: GloSplat: Joint Pose-Appearance Optimization for Faster and More Accurate 3D Reconstruction
---

# GloSplat: Joint Pose-Appearance Optimization for Faster and More Accurate 3D Reconstruction
**arXiv**：[2603.04847v1](https://arxiv.org/abs/2603.04847) · [PDF](https://arxiv.org/pdf/2603.04847.pdf)  
**作者**：Tianyu Xiong, Rui Li, Linjie Li, Jiaqi Yang  

**一句话要点**：提出GloSplat框架，通过联合位姿-外观优化提升3D高斯溅射重建的速度与精度

**关键词**：3D高斯溅射, 联合优化, 运动恢复结构, 新视角合成, 特征轨迹, 无COLMAP重建

## 3 点简述
- 核心问题：传统3D重建将特征提取、匹配、运动恢复结构和新视角合成作为独立优化问题，导致效率与精度受限
- 方法要点：在3D高斯溅射训练中，联合优化位姿与外观，保留显式SfM特征轨迹作为可优化参数，结合重投影损失与光度监督
- 实验或效果：GloSplat-F在无COLMAP方法中达到最优，GloSplat-A超越所有基于COLMAP的基线，实现更快更准重建

## 摘要（原文）

> Feature extraction, matching, structure from motion (SfM), and novel view synthesis (NVS) have traditionally been treated as separate problems with independent optimization objectives. We present GloSplat, a framework that performs \emph{joint pose-appearance optimization} during 3D Gaussian Splatting training. Unlike prior joint optimization methods (BARF, NeRF--, 3RGS) that rely purely on photometric gradients for pose refinement, GloSplat preserves \emph{explicit SfM feature tracks} as first-class entities throughout training: track 3D points are maintained as separate optimizable parameters from Gaussian primitives, providing persistent geometric anchors via a reprojection loss that operates alongside photometric supervision. This architectural choice prevents early-stage pose drift while enabling fine-grained refinement -- a capability absent in photometric-only approaches. We introduce two pipeline variants: (1) \textbf{GloSplat-F}, a COLMAP-free variant using retrieval-based pair selection for efficient reconstruction, and (2) \textbf{GloSplat-A}, an exhaustive matching variant for maximum quality. Both employ global SfM initialization followed by joint photometric-geometric optimization during 3DGS training. Experiments demonstrate that GloSplat-F achieves state-of-the-art among COLMAP-free methods while GloSplat-A surpasses all COLMAP-based baselines.

