---
layout: default
title: Graph Recognition via Subgraph Prediction
---

# Graph Recognition via Subgraph Prediction
**arXiv**：[2601.15133v1](https://arxiv.org/abs/2601.15133) · [PDF](https://arxiv.org/pdf/2601.15133.pdf)  
**作者**：André Eberhard, Gerhard Neumann, Pascal Friederich  

**一句话要点**：提出GraSP方法，通过子图预测实现图像中多样化图形的通用识别。

**关键词**：视觉图识别, 子图预测, 通用框架, 跨任务迁移, 图像分析

## 3 点简述
- 核心问题：视觉图识别缺乏统一方法，现有方案难以跨任务迁移。
- 方法要点：基于子图预测，设计通用框架，无需任务特定修改即可应用。
- 实验或效果：在合成基准和真实应用中验证，支持多种图形类型和绘制方式。

## 摘要（原文）

> Despite tremendous improvements in tasks such as image classification, object detection, and segmentation, the recognition of visual relationships, commonly modeled as the extraction of a graph from an image, remains a challenging task. We believe that this mainly stems from the fact that there is no canonical way to approach the visual graph recognition task. Most existing solutions are specific to a problem and cannot be transferred between different contexts out-of-the box, even though the conceptual problem remains the same. With broad applicability and simplicity in mind, in this paper we develop a method, \textbf{Gra}ph Recognition via \textbf{S}ubgraph \textbf{P}rediction (\textbf{GraSP}), for recognizing graphs in images. We show across several synthetic benchmarks and one real-world application that our method works with a set of diverse types of graphs and their drawings, and can be transferred between tasks without task-specific modifications, paving the way to a more unified framework for visual graph recognition.

