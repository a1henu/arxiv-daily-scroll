---
layout: default
title: SelfOccFlow: Towards end-to-end self-supervised 3D Occupancy Flow prediction
---

# SelfOccFlow: Towards end-to-end self-supervised 3D Occupancy Flow prediction
**arXiv**：[2602.23894v1](https://arxiv.org/abs/2602.23894) · [PDF](https://arxiv.org/pdf/2602.23894.pdf)  
**作者**：Xavier Timoneda, Markus Herb, Fabian Duerr, Daniel Goehring  

**一句话要点**：提出SelfOccFlow，一种自监督3D占用流预测方法，用于自动驾驶场景感知。

**关键词**：3D占用流预测, 自监督学习, 自动驾驶, 动态场景理解, 符号距离场

## 3 点简述
- 核心问题：现有方法依赖昂贵标注或外部监督，难以高效估计动态环境中的3D占用和运动。
- 方法要点：通过解耦静态和动态符号距离场，并利用时间聚合和特征余弦相似性自监督学习运动。
- 实验或效果：在SemanticKITTI、KITTI-MOT和nuScenes数据集上验证了方法的有效性。

## 摘要（原文）

> Estimating 3D occupancy and motion at the vehicle's surroundings is essential for autonomous driving, enabling situational awareness in dynamic environments. Existing approaches jointly learn geometry and motion but rely on expensive 3D occupancy and flow annotations, velocity labels from bounding boxes, or pretrained optical flow models. We propose a self-supervised method for 3D occupancy flow estimation that eliminates the need for human-produced annotations or external flow supervision. Our method disentangles the scene into separate static and dynamic signed distance fields and learns motion implicitly through temporal aggregation. Additionally, we introduce a strong self-supervised flow cue derived from features' cosine similarities. We demonstrate the efficacy of our 3D occupancy flow method on SemanticKITTI, KITTI-MOT, and nuScenes.

