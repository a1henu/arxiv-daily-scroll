---
layout: default
title: Object Pose Distribution Estimation for Determining Revolution and Reflection Uncertainty in Point Clouds
---

# Object Pose Distribution Estimation for Determining Revolution and Reflection Uncertainty in Point Clouds
**arXiv**：[2512.07211v1](https://arxiv.org/abs/2512.07211) · [PDF](https://arxiv.org/pdf/2512.07211.pdf)  
**作者**：Frederik Hagelskjær, Dimitrios Arapis, Steffen Madsen, Thorbjørn Mosekjær Iversen  

**一句话要点**：提出基于神经网络的物体姿态分布估计方法，仅用3D无色数据解决工业场景中的姿态不确定性

**关键词**：姿态分布估计, 3D点云, 深度学习, 工业机器人, 对称性处理, 不确定性建模

## 3 点简述
- 核心问题：现有姿态估计方法依赖颜色信息，无法处理工业场景中无色数据的视觉模糊性。
- 方法要点：利用深度学习从3D点云估计姿态分布，专注于反射和旋转对称性，可扩展至完整SE(3)。
- 实验或效果：在真实世界拣选场景中验证，处理几何模糊物体，代码已开源。

## 摘要（原文）

> Object pose estimation is crucial to robotic perception and typically provides a single-pose estimate. However, a single estimate cannot capture pose uncertainty deriving from visual ambiguity, which can lead to unreliable behavior. Existing pose distribution methods rely heavily on color information, often unavailable in industrial settings.
>   We propose a novel neural network-based method for estimating object pose uncertainty using only 3D colorless data. To the best of our knowledge, this is the first approach that leverages deep learning for pose distribution estimation without relying on RGB input. We validate our method in a real-world bin picking scenario with objects of varying geometric ambiguity. Our current implementation focuses on symmetries in reflection and revolution, but the framework is extendable to full SE(3) pose distribution estimation. Source code available at opde3d.github.io

