---
layout: default
title: Modeling 3D Pedestrian-Vehicle Interactions for Vehicle-Conditioned Pose Forecasting
---

# Modeling 3D Pedestrian-Vehicle Interactions for Vehicle-Conditioned Pose Forecasting
**arXiv**：[2602.08962v1](https://arxiv.org/abs/2602.08962) · [PDF](https://arxiv.org/pdf/2602.08962.pdf)  
**作者**：Guangxun Zhu, Xuan Liu, Nicolas Pugeault, Chongfeng Wei, Edmond S. L. Ho  

**一句话要点**：提出3D车辆条件化行人姿态预测框架，以增强自动驾驶中行人-车辆交互建模。

**关键词**：3D姿态预测, 行人-车辆交互, 自动驾驶, 跨注意力机制, 多智能体建模

## 3 点简述
- 核心问题：在复杂城市环境中准确预测行人运动对自动驾驶安全至关重要，需考虑车辆交互。
- 方法要点：基于TBIFormer架构，引入车辆编码器和行人-车辆交互跨注意力模块，融合历史行人运动与周围车辆信息。
- 实验或效果：通过增强Waymo-3DSkelMo数据集并进行广泛实验，显著提升预测准确性，验证了车辆感知3D姿态预测的重要性。

## 摘要（原文）

> Accurately predicting pedestrian motion is crucial for safe and reliable autonomous driving in complex urban environments. In this work, we present a 3D vehicle-conditioned pedestrian pose forecasting framework that explicitly incorporates surrounding vehicle information. To support this, we enhance the Waymo-3DSkelMo dataset with aligned 3D vehicle bounding boxes, enabling realistic modeling of multi-agent pedestrian-vehicle interactions. We introduce a sampling scheme to categorize scenes by pedestrian and vehicle count, facilitating training across varying interaction complexities. Our proposed network adapts the TBIFormer architecture with a dedicated vehicle encoder and pedestrian-vehicle interaction cross-attention module to fuse pedestrian and vehicle features, allowing predictions to be conditioned on both historical pedestrian motion and surrounding vehicles. Extensive experiments demonstrate substantial improvements in forecasting accuracy and validate different approaches for modeling pedestrian-vehicle interactions, highlighting the importance of vehicle-aware 3D pose prediction for autonomous driving. Code is available at: https://github.com/GuangxunZhu/VehCondPose3D

