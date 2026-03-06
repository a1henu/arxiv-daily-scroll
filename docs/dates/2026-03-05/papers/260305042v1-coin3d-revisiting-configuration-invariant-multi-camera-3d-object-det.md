---
layout: default
title: CoIn3D: Revisiting Configuration-Invariant Multi-Camera 3D Object Detection
---

# CoIn3D: Revisiting Configuration-Invariant Multi-Camera 3D Object Detection
**arXiv**：[2603.05042v1](https://arxiv.org/abs/2603.05042) · [PDF](https://arxiv.org/pdf/2603.05042.pdf)  
**作者**：Zhaonian Kuang, Rui Ding, Haotian Wang, Xinhu Zheng, Meng Yang, Gang Hua  

**一句话要点**：提出CoIn3D框架以解决多相机3D目标检测在未知配置下的泛化问题

**关键词**：多相机3D目标检测, 配置不变性, 空间先验, 特征调制, 数据增强, 泛化能力

## 3 点简述
- 核心问题：多相机3D检测模型难以泛化到新相机配置，源于空间先验差异
- 方法要点：通过空间感知特征调制和相机感知数据增强整合空间先验
- 实验或效果：在NuScenes等数据集上，基于BEVDepth等范式实现强跨配置性能

## 摘要（原文）

> Multi-camera 3D object detection (MC3D) has attracted increasing attention with the growing deployment of multi-sensor physical agents, such as robots and autonomous vehicles. However, MC3D models still struggle to generalize to unseen platforms with new multi-camera configurations. Current solutions simply employ a meta-camera for unified representation but lack comprehensive consideration. In this paper, we revisit this issue and identify that the devil lies in spatial prior discrepancies across source and target configurations, including different intrinsics, extrinsics, and array layouts. To address this, we propose CoIn3D, a generalizable MC3D framework that enables strong transferability from source configurations to unseen target ones. CoIn3D explicitly incorporates all identified spatial priors into both feature embedding and image observation through spatial-aware feature modulation (SFM) and camera-aware data augmentation (CDA), respectively. SFM enriches feature space by integrating four spatial representations, such as focal length, ground depth, ground gradient, and Plücker coordinate. CDA improves observation diversity under various configurations via a training-free dynamic novel-view image synthesis scheme. Extensive experiments demonstrate that CoIn3D achieves strong cross-configuration performance on landmark datasets such as NuScenes, Waymo, and Lyft, under three dominant MC3D paradigms represented by BEVDepth, BEVFormer, and PETR.

