---
layout: default
title: Training Deep Stereo Matching Networks on Tree Branch Imagery: A Benchmark Study for Real-Time UAV Forestry Applications
---

# Training Deep Stereo Matching Networks on Tree Branch Imagery: A Benchmark Study for Real-Time UAV Forestry Applications
**arXiv**：[2602.19763v1](https://arxiv.org/abs/2602.19763) · [PDF](https://arxiv.org/pdf/2602.19763.pdf)  
**作者**：Yida Lin, Bing Xue, Mengjie Zhang, Sam Schofield, Richard Green  

**一句话要点**：训练十种深度立体匹配网络于树枝图像，为无人机林业应用提供实时基准研究。

**关键词**：立体匹配, 无人机林业, 深度估计, 实时处理, 基准研究, 树枝图像

## 3 点简述
- 核心问题：无人机自主修剪树木需实时深度估计，但立体匹配在植被场景易出错。
- 方法要点：使用Canterbury树枝数据集，以DEFOM生成视差图训练十种网络，涵盖多种设计。
- 实验或效果：BANet-3D质量最佳，RAFT-Stereo场景理解最高，AnyNet在1080P下接近实时。

## 摘要（原文）

> Autonomous drone-based tree pruning needs accurate, real-time depth estimation from stereo cameras. Depth is computed from disparity maps using $Z = f B/d$, so even small disparity errors cause noticeable depth mistakes at working distances. Building on our earlier work that identified DEFOM-Stereo as the best reference disparity generator for vegetation scenes, we present the first study to train and test ten deep stereo matching networks on real tree branch images. We use the Canterbury Tree Branches dataset -- 5,313 stereo pairs from a ZED Mini camera at 1080P and 720P -- with DEFOM-generated disparity maps as training targets. The ten methods cover step-by-step refinement, 3D convolution, edge-aware attention, and lightweight designs. Using perceptual metrics (SSIM, LPIPS, ViTScore) and structural metrics (SIFT/ORB feature matching), we find that BANet-3D produces the best overall quality (SSIM = 0.883, LPIPS = 0.157), while RAFT-Stereo scores highest on scene-level understanding (ViTScore = 0.799). Testing on an NVIDIA Jetson Orin Super (16 GB, independently powered) mounted on our drone shows that AnyNet reaches 6.99 FPS at 1080P -- the only near-real-time option -- while BANet-2D gives the best quality-speed balance at 1.21 FPS. We also compare 720P and 1080P processing times to guide resolution choices for forestry drone systems.

