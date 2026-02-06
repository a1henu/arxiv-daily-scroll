---
layout: default
title: Bagging-Based Model Merging for Robust General Text Embeddings
---

# Bagging-Based Model Merging for Robust General Text Embeddings
**arXiv**：[2602.05787v1](https://arxiv.org/abs/2602.05787) · [PDF](https://arxiv.org/pdf/2602.05787.pdf)  
**作者**：Hengran Zhang, Keping Bi, Jiafeng Guo, Jiaming Zhang, Wenbo Yang, Daiting Shi, Xueqi Cheng  

**一句话要点**：提出基于Bagging的模型合并方法，以提升文本嵌入模型的鲁棒性和增量学习效率。

**关键词**：文本嵌入模型, 模型合并, 多任务训练, 增量学习, 鲁棒性

## 3 点简述
- 研究多任务训练策略，发现批级混排性能最佳但存在域外泛化和增量学习限制。
- 提出Bagging-based rObust mOdel Merging，通过训练子集模型并合并来增强鲁棒性。
- 实验表明该方法在多个基准上优于批级混排，并显著降低增量学习成本。

## 摘要（原文）

> General-purpose text embedding models underpin a wide range of NLP and information retrieval applications, and are typically trained on large-scale multi-task corpora to encourage broad generalization. However, it remains unclear how different multi-task training strategies compare in practice, and how to efficiently adapt embedding models as new domains and data types continually emerge. In this work, we present a systematic study of multi-task training for text embeddings from two perspectives: data scheduling and model merging. We compare batch-level shuffling, sequential training variants, two-stage training, and multiple merging granularities, and find that simple batch-level shuffling consistently yields the strongest overall performance, suggesting that task conflicts are limited and training datasets are largely complementary. Despite its effectiveness, batch-level shuffling exhibits two practical limitations: suboptimal out-of-domain (OOD) generalization and poor suitability for incremental learning due to expensive full retraining. To address these issues, we propose Bagging-based rObust mOdel Merging (\modelname), which trains multiple embedding models on sampled subsets and merges them into a single model, improving robustness while retaining single-model inference efficiency. Moreover, \modelname naturally supports efficient incremental updates by training lightweight update models on new data with a small historical subset and merging them into the existing model. Experiments across diverse embedding benchmarks demonstrate that \modelname consistently improves both in-domain and OOD performance over full-corpus batch-level shuffling, while substantially reducing training cost in incremental learning settings.

