---
layout: default
title: HEIR: Learning Graph-Based Motion Hierarchies
---

# HEIR: Learning Graph-Based Motion Hierarchies
**arXiv**：[2510.26786v1](https://arxiv.org/abs/2510.26786) · [PDF](https://arxiv.org/pdf/2510.26786.pdf)  
**作者**：Cheng Zheng, William Koch, Baiang Li, Felix Heide  

**一句话要点**：提出基于图学习的运动层次模型，以数据驱动方式建模复杂运动关系

**关键词**：运动层次建模, 图神经网络, 可微分学习, 高斯溅射, 数据驱动方法

## 3 点简述
- 现有方法依赖手动定义的运动层次，泛化性受限
- 使用图神经网络学习可微分层次，分解全局运动为继承模式和局部残差
- 在1D/2D运动和3D高斯溅射场景中验证层次重建和变形效果

## 摘要（原文）

> Hierarchical structures of motion exist across research fields, including
> computer vision, graphics, and robotics, where complex dynamics typically arise
> from coordinated interactions among simpler motion components. Existing methods
> to model such dynamics typically rely on manually-defined or heuristic
> hierarchies with fixed motion primitives, limiting their generalizability
> across different tasks. In this work, we propose a general hierarchical motion
> modeling method that learns structured, interpretable motion relationships
> directly from data. Our method represents observed motions using graph-based
> hierarchies, explicitly decomposing global absolute motions into
> parent-inherited patterns and local motion residuals. We formulate hierarchy
> inference as a differentiable graph learning problem, where vertices represent
> elemental motions and directed edges capture learned parent-child dependencies
> through graph neural networks. We evaluate our hierarchical reconstruction
> approach on three examples: 1D translational motion, 2D rotational motion, and
> dynamic 3D scene deformation via Gaussian splatting. Experimental results show
> that our method reconstructs the intrinsic motion hierarchy in 1D and 2D cases,
> and produces more realistic and interpretable deformations compared to the
> baseline on dynamic 3D Gaussian splatting scenes. By providing an adaptable,
> data-driven hierarchical modeling paradigm, our method offers a formulation
> applicable to a broad range of motion-centric tasks. Project Page:
> https://light.princeton.edu/HEIR/

