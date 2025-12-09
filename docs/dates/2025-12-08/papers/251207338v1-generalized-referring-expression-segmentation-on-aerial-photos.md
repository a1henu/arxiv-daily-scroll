---
layout: default
title: Generalized Referring Expression Segmentation on Aerial Photos
---

# Generalized Referring Expression Segmentation on Aerial Photos
**arXiv**：[2512.07338v1](https://arxiv.org/abs/2512.07338) · [PDF](https://arxiv.org/pdf/2512.07338.pdf)  
**作者**：Luís Marnoto, Alexandre Bernardino, Bruno Martins  

**一句话要点**：提出Aerial-D数据集与RSRefSeg架构，以解决航空影像中的指代表达分割挑战。

**关键词**：指代表达分割, 航空影像, 大规模数据集, LLM增强, 语义分割, 历史影像处理

## 3 点简述
- 核心问题：航空影像分辨率多变、色彩不一致、目标小且密集，导致指代表达分割困难。
- 方法要点：构建大规模Aerial-D数据集，结合规则生成与LLM增强，并采用RSRefSeg架构进行训练。
- 实验或效果：在当代基准上表现竞争性，对历史影像的单色、褪色和颗粒退化保持高精度。

## 摘要（原文）

> Referring expression segmentation is a fundamental task in computer vision that integrates natural language understanding with precise visual localization of target regions. Considering aerial imagery (e.g., modern aerial photos collected through drones, historical photos from aerial archives, high-resolution satellite imagery, etc.) presents unique challenges because spatial resolution varies widely across datasets, the use of color is not consistent, targets often shrink to only a few pixels, and scenes contain very high object densities and objects with partial occlusions. This work presents Aerial-D, a new large-scale referring expression segmentation dataset for aerial imagery, comprising 37,288 images with 1,522,523 referring expressions that cover 259,709 annotated targets, spanning across individual object instances, groups of instances, and semantic regions covering 21 distinct classes that range from vehicles and infrastructure to land coverage types. The dataset was constructed through a fully automatic pipeline that combines systematic rule-based expression generation with a Large Language Model (LLM) enhancement procedure that enriched both the linguistic variety and the focus on visual details within the referring expressions. Filters were additionally used to simulate historic imaging conditions for each scene. We adopted the RSRefSeg architecture, and trained models on Aerial-D together with prior aerial datasets, yielding unified instance and semantic segmentation from text for both modern and historical images. Results show that the combined training achieves competitive performance on contemporary benchmarks, while maintaining strong accuracy under monochrome, sepia, and grainy degradations that appear in archival aerial photography. The dataset, trained models, and complete software pipeline are publicly available at https://luispl77.github.io/aerial-d .

