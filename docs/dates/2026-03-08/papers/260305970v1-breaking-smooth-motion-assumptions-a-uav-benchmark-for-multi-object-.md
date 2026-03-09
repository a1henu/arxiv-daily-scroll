---
layout: default
title: Breaking Smooth-Motion Assumptions: A UAV Benchmark for Multi-Object Tracking in Complex and Adverse Conditions
---

# Breaking Smooth-Motion Assumptions: A UAV Benchmark for Multi-Object Tracking in Complex and Adverse Conditions
**arXiv**：[2603.05970v1](https://arxiv.org/abs/2603.05970) · [PDF](https://arxiv.org/pdf/2603.05970.pdf)  
**作者**：Jingtao Ye, Kexin Zhang, Xunchi Ma, Yuehan Li, Guangming Zhu, Peiyi Shen, Linhua Jiang, Xiangdong Zhang, Liang Zhang  

**一句话要点**：提出DynUAV基准以解决无人机视角下动态复杂场景的多目标跟踪挑战

**关键词**：无人机多目标跟踪, 动态基准, 复杂场景, 自运动挑战, 工业目标检测

## 3 点简述
- 核心问题：现有无人机多目标跟踪基准缺乏剧烈自运动和复杂表观轨迹，导致跟踪性能受限
- 方法要点：构建包含42个视频序列和170万标注的DynUAV基准，涵盖车辆、行人及工业设备类别
- 实验或效果：评估显示先进跟踪器在动态条件下检测与关联能力不足，验证基准的严格性

## 摘要（原文）

> The rapid movements and agile maneuvers of unmanned aerial vehicles (UAVs) induce significant observational challenges for multi-object tracking (MOT). However, existing UAV-perspective MOT benchmarks often lack these complexities, featuring predominantly predictable camera dynamics and linear motion patterns. To address this gap, we introduce DynUAV, a new benchmark for dynamic UAV-perspective MOT, characterized by intense ego-motion and the resulting complex apparent trajectories. The benchmark comprises 42 video sequences with over 1.7 million bounding box annotations, covering vehicles, pedestrians, and specialized industrial categories such as excavators, bulldozers and cranes. Compared to existing benchmarks, DynUAV introduces substantial challenges arising from ego-motion, including drastic scale changes and viewpoint changes, as well as motion blur. Comprehensive evaluations of state-of-the-art trackers on DynUAV reveal their limitations, particularly in managing the intertwined challenges of detection and association under such dynamic conditions, thereby establishing DynUAV as a rigorous benchmark. We anticipate that DynUAV will serve as a demanding testbed to spur progress in real-world UAV-perspective MOT, and we will make all resources available at link.

