---
layout: default
title: Bagging-Based Model Merging for Robust General Text Embeddings
---

# Bagging-Based Model Merging for Robust General Text Embeddings
**arXiv**：[2602.05787v1](https://arxiv.org/abs/2602.05787) · [PDF](https://arxiv.org/pdf/2602.05787.pdf)  
**作者**：Hengran Zhang, Keping Bi, Jiafeng Guo, Jiaming Zhang, Wenbo Yang, Daiting Shi, Xueqi Cheng  

**一句话要点**：提出基于Bagging的模型合并方法，以提升文本嵌入模型的鲁棒性和增量学习效率。

**关键词**：文本嵌入模型, 多任务训练, 模型合并, 鲁棒性, 增量学习

## 3 点简述
- 核心问题：多任务训练策略比较及模型适应新域/数据类型的效率问题。
- 方法要点：通过采样子集训练多个模型并合并，增强鲁棒性并支持高效增量更新。
- 实验或效果：在多个基准测试中，优于全语料批级混洗，提升域内外性能并降低训练成本。

## 摘要（原文）

> General-purpose text embedding models underpin a wide range of NLP and information retrieval applications, and are typically trained on large-scale multi-task corpora to encourage broad generalization. However, it remains unclear how different multi-task training strategies compare in practice, and how to efficiently adapt embedding models as new domains and data types continually emerge. In this work, we present a systematic study of multi-task training for text embeddings from two perspectives: data scheduling and model merging. We compare batch-level shuffling, sequential training variants, two-stage training, and multiple merging granularities, and find that simple batch-level shuffling consistently yields the strongest overall performance, suggesting that task conflicts are limited and training datasets are largely complementary. Despite its effectiveness, batch-level shuffling exhibits two practical limitations: suboptimal out-of-domain (OOD) generalization and poor suitability for incremental learning due to expensive full retraining. To address these issues, we propose Bagging-based rObust mOdel Merging (\modelname), which trains multiple embedding models on sampled subsets and merges them into a single model, improving robustness while retaining single-model inference efficiency. Moreover, \modelname naturally supports efficient incremental updates by training lightweight update models on new data with a small historical subset and merging them into the existing model. Experiments across diverse embedding benchmarks demonstrate that \modelname consistently improves both in-domain and OOD performance over full-corpus batch-level shuffling, while substantially reducing training cost in incremental learning settings.

