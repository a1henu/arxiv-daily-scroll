---
layout: default
title: FoundationPose-Initialized 3D-2D Liver Registration for Surgical Augmented Reality
---

# FoundationPose-Initialized 3D-2D Liver Registration for Surgical Augmented Reality
**arXiv**：[2602.17517v1](https://arxiv.org/abs/2602.17517) · [PDF](https://arxiv.org/pdf/2602.17517.pdf)  
**作者**：Hanyuan Zhang, Lucas He, Runlong He, Abdolrahim Kadkhodamohammadi, Danail Stoyanov, Brian R. Davidson, Evangelos B. Mazomenos, Matthew J. Clarkson  

**一句话要点**：提出基于FoundationPose和NICP的3D-2D肝脏配准方法，用于腹腔镜手术增强现实，以降低工程复杂度。

**关键词**：增强现实手术, 3D-2D配准, 非刚性迭代最近点, 腹腔镜肝脏手术, 深度图配准, 姿态估计

## 3 点简述
- 核心问题：腹腔镜肝脏手术中，现有配准方法依赖器官轮廓和有限元模型，工程复杂且需专业知识。
- 方法要点：结合腹腔镜深度图与基础姿态估计器进行相机-肝脏姿态估计，并用非刚性迭代最近点替代有限元变形模型。
- 实验或效果：在真实患者数据上，深度增强方法平均配准误差为9.91毫米，刚性-NICP组合优于仅刚性配准。

## 摘要（原文）

> Augmented reality can improve tumor localization in laparoscopic liver surgery. Existing registration pipelines typically depend on organ contours; deformable (non-rigid) alignment is often handled with finite-element (FE) models coupled to dimensionality-reduction or machine-learning components. We integrate laparoscopic depth maps with a foundation pose estimator for camera-liver pose estimation and replace FE-based deformation with non-rigid iterative closest point (NICP) to lower engineering/modeling complexity and expertise requirements. On real patient data, the depth-augmented foundation pose approach achieved 9.91 mm mean registration error in 3 cases. Combined rigid-NICP registration outperformed rigid-only registration, demonstrating NICP as an efficient substitute for finite-element deformable models. This pipeline achieves clinically relevant accuracy while offering a lightweight, engineering-friendly alternative to FE-based deformation.

