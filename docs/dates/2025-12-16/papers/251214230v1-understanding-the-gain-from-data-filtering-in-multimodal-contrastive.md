---
layout: default
title: Understanding the Gain from Data Filtering in Multimodal Contrastive Learning
---

# Understanding the Gain from Data Filtering in Multimodal Contrastive Learning
**arXiv**：[2512.14230v1](https://arxiv.org/abs/2512.14230) · [PDF](https://arxiv.org/pdf/2512.14230.pdf)  
**作者**：Divyansh Pareek, Sewoong Oh, Simon S. Du  

**一句话要点**：理论分析数据过滤在多模态对比学习中的增益，解释教师模型过滤的实证成功。

**关键词**：多模态对比学习, 数据过滤, 教师模型过滤, 理论分析, 误差界

## 3 点简述
- 核心问题：互联网规模多模态数据质量低，数据过滤对表示学习性能的影响未知。
- 方法要点：在线性对比学习设置下，理论推导过滤前后误差界，量化过滤增益。
- 实验或效果：证明教师过滤在大η和小η机制下分别将误差上界降至1/√(ηn)和1/√n。

## 摘要（原文）

> The success of modern multimodal representation learning relies on internet-scale datasets. Due to the low quality of a large fraction of raw web data, data curation has become a critical step in the training pipeline. Filtering using a trained model (i.e., teacher-based filtering) has emerged as a successful solution, leveraging a pre-trained model to compute quality scores. To explain the empirical success of teacher-based filtering, we characterize the performance of filtered contrastive learning under the standard bimodal data generation model. Denoting $η\in(0,1]$ as the fraction of data with correctly matched modalities among $n$ paired samples, we utilize a linear contrastive learning setup to show a provable benefit of data filtering: $(i)$ the error without filtering is upper and lower bounded by $\frac{1}{η\sqrt{n}}$, and $(ii)$ the error with teacher-based filtering is upper bounded by $\frac{1}{\sqrt{ηn}}$ in the large $η$ regime, and by $\frac{1}{\sqrt{n}}$ in the small $η$ regime.

