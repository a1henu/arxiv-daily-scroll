---
layout: default
title: FLIGHT: Fibonacci Lattice-based Inference for Geometric Heading in real-Time
---

# FLIGHT: Fibonacci Lattice-based Inference for Geometric Heading in real-Time
**arXiv**：[2602.23115v1](https://arxiv.org/abs/2602.23115) · [PDF](https://arxiv.org/pdf/2602.23115.pdf)  
**作者**：David Dirnfeld, Fabien Delattre, Pedro Miraldo, Erik Learned-Miller  

**一句话要点**：提出基于斐波那契格点的球面霍夫变换方法，用于实时估计单目视频中的相机航向。

**关键词**：单目视觉, 相机运动估计, 霍夫变换, 斐波那契格点, 实时处理, 航向校正

## 3 点简述
- 核心问题：单目相机运动估计中，现有方法在噪声和异常值增加时精度下降或计算成本高。
- 方法要点：利用对应点生成大圆方向，通过斐波那契格点离散化球面进行投票，增强鲁棒性。
- 实验或效果：在三个数据集上验证了精度与效率的帕累托前沿，SLAM实验中通过航向校正降低RMSE。

## 摘要（原文）

> Estimating camera motion from monocular video is a fundamental problem in computer vision, central to tasks such as SLAM, visual odometry, and structure-from-motion. Existing methods that recover the camera's heading under known rotation, whether from an IMU or an optimization algorithm, tend to perform well in low-noise, low-outlier conditions, but often decrease in accuracy or become computationally expensive as noise and outlier levels increase. To address these limitations, we propose a novel generalization of the Hough transform on the unit sphere (S(2)) to estimate the camera's heading. First, the method extracts correspondences between two frames and generates a great circle of directions compatible with each pair of correspondences. Then, by discretizing the unit sphere using a Fibonacci lattice as bin centers, each great circle casts votes for a range of directions, ensuring that features unaffected by noise or dynamic objects vote consistently for the correct motion direction. Experimental results on three datasets demonstrate that the proposed method is on the Pareto frontier of accuracy versus efficiency. Additionally, experiments on SLAM show that the proposed method reduces RMSE by correcting the heading during camera pose initialization.

