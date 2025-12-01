---
layout: default
title: DAONet-YOLOv8: An Occlusion-Aware Dual-Attention Network for Tea Leaf Pest and Disease Detection
---

# DAONet-YOLOv8: An Occlusion-Aware Dual-Attention Network for Tea Leaf Pest and Disease Detection
**arXiv**：[2511.23222v1](https://arxiv.org/abs/2511.23222) · [PDF](https://arxiv.org/pdf/2511.23222.pdf)  
**作者**：Yefeng Wu, Shan Wan, Ling Wu, Yecheng Zhao  

**一句话要点**：提出DAONet-YOLOv8以解决茶园复杂背景下茶叶病虫害检测中的遮挡问题

**关键词**：茶叶病虫害检测, 遮挡感知网络, 双注意力机制, YOLOv8改进, 动态合成卷积, 茶园图像分析

## 3 点简述
- 核心问题：茶园复杂背景、光照变化和枝叶遮挡导致现有检测器漏检和误检。
- 方法要点：引入双注意力融合模块、遮挡感知检测头和动态合成卷积模块，增强特征提取和遮挡处理能力。
- 实验或效果：在真实茶园数据集上，精度、召回率和mAP均优于YOLOv8n基线，参数减少16.7%。

## 摘要（原文）

> Accurate detection of tea leaf pests and diseases in real plantations remains challenging due to complex backgrounds, variable illumination, and frequent occlusions among dense branches and leaves. Existing detectors often suffer from missed detections and false positives in such scenarios. To address these issues, we propose DAONet-YOLOv8, an enhanced YOLOv8 variant with three key improvements: (1) a Dual-Attention Fusion Module (DAFM) that combines convolutional local feature extraction with self-attention based global context modeling to focus on subtle lesion regions while suppressing background noise; (2) an occlusion-aware detection head (Detect-OAHead) that learns the relationship between visible and occluded parts to compensate for missing lesion features; and (3) a C2f-DSConv module employing dynamic synthesis convolutions with multiple kernel shapes to better capture irregular lesion boundaries. Experiments on our real-world tea plantation dataset containing six pest and disease categories demonstrate that DAONet-YOLOv8 achieves 92.97% precision, 92.80% recall, 97.10% mAP@50 and 76.90% mAP@50:95, outperforming the YOLOv8n baseline by 2.34, 4.68, 1.40 and 1.80 percentage points respectively, while reducing parameters by 16.7%. Comparative experiments further confirm that DAONet-YOLOv8 achieves superior performance over mainstream detection models.

