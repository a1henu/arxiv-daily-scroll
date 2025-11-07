---
layout: default
title: GraspView: Active Perception Scoring and Best-View Optimization for Robotic Grasping in Cluttered Environments
---

# GraspView: Active Perception Scoring and Best-View Optimization for Robotic Grasping in Cluttered Environments
**arXiv**：[2511.04199v1](https://arxiv.org/abs/2511.04199) · [PDF](https://arxiv.org/pdf/2511.04199.pdf)  
**作者**：Shenglin Wang, Mingtong Dai, Jingxuan Su, Lingbo Liu, Chunjie Chen, Xinyu Wu, Liang Lin  

**一句话要点**：提出GraspView以解决杂乱环境中RGB-only机器人抓取问题

**关键词**：机器人抓取, RGB-only感知, 主动视觉, 3D场景重建, 杂乱环境, 多视图融合

## 3 点简述
- 核心问题：杂乱环境中遮挡、感知质量差和3D重建不一致导致抓取失败
- 方法要点：集成全局场景重建、主动感知评分和在线度量对齐模块
- 实验或效果：在多种桌面物体上显著优于RGB-D和单视图RGB基线

## 摘要（原文）

> Robotic grasping is a fundamental capability for autonomous manipulation, yet
> remains highly challenging in cluttered environments where occlusion, poor
> perception quality, and inconsistent 3D reconstructions often lead to unstable
> or failed grasps. Conventional pipelines have widely relied on RGB-D cameras to
> provide geometric information, which fail on transparent or glossy objects and
> degrade at close range. We present GraspView, an RGB-only robotic grasping
> pipeline that achieves accurate manipulation in cluttered environments without
> depth sensors. Our framework integrates three key components: (i) global
> perception scene reconstruction, which provides locally consistent, up-to-scale
> geometry from a single RGB view and fuses multi-view projections into a
> coherent global 3D scene; (ii) a render-and-score active perception strategy,
> which dynamically selects next-best-views to reveal occluded regions; and (iii)
> an online metric alignment module that calibrates VGGT predictions against
> robot kinematics to ensure physical scale consistency. Building on these
> tailor-designed modules, GraspView performs best-view global grasping, fusing
> multi-view reconstructions and leveraging GraspNet for robust execution.
> Experiments on diverse tabletop objects demonstrate that GraspView
> significantly outperforms both RGB-D and single-view RGB baselines, especially
> under heavy occlusion, near-field sensing, and with transparent objects. These
> results highlight GraspView as a practical and versatile alternative to RGB-D
> pipelines, enabling reliable grasping in unstructured real-world environments.

