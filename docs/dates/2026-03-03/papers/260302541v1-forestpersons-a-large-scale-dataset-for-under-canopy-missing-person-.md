---
layout: default
title: ForestPersons: A Large-Scale Dataset for Under-Canopy Missing Person Detection
---

# ForestPersons: A Large-Scale Dataset for Under-Canopy Missing Person Detection
**arXiv**：[2603.02541v1](https://arxiv.org/abs/2603.02541) · [PDF](https://arxiv.org/pdf/2603.02541.pdf)  
**作者**：Deokyun Kim, Jeongjun Lee, Jungwon Choi, Jonggeon Park, Giyoung Lee, Yookyung Kim, Myungseok Ki, Juho Lee, Jihun Cha  

**一句话要点**：提出ForestPersons数据集以解决森林冠层下失踪人员检测的挑战

**关键词**：森林搜救, 冠层下检测, 遮挡感知, 微飞行器, 大规模数据集, 人员检测

## 3 点简述
- 森林冠层遮挡导致无人机航拍图像难以检测失踪人员，需冠层下视角
- ForestPersons包含96,482张图像和204,078个标注，支持遮挡感知分析
- 基线评估显示现有模型性能有限，凸显数据集对搜救任务的重要性

## 摘要（原文）

> Detecting missing persons in forest environments remains a challenge, as dense canopy cover often conceals individuals from detection in top-down or oblique aerial imagery typically captured by Unmanned Aerial Vehicles (UAVs). While UAVs are effective for covering large, inaccessible areas, their aerial perspectives often miss critical visual cues beneath the forest canopy. This limitation underscores the need for under-canopy perspectives better suited for detecting missing persons in such environments. To address this gap, we introduce ForestPersons, a novel large-scale dataset specifically designed for under-canopy person detection. ForestPersons contains 96,482 images and 204,078 annotations collected under diverse environmental and temporal conditions. Each annotation includes a bounding box, pose, and visibility label for occlusion-aware analysis. ForestPersons provides ground-level and low-altitude perspectives that closely reflect the visual conditions encountered by Micro Aerial Vehicles (MAVs) during forest Search and Rescue (SAR) missions. Our baseline evaluations reveal that standard object detection models, trained on prior large-scale object detection datasets or SAR-oriented datasets, show limited performance on ForestPersons. This indicates that prior benchmarks are not well aligned with the challenges of missing person detection under the forest canopy. We offer this benchmark to support advanced person detection capabilities in real-world SAR scenarios. The dataset is publicly available at https://huggingface.co/datasets/etri/ForestPersons.

