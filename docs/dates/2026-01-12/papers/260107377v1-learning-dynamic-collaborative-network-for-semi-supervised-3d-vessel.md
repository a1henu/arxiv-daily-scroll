---
layout: default
title: Learning Dynamic Collaborative Network for Semi-supervised 3D Vessel Segmentation
---

# Learning Dynamic Collaborative Network for Semi-supervised 3D Vessel Segmentation
**arXiv**：[2601.07377v1](https://arxiv.org/abs/2601.07377) · [PDF](https://arxiv.org/pdf/2601.07377.pdf)  
**作者**：Jiao Xu, Xin Chen, Lihe Zhang  

**一句话要点**：提出动态协作网络DiCo以解决半监督3D血管分割中教师模型认知偏差问题

**关键词**：半监督学习, 3D血管分割, 动态协作网络, 多视图集成, 对抗监督, 医学图像分析

## 3 点简述
- 针对3D血管数据复杂性导致教师模型性能不稳定，提出动态切换教师-学生角色的协作网络
- 引入多视图集成模块模拟医生多角度分析，并采用对抗监督约束未标注数据中血管形状
- 在三个3D血管分割基准测试中实现最先进性能，代码已开源

## 摘要（原文）

> In this paper, we present a new dynamic collaborative network for semi-supervised 3D vessel segmentation, termed DiCo. Conventional mean teacher (MT) methods typically employ a static approach, where the roles of the teacher and student models are fixed. However, due to the complexity of 3D vessel data, the teacher model may not always outperform the student model, leading to cognitive biases that can limit performance. To address this issue, we propose a dynamic collaborative network that allows the two models to dynamically switch their teacher-student roles. Additionally, we introduce a multi-view integration module to capture various perspectives of the inputs, mirroring the way doctors conduct medical analysis. We also incorporate adversarial supervision to constrain the shape of the segmented vessels in unlabeled data. In this process, the 3D volume is projected into 2D views to mitigate the impact of label inconsistencies. Experiments demonstrate that our DiCo method sets new state-of-the-art performance on three 3D vessel segmentation benchmarks. The code repository address is https://github.com/xujiaommcome/DiCo

