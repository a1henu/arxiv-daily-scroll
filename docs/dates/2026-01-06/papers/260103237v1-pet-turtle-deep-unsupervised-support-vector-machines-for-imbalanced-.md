---
layout: default
title: PET-TURTLE: Deep Unsupervised Support Vector Machines for Imbalanced Data Clusters
---

# PET-TURTLE: Deep Unsupervised Support Vector Machines for Imbalanced Data Clusters
**arXiv**：[2601.03237v1](https://arxiv.org/abs/2601.03237) · [PDF](https://arxiv.org/pdf/2601.03237.pdf)  
**作者**：Javier Salazar Cavazos  

**一句话要点**：提出PET-TURTLE以解决不平衡数据聚类问题，通过幂律先验和稀疏logits提升准确性。

**关键词**：深度聚类, 不平衡数据, 支持向量机, 无监督学习, 幂律先验, 稀疏logits

## 3 点简述
- 核心问题：TURTLE算法假设数据簇平衡，在不平衡数据上产生非理想超平面，导致聚类错误增加。
- 方法要点：引入幂律先验泛化成本函数处理不平衡分布，并添加稀疏logits简化搜索空间，优化标签更新过程。
- 实验或效果：在合成和真实数据上验证，PET-TURTLE提高不平衡数据准确性，防止少数簇过预测，并增强整体聚类性能。

## 摘要（原文）

> Foundation vision, audio, and language models enable zero-shot performance on downstream tasks via their latent representations. Recently, unsupervised learning of data group structure with deep learning methods has gained popularity. TURTLE, a state of the art deep clustering algorithm, uncovers data labeling without supervision by alternating label and hyperplane updates, maximizing the hyperplane margin, in a similar fashion to support vector machines (SVMs). However, TURTLE assumes clusters are balanced; when data is imbalanced, it yields non-ideal hyperplanes that cause higher clustering error. We propose PET-TURTLE, which generalizes the cost function to handle imbalanced data distributions by a power law prior. Additionally, by introducing sparse logits in the labeling process, PET-TURTLE optimizes a simpler search space that in turn improves accuracy for balanced datasets. Experiments on synthetic and real data show that PET-TURTLE improves accuracy for imbalanced sources, prevents over-prediction of minority clusters, and enhances overall clustering.

