---
layout: default
title: DeltaMIL: Gated Memory Integration for Efficient and Discriminative Whole Slide Image Analysis
---

# DeltaMIL: Gated Memory Integration for Efficient and Discriminative Whole Slide Image Analysis
**arXiv**：[2512.19331v1](https://arxiv.org/abs/2512.19331) · [PDF](https://arxiv.org/pdf/2512.19331.pdf)  
**作者**：Yueting Zhu, Yuehao Song, Shuai Zhang, Wenyu Liu, Xinggang Wang  

**一句话要点**：提出DeltaMIL框架，通过门控记忆整合解决全切片图像分析中的信息冗余与分散问题。

**关键词**：全切片图像分析, 多示例学习, 门控记忆整合, 动态特征更新, 病理图像分类, 生存预测

## 3 点简述
- 核心问题：全切片图像规模大、异质性强，导致信息冗余分散，现有多示例学习方法难以有效筛选和整合判别性信号。
- 方法要点：利用门控delta规则，结合遗忘与记忆机制，动态更新记忆以过滤无关信息并整合相关特征，同时引入局部模式混合机制保留细粒度病理局部性。
- 实验或效果：在生存预测和切片级分类任务中，DeltaMIL使用ResNet-50和UNI特征均实现性能提升，达到先进水平。

## 摘要（原文）

> Whole Slide Images (WSIs) are typically analyzed using multiple instance learning (MIL) methods. However, the scale and heterogeneity of WSIs generate highly redundant and dispersed information, making it difficult to identify and integrate discriminative signals. Existing MIL methods either fail to discard uninformative cues effectively or have limited ability to consolidate relevant features from multiple patches, which restricts their performance on large and heterogeneous WSIs. To address this issue, we propose DeltaMIL, a novel MIL framework that explicitly selects semantically relevant regions and integrates the discriminative information from WSIs. Our method leverages the gated delta rule to efficiently filter and integrate information through a block combining forgetting and memory mechanisms. The delta mechanism dynamically updates the memory by removing old values and inserting new ones according to their correlation with the current patch. The gating mechanism further enables rapid forgetting of irrelevant signals. Additionally, DeltaMIL integrates a complementary local pattern mixing mechanism to retain fine-grained pathological locality. Our design enhances the extraction of meaningful cues and suppresses redundant or noisy information, which improves the model's robustness and discriminative power. Experiments demonstrate that DeltaMIL achieves state-of-the-art performance. Specifically, for survival prediction, DeltaMIL improves performance by 3.69\% using ResNet-50 features and 2.36\% using UNI features. For slide-level classification, it increases accuracy by 3.09\% with ResNet-50 features and 3.75\% with UNI features. These results demonstrate the strong and consistent performance of DeltaMIL across diverse WSI tasks.

