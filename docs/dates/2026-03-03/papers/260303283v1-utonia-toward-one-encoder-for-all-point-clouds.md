---
layout: default
title: Utonia: Toward One Encoder for All Point Clouds
---

# Utonia: Toward One Encoder for All Point Clouds
**arXiv**：[2603.03283v1](https://arxiv.org/abs/2603.03283) · [PDF](https://arxiv.org/pdf/2603.03283.pdf)  
**作者**：Yujia Zhang, Xiaoyang Wu, Yunhan Yang, Xianzhe Fan, Han Li, Yuechen Zhang, Zehao Huang, Naiyan Wang, Hengshuang Zhao  

**一句话要点**：提出Utonia，一个跨域自监督点云Transformer编码器，统一多源点云表示以提升感知与推理能力。

**关键词**：点云统一编码, 跨域自监督学习, Transformer编码器, 多源点云融合, 机器人视觉, 空间推理

## 3 点简述
- 核心问题：点云数据来自不同领域（如遥感、LiDAR、RGB-D），具有几何、密度和先验差异，难以统一建模。
- 方法要点：通过自监督训练，使单个Transformer编码器学习跨域一致表示空间，支持多源点云融合。
- 实验或效果：在感知任务中提升性能，并观察到联合训练带来的涌现行为；在机器人操作和空间推理中验证了表示的有效性。

## 摘要（原文）

> We dream of a future where point clouds from all domains can come together to shape a single model that benefits them all. Toward this goal, we present Utonia, a first step toward training a single self-supervised point transformer encoder across diverse domains, spanning remote sensing, outdoor LiDAR, indoor RGB-D sequences, object-centric CAD models, and point clouds lifted from RGB-only videos. Despite their distinct sensing geometries, densities, and priors, Utonia learns a consistent representation space that transfers across domains. This unification improves perception capability while revealing intriguing emergent behaviors that arise only when domains are trained jointly. Beyond perception, we observe that Utonia representations can also benefit embodied and multimodal reasoning: conditioning vision-language-action policies on Utonia features improves robotic manipulation, and integrating them into vision-language models yields gains on spatial reasoning. We hope Utonia can serve as a step toward foundation models for sparse 3D data, and support downstream applications in AR/VR, robotics, and autonomous driving.

