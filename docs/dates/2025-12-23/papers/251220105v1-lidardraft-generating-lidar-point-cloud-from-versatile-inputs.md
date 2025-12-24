---
layout: default
title: LiDARDraft: Generating LiDAR Point Cloud from Versatile Inputs
---

# LiDARDraft: Generating LiDAR Point Cloud from Versatile Inputs
**arXiv**：[2512.20105v1](https://arxiv.org/abs/2512.20105) · [PDF](https://arxiv.org/pdf/2512.20105.pdf)  
**作者**：Haiyun Wei, Fan Lu, Yunwei Zhu, Zehan Zheng, Weiyi Xue, Lin Shao, Xudong Zhang, Ya Wu, Rong Fu, Guang Chen  

**一句话要点**：提出LiDARDraft，利用3D布局从多样化输入生成可控LiDAR点云，用于自动驾驶仿真。

**关键词**：LiDAR点云生成, 自动驾驶仿真, 3D布局, 可控生成, ControlNet, 多样化输入

## 3 点简述
- 核心问题：现有方法在复杂LiDAR点云分布与简单控制信号间不平衡，难以实现高质量和多样化可控生成。
- 方法要点：将文本、图像和点云统一表示为3D布局，转化为语义和深度信号，基于rangemap的ControlNet指导生成。
- 实验或效果：像素级对齐方法在可控生成中表现优异，支持从文本、图像和草图创建自动驾驶环境。

## 摘要（原文）

> Generating realistic and diverse LiDAR point clouds is crucial for autonomous driving simulation. Although previous methods achieve LiDAR point cloud generation from user inputs, they struggle to attain high-quality results while enabling versatile controllability, due to the imbalance between the complex distribution of LiDAR point clouds and the simple control signals. To address the limitation, we propose LiDARDraft, which utilizes the 3D layout to build a bridge between versatile conditional signals and LiDAR point clouds. The 3D layout can be trivially generated from various user inputs such as textual descriptions and images. Specifically, we represent text, images, and point clouds as unified 3D layouts, which are further transformed into semantic and depth control signals. Then, we employ a rangemap-based ControlNet to guide LiDAR point cloud generation. This pixel-level alignment approach demonstrates excellent performance in controllable LiDAR point clouds generation, enabling "simulation from scratch", allowing self-driving environments to be created from arbitrary textual descriptions, images and sketches.

