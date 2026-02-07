---
layout: default
title: PIRATR: Parametric Object Inference for Robotic Applications with Transformers in 3D Point Clouds
---

# PIRATR: Parametric Object Inference for Robotic Applications with Transformers in 3D Point Clouds
**arXiv**：[2602.05557v1](https://arxiv.org/abs/2602.05557) · [PDF](https://arxiv.org/pdf/2602.05557.pdf)  
**作者**：Michael Schwingshackl, Fabio F. Oberweger, Mario Niedermeyer, Huemer Johannes, Markus Murschitz  

**一句话要点**：提出PIRATR框架，用于机器人点云中的参数化3D物体检测与姿态估计。

**关键词**：3D物体检测, 参数化感知, 点云处理, 机器人视觉, Transformer模型, 合成数据训练

## 3 点简述
- 核心问题：在遮挡点云中实现多类别6自由度姿态和参数化属性的联合估计。
- 方法要点：基于PI3DETR扩展，采用模块化类别特定头，支持新物体类型扩展。
- 实验或效果：在合成数据训练后，无需微调，在真实室外LiDAR扫描中达到0.919 mAP。

## 摘要（原文）

> We present PIRATR, an end-to-end 3D object detection framework for robotic use cases in point clouds. Extending PI3DETR, our method streamlines parametric 3D object detection by jointly estimating multi-class 6-DoF poses and class-specific parametric attributes directly from occlusion-affected point cloud data. This formulation enables not only geometric localization but also the estimation of task-relevant properties for parametric objects, such as a gripper's opening, where the 3D model is adjusted according to simple, predefined rules. The architecture employs modular, class-specific heads, making it straightforward to extend to novel object types without re-designing the pipeline. We validate PIRATR on an automated forklift platform, focusing on three structurally and functionally diverse categories: crane grippers, loading platforms, and pallets. Trained entirely in a synthetic environment, PIRATR generalizes effectively to real outdoor LiDAR scans, achieving a detection mAP of 0.919 without additional fine-tuning. PIRATR establishes a new paradigm of pose-aware, parameterized perception. This bridges the gap between low-level geometric reasoning and actionable world models, paving the way for scalable, simulation-trained perception systems that can be deployed in dynamic robotic environments. Code available at https://github.com/swingaxe/piratr.

