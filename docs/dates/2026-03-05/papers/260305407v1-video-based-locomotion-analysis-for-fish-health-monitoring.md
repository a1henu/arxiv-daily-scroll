---
layout: default
title: Video-based Locomotion Analysis for Fish Health Monitoring
---

# Video-based Locomotion Analysis for Fish Health Monitoring
**arXiv**：[2603.05407v1](https://arxiv.org/abs/2603.05407) · [PDF](https://arxiv.org/pdf/2603.05407.pdf)  
**作者**：Timon Palm, Clemens Seibold, Anna Hilsmann, Peter Eisert  

**一句话要点**：提出基于视频多目标跟踪的鱼类运动分析系统，用于健康监测

**关键词**：鱼类健康监测, 视频分析, 多目标跟踪, YOLOv11, 运动分析, 水产养殖

## 3 点简述
- 核心问题：通过分析鱼类运动活动推断其生理和病理状态，以早期检测疾病并保障动物福利。
- 方法要点：采用YOLOv11检测器嵌入检测跟踪框架，并探索多帧融合以提升检测精度。
- 实验或效果：在家庭水族箱环境中手动标注的苏拉威西米鱼数据集上评估，能可靠测量游泳方向和速度。

## 摘要（原文）

> Monitoring the health conditions of fish is essential, as it enables the early detection of disease, safeguards animal welfare, and contributes to sustainable aquaculture practices. Physiological and pathological conditions of cultivated fish can be inferred by analyzing locomotion activities. In this paper, we present a system that estimates the locomotion activities from videos using multi object tracking. The core of our approach is a YOLOv11 detector embedded in a tracking-by-detection framework. We investigate various configurations of the YOLOv11-architecture as well as extensions that incorporate multiple frames to improve detection accuracy. Our system is evaluated on a manually annotated dataset of Sulawesi ricefish recorded in a home-aquarium-like setup, demonstrating its ability to reliably measure swimming direction and speed for fish health monitoring. The dataset will be made publicly available upon publication.

