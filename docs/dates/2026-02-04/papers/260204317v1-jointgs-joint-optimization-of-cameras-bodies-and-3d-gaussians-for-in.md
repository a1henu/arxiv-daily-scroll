---
layout: default
title: JOintGS: Joint Optimization of Cameras, Bodies and 3D Gaussians for In-the-Wild Monocular Reconstruction
---

# JOintGS: Joint Optimization of Cameras, Bodies and 3D Gaussians for In-the-Wild Monocular Reconstruction
**arXiv**：[2602.04317v1](https://arxiv.org/abs/2602.04317) · [PDF](https://arxiv.org/pdf/2602.04317.pdf)  
**作者**：Zihan Lou, Jinlong Fan, Sihan Ma, Yuxiang Yang, Jing Zhang  

**一句话要点**：提出JOintGS框架，通过联合优化相机、人体姿态和3D高斯，解决野外单目视频中高保真可动画3D人体重建的挑战。

**关键词**：单目3D重建, 3D高斯溅射, 人体姿态优化, 相机标定, 动态场景建模, 实时渲染

## 3 点简述
- 核心问题：野外单目视频中，相机参数和人体姿态估计不准确，限制了3D高斯溅射方法的重建质量。
- 方法要点：联合优化相机外参、人体姿态和3D高斯表示，利用前景-背景解耦实现相互增强，并引入时间动态模块和残差颜色场。
- 实验或效果：在NeuMan和EMDB数据集上，PSNR提升2.1dB，优于现有方法，保持实时渲染，对噪声初始化具有鲁棒性。

## 摘要（原文）

> Reconstructing high-fidelity animatable 3D human avatars from monocular RGB videos remains challenging, particularly in unconstrained in-the-wild scenarios where camera parameters and human poses from off-the-shelf methods (e.g., COLMAP, HMR2.0) are often inaccurate. Splatting (3DGS) advances demonstrate impressive rendering quality and real-time performance, they critically depend on precise camera calibration and pose annotations, limiting their applicability in real-world settings. We present JOintGS, a unified framework that jointly optimizes camera extrinsics, human poses, and 3D Gaussian representations from coarse initialization through a synergistic refinement mechanism. Our key insight is that explicit foreground-background disentanglement enables mutual reinforcement: static background Gaussians anchor camera estimation via multi-view consistency; refined cameras improve human body alignment through accurate temporal correspondence; optimized human poses enhance scene reconstruction by removing dynamic artifacts from static constraints. We further introduce a temporal dynamics module to capture fine-grained pose-dependent deformations and a residual color field to model illumination variations. Extensive experiments on NeuMan and EMDB datasets demonstrate that JOintGS achieves superior reconstruction quality, with 2.1~dB PSNR improvement over state-of-the-art methods on NeuMan dataset, while maintaining real-time rendering. Notably, our method shows significantly enhanced robustness to noisy initialization compared to the baseline.Our source code is available at https://github.com/MiliLab/JOintGS.

