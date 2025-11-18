---
layout: default
title: GUIDE: Gaussian Unified Instance Detection for Enhanced Obstacle Perception in Autonomous Driving
---

# GUIDE: Gaussian Unified Instance Detection for Enhanced Obstacle Perception in Autonomous Driving
**arXiv**：[2511.12941v1](https://arxiv.org/abs/2511.12941) · [PDF](https://arxiv.org/pdf/2511.12941.pdf)  
**作者**：Chunyong Hu, Qi Luo, Jianyun Xu, Song Wang, Qiang Li, Sheng Yang  

**一句话要点**：提出GUIDE框架，利用3D高斯实现实例检测与占用预测，以解决自动驾驶中不规则障碍物感知问题。

**关键词**：自动驾驶感知, 3D高斯建模, 实例检测, 占用预测, 稀疏表示, 障碍物跟踪

## 3 点简述
- 核心问题：传统3D边界框方法难以准确表示不规则形状障碍物，影响自动驾驶决策。
- 方法要点：采用稀疏表示策略，通过高斯到体素投影提供细粒度实例级占用数据，降低计算成本。
- 实验或效果：在nuScenes数据集上实例占用mAP达21.61，比现有方法提升50%，并具备竞争性跟踪能力。

## 摘要（原文）

> In the realm of autonomous driving, accurately detecting surrounding obstacles is crucial for effective decision-making. Traditional methods primarily rely on 3D bounding boxes to represent these obstacles, which often fail to capture the complexity of irregularly shaped, real-world objects. To overcome these limitations, we present GUIDE, a novel framework that utilizes 3D Gaussians for instance detection and occupancy prediction. Unlike conventional occupancy prediction methods, GUIDE also offers robust tracking capabilities. Our framework employs a sparse representation strategy, using Gaussian-to-Voxel Splatting to provide fine-grained, instance-level occupancy data without the computational demands associated with dense voxel grids. Experimental validation on the nuScenes dataset demonstrates GUIDE's performance, with an instance occupancy mAP of 21.61, marking a 50\% improvement over existing methods, alongside competitive tracking capabilities. GUIDE establishes a new benchmark in autonomous perception systems, effectively combining precision with computational efficiency to better address the complexities of real-world driving environments.

