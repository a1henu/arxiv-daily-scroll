---
layout: default
title: Grow with the Flow: 4D Reconstruction of Growing Plants with Gaussian Flow Fields
---

# Grow with the Flow: 4D Reconstruction of Growing Plants with Gaussian Flow Fields
**arXiv**：[2602.08958v1](https://arxiv.org/abs/2602.08958) · [PDF](https://arxiv.org/pdf/2602.08958.pdf)  
**作者**：Weihan Luo, Lily Goli, Sherwin Bahmani, Felix Taubner, Andrea Tagliasacchi, David B. Lindell  

**一句话要点**：提出3D高斯流场表示以解决植物生长动态建模中几何新增与非线性运动问题

**关键词**：植物生长建模, 3D高斯流场, 动态场景重建, 非线性运动建模, 多视角时序数据

## 3 点简述
- 核心问题：植物生长涉及几何新增，现有变形场和4D高斯溅射方法无法有效建模非线性动态
- 方法要点：基于高斯参数的时间变化导数建模生长，通过反向生长初始化高斯原语
- 实验或效果：在多视角植物生长数据集上实现优于先前方法的图像质量和几何精度

## 摘要（原文）

> Modeling the time-varying 3D appearance of plants during their growth poses unique challenges: unlike many dynamic scenes, plants generate new geometry over time as they expand, branch, and differentiate. Recent motion modeling techniques are ill-suited to this problem setting. For example, deformation fields cannot introduce new geometry, and 4D Gaussian splatting constrains motion to a linear trajectory in space and time and cannot track the same set of Gaussians over time. Here, we introduce a 3D Gaussian flow field representation that models plant growth as a time-varying derivative over Gaussian parameters -- position, scale, orientation, color, and opacity -- enabling nonlinear and continuous-time growth dynamics. To initialize a sufficient set of Gaussian primitives, we reconstruct the mature plant and learn a process of reverse growth, effectively simulating the plant's developmental history in reverse. Our approach achieves superior image quality and geometric accuracy compared to prior methods on multi-view timelapse datasets of plant growth, providing a new approach for appearance modeling of growing 3D structures.

