---
layout: default
title: Training Together, Diagnosing Better: Federated Learning for Collagen VI-Related Dystrophies
---

# Training Together, Diagnosing Better: Federated Learning for Collagen VI-Related Dystrophies
**arXiv**：[2512.16876v1](https://arxiv.org/abs/2512.16876) · [PDF](https://arxiv.org/pdf/2512.16876.pdf)  
**作者**：Astrid Brull, Sara Aguti, Véronique Bolduc, Ying Hu, Daniel M. Jimenez-Gutierrez, Enrique Zuazua, Joaquin Del-Rio, Oleksii Sliusarenko, Haiyan Zhou, Francesco Muntoni, Carsten G. Bönnemann, Xabi Uribe-Etxebarria  

**一句话要点**：提出联邦学习方案以解决胶原VI相关肌营养不良症诊断中的数据稀缺与隐私问题

**关键词**：联邦学习, 罕见病诊断, 胶原VI相关肌营养不良症, 医学图像分析, 隐私保护, 机器学习模型

## 3 点简述
- 核心问题：罕见病诊断因数据稀缺和隐私法规限制，难以跨机构共享数据。
- 方法要点：使用Sherpa.ai联邦学习平台，在分布式数据集上协作训练模型，保持数据本地化。
- 实验或效果：模型分类三种致病机制，F1分数达0.82，优于单机构模型（0.57-0.75）。

## 摘要（原文）

> The application of Machine Learning (ML) to the diagnosis of rare diseases, such as collagen VI-related dystrophies (COL6-RD), is fundamentally limited by the scarcity and fragmentation of available data. Attempts to expand sampling across hospitals, institutions, or countries with differing regulations face severe privacy, regulatory, and logistical obstacles that are often difficult to overcome. The Federated Learning (FL) provides a promising solution by enabling collaborative model training across decentralized datasets while keeping patient data local and private. Here, we report a novel global FL initiative using the Sherpa.ai FL platform, which leverages FL across distributed datasets in two international organizations for the diagnosis of COL6-RD, using collagen VI immunofluorescence microscopy images from patient-derived fibroblast cultures. Our solution resulted in an ML model capable of classifying collagen VI patient images into the three primary pathogenic mechanism groups associated with COL6-RD: exon skipping, glycine substitution, and pseudoexon insertion. This new approach achieved an F1-score of 0.82, outperforming single-organization models (0.57-0.75). These results demonstrate that FL substantially improves diagnostic utility and generalizability compared to isolated institutional models. Beyond enabling more accurate diagnosis, we anticipate that this approach will support the interpretation of variants of uncertain significance and guide the prioritization of sequencing strategies to identify novel pathogenic variants.

