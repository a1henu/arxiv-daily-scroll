---
layout: default
title: MetaRank: Task-Aware Metric Selection for Model Transferability Estimation
---

# MetaRank: Task-Aware Metric Selection for Model Transferability Estimation
**arXiv**：[2511.21007v1](https://arxiv.org/abs/2511.21007) · [PDF](https://arxiv.org/pdf/2511.21007.pdf)  
**作者**：Yuhang Liu, Wenjie Zhao, Yunhui Guo  

**一句话要点**：提出MetaRank框架以解决迁移学习中模型可迁移性估计的度量选择问题

**关键词**：模型可迁移性估计, 元学习, 度量选择, 迁移学习, 文本嵌入, 学习排序

## 3 点简述
- 核心问题：MTE度量选择依赖任务，无通用最优度量，导致选择效率低
- 方法要点：使用元学习框架，编码数据集和度量文本描述，学习度量排名
- 实验或效果：在11个模型和11个数据集上验证，MetaRank显著提升度量选择效果

## 摘要（原文）

> Selecting an appropriate pre-trained source model is a critical, yet computationally expensive, task in transfer learning. Model Transferability Estimation (MTE) methods address this by providing efficient proxy metrics to rank models without full fine-tuning. In practice, the choice of which MTE metric to use is often ad hoc or guided simply by a metric's average historical performance. However, we observe that the effectiveness of MTE metrics is highly task-dependent and no single metric is universally optimal across all target datasets. To address this gap, we introduce MetaRank, a meta-learning framework for automatic, task-aware MTE metric selection. We formulate metric selection as a learning-to-rank problem. Rather than relying on conventional meta-features, MetaRank encodes textual descriptions of both datasets and MTE metrics using a pretrained language model, embedding them into a shared semantic space. A meta-predictor is then trained offline on diverse meta-tasks to learn the intricate relationship between dataset characteristics and metric mechanisms, optimized with a listwise objective that prioritizes correctly ranking the top-performing metrics. During the subsequent online phase, MetaRank efficiently ranks the candidate MTE metrics for a new, unseen target dataset based on its textual description, enabling practitioners to select the most appropriate metric a priori. Extensive experiments across 11 pretrained models and 11 target datasets demonstrate the strong effectiveness of our approach.

