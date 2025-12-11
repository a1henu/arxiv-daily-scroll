---
layout: default
title: NordFKB: a fine-grained benchmark dataset for geospatial AI in Norway
---

# NordFKB: a fine-grained benchmark dataset for geospatial AI in Norway
**arXiv**：[2512.09913v1](https://arxiv.org/abs/2512.09913) · [PDF](https://arxiv.org/pdf/2512.09913.pdf)  
**作者**：Sander Riisøen Jyhne, Aditya Gupta, Ben Worsley, Marianne Andersen, Ivar Oveland, Alexander Salveson Nossum  

**一句话要点**：提出NordFKB细粒度基准数据集，用于挪威地理空间AI研究

**关键词**：地理空间AI, 细粒度数据集, 语义分割, 目标检测, 挪威地理数据, 基准评估

## 3 点简述
- 核心问题：缺乏挪威地理空间AI的细粒度基准数据集，限制方法评估与比较。
- 方法要点：基于权威FKB数据，提供高分辨率正射影像与36类语义标注，覆盖七地理区域。
- 实验或效果：发布标准化评估协议与工具，支持语义分割与目标检测，确保可复现研究。

## 摘要（原文）

> We present NordFKB, a fine-grained benchmark dataset for geospatial AI in Norway, derived from the authoritative, highly accurate, national Felles KartdataBase (FKB). The dataset contains high-resolution orthophotos paired with detailed annotations for 36 semantic classes, including both per-class binary segmentation masks in GeoTIFF format and COCO-style bounding box annotations. Data is collected from seven geographically diverse areas, ensuring variation in climate, topography, and urbanization. Only tiles containing at least one annotated object are included, and training/validation splits are created through random sampling across areas to ensure representative class and context distributions. Human expert review and quality control ensures high annotation accuracy. Alongside the dataset, we release a benchmarking repository with standardized evaluation protocols and tools for semantic segmentation and object detection, enabling reproducible and comparable research. NordFKB provides a robust foundation for advancing AI methods in mapping, land administration, and spatial planning, and paves the way for future expansions in coverage, temporal scope, and data modalities.

