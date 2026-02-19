---
layout: default
title: Markerless 6D Pose Estimation and Position-Based Visual Servoing for Endoscopic Continuum Manipulators
---

# Markerless 6D Pose Estimation and Position-Based Visual Servoing for Endoscopic Continuum Manipulators
**arXiv**：[2602.16365v1](https://arxiv.org/abs/2602.16365) · [PDF](https://arxiv.org/pdf/2602.16365.pdf)  
**作者**：Junhyun Park, Chunggil An, Myeongbo Park, Ihsan Ullah, Sihyeong Park, Minho Hwang  

**一句话要点**：提出无标记立体6D位姿估计与基于位置的视觉伺服框架，用于内窥镜连续体机械臂的精确闭环控制。

**关键词**：无标记位姿估计, 视觉伺服, 连续体机械臂, 立体视觉, 仿真到真实迁移, 闭环控制

## 3 点简述
- 核心问题：连续体机械臂因迟滞、柔顺性和远端感知有限，导致位姿估计与闭环控制困难。
- 方法要点：通过立体感知多特征融合网络和基于渲染的前馈细化模块，增强几何可观测性并实现单次位姿校正。
- 实验或效果：真实世界验证中，位姿估计平均平移误差0.83毫米，视觉伺服相比开环控制平移误差减少85%。

## 摘要（原文）

> Continuum manipulators in flexible endoscopic surgical systems offer high dexterity for minimally invasive procedures; however, accurate pose estimation and closed-loop control remain challenging due to hysteresis, compliance, and limited distal sensing. Vision-based approaches reduce hardware complexity but are often constrained by limited geometric observability and high computational overhead, restricting real-time closed-loop applicability. This paper presents a unified framework for markerless stereo 6D pose estimation and position-based visual servoing of continuum manipulators. A photo-realistic simulation pipeline enables large-scale automatic training with pixel-accurate annotations. A stereo-aware multi-feature fusion network jointly exploits segmentation masks, keypoints, heatmaps, and bounding boxes to enhance geometric observability. To enforce geometric consistency without iterative optimization, a feed-forward rendering-based refinement module predicts residual pose corrections in a single pass. A self-supervised sim-to-real adaptation strategy further improves real-world performance using unlabeled data. Extensive real-world validation achieves a mean translation error of 0.83 mm and a mean rotation error of 2.76° across 1,000 samples. Markerless closed-loop visual servoing driven by the estimated pose attains accurate trajectory tracking with a mean translation error of 2.07 mm and a mean rotation error of 7.41°, corresponding to 85% and 59% reductions compared to open-loop control, together with high repeatability in repeated point-reaching tasks. To the best of our knowledge, this work presents the first fully markerless pose-estimation-driven position-based visual servoing framework for continuum manipulators, enabling precise closed-loop control without physical markers or embedded sensing.

