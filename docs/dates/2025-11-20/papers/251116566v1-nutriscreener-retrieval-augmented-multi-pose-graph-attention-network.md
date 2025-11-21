---
layout: default
title: NutriScreener: Retrieval-Augmented Multi-Pose Graph Attention Network for Malnourishment Screening
---

# NutriScreener: Retrieval-Augmented Multi-Pose Graph Attention Network for Malnourishment Screening
**arXiv**：[2511.16566v1](https://arxiv.org/abs/2511.16566) · [PDF](https://arxiv.org/pdf/2511.16566.pdf)  
**作者**：Misaal Khan, Mayank Vatsa, Kuldeep Singh, Richa Singh  

**一句话要点**：提出NutriScreener以解决儿童营养不良筛查的可扩展性问题

**关键词**：营养不良筛查, 图注意力网络, 知识检索, 多姿态检测, CLIP嵌入, 低资源环境

## 3 点简述
- 核心问题：儿童营养不良筛查方法劳动密集且难以扩展，阻碍早期干预。
- 方法要点：结合CLIP视觉嵌入、知识检索和图注意力网络，实现多姿态检测。
- 实验或效果：在临床研究中获高评分，跨数据集召回提升25%，RMSE降低3.5厘米。

## 摘要（原文）

> Child malnutrition remains a global crisis, yet existing screening methods are laborious and poorly scalable, hindering early intervention. In this work, we present NutriScreener, a retrieval-augmented, multi-pose graph attention network that combines CLIP-based visual embeddings, class-boosted knowledge retrieval, and context awareness to enable robust malnutrition detection and anthropometric prediction from children's images, simultaneously addressing generalizability and class imbalance. In a clinical study, doctors rated it 4.3/5 for accuracy and 4.6/5 for efficiency, confirming its deployment readiness in low-resource settings. Trained and tested on 2,141 children from AnthroVision and additionally evaluated on diverse cross-continent populations, including ARAN and an in-house collected CampusPose dataset, it achieves 0.79 recall, 0.82 AUC, and significantly lower anthropometric RMSEs, demonstrating reliable measurement in unconstrained pediatric settings. Cross-dataset results show up to 25% recall gain and up to 3.5 cm RMSE reduction using demographically matched knowledge bases. NutriScreener offers a scalable and accurate solution for early malnutrition detection in low-resource environments.

