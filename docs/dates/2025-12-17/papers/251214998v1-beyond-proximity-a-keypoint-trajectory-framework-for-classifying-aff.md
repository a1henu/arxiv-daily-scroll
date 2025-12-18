---
layout: default
title: Beyond Proximity: A Keypoint-Trajectory Framework for Classifying Affiliative and Agonistic Social Networks in Dairy Cattle
---

# Beyond Proximity: A Keypoint-Trajectory Framework for Classifying Affiliative and Agonistic Social Networks in Dairy Cattle
**arXiv**：[2512.14998v1](https://arxiv.org/abs/2512.14998) · [PDF](https://arxiv.org/pdf/2512.14998.pdf)  
**作者**：Sibi Parivendan, Kashfia Sailunaz, Suresh Neethirajan  

**一句话要点**：提出基于关键点轨迹的框架，以区分奶牛亲和行为与攻击行为，提升精准畜牧中的社交网络分析。

**关键词**：关键点轨迹, 社交行为分类, 精准畜牧, 计算机视觉, 多目标跟踪, 姿态估计

## 3 点简述
- 核心问题：现有方法依赖静态接近阈值，无法在复杂牛舍环境中区分亲和行为与攻击行为，限制社交网络分析的客观性。
- 方法要点：通过YOLOv11、ByteTrack和ZebraPose构建端到端视觉流程，从关键点轨迹提取运动特征，用支持向量机分类行为。
- 实验或效果：在商业牛舍数据上，仅使用姿态信息实现77.51%的分类准确率，相比仅基于接近度的方法有显著提升。

## 摘要（原文）

> Precision livestock farming requires objective assessment of social behavior to support herd welfare monitoring, yet most existing approaches infer interactions using static proximity thresholds that cannot distinguish affiliative from agonistic behaviors in complex barn environments. This limitation constrains the interpretability of automated social network analysis in commercial settings. We present a pose-based computational framework for interaction classification that moves beyond proximity heuristics by modeling the spatiotemporal geometry of anatomical keypoints. Rather than relying on pixel-level appearance or simple distance measures, the proposed method encodes interaction-specific motion signatures from keypoint trajectories, enabling differentiation of social interaction valence. The framework is implemented as an end-to-end computer vision pipeline integrating YOLOv11 for object detection (mAP@0.50: 96.24%), supervised individual identification (98.24% accuracy), ByteTrack for multi-object tracking (81.96% accuracy), ZebraPose for 27-point anatomical keypoint estimation, and a support vector machine classifier trained on pose-derived distance dynamics. On annotated interaction clips collected from a commercial dairy barn, the classifier achieved 77.51% accuracy in distinguishing affiliative and agonistic behaviors using pose information alone. Comparative evaluation against a proximity-only baseline shows substantial gains in behavioral discrimination, particularly for affiliative interactions. The results establish a proof-of-concept for automated, vision-based inference of social interactions suitable for constructing interaction-aware social networks, with near-real-time performance on commodity hardware.

