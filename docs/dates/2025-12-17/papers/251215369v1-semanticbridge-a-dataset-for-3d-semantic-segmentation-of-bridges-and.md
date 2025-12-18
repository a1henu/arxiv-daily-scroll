---
layout: default
title: SemanticBridge -- A Dataset for 3D Semantic Segmentation of Bridges and Domain Gap Analysis
---

# SemanticBridge -- A Dataset for 3D Semantic Segmentation of Bridges and Domain Gap Analysis
**arXiv**：[2512.15369v1](https://arxiv.org/abs/2512.15369) · [PDF](https://arxiv.org/pdf/2512.15369.pdf)  
**作者**：Maximilian Kellner, Mariana Ferrandon Cervantes, Yuandong Pan, Ruodan Lu, Ioannis Brilakis, Alexander Reiterer  

**一句话要点**：提出SemanticBridge数据集以解决桥梁3D语义分割及传感器差异导致的领域差距问题

**关键词**：3D语义分割, 桥梁检测, 领域差距分析, 传感器差异, 基础设施维护

## 3 点简述
- 核心问题：基础设施检测中桥梁3D语义分割缺乏专用数据集，传感器差异影响模型泛化。
- 方法要点：构建多国桥梁高分辨率3D扫描数据集，提供详细语义标签，支持自动化分割。
- 实验或效果：评估三种先进模型，发现传感器差异可导致mIoU下降达11.4%。

## 摘要（原文）

> We propose a novel dataset that has been specifically designed for 3D semantic segmentation of bridges and the domain gap analysis caused by varying sensors. This addresses a critical need in the field of infrastructure inspection and maintenance, which is essential for modern society. The dataset comprises high-resolution 3D scans of a diverse range of bridge structures from various countries, with detailed semantic labels provided for each. Our initial objective is to facilitate accurate and automated segmentation of bridge components, thereby advancing the structural health monitoring practice. To evaluate the effectiveness of existing 3D deep learning models on this novel dataset, we conduct a comprehensive analysis of three distinct state-of-the-art architectures. Furthermore, we present data acquired through diverse sensors to quantify the domain gap resulting from sensor variations. Our findings indicate that all architectures demonstrate robust performance on the specified task. However, the domain gap can potentially lead to a decline in the performance of up to 11.4% mIoU.

