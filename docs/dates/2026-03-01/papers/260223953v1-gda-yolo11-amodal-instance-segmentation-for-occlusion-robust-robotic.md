---
layout: default
title: GDA-YOLO11: Amodal Instance Segmentation for Occlusion-Robust Robotic Fruit Harvesting
---

# GDA-YOLO11: Amodal Instance Segmentation for Occlusion-Robust Robotic Fruit Harvesting
**arXiv**：[2602.23953v1](https://arxiv.org/abs/2602.23953) · [PDF](https://arxiv.org/pdf/2602.23953.pdf)  
**作者**：Caner Beldek, Emre Sariyildiz, Son Lam Phung, Gursel Alici  

**一句话要点**：提出GDA-YOLO11模态实例分割模型以增强机器人水果采摘的遮挡鲁棒性

**关键词**：模态实例分割, 机器人水果采摘, 遮挡鲁棒性, 非对称掩码损失, 采摘点估计, 农业自主系统

## 3 点简述
- 核心问题：遮挡导致水果检测与定位不准确，造成作物损失。
- 方法要点：结合架构改进与非对称掩码损失，推断完整水果掩码并估计采摘点。
- 实验或效果：在柑橘数据集上性能优于YOLO11n，遮挡场景下采摘成功率提升。

## 摘要（原文）

> Occlusion remains a critical challenge in robotic fruit harvesting, as undetected or inaccurately localised fruits often results in substantial crop losses. To mitigate this issue, we propose a harvesting framework using a new amodal segmentation model, GDA-YOLO11, which incorporates architectural improvements and an updated asymmetric mask loss. The proposed model is trained on a modified version of a public citrus dataset and evaluated on both the base dataset and occlusion-sensitive subsets with varying occlusion levels. Within the framework, full fruit masks, including invisible regions, are inferred by GDA-YOLO11, and picking points are subsequently estimated using the Euclidean distance transform. These points are then projected into 3D coordinates for robotic harvesting execution. Experiments were conducted using real citrus fruits in a controlled environment simulating occlusion scenarios. Notably, to the best of our knowledge, this study provides the first practical demonstration of amodal instance segmentation in robotic fruit harvesting. GDA-YOLO11 achieves a precision of 0.844, recall of 0.846, mAP@50 of 0.914, and mAP@50:95 of 0.636, outperforming YOLO11n by 5.1%, 1.3%, and 1.0% in precision, mAP@50, and mAP@50:95, respectively. The framework attains harvesting success rates of 92.59%, 85.18%, 48.14%, and 22.22% at zero to high occlusion levels, improving success by 3.5% under medium and high occlusion. These findings demonstrate that GDA-YOLO11 enhances occlusion robust segmentation and streamlines perception-to-action integration, paving the way for more reliable autonomous systems in agriculture.

