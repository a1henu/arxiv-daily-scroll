---
layout: default
title: 3D Point Cloud Object Detection on Edge Devices for Split Computing
---

# 3D Point Cloud Object Detection on Edge Devices for Split Computing
**arXiv**：[2511.02293v1](https://arxiv.org/abs/2511.02293) · [PDF](https://arxiv.org/pdf/2511.02293.pdf)  
**作者**：Taisuke Noguchi, Takuya Azumi  

**一句话要点**：提出基于分割计算的3D点云目标检测方法，以降低边缘设备计算负担。

**关键词**：3D点云检测, 分割计算, 边缘计算, LiDAR数据处理, 推理优化

## 3 点简述
- 核心问题：复杂3D点云检测模型在边缘设备上处理时间长、功耗高。
- 方法要点：采用分割计算，仅传输中间数据，减少边缘计算负担。
- 实验效果：分割后推理时间最多减少70.8%，边缘执行时间最多减少90.0%。

## 摘要（原文）

> The field of autonomous driving technology is rapidly advancing, with deep
> learning being a key component. Particularly in the field of sensing, 3D point
> cloud data collected by LiDAR is utilized to run deep neural network models for
> 3D object detection. However, these state-of-the-art models are complex,
> leading to longer processing times and increased power consumption on edge
> devices. The objective of this study is to address these issues by leveraging
> Split Computing, a distributed machine learning inference method. Split
> Computing aims to lessen the computational burden on edge devices, thereby
> reducing processing time and power consumption. Furthermore, it minimizes the
> risk of data breaches by only transmitting intermediate data from the deep
> neural network model. Experimental results show that splitting after
> voxelization reduces the inference time by 70.8% and the edge device execution
> time by 90.0%. When splitting within the network, the inference time is reduced
> by up to 57.1%, and the edge device execution time is reduced by up to 69.5%.

