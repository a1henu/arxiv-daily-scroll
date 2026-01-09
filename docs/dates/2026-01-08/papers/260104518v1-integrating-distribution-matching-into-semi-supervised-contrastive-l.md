---
layout: default
title: Integrating Distribution Matching into Semi-Supervised Contrastive Learning for Labeled and Unlabeled Data
---

# Integrating Distribution Matching into Semi-Supervised Contrastive Learning for Labeled and Unlabeled Data
**arXiv**：[2601.04518v1](https://arxiv.org/abs/2601.04518) · [PDF](https://arxiv.org/pdf/2601.04518.pdf)  
**作者**：Shogo Nakayama, Masahiro Okuda  

**一句话要点**：提出结合分布匹配的半监督对比学习方法，以提升小标注数据与大无标注数据场景下的图像分类精度。

**关键词**：半监督学习, 对比学习, 分布匹配, 伪标签, 图像分类, 特征嵌入

## 3 点简述
- 核心问题：半监督学习中，小量标注数据与大量无标注数据共存，伪标签方法需改进以提升分类准确性。
- 方法要点：在基于伪标签的半监督对比学习中，引入标注与无标注特征嵌入的分布匹配，以优化特征表示。
- 实验或效果：在多个数据集上验证，该方法能提高图像分类的准确率，具体提升幅度未知。

## 摘要（原文）

> The advancement of deep learning has greatly improved supervised image classification. However, labeling data is costly, prompting research into unsupervised learning methods such as contrastive learning. In real-world scenarios, fully unlabeled datasets are rare, making semi-supervised learning (SSL) highly relevant in scenarios where a small amount of labeled data coexists with a large volume of unlabeled data. A well-known semi-supervised contrastive learning approach involves assigning pseudo-labels to unlabeled data. This study aims to enhance pseudo-label-based SSL by incorporating distribution matching between labeled and unlabeled feature embeddings to improve image classification accuracy across multiple datasets.

