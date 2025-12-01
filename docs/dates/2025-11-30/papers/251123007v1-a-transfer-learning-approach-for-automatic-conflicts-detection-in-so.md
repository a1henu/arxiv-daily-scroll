---
layout: default
title: A transfer learning approach for automatic conflicts detection in software requirement sentence pairs based on dual encoders
---

# A transfer learning approach for automatic conflicts detection in software requirement sentence pairs based on dual encoders
**arXiv**：[2511.23007v1](https://arxiv.org/abs/2511.23007) · [PDF](https://arxiv.org/pdf/2511.23007.pdf)  
**作者**：Yizheng Wang, Tao Jiang, Jinyan Bai, Zhengbin Zou, Tiancheng Xue, Nan Zhang, Jie Luan  

**一句话要点**：提出基于SBERT和SimCSE的双编码器迁移学习框架，以提升软件需求冲突检测的准确性和跨域性能。

**关键词**：软件需求冲突检测, 双编码器, 迁移学习, SBERT, SimCSE, 混合损失优化

## 3 点简述
- 核心问题：软件需求文档中需求对冲突检测面临数据不平衡、语义提取有限和跨域迁移学习性能不足的挑战。
- 方法要点：采用SBERT和SimCSE双编码器生成嵌入，结合六元素拼接策略和带混合损失优化的两层全连接网络。
- 实验或效果：在域内设置中宏F1和加权F1提升10.4%，跨域场景中宏F1提升11.4%。

## 摘要（原文）

> Software Requirement Document (RD) typically contain tens of thousands of individual requirements, and ensuring consistency among these requirements is critical for the success of software engineering projects. Automated detection methods can significantly enhance efficiency and reduce costs; however, existing approaches still face several challenges, including low detection accuracy on imbalanced data, limited semantic extraction due to the use of a single encoder, and suboptimal performance in cross-domain transfer learning. To address these issues, this paper proposes a Transferable Software Requirement Conflict Detection Framework based on SBERT and SimCSE, termed TSRCDF-SS. First, the framework employs two independent encoders, Sentence-BERT (SBERT) and Simple Contrastive Sentence Embedding (SimCSE), to generate sentence embeddings for requirement pairs, followed by a six-element concatenation strategy. Furthermore, the classifier is enhanced by a two-layer fully connected feedforward neural network (FFNN) with a hybrid loss optimization strategy that integrates a variant of Focal Loss, domain-specific constraints, and a confidence-based penalty term. Finally, the framework synergistically integrates sequential and cross-domain transfer learning. Experimental results demonstrate that the proposed framework achieves a 10.4% improvement in both macro-F1 and weighted-F1 scores in in-domain settings, and an 11.4% increase in macro-F1 in cross-domain scenarios.

