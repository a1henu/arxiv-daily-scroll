---
layout: default
title: YCB-Ev SD: Synthetic event-vision dataset for 6DoF object pose estimation
---

# YCB-Ev SD: Synthetic event-vision dataset for 6DoF object pose estimation
**arXiv**：[2511.11344v1](https://arxiv.org/abs/2511.11344) · [PDF](https://arxiv.org/pdf/2511.11344.pdf)  
**作者**：Pavel Rojtberg, Julius Kühn  

**一句话要点**：提出YCB-Ev SD合成事件相机数据集，用于6DoF物体姿态估计。

**关键词**：事件相机数据集, 6DoF姿态估计, 合成数据生成, 时间表面编码, 极性信息, CNN推理

## 3 点简述
- 核心问题：事件视觉缺乏全面合成数据集，阻碍6DoF姿态估计研究。
- 方法要点：基于PBR渲染生成5万事件序列，采用线性相机运动确保场景覆盖。
- 实验或效果：线性衰减时间表面与双通道极性编码在CNN推理中表现最优。

## 摘要（原文）

> We introduce YCB-Ev SD, a synthetic dataset of event-camera data at standard definition (SD) resolution for 6DoF object pose estimation. While synthetic data has become fundamental in frame-based computer vision, event-based vision lacks comparable comprehensive resources. Addressing this gap, we present 50,000 event sequences of 34 ms duration each, synthesized from Physically Based Rendering (PBR) scenes of YCB-Video objects following the Benchmark for 6D Object Pose (BOP) methodology. Our generation framework employs simulated linear camera motion to ensure complete scene coverage, including background activity.
>   Through systematic evaluation of event representations for CNN-based inference, we demonstrate that time-surfaces with linear decay and dual-channel polarity encoding achieve superior pose estimation performance, outperforming exponential decay and single-channel alternatives by significant margins. Our analysis reveals that polarity information contributes most substantially to performance gains, while linear temporal encoding preserves critical motion information more effectively than exponential decay. The dataset is provided in a structured format with both raw event streams and precomputed optimal representations to facilitate immediate research use and reproducible benchmarking.
>   The dataset is publicly available at https://huggingface.co/datasets/paroj/ycbev_sd.

