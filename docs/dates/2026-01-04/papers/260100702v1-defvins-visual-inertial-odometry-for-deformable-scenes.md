---
layout: default
title: DefVINS: Visual-Inertial Odometry for Deformable Scenes
---

# DefVINS: Visual-Inertial Odometry for Deformable Scenes
**arXiv**：[2601.00702v1](https://arxiv.org/abs/2601.00702) · [PDF](https://arxiv.org/pdf/2601.00702.pdf)  
**作者**：Samuel Cerezo, Javier Civera  

**一句话要点**：提出DefVINS框架，通过分离刚性与非刚性运动以解决可变形场景中的视觉-惯性里程计问题。

**关键词**：视觉-惯性里程计, 可变形场景, 嵌入变形图, 可观测性分析, IMU锚定, 非刚性运动

## 3 点简述
- 核心问题：可变形场景违反刚性假设，导致传统VIO过拟合局部非刚性运动或严重漂移。
- 方法要点：使用嵌入变形图表示非刚性扭曲，结合IMU锚定刚性状态，并基于可观测性分析渐进激活非刚性自由度。
- 实验或效果：消融研究显示，结合惯性约束与可观测性感知的激活策略，在非刚性环境中提高了鲁棒性。

## 摘要（原文）

> Deformable scenes violate the rigidity assumptions underpinning classical visual-inertial odometry (VIO), often leading to over-fitting to local non-rigid motion or severe drift when deformation dominates visual parallax. We introduce DefVINS, a visual-inertial odometry framework that explicitly separates a rigid, IMU-anchored state from a non--rigid warp represented by an embedded deformation graph. The system is initialized using a standard VIO procedure that fixes gravity, velocity, and IMU biases, after which non-rigid degrees of freedom are activated progressively as the estimation becomes well conditioned. An observability analysis is included to characterize how inertial measurements constrain the rigid motion and render otherwise unobservable modes identifiable in the presence of deformation. This analysis motivates the use of IMU anchoring and informs a conditioning-based activation strategy that prevents ill-posed updates under poor excitation. Ablation studies demonstrate the benefits of combining inertial constraints with observability-aware deformation activation, resulting in improved robustness under non-rigid environments.

