---
layout: default
title: Towards High-Consistency Embodied World Model with Multi-View Trajectory Videos
---

# Towards High-Consistency Embodied World Model with Multi-View Trajectory Videos
**arXiv**：[2511.12882v1](https://arxiv.org/abs/2511.12882) · [PDF](https://arxiv.org/pdf/2511.12882.pdf)  
**作者**：Taiyi Su, Jian Zhu, Yaxuan Li, Chong Ma, Zitai Huang, Yichen Zhu, Hanli Wang, Yi Xu  

**一句话要点**：提出MTV-World模型，通过多视角轨迹视频控制解决具身世界模型物理交互不一致问题

**关键词**：具身世界模型, 多视角轨迹视频, 物理交互一致性, 机器人控制, 视觉预测, 空间信息补偿

## 3 点简述
- 核心问题：现有模型难以将低级动作精确转换为机器人运动，导致预测帧与现实物理交互不一致
- 方法要点：使用多视角轨迹视频作为控制信号，补偿空间信息损失，提升预测一致性
- 实验或效果：在复杂双臂场景中实现精确控制和准确物理交互建模，采用Jaccard指数评估空间一致性

## 摘要（原文）

> Embodied world models aim to predict and interact with the physical world through visual observations and actions. However, existing models struggle to accurately translate low-level actions (e.g., joint positions) into precise robotic movements in predicted frames, leading to inconsistencies with real-world physical interactions. To address these limitations, we propose MTV-World, an embodied world model that introduces Multi-view Trajectory-Video control for precise visuomotor prediction. Specifically, instead of directly using low-level actions for control, we employ trajectory videos obtained through camera intrinsic and extrinsic parameters and Cartesian-space transformation as control signals. However, projecting 3D raw actions onto 2D images inevitably causes a loss of spatial information, making a single view insufficient for accurate interaction modeling. To overcome this, we introduce a multi-view framework that compensates for spatial information loss and ensures high-consistency with physical world. MTV-World forecasts future frames based on multi-view trajectory videos as input and conditioning on an initial frame per view. Furthermore, to systematically evaluate both robotic motion precision and object interaction accuracy, we develop an auto-evaluation pipeline leveraging multimodal large models and referring video object segmentation models. To measure spatial consistency, we formulate it as an object location matching problem and adopt the Jaccard Index as the evaluation metric. Extensive experiments demonstrate that MTV-World achieves precise control execution and accurate physical interaction modeling in complex dual-arm scenarios.

