---
layout: default
title: From Isolation to Integration: Building an Adaptive Expert Forest for Pre-Trained Model-based Class-Incremental Learning
---

# From Isolation to Integration: Building an Adaptive Expert Forest for Pre-Trained Model-based Class-Incremental Learning
**arXiv**：[2602.20911v1](https://arxiv.org/abs/2602.20911) · [PDF](https://arxiv.org/pdf/2602.20911.pdf)  
**作者**：Ruiqi Liu, Boyu Diao, Hangda Liu, Zhulin An, Fei Wang, Yongjun Xu  

**一句话要点**：提出语义引导自适应专家森林以解决预训练模型类增量学习中的知识孤立问题

**关键词**：类增量学习, 预训练模型, 适配器, 知识共享, 专家森林, 语义聚类

## 3 点简述
- 核心问题：类增量学习中冻结预训练模型并训练独立适配器导致知识孤立，无法利用任务间关系。
- 方法要点：基于语义关系将任务聚类，在簇内构建平衡专家树，通过合并相似任务适配器实现知识共享。
- 实验或效果：在多个基准数据集上达到最先进性能，通过激活相关专家加权预测提升准确性。

## 摘要（原文）

> Class-Incremental Learning (CIL) requires models to learn new classes without forgetting old ones. A common method is to freeze a pre-trained model and train a new, lightweight adapter for each task. While this prevents forgetting, it treats the learned knowledge as a simple, unstructured collection and fails to use the relationships between tasks. To this end, we propose the Semantic-guided Adaptive Expert Forest (SAEF), a new method that organizes adapters into a structured hierarchy for better knowledge sharing. SAEF first groups tasks into conceptual clusters based on their semantic relationships. Then, within each cluster, it builds a balanced expert tree by creating new adapters from merging the adapters of similar tasks. At inference time, SAEF finds and activates a set of relevant experts from the forest for any given input. The final prediction is made by combining the outputs of these activated experts, weighted by how confident each expert is. Experiments on several benchmark datasets show that SAEF achieves SOTA performance.

