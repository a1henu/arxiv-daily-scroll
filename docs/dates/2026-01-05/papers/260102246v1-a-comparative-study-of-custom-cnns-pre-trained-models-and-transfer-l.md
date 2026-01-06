---
layout: default
title: A Comparative Study of Custom CNNs, Pre-trained Models, and Transfer Learning Across Multiple Visual Datasets
---

# A Comparative Study of Custom CNNs, Pre-trained Models, and Transfer Learning Across Multiple Visual Datasets
**arXiv**：[2601.02246v1](https://arxiv.org/abs/2601.02246) · [PDF](https://arxiv.org/pdf/2601.02246.pdf)  
**作者**：Annoor Sharara Akhand  

**一句话要点**：比较定制CNN、预训练模型与迁移学习在多个视觉数据集上的性能与效率

**关键词**：卷积神经网络, 迁移学习, 图像分类, 性能比较, 效率评估

## 3 点简述
- 核心问题：比较三种视觉识别范式（定制CNN、预训练特征提取、迁移学习）在真实数据集上的表现。
- 方法要点：在五个图像分类数据集上评估准确性、F1分数、训练时间和参数数量。
- 实验或效果：迁移学习性能最佳，定制CNN在计算受限时提供效率-准确性平衡。

## 摘要（原文）

> Convolutional Neural Networks (CNNs) are a standard approach for visual recognition due to their capacity to learn hierarchical representations from raw pixels. In practice, practitioners often choose among (i) training a compact custom CNN from scratch, (ii) using a large pre-trained CNN as a fixed feature extractor, and (iii) performing transfer learning via partial or full fine-tuning of a pre-trained backbone. This report presents a controlled comparison of these three paradigms across five real-world image classification datasets spanning road-surface defect recognition, agricultural variety identification, fruit/leaf disease recognition, pedestrian walkway encroachment recognition, and unauthorized vehicle recognition. Models are evaluated using accuracy and macro F1-score, complemented by efficiency metrics including training time per epoch and parameter counts. The results show that transfer learning consistently yields the strongest predictive performance, while the custom CNN provides an attractive efficiency--accuracy trade-off, especially when compute and memory budgets are constrained.

