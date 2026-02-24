---
layout: default
title: One2Scene: Geometric Consistent Explorable 3D Scene Generation from a Single Image
---

# One2Scene: Geometric Consistent Explorable 3D Scene Generation from a Single Image
**arXiv**：[2602.19766v1](https://arxiv.org/abs/2602.19766) · [PDF](https://arxiv.org/pdf/2602.19766.pdf)  
**作者**：Pengfei Wang, Liyi Chen, Zhiyuan Ma, Yanjun Guo, Guowen Zhang, Lei Zhang  

**一句话要点**：提出One2Scene框架，通过分解任务实现单图像生成可探索3D场景

**关键词**：单图像3D重建, 可探索场景生成, 高斯溅射, 多视图立体匹配, 几何一致性

## 3 点简述
- 核心问题：单图像生成可探索3D场景时，现有方法在视角远离原始位置时易产生几何失真和噪声。
- 方法要点：将问题分解为全景图生成、3D几何支架构建和新视角生成三个子任务，利用多视图立体匹配和双向特征融合确保几何一致性。
- 实验或效果：在多个任务上显著优于现有方法，支持大相机运动下的稳定探索。

## 摘要（原文）

> Generating explorable 3D scenes from a single image is a highly challenging problem in 3D vision. Existing methods struggle to support free exploration, often producing severe geometric distortions and noisy artifacts when the viewpoint moves far from the original perspective. We introduce \textbf{One2Scene}, an effective framework that decomposes this ill-posed problem into three tractable sub-tasks to enable immersive explorable scene generation. We first use a panorama generator to produce anchor views from a single input image as initialization. Then, we lift these 2D anchors into an explicit 3D geometric scaffold via a generalizable, feed-forward Gaussian Splatting network. Instead of treating the panorama as a single image for reconstruction, we project it into multiple sparse anchor views and reformulate the reconstruction task as multi-view stereo matching, which allows us to leverage robust geometric priors learned from large-scale multi-view datasets. A bidirectional feature fusion module is used to enforce cross-view consistency, yielding an efficient and geometrically reliable scaffold. Finally, the scaffold serves as a strong prior for a novel view generator to produce photorealistic and geometrically accurate views at arbitrary cameras. By explicitly conditioning on a 3D-consistent scaffold to perform reconstruction, One2Scene works stably under large camera motions, supporting immersive scene exploration. Extensive experiments show that One2Scene substantially outperforms state-of-the-art methods in panorama depth estimation, feed-forward 360° reconstruction, and explorable 3D scene generation. Code and models will be released.

