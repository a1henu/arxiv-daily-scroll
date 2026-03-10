---
layout: default
title: ER-Pose: Rethinking Keypoint-Driven Representation Learning for Real-Time Human Pose Estimation
---

# ER-Pose: Rethinking Keypoint-Driven Representation Learning for Real-Time Human Pose Estimation
**arXiv**：[2603.08681v1](https://arxiv.org/abs/2603.08681) · [PDF](https://arxiv.org/pdf/2603.08681.pdf)  
**作者**：Nanjun Li, Pinqi Cheng, Zean Liu, Minghe Tian, Xuanyin Wang  

**一句话要点**：提出ER-Pose，通过关键点驱动学习范式解决单阶段多人姿态估计中的任务对齐问题

**关键词**：单阶段姿态估计, 关键点驱动学习, 动态样本分配, 平滑OKS损失, 实时推理, 多人姿态估计

## 3 点简述
- 核心问题：单阶段姿态估计沿用检测的框驱动范式，导致样本分配和特征表示偏差，限制精度
- 方法要点：移除框预测，设计关键点驱动头部和动态样本分配，引入平滑OKS损失优化回归
- 实验或效果：在MS COCO和CrowdPose上，ER-Pose-n相比YOLO-Pose提升AP，参数更少且推理高效

## 摘要（原文）

> Single-stage multi-person pose estimation aims to jointly perform human localization and keypoint prediction within a unified framework, offering advantages in inference efficiency and architectural simplicity. Consequently, multi-scale real-time detection architectures, such as YOLO-like models, are widely adopted for real-time pose estimation. However, these approaches typically inherit a box-driven modeling paradigm from object detection, in which pose estimation is implicitly constrained by bounding-box supervision during training. This formulation introduces biases in sample assignment and feature representation, resulting in task misalignment and ultimately limiting pose estimation accuracy. In this work, we revisit box-driven single-stage pose estimation from a keypoint-driven perspective and identify semantic conflicts among parallel objectives as a key source of performance degradation. To address this issue, we propose a keypoint-driven learning paradigm that elevates pose estimation to a primary prediction objective. Specifically, we remove bounding-box prediction and redesign the prediction head to better accommodate the high-dimensional structured representations for pose estimation. We further introduce a keypoint-driven dynamic sample assignment strategy to align training objectives with pose evaluation metrics, enabling dense supervision during training and efficient NMS-free inference. In addition, we propose a smooth OKS-based loss function to stabilize optimization in regression-based pose estimation. Based on these designs, we develop a single-stage multi-person pose estimation framework, termed ER-Pose. On MS COCO and CrowdPose, ER-Pose-n achieves AP improvements of 3.2/6.7 without pre-training and 7.4/4.9 with pre-training respectively compared with the baseline YOLO-Pose. These improvements are achieved with fewer parameters and higher inference efficiency.

