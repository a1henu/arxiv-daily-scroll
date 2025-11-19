---
layout: default
title: BCE3S: Binary Cross-Entropy Based Tripartite Synergistic Learning for Long-tailed Recognition
---

# BCE3S: Binary Cross-Entropy Based Tripartite Synergistic Learning for Long-tailed Recognition
**arXiv**：[2511.14097v1](https://arxiv.org/abs/2511.14097) · [PDF](https://arxiv.org/pdf/2511.14097.pdf)  
**作者**：Weijia Fan, Qiufu Li, Jiajun Wen, Xiaoyang Peng  

**一句话要点**：提出基于二元交叉熵的三方协同学习以解决长尾识别问题

**关键词**：长尾识别, 二元交叉熵, 特征学习, 分类器平衡, 协同学习

## 3 点简述
- 长尾识别中，现有交叉熵损失难以学习高类内紧密度和类间分离性特征
- BCE3S通过联合、对比和均匀学习，优化特征和分类器，提升紧密度与分离性
- 在多个长尾数据集上实现SOTA性能，验证方法有效性

## 摘要（原文）

> For long-tailed recognition (LTR) tasks, high intra-class compactness and inter-class separability in both head and tail classes, as well as balanced separability among all the classifier vectors, are preferred. The existing LTR methods based on cross-entropy (CE) loss not only struggle to learn features with desirable properties but also couple imbalanced classifier vectors in the denominator of its Softmax, amplifying the imbalance effects in LTR. In this paper, for the LTR, we propose a binary cross-entropy (BCE)-based tripartite synergistic learning, termed BCE3S, which consists of three components: (1) BCE-based joint learning optimizes both the classifier and sample features, which achieves better compactness and separability among features than the CE-based joint learning, by decoupling the metrics between feature and the imbalanced classifier vectors in multiple Sigmoid; (2) BCE-based contrastive learning further improves the intra-class compactness of features; (3) BCE-based uniform learning balances the separability among classifier vectors and interactively enhances the feature properties by combining with the joint learning. The extensive experiments show that the LTR model trained by BCE3S not only achieves higher compactness and separability among sample features, but also balances the classifier's separability, achieving SOTA performance on various long-tailed datasets such as CIFAR10-LT, CIFAR100-LT, ImageNet-LT, and iNaturalist2018.

