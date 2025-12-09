---
layout: default
title: Structure-Aware Feature Rectification with Region Adjacency Graphs for Training-Free Open-Vocabulary Semantic Segmentation
---

# Structure-Aware Feature Rectification with Region Adjacency Graphs for Training-Free Open-Vocabulary Semantic Segmentation
**arXiv**：[2512.07360v1](https://arxiv.org/abs/2512.07360) · [PDF](https://arxiv.org/pdf/2512.07360.pdf)  
**作者**：Qiming Huang, Hao Ai, Jianbo Jiao  

**一句话要点**：提出基于区域邻接图的结构感知特征校正方法，以提升无训练开放词汇语义分割的局部一致性。

**关键词**：开放词汇语义分割, 结构感知特征校正, 区域邻接图, 无训练方法, 局部一致性

## 3 点简述
- 核心问题：CLIP模型在开放词汇语义分割中因全局语义对齐导致局部区域预测噪声和不一致。
- 方法要点：利用低层特征构建区域邻接图，捕获局部结构关系，校正CLIP特征以增强局部判别力。
- 实验或效果：在多个开放词汇分割基准上有效抑制噪声，提升区域一致性，实现强性能。

## 摘要（原文）

> Benefiting from the inductive biases learned from large-scale datasets, open-vocabulary semantic segmentation (OVSS) leverages the power of vision-language models, such as CLIP, to achieve remarkable progress without requiring task-specific training. However, due to CLIP's pre-training nature on image-text pairs, it tends to focus on global semantic alignment, resulting in suboptimal performance when associating fine-grained visual regions with text. This leads to noisy and inconsistent predictions, particularly in local areas. We attribute this to a dispersed bias stemming from its contrastive training paradigm, which is difficult to alleviate using CLIP features alone. To address this, we propose a structure-aware feature rectification approach that incorporates instance-specific priors derived directly from the image. Specifically, we construct a region adjacency graph (RAG) based on low-level features (e.g., colour and texture) to capture local structural relationships and use it to refine CLIP features by enhancing local discrimination. Extensive experiments show that our method effectively suppresses segmentation noise, improves region-level consistency, and achieves strong performance on multiple open-vocabulary segmentation benchmarks.

