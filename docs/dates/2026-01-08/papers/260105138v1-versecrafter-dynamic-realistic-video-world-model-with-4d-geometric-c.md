---
layout: default
title: VerseCrafter: Dynamic Realistic Video World Model with 4D Geometric Control
---

# VerseCrafter: Dynamic Realistic Video World Model with 4D Geometric Control
**arXiv**：[2601.05138v1](https://arxiv.org/abs/2601.05138) · [PDF](https://arxiv.org/pdf/2601.05138.pdf)  
**作者**：Sixiao Zheng, Minghao Yin, Wenbo Hu, Xiaoyu Li, Ying Shan, Yanwei Fu  

**一句话要点**：提出VerseCrafter，通过4D几何控制实现动态真实视频世界模型，统一控制相机与多物体运动。

**关键词**：视频世界模型, 4D几何控制, 3D高斯轨迹, 视频扩散模型, 自动数据引擎, 动态视频生成

## 3 点简述
- 现有视频世界模型难以统一精确控制相机与多物体运动，因视频动态基于2D投影平面。
- 引入4D几何控制表示，用静态背景点云和物体3D高斯轨迹编码世界状态，捕获物体路径与概率3D占用。
- 开发自动数据引擎从野外视频提取4D控制，训练模型生成高保真、视图一致视频，精确遵循指定动态。

## 摘要（原文）

> Video world models aim to simulate dynamic, real-world environments, yet existing methods struggle to provide unified and precise control over camera and multi-object motion, as videos inherently operate dynamics in the projected 2D image plane. To bridge this gap, we introduce VerseCrafter, a 4D-aware video world model that enables explicit and coherent control over both camera and object dynamics within a unified 4D geometric world state. Our approach is centered on a novel 4D Geometric Control representation, which encodes the world state through a static background point cloud and per-object 3D Gaussian trajectories. This representation captures not only an object's path but also its probabilistic 3D occupancy over time, offering a flexible, category-agnostic alternative to rigid bounding boxes or parametric models. These 4D controls are rendered into conditioning signals for a pretrained video diffusion model, enabling the generation of high-fidelity, view-consistent videos that precisely adhere to the specified dynamics. Unfortunately, another major challenge lies in the scarcity of large-scale training data with explicit 4D annotations. We address this by developing an automatic data engine that extracts the required 4D controls from in-the-wild videos, allowing us to train our model on a massive and diverse dataset.

