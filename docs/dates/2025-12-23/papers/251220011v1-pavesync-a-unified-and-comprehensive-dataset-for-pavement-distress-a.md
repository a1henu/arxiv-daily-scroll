---
layout: default
title: PaveSync: A Unified and Comprehensive Dataset for Pavement Distress Analysis and Classification
---

# PaveSync: A Unified and Comprehensive Dataset for Pavement Distress Analysis and Classification
**arXiv**：[2512.20011v1](https://arxiv.org/abs/2512.20011) · [PDF](https://arxiv.org/pdf/2512.20011.pdf)  
**作者**：Blessing Agyei Kyem, Joshua Kofi Asamoah, Anthony Dontoh, Andrews Danyo, Eugene Denteh, Armstrong Aboah  

**一句话要点**：提出PaveSync数据集以解决路面缺陷检测中数据集标准化不足的问题。

**关键词**：路面缺陷检测, 数据集标准化, 目标检测, 基准测试, 零样本迁移

## 3 点简述
- 核心问题：现有数据集在标注风格、缺陷类型定义和格式上不一致，限制统一训练和模型泛化。
- 方法要点：整合多个公开来源，构建包含52747张图像、135277个边界框标注的标准化数据集，覆盖13种缺陷类型和多样真实条件。
- 实验或效果：通过YOLOv8-YOLOv12、Faster R-CNN和DETR等模型基准测试，展示数据集在多种场景下的竞争性能，支持零样本迁移。

## 摘要（原文）

> Automated pavement defect detection often struggles to generalize across diverse real-world conditions due to the lack of standardized datasets. Existing datasets differ in annotation styles, distress type definitions, and formats, limiting their integration for unified training. To address this gap, we introduce a comprehensive benchmark dataset that consolidates multiple publicly available sources into a standardized collection of 52747 images from seven countries, with 135277 bounding box annotations covering 13 distinct distress types. The dataset captures broad real-world variation in image quality, resolution, viewing angles, and weather conditions, offering a unique resource for consistent training and evaluation. Its effectiveness was demonstrated through benchmarking with state-of-the-art object detection models including YOLOv8-YOLOv12, Faster R-CNN, and DETR, which achieved competitive performance across diverse scenarios. By standardizing class definitions and annotation formats, this dataset provides the first globally representative benchmark for pavement defect detection and enables fair comparison of models, including zero-shot transfer to new environments.

