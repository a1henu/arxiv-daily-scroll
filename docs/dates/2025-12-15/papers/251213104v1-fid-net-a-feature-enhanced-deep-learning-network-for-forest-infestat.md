---
layout: default
title: FID-Net: A Feature-Enhanced Deep Learning Network for Forest Infestation Detection
---

# FID-Net: A Feature-Enhanced Deep Learning Network for Forest Infestation Detection
**arXiv**：[2512.13104v1](https://arxiv.org/abs/2512.13104) · [PDF](https://arxiv.org/pdf/2512.13104.pdf)  
**作者**：Yan Zhang, Baoxin Li, Han Sun, Yuhang Gao, Mingtai Zhang, Pei Wang  

**一句话要点**：提出FID-Net以解决无人机可见光图像中森林病虫害树木的检测与空间分析问题

**关键词**：森林病虫害检测, 无人机图像分析, 深度学习模型, 特征增强, 空间分析, YOLOv8

## 3 点简述
- 核心问题：传统方法在大规模、细粒度森林病虫害检测中存在局限性，需高效监测以维护生态系统稳定。
- 方法要点：基于YOLOv8n，引入特征增强模块、自适应多尺度特征融合模块和高效通道注意力机制，提升检测精度。
- 实验或效果：在32个森林样地数据集上，FID-Net在精度、召回率和mAP指标上优于主流YOLO模型，并支持空间分析。

## 摘要（原文）

> Forest pests threaten ecosystem stability, requiring efficient monitoring. To overcome the limitations of traditional methods in large-scale, fine-grained detection, this study focuses on accurately identifying infected trees and analyzing infestation patterns. We propose FID-Net, a deep learning model that detects pest-affected trees from UAV visible-light imagery and enables infestation analysis via three spatial metrics. Based on YOLOv8n, FID-Net introduces a lightweight Feature Enhancement Module (FEM) to extract disease-sensitive cues, an Adaptive Multi-scale Feature Fusion Module (AMFM) to align and fuse dual-branch features (RGB and FEM-enhanced), and an Efficient Channel Attention (ECA) mechanism to enhance discriminative information efficiently. From detection results, we construct a pest situation analysis framework using: (1) Kernel Density Estimation to locate infection hotspots; (2) neighborhood evaluation to assess healthy trees' infection risk; (3) DBSCAN clustering to identify high-density healthy clusters as priority protection zones. Experiments on UAV imagery from 32 forest plots in eastern Tianshan, China, show that FID-Net achieves 86.10% precision, 75.44% recall, 82.29% mAP@0.5, and 64.30% mAP@0.5:0.95, outperforming mainstream YOLO models. Analysis confirms infected trees exhibit clear clustering, supporting targeted forest protection. FID-Net enables accurate tree health discrimination and, combined with spatial metrics, provides reliable data for intelligent pest monitoring, early warning, and precise management.

