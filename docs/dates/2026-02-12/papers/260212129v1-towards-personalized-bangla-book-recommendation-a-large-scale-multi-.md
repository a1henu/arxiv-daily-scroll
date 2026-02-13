---
layout: default
title: Towards Personalized Bangla Book Recommendation: A Large-Scale Multi-Entity Book Graph Dataset
---

# Towards Personalized Bangla Book Recommendation: A Large-Scale Multi-Entity Book Graph Dataset
**arXiv**：[2602.12129v1](https://arxiv.org/abs/2602.12129) · [PDF](https://arxiv.org/pdf/2602.12129.pdf)  
**作者**：Rahin Arefin Ahmed, Md. Anik Chowdhury, Sakil Ahmed Sheikh Reza, Devnil Bhattacharjee, Muhammad Abdullah Adnan, Nafis Sadeq  

**一句话要点**：提出大规模多实体孟加拉语图书图数据集RokomariBG，以支持低资源语言下的个性化推荐研究。

**关键词**：孟加拉语图书推荐, 异构图数据集, 低资源语言推荐, 图神经网络, 基准测试, 个性化推荐

## 3 点简述
- 核心问题：孟加拉语文学个性化推荐缺乏结构化、大规模公开数据集。
- 方法要点：构建包含图书、用户、作者等实体的异构图，提供八种关系类型。
- 实验或效果：基准测试显示神经检索模型性能最佳（NDCG@10=0.204），强调多关系结构和文本信息的重要性。

## 摘要（原文）

> Personalized book recommendation in Bangla literature has been constrained by the lack of structured, large-scale, and publicly available datasets. This work introduces RokomariBG, a large-scale, multi-entity heterogeneous book graph dataset designed to support research on personalized recommendation in a low-resource language setting. The dataset comprises 127,302 books, 63,723 users, 16,601 authors, 1,515 categories, 2,757 publishers, and 209,602 reviews, connected through eight relation types and organized as a comprehensive knowledge graph.
>   To demonstrate the utility of the dataset, we provide a systematic benchmarking study on the Top-N recommendation task, evaluating a diverse set of representative recommendation models, including classical collaborative filtering methods, matrix factorization models, content-based approaches, graph neural networks, a hybrid matrix factorization model with side information, and a neural two-tower retrieval architecture. The benchmarking results highlight the importance of leveraging multi-relational structure and textual side information, with neural retrieval models achieving the strongest performance (NDCG@10 = 0.204). Overall, this work establishes a foundational benchmark and a publicly available resource for Bangla book recommendation research, enabling reproducible evaluation and future studies on recommendation in low-resource cultural domains. The dataset and code are publicly available at https://github.com/backlashblitz/Bangla-Book-Recommendation-Dataset

