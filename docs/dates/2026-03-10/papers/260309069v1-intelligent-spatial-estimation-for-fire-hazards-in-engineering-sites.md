---
layout: default
title: Intelligent Spatial Estimation for Fire Hazards in Engineering Sites: An Enhanced YOLOv8-Powered Proximity Analysis Framework
---

# Intelligent Spatial Estimation for Fire Hazards in Engineering Sites: An Enhanced YOLOv8-Powered Proximity Analysis Framework
**arXiv**：[2603.09069v1](https://arxiv.org/abs/2603.09069) · [PDF](https://arxiv.org/pdf/2603.09069.pdf)  
**作者**：Ammar K. AlMhdawi, Nonso Nnamoko, Alaa Mashan Ubaid  

**一句话要点**：提出增强型YOLOv8双模型框架，用于工程现场火灾检测与邻近风险分析

**关键词**：火灾检测, 邻近分析, YOLOv8, 风险评估, 实例分割, 工程安全

## 3 点简述
- 核心问题：传统视觉监测仅检测火灾，缺乏对邻近风险的量化评估。
- 方法要点：结合YOLOv8实例分割与COCO预训练检测模型，计算像素距离并转换为实际测量。
- 实验或效果：在9860张图像数据集上，精度、召回率和F1分数超90%，mAP@0.5高于91%。

## 摘要（原文）

> This study proposes an enhanced dual-model YOLOv8 framework for intelligent fire detection and proximity-aware risk assessment, extending conventional vision-based monitoring beyond simple detection to actionable hazard prioritization. The system is trained on a dataset of 9,860 annotated images to segment fire and smoke across complex environments. The framework combines a primary YOLOv8 instance segmentation model for fire and smoke detection with a secondary object detection model pretrained on the COCO dataset to identify surrounding entities such as people, vehicles, and infrastructure. By integrating the outputs of both models, the system computes pixel-based distances between detected fire regions and nearby objects and converts these values into approximate real-world measurements using a pixel-to-meter scaling approach. This proximity information is incorporated into a risk assessment mechanism that combines fire evidence, object vulnerability, and distance-based exposure to produce a quantitative risk score and alert level. The proposed framework achieves strong performance, with precision, recall, and F1 scores exceeding 90% and mAP@0.5 above 91%. The system generates annotated visual outputs showing fire locations, detected objects, estimated distances, and contextual risk information to support situational awareness. Implemented using open-source tools within the Google Colab environment, the framework is lightweight and suitable for deployment in industrial and resource-constrained settings.

