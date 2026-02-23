---
layout: default
title: Have We Mastered Scale in Deep Monocular Visual SLAM? The ScaleMaster Dataset and Benchmark
---

# Have We Mastered Scale in Deep Monocular Visual SLAM? The ScaleMaster Dataset and Benchmark
**arXiv**：[2602.18174v1](https://arxiv.org/abs/2602.18174) · [PDF](https://arxiv.org/pdf/2602.18174.pdf)  
**作者**：Hyoseok Ju, Bokeon Suh, Giseop Kim  

**一句话要点**：提出ScaleMaster数据集与基准，以评估大规模室内环境中深度单目视觉SLAM的尺度一致性。

**关键词**：单目视觉SLAM, 尺度一致性, 室内大尺度环境, 数据集基准, 地图质量评估, 深度学习方法

## 3 点简述
- 核心问题：现有深度单目视觉SLAM在室内大尺度场景中面临尺度漂移和模糊性，缺乏针对性基准。
- 方法要点：构建首个专注于多楼层、长轨迹等挑战场景的ScaleMaster数据集，支持直接地图质量评估。
- 实验或效果：分析显示先进系统在现有基准表现良好，但在真实大尺度环境中存在严重尺度相关失败。

## 摘要（原文）

> Recent advances in deep monocular visual Simultaneous Localization and Mapping (SLAM) have achieved impressive accuracy and dense reconstruction capabilities, yet their robustness to scale inconsistency in large-scale indoor environments remains largely unexplored. Existing benchmarks are limited to room-scale or structurally simple settings, leaving critical issues of intra-session scale drift and inter-session scale ambiguity insufficiently addressed. To fill this gap, we introduce the ScaleMaster Dataset, the first benchmark explicitly designed to evaluate scale consistency under challenging scenarios such as multi-floor structures, long trajectories, repetitive views, and low-texture regions. We systematically analyze the vulnerability of state-of-the-art deep monocular visual SLAM systems to scale inconsistency, providing both quantitative and qualitative evaluations. Crucially, our analysis extends beyond traditional trajectory metrics to include a direct map-to-map quality assessment using metrics like Chamfer distance against high-fidelity 3D ground truth. Our results reveal that while recent deep monocular visual SLAM systems demonstrate strong performance on existing benchmarks, they suffer from severe scale-related failures in realistic, large-scale indoor environments. By releasing the ScaleMaster dataset and baseline results, we aim to establish a foundation for future research toward developing scale-consistent and reliable visual SLAM systems.

