---
layout: default
title: Relative Energy Learning for LiDAR Out-of-Distribution Detection
---

# Relative Energy Learning for LiDAR Out-of-Distribution Detection
**arXiv**：[2511.06720v1](https://arxiv.org/abs/2511.06720) · [PDF](https://arxiv.org/pdf/2511.06720.pdf)  
**作者**：Zizhao Li, Zhengkang Xiang, Jiayang Ao, Joseph West, Kourosh Khoshelham  

**一句话要点**：提出相对能量学习以解决LiDAR点云中分布外检测的误报问题

**关键词**：LiDAR点云, 分布外检测, 相对能量学习, 数据合成, 自动驾驶安全

## 3 点简述
- 核心问题：LiDAR点云分布外检测难以区分罕见异常与常见类，导致高误报率
- 方法要点：利用正负logits能量差作为相对评分函数，结合Point Raise合成异常数据
- 实验或效果：在SemanticKITTI和STU基准上显著优于现有方法，提升鲁棒性

## 摘要（原文）

> Out-of-distribution (OOD) detection is a critical requirement for reliable
> autonomous driving, where safety depends on recognizing road obstacles and
> unexpected objects beyond the training distribution. Despite extensive research
> on OOD detection in 2D images, direct transfer to 3D LiDAR point clouds has
> been proven ineffective. Current LiDAR OOD methods struggle to distinguish rare
> anomalies from common classes, leading to high false-positive rates and
> overconfident errors in safety-critical settings. We propose Relative Energy
> Learning (REL), a simple yet effective framework for OOD detection in LiDAR
> point clouds. REL leverages the energy gap between positive (in-distribution)
> and negative logits as a relative scoring function, mitigating calibration
> issues in raw energy values and improving robustness across various scenes. To
> address the absence of OOD samples during training, we propose a lightweight
> data synthesis strategy called Point Raise, which perturbs existing point
> clouds to generate auxiliary anomalies without altering the inlier semantics.
> Evaluated on SemanticKITTI and the Spotting the Unexpected (STU) benchmark, REL
> consistently outperforms existing methods by a large margin. Our results
> highlight that modeling relative energy, combined with simple synthetic
> outliers, provides a principled and scalable solution for reliable OOD
> detection in open-world autonomous driving.

