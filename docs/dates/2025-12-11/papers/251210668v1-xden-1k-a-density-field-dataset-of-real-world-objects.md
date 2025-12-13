---
layout: default
title: XDen-1K: A Density Field Dataset of Real-World Objects
---

# XDen-1K: A Density Field Dataset of Real-World Objects
**arXiv**：[2512.10668v1](https://arxiv.org/abs/2512.10668) · [PDF](https://arxiv.org/pdf/2512.10668.pdf)  
**作者**：Jingxuan Zhang, Tianqi Yu, Yatu Zhang, Jinze Wu, Kaixin Yao, Jingyang Liu, Yuyao Zhang, Jiayuan Gu, Jingyi Yu  

**一句话要点**：提出XDen-1K数据集以解决真实物体内部物理属性数据缺失问题

**关键词**：体积密度估计, 多模态数据集, 物理属性恢复, 机器人操作, X射线扫描, 3D几何模型

## 3 点简述
- 核心问题：现有模型忽略物体内部物理属性如体积密度，影响机器人操作和物理模拟准确性
- 方法要点：提供1000个真实物体的多模态数据，包括高分辨率3D模型和X射线扫描，并开发优化框架恢复密度场
- 实验或效果：通过体积分割和机器人任务实验，证明数据集能提升质心估计精度和操作成功率

## 摘要（原文）

> A deep understanding of the physical world is a central goal for embodied AI and realistic simulation. While current models excel at capturing an object's surface geometry and appearance, they largely neglect its internal physical properties. This omission is critical, as properties like volumetric density are fundamental for predicting an object's center of mass, stability, and interaction dynamics in applications ranging from robotic manipulation to physical simulation. The primary bottleneck has been the absence of large-scale, real-world data. To bridge this gap, we introduce XDen-1K, the first large-scale, multi-modal dataset designed for real-world physical property estimation, with a particular focus on volumetric density. The core of this dataset consists of 1,000 real-world objects across 148 categories, for which we provide comprehensive multi-modal data, including a high-resolution 3D geometric model with part-level annotations and a corresponding set of real-world biplanar X-ray scans. Building upon this data, we introduce a novel optimization framework that recovers a high-fidelity volumetric density field of each object from its sparse X-ray views. To demonstrate its practical value, we add X-ray images as a conditioning signal to an existing segmentation network and perform volumetric segmentation. Furthermore, we conduct experiments on downstream robotics tasks. The results show that leveraging the dataset can effectively improve the accuracy of center-of-mass estimation and the success rate of robotic manipulation. We believe XDen-1K will serve as a foundational resource and a challenging new benchmark, catalyzing future research in physically grounded visual inference and embodied AI.

