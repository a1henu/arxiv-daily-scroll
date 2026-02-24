---
layout: default
title: Learning Positive-Incentive Point Sampling in Neural Implicit Fields for Object Pose Estimation
---

# Learning Positive-Incentive Point Sampling in Neural Implicit Fields for Object Pose Estimation
**arXiv**：[2602.19937v1](https://arxiv.org/abs/2602.19937) · [PDF](https://arxiv.org/pdf/2602.19937.pdf)  
**作者**：Yifei Shi, Boyan Wan, Xin Xu, Kai Xu  

**一句话要点**：提出SO(3)-等变卷积隐式网络与正激励点采样策略以提升遮挡和噪声场景下的物体姿态估计性能

**关键词**：神经隐式场, 物体姿态估计, SO(3)-等变性, 点采样策略, 遮挡处理, 噪声鲁棒性

## 3 点简述
- 核心问题：神经隐式场在相机空间未观测区域预测规范坐标时因缺乏直接信号导致高不确定性，影响姿态估计准确性。
- 方法要点：结合SO(3)-等变卷积隐式网络实现任意查询点的等变属性估计，并采用正激励点采样策略动态优化采样位置。
- 实验或效果：在三个姿态估计数据集上超越现有方法，在未见姿态、高遮挡、新几何和严重噪声等挑战场景中表现显著提升。

## 摘要（原文）

> Learning neural implicit fields of 3D shapes is a rapidly emerging field that enables shape representation at arbitrary resolutions. Due to the flexibility, neural implicit fields have succeeded in many research areas, including shape reconstruction, novel view image synthesis, and more recently, object pose estimation. Neural implicit fields enable learning dense correspondences between the camera space and the object's canonical space-including unobserved regions in camera space-significantly boosting object pose estimation performance in challenging scenarios like highly occluded objects and novel shapes. Despite progress, predicting canonical coordinates for unobserved camera-space regions remains challenging due to the lack of direct observational signals. This necessitates heavy reliance on the model's generalization ability, resulting in high uncertainty. Consequently, densely sampling points across the entire camera space may yield inaccurate estimations that hinder the learning process and compromise performance. To alleviate this problem, we propose a method combining an SO(3)-equivariant convolutional implicit network and a positive-incentive point sampling (PIPS) strategy. The SO(3)-equivariant convolutional implicit network estimates point-level attributes with SO(3)-equivariance at arbitrary query locations, demonstrating superior performance compared to most existing baselines. The PIPS strategy dynamically determines sampling locations based on the input, thereby boosting the network's accuracy and training efficiency. Our method outperforms the state-of-the-art on three pose estimation datasets. Notably, it demonstrates significant improvements in challenging scenarios, such as objects captured with unseen pose, high occlusion, novel geometry, and severe noise.

