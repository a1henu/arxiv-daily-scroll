---
layout: default
title: Active Learning-Driven Lightweight YOLOv9: Enhancing Efficiency in Smart Agriculture
---

# Active Learning-Driven Lightweight YOLOv9: Enhancing Efficiency in Smart Agriculture
**arXiv**：[2601.22732v1](https://arxiv.org/abs/2601.22732) · [PDF](https://arxiv.org/pdf/2601.22732.pdf)  
**作者**：Hung-Chih Tu, Bo-Syun Chen, Yun-Chien Cheng  

**一句话要点**：提出主动学习驱动的轻量YOLOv9框架，以提升温室农业机器人实时检测效率

**关键词**：轻量目标检测, 主动学习, 农业机器人, 边缘计算, 多尺度检测, 类别不平衡

## 3 点简述
- 核心问题：温室环境中番茄和番茄花检测面临尺度变化、遮挡和类别不平衡挑战，影响实时部署精度。
- 方法要点：分析目标尺寸分布优化学习稳定性，集成轻量特征提取与注意力机制，采用主动学习策略选择高信息样本。
- 实验或效果：在有限标注下实现67.8% mAP，保持低参数量和推理成本，验证了智能农业应用的可行性。

## 摘要（原文）

> This study addresses the demand for real-time detection of tomatoes and tomato flowers by agricultural robots deployed on edge devices in greenhouse environments. Under practical imaging conditions, object detection systems often face challenges such as large scale variations caused by varying camera distances, severe occlusion from plant structures, and highly imbalanced class distributions. These factors make conventional object detection approaches that rely on fully annotated datasets difficult to simultaneously achieve high detection accuracy and deployment efficiency. To overcome these limitations, this research proposes an active learning driven lightweight object detection framework, integrating data analysis, model design, and training strategy. First, the size distribution of objects in raw agricultural images is analyzed to redefine an operational target range, thereby improving learning stability under real-world conditions. Second, an efficient feature extraction module is incorporated to reduce computational cost, while a lightweight attention mechanism is introduced to enhance feature representation under multi-scale and occluded scenarios. Finally, an active learning strategy is employed to iteratively select high-information samples for annotation and training under a limited labeling budget, effectively improving the recognition performance of minority and small-object categories. Experimental results demonstrate that, while maintaining a low parameter count and inference cost suitable for edge-device deployment, the proposed method effectively improves the detection performance of tomatoes and tomato flowers in raw images. Under limited annotation conditions, the framework achieves an overall detection accuracy of 67.8% mAP, validating its practicality and feasibility for intelligent agricultural applications.

