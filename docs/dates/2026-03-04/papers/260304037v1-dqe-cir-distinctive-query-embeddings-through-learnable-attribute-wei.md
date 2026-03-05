---
layout: default
title: DQE-CIR: Distinctive Query Embeddings through Learnable Attribute Weights and Target Relative Negative Sampling in Composed Image Retrieval
---

# DQE-CIR: Distinctive Query Embeddings through Learnable Attribute Weights and Target Relative Negative Sampling in Composed Image Retrieval
**arXiv**：[2603.04037v1](https://arxiv.org/abs/2603.04037) · [PDF](https://arxiv.org/pdf/2603.04037.pdf)  
**作者**：Geon Park, Ji-Hoon Park, Seong-Whan Lee  

**一句话要点**：提出DQE-CIR方法，通过可学习属性权重和目标相对负采样提升组合图像检索的查询区分度。

**关键词**：组合图像检索, 查询嵌入, 负采样, 属性权重, 对比学习, 细粒度检索

## 3 点简述
- 核心问题：现有方法在组合图像检索中因对比学习框架导致相关性抑制和语义混淆，查询表示区分度不足。
- 方法要点：引入可学习属性权重以强调文本条件视觉特征，并设计目标相对负采样选择信息性负样本。
- 实验或效果：未知，但方法旨在通过改进查询区分度和减少混淆，提升细粒度属性修改的检索可靠性。

## 摘要（原文）

> Composed image retrieval (CIR) addresses the task of retrieving a target image by jointly interpreting a reference image and a modification text that specifies the intended change. Most existing methods are still built upon contrastive learning frameworks that treat the ground truth image as the only positive instance and all remaining images as negatives. This strategy inevitably introduces relevance suppression, where semantically related yet valid images are incorrectly pushed away, and semantic confusion, where different modification intents collapse into overlapping regions of the embedding space. As a result, the learned query representations often lack discriminativeness, particularly at fine-grained attribute modifications. To overcome these limitations, we propose distinctive query embeddings through learnable attribute weights and target relative negative sampling (DQE-CIR), a method designed to learn distinctive query embeddings by explicitly modeling target relative relevance during training. DQE-CIR incorporates learnable attribute weighting to emphasize distinctive visual features conditioned on the modification text, enabling more precise feature alignment between language and vision. Furthermore, we introduce target relative negative sampling, which constructs a target relative similarity distribution and selects informative negatives from a mid-zone region that excludes both easy negatives and ambiguous false negatives. This strategy enables more reliable retrieval for fine-grained attribute changes by improving query discriminativeness and reducing confusion caused by semantically similar but irrelevant candidates.

