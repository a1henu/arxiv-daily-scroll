---
layout: default
title: Multi-temporal Adaptive Red-Green-Blue and Long-Wave Infrared Fusion for You Only Look Once-Based Landmine Detection from Unmanned Aerial Systems
---

# Multi-temporal Adaptive Red-Green-Blue and Long-Wave Infrared Fusion for You Only Look Once-Based Landmine Detection from Unmanned Aerial Systems
**arXiv**：[2512.20487v1](https://arxiv.org/abs/2512.20487) · [PDF](https://arxiv.org/pdf/2512.20487.pdf)  
**作者**：James E. Gallagher, Edward J. Oughton, Jana Kosecka  

**一句话要点**：提出自适应RGB与LWIR融合方法，基于YOLO架构优化无人机系统对地表地雷的检测性能。

**关键词**：地雷检测, 无人机系统, 多模态融合, YOLO架构, 热红外成像

## 3 点简述
- 核心问题：地表地雷检测面临热对比度利用不足，影响人道主义排雷效率。
- 方法要点：采用多时相自适应RGB与LWIR融合，结合YOLO架构增强特征提取。
- 实验或效果：YOLOv11在最优参数下达到86.8% mAP，训练速度比RF-DETR快17.7倍。

## 摘要（原文）

> Landmines remain a persistent humanitarian threat, with 110 million actively deployed mines across 60 countries, claiming 26,000 casualties annually. This research evaluates adaptive Red-Green-Blue (RGB) and Long-Wave Infrared (LWIR) fusion for Unmanned Aerial Systems (UAS)-based detection of surface-laid landmines, leveraging the thermal contrast between the ordnance and the surrounding soil to enhance feature extraction. Using You Only Look Once (YOLO) architectures (v8, v10, v11) across 114 test images, generating 35,640 model-condition evaluations, YOLOv11 achieved optimal performance (86.8% mAP), with 10 to 30% thermal fusion at 5 to 10m altitude identified as the optimal detection parameters. A complementary architectural comparison revealed that while RF-DETR achieved the highest accuracy (69.2% mAP), followed by Faster R-CNN (67.6%), YOLOv11 (64.2%), and RetinaNet (50.2%), YOLOv11 trained 17.7 times faster than the transformer-based RF-DETR (41 minutes versus 12 hours), presenting a critical accuracy-efficiency tradeoff for operational deployment. Aggregated multi-temporal training datasets outperformed season-specific approaches by 1.8 to 9.6%, suggesting that models benefit from exposure to diverse thermal conditions. Anti-Tank (AT) mines achieved 61.9% detection accuracy, compared with 19.2% for Anti-Personnel (AP) mines, reflecting both the size differential and thermal-mass differences between these ordnance classes. As this research examined surface-laid mines where thermal contrast is maximized, future research should quantify thermal contrast effects for mines buried at varying depths across heterogeneous soil types.

