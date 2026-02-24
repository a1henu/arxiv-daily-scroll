---
layout: default
title: DReX: An Explainable Deep Learning-based Multimodal Recommendation Framework
---

# DReX: An Explainable Deep Learning-based Multimodal Recommendation Framework
**arXiv**：[2602.19702v1](https://arxiv.org/abs/2602.19702) · [PDF](https://arxiv.org/pdf/2602.19702.pdf)  
**作者**：Adamya Shyam, Venkateswara Rao Kagita, Bharti Rana, Vikas Kumar  

**一句话要点**：提出DReX框架，通过增量更新机制解决多模态推荐中用户与物品表示对齐问题。

**关键词**：多模态推荐, 表示学习, 门控循环单元, 可解释性, 增量更新

## 3 点简述
- 核心问题：现有多模态推荐方法存在模态孤立处理、数据完整依赖和表示对齐不足等限制。
- 方法要点：使用门控循环单元增量整合交互级多模态特征，统一优化用户和物品表示。
- 实验或效果：在三个真实数据集上超越先进方法，并生成可解释的关键词配置文件。

## 摘要（原文）

> Multimodal recommender systems leverage diverse data sources, such as user interactions, content features, and contextual information, to address challenges like cold-start and data sparsity. However, existing methods often suffer from one or more key limitations: processing different modalities in isolation, requiring complete multimodal data for each interaction during training, or independent learning of user and item representations. These factors contribute to increased complexity and potential misalignment between user and item embeddings. To address these challenges, we propose DReX, a unified multimodal recommendation framework that incrementally refines user and item representations by leveraging interaction-level features from multimodal feedback. Our model employs gated recurrent units to selectively integrate these fine-grained features into global representations. This incremental update mechanism provides three key advantages: (1) simultaneous modeling of both nuanced interaction details and broader preference patterns, (2) eliminates the need for separate user and item feature extraction processes, leading to enhanced alignment in their learned representation, and (3) inherent robustness to varying or missing modalities. We evaluate the performance of the proposed approach on three real-world datasets containing reviews and ratings as interaction modalities. By considering review text as a modality, our approach automatically generates interpretable keyword profiles for both users and items, which supplement the recommendation process with interpretable preference indicators. Experiment results demonstrate that our approach outperforms state-of-the-art methods across all evaluated datasets.

