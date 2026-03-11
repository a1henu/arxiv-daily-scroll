---
layout: default
title: DRIFT: Dual-Representation Inter-Fusion Transformer for Automated Driving Perception with 4D Radar Point Clouds
---

# DRIFT: Dual-Representation Inter-Fusion Transformer for Automated Driving Perception with 4D Radar Point Clouds
**arXiv**：[2603.09695v1](https://arxiv.org/abs/2603.09695) · [PDF](https://arxiv.org/pdf/2603.09695.pdf)  
**作者**：Siqi Pei, Andras Palffy, Dariu M. Gavrila  

**一句话要点**：提出DRIFT模型，通过双路径架构融合局部与全局特征，提升4D雷达点云在自动驾驶感知中的性能。

**关键词**：4D雷达点云, 自动驾驶感知, 双路径架构, 特征融合, 目标检测, 自由道路估计

## 3 点简述
- 核心问题：4D雷达点云密度低，需有效利用局部和全局上下文信息。
- 方法要点：采用点路径和柱路径并行处理，通过特征共享层融合双表示。
- 实验或效果：在VoD数据集上，mAP达52.6%，优于CenterPoint等基线。

## 摘要（原文）

> 4D radars, which provide 3D point cloud data along with Doppler velocity, are attractive components of modern automated driving systems due to their low cost and robustness under adverse weather conditions. However, they provide a significantly lower point cloud density than LiDAR sensors. This makes it important to exploit not only local but also global contextual scene information. This paper proposes DRIFT, a model that effectively captures and fuses both local and global contexts through a dual-path architecture. The model incorporates a point path to aggregate fine-grained local features and a pillar path to encode coarse-grained global features. These two parallel paths are intertwined via novel feature-sharing layers at multiple stages, enabling full utilization of both representations. DRIFT is evaluated on the widely used View-of-Delft (VoD) dataset and a proprietary internal dataset. It outperforms the baselines on the tasks of object detection and/or free road estimation. For example, DRIFT achieves a mean average precision (mAP) of 52.6\% (compared to, say, 45.4\% of CenterPoint) on the VoD dataset.

