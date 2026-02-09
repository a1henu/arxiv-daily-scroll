---
layout: default
title: BrokenBind: Universal Modality Exploration beyond Dataset Boundaries
---

# BrokenBind: Universal Modality Exploration beyond Dataset Boundaries
**arXiv**：[2602.06451v1](https://arxiv.org/abs/2602.06451) · [PDF](https://arxiv.org/pdf/2602.06451.pdf)  
**作者**：Zhuo Huang, Runnan Chen, Bo Han, Gang Niu, Masashi Sugiyama, Tongliang Liu  

**一句话要点**：提出BrokenBind以解决多模态学习中数据集限制导致的泛化问题

**关键词**：多模态学习, 伪嵌入生成, 数据集泛化, 模态绑定, 低数据学习

## 3 点简述
- 核心问题：现有方法受限于数据集模态，泛化到未见模态时存在偏差
- 方法要点：利用多个数据集生成伪嵌入，绑定不同数据集的模态以实现通用探索
- 实验或效果：在低数据场景和复杂绑定中优于基线方法，验证了有效性

## 摘要（原文）

> Multi-modal learning combines various modalities to provide a comprehensive understanding of real-world problems. A common strategy is to directly bind different modalities together in a specific joint embedding space. However, the capability of existing methods is restricted within the modalities presented in the given dataset, thus they are biased when generalizing to unpresented modalities in downstream tasks. As a result, due to such inflexibility, the viability of previous methods is seriously hindered by the cost of acquiring multi-modal datasets. In this paper, we introduce BrokenBind, which focuses on binding modalities that are presented from different datasets. To achieve this, BrokenBind simultaneously leverages multiple datasets containing the modalities of interest and one shared modality. Though the two datasets do not correspond to each other due to distribution mismatch, we can capture their relationship to generate pseudo embeddings to fill in the missing modalities of interest, enabling flexible and generalized multi-modal learning. Under our framework, any two modalities can be bound together, free from the dataset limitation, to achieve universal modality exploration. Further, to reveal the capability of our method, we study intensified scenarios where more than two datasets are needed for modality binding and show the effectiveness of BrokenBind in low-data regimes. Through extensive evaluation, we carefully justify the superiority of BrokenBind compared to well-known multi-modal baseline methods.

