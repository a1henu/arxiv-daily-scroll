---
layout: default
title: PAGE-4D: Disentangled Pose and Geometry Estimation for 4D Perception
---

# PAGE-4D: Disentangled Pose and Geometry Estimation for 4D Perception
**arXiv**：[2510.17568v1](https://arxiv.org/abs/2510.17568) · [PDF](https://arxiv.org/pdf/2510.17568.pdf)  
**作者**：Kaichen Zhou, Yuhan Wang, Grace Chen, Xinhai Chang, Gaspard Beaudouin, Fangneng Zhan, Paul Pu Liang, Mengyu Wang  

**一句话要点**：提出PAGE-4D以解决动态场景中相机姿态与几何重建的冲突

**关键词**：4D感知, 相机姿态估计, 深度预测, 点云重建, 动态场景处理, 多任务学习

## 3 点简述
- 核心问题：静态模型在动态场景中表现不佳，任务间存在冲突
- 方法要点：使用动态感知聚合器解耦静态与动态信息
- 实验或效果：在动态场景中优于VGGT，提升姿态估计与重建精度

## 摘要（原文）

> Recent 3D feed-forward models, such as the Visual Geometry Grounded
> Transformer (VGGT), have shown strong capability in inferring 3D attributes of
> static scenes. However, since they are typically trained on static datasets,
> these models often struggle in real-world scenarios involving complex dynamic
> elements, such as moving humans or deformable objects like umbrellas. To
> address this limitation, we introduce PAGE-4D, a feedforward model that extends
> VGGT to dynamic scenes, enabling camera pose estimation, depth prediction, and
> point cloud reconstruction -- all without post-processing. A central challenge
> in multi-task 4D reconstruction is the inherent conflict between tasks:
> accurate camera pose estimation requires suppressing dynamic regions, while
> geometry reconstruction requires modeling them. To resolve this tension, we
> propose a dynamics-aware aggregator that disentangles static and dynamic
> information by predicting a dynamics-aware mask -- suppressing motion cues for
> pose estimation while amplifying them for geometry reconstruction. Extensive
> experiments show that PAGE-4D consistently outperforms the original VGGT in
> dynamic scenarios, achieving superior results in camera pose estimation,
> monocular and video depth estimation, and dense point map reconstruction.

