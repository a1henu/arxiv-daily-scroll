---
layout: default
title: LAA3D: A Benchmark of Detecting and Tracking Low-Altitude Aircraft in 3D Space
---

# LAA3D: A Benchmark of Detecting and Tracking Low-Altitude Aircraft in 3D Space
**arXiv**：[2511.19057v1](https://arxiv.org/abs/2511.19057) · [PDF](https://arxiv.org/pdf/2511.19057.pdf)  
**作者**：Hai Wu, Shuai Tang, Jiale Wang, Longkun Zou, Mingyue Guo, Rongqin Liang, Ke Chen, Yaowei Wang  

**一句话要点**：提出LAA3D基准以解决低空飞行器3D感知数据集稀缺问题

**关键词**：3D目标检测, 低空飞行器跟踪, 合成数据生成, sim-to-real泛化, 单目3D定位, 多任务基准

## 3 点简述
- 核心问题：低空飞行器3D感知数据集稀缺，阻碍精确定位与行为理解。
- 方法要点：构建大规模数据集，含真实与合成图像，支持3D检测与跟踪任务。
- 实验或效果：提出MonoLAA基线，合成数据预训练后微调，实现强sim-to-real泛化。

## 摘要（原文）

> Perception of Low-Altitude Aircraft (LAA) in 3D space enables precise 3D object localization and behavior understanding. However, datasets tailored for 3D LAA perception remain scarce. To address this gap, we present LAA3D, a large-scale dataset designed to advance 3D detection and tracking of low-altitude aerial vehicles. LAA3D contains 15,000 real images and 600,000 synthetic frames, captured across diverse scenarios, including urban and suburban environments. It covers multiple aerial object categories, including electric Vertical Take-Off and Landing (eVTOL) aircraft, Micro Aerial Vehicles (MAVs), and Helicopters. Each instance is annotated with 3D bounding box, class label, and instance identity, supporting tasks such as 3D object detection, 3D multi-object tracking (MOT), and 6-DoF pose estimation. Besides, we establish the LAA3D Benchmark, integrating multiple tasks and methods with unified evaluation protocols for comparison. Furthermore, we propose MonoLAA, a monocular 3D detection baseline, achieving robust 3D localization from zoom cameras with varying focal lengths. Models pretrained on synthetic images transfer effectively to real-world data with fine-tuning, demonstrating strong sim-to-real generalization. Our LAA3D provides a comprehensive foundation for future research in low-altitude 3D object perception.

