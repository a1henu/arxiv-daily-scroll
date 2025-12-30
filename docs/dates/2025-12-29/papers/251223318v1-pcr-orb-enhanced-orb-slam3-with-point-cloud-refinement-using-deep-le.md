---
layout: default
title: PCR-ORB: Enhanced ORB-SLAM3 with Point Cloud Refinement Using Deep Learning-Based Dynamic Object Filtering
---

# PCR-ORB: Enhanced ORB-SLAM3 with Point Cloud Refinement Using Deep Learning-Based Dynamic Object Filtering
**arXiv**：[2512.23318v1](https://arxiv.org/abs/2512.23318) · [PDF](https://arxiv.org/pdf/2512.23318.pdf)  
**作者**：Sheng-Kai Chen, Jie-Yu Chao, Jr-Yu Chang, Po-Lien Wu, Po-Chiang Lin  

**一句话要点**：提出PCR-ORB，通过深度学习点云精炼增强ORB-SLAM3以应对动态环境挑战。

**关键词**：动态SLAM, 点云精炼, 语义分割, ORB-SLAM3, 实时处理

## 3 点简述
- 核心问题：动态环境中移动物体影响vSLAM的跟踪精度和地图一致性。
- 方法要点：集成YOLOv8语义分割与CUDA加速，采用多阶段过滤策略进行点云精炼。
- 实验或效果：在KITTI数据集上评估，部分序列性能显著提升，但效果因场景而异。

## 摘要（原文）

> Visual Simultaneous Localization and Mapping (vSLAM) systems encounter substantial challenges in dynamic environments where moving objects compromise tracking accuracy and map consistency. This paper introduces PCR-ORB (Point Cloud Refinement ORB), an enhanced ORB-SLAM3 framework that integrates deep learning-based point cloud refinement to mitigate dynamic object interference. Our approach employs YOLOv8 for semantic segmentation combined with CUDA-accelerated processing to achieve real-time performance. The system implements a multi-stage filtering strategy encompassing ground plane estimation, sky region removal, edge filtering, and temporal consistency validation. Comprehensive evaluation on the KITTI dataset (sequences 00-09) demonstrates performance characteristics across different environmental conditions and scene types. Notable improvements are observed in specific sequences, with sequence 04 achieving 25.9% improvement in ATE RMSE and 30.4% improvement in ATE median. However, results show mixed performance across sequences, indicating scenario-dependent effectiveness. The implementation provides insights into dynamic object filtering challenges and opportunities for robust navigation in complex environments.

