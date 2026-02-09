---
layout: default
title: CytoCrowd: A Multi-Annotator Benchmark Dataset for Cytology Image Analysis
---

# CytoCrowd: A Multi-Annotator Benchmark Dataset for Cytology Image Analysis
**arXiv**：[2602.06674v1](https://arxiv.org/abs/2602.06674) · [PDF](https://arxiv.org/pdf/2602.06674.pdf)  
**作者**：Yonghao Si, Xingyuan Zeng, Zhao Chen, Libin Zheng, Caleb Chen Cao, Lei Chen, Jian Yin  

**一句话要点**：提出CytoCrowd数据集以解决细胞学图像分析中标注不一致与评估标准缺失的问题

**关键词**：细胞学图像分析, 多标注者数据集, 医学图像基准, 标注聚合算法, 对象检测, 分类任务

## 3 点简述
- 核心问题：现有医学图像数据集常隐藏专家分歧或缺乏独立金标准，影响模型在真实场景的评估
- 方法要点：提供446张高分辨率图像，包含四位病理学家的原始冲突标注和一位资深专家的独立金标准
- 实验或效果：作为基准支持标准计算机视觉任务和标注聚合算法评估，实验展示了其挑战性和价值

## 摘要（原文）

> High-quality annotated datasets are crucial for advancing machine learning in medical image analysis. However, a critical gap exists: most datasets either offer a single, clean ground truth, which hides real-world expert disagreement, or they provide multiple annotations without a separate gold standard for objective evaluation. To bridge this gap, we introduce CytoCrowd, a new public benchmark for cytology analysis. The dataset features 446 high-resolution images, each with two key components: (1) raw, conflicting annotations from four independent pathologists, and (2) a separate, high-quality gold-standard ground truth established by a senior expert. This dual structure makes CytoCrowd a versatile resource. It serves as a benchmark for standard computer vision tasks, such as object detection and classification, using the ground truth. Simultaneously, it provides a realistic testbed for evaluating annotation aggregation algorithms that must resolve expert disagreements. We provide comprehensive baseline results for both tasks. Our experiments demonstrate the challenges presented by CytoCrowd and establish its value as a resource for developing the next generation of models for medical image analysis.

