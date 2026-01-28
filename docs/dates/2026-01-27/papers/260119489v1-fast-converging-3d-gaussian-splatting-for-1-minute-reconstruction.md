---
layout: default
title: Fast Converging 3D Gaussian Splatting for 1-Minute Reconstruction
---

# Fast Converging 3D Gaussian Splatting for 1-Minute Reconstruction
**arXiv**：[2601.19489v1](https://arxiv.org/abs/2601.19489) · [PDF](https://arxiv.org/pdf/2601.19489.pdf)  
**作者**：Ziyu Zhang, Tianle Liu, Diantao Tu, Shuhan Shen  

**一句话要点**：提出快速收敛的3D高斯溅射方法，实现一分钟内高保真重建，适用于SIGGRAPH Asia挑战赛的异构设置。

**关键词**：3D高斯溅射, 快速重建, 异构优化, 姿态优化, 深度监督, 多视图一致性

## 3 点简述
- 核心问题：在SIGGRAPH Asia挑战赛中，需在一分钟内处理SLAM噪声轨迹和COLMAP准确轨迹的异构重建场景。
- 方法要点：采用两阶段方案，包括反向优化、紧凑溅射、锚点表示和全局姿态优化，针对不同轨迹调整策略。
- 实验或效果：在比赛中获得最高PSNR 28.43，排名第一，验证了方法在严格时间预算下的高效性和鲁棒性。

## 摘要（原文）

> We present a fast 3DGS reconstruction pipeline designed to converge within one minute, developed for the SIGGRAPH Asia 3DGS Fast Reconstruction Challenge. The challenge consists of an initial round using SLAM-generated camera poses (with noisy trajectories) and a final round using COLMAP poses (highly accurate). To robustly handle these heterogeneous settings, we develop a two-stage solution. In the first round, we use reverse per-Gaussian parallel optimization and compact forward splatting based on Taming-GS and Speedy-splat, load-balanced tiling, an anchor-based Neural-Gaussian representation enabling rapid convergence with fewer learnable parameters, initialization from monocular depth and partially from feed-forward 3DGS models, and a global pose refinement module for noisy SLAM trajectories. In the final round, the accurate COLMAP poses change the optimization landscape; we disable pose refinement, revert from Neural-Gaussians back to standard 3DGS to eliminate MLP inference overhead, introduce multi-view consistency-guided Gaussian splitting inspired by Fast-GS, and introduce a depth estimator to supervise the rendered depth. Together, these techniques enable high-fidelity reconstruction under a strict one-minute budget. Our method achieved the top performance with a PSNR of 28.43 and ranked first in the competition.

