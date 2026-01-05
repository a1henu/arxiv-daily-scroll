---
layout: default
title: AdaGaR: Adaptive Gabor Representation for Dynamic Scene Reconstruction
---

# AdaGaR: Adaptive Gabor Representation for Dynamic Scene Reconstruction
**arXiv**：[2601.00796v1](https://arxiv.org/abs/2601.00796) · [PDF](https://arxiv.org/pdf/2601.00796.pdf)  
**作者**：Jiewen Chan, Zhenjun Zhao, Yu-Lun Liu  

**一句话要点**：提出AdaGaR框架，通过自适应Gabor表示和时序连续性约束解决单目视频动态场景重建问题。

**关键词**：动态场景重建, 自适应Gabor表示, 时序连续性, 单目视频, 三维重建, 帧插值

## 3 点简述
- 核心问题：现有方法在动态场景重建中难以平衡高频细节捕获与能量稳定性，且缺乏时序连续性导致运动伪影。
- 方法要点：引入自适应Gabor表示，通过可学习频率权重和能量补偿优化高斯基元；采用三次Hermite样条与时序曲率正则化确保平滑运动。
- 实验或效果：在Tap-Vid DAVIS数据集上实现SOTA性能，并在帧插值、深度一致性等任务中展示强泛化能力。

## 摘要（原文）

> Reconstructing dynamic 3D scenes from monocular videos requires simultaneously capturing high-frequency appearance details and temporally continuous motion. Existing methods using single Gaussian primitives are limited by their low-pass filtering nature, while standard Gabor functions introduce energy instability. Moreover, lack of temporal continuity constraints often leads to motion artifacts during interpolation. We propose AdaGaR, a unified framework addressing both frequency adaptivity and temporal continuity in explicit dynamic scene modeling. We introduce Adaptive Gabor Representation, extending Gaussians through learnable frequency weights and adaptive energy compensation to balance detail capture and stability. For temporal continuity, we employ Cubic Hermite Splines with Temporal Curvature Regularization to ensure smooth motion evolution. An Adaptive Initialization mechanism combining depth estimation, point tracking, and foreground masks establishes stable point cloud distributions in early training. Experiments on Tap-Vid DAVIS demonstrate state-of-the-art performance (PSNR 35.49, SSIM 0.9433, LPIPS 0.0723) and strong generalization across frame interpolation, depth consistency, video editing, and stereo view synthesis. Project page: https://jiewenchan.github.io/AdaGaR/

