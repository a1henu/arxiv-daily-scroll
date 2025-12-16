---
layout: default
title: Light Field Based 6DoF Tracking of Previously Unobserved Objects
---

# Light Field Based 6DoF Tracking of Previously Unobserved Objects
**arXiv**：[2512.13007v1](https://arxiv.org/abs/2512.13007) · [PDF](https://arxiv.org/pdf/2512.13007.pdf)  
**作者**：Nikolai Goncharov, James L. Gray, Donald G. Dansereau  

**一句话要点**：提出基于光场图像的6DoF跟踪方法，无需预训练模型，适用于未观测复杂物体。

**关键词**：光场图像, 6DoF跟踪, 未观测物体, 高斯溅射, 可微渲染, 机器人视觉

## 3 点简述
- 核心问题：现有高性能跟踪方法依赖预捕获物体视图，限制于已知物体集，且对复杂外观（如反射）敏感。
- 方法要点：利用视觉基础模型从光场输入提取语义和几何特征，转换为视图相关高斯溅射作为统一对象表示，支持可微渲染和姿态优化。
- 实验或效果：在包含挑战性反射物体的光场跟踪数据集上实验，与最先进基于模型的跟踪器竞争，推动机器人系统通用物体跟踪。

## 摘要（原文）

> Object tracking is an important step in robotics and reautonomous driving pipelines, which has to generalize to previously unseen and complex objects. Existing high-performing methods often rely on pre-captured object views to build explicit reference models, which restricts them to a fixed set of known objects. However, such reference models can struggle with visually complex appearance, reducing the quality of tracking. In this work, we introduce an object tracking method based on light field images that does not depend on a pre-trained model, while being robust to complex visual behavior, such as reflections. We extract semantic and geometric features from light field inputs using vision foundation models and convert them into view-dependent Gaussian splats. These splats serve as a unified object representation, supporting differentiable rendering and pose optimization. We further introduce a light field object tracking dataset containing challenging reflective objects with precise ground truth poses. Experiments demonstrate that our method is competitive with state-of-the-art model-based trackers in these difficult cases, paving the way toward universal object tracking in robotic systems. Code/data available at https://github.com/nagonch/LiFT-6DoF.

