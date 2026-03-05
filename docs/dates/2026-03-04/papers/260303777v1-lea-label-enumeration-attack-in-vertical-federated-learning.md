---
layout: default
title: LEA: Label Enumeration Attack in Vertical Federated Learning
---

# LEA: Label Enumeration Attack in Vertical Federated Learning
**arXiv**：[2603.03777v1](https://arxiv.org/abs/2603.03777) · [PDF](https://arxiv.org/pdf/2603.03777.pdf)  
**作者**：Wenhao Jiang, Shaojing Fu, Yuchuan Luo, Lin Liu  

**一句话要点**：提出标签枚举攻击（LEA）以解决垂直联邦学习中标签隐私泄露问题

**关键词**：垂直联邦学习, 标签隐私攻击, 梯度相似度, 聚类枚举, 模型一致性评估

## 3 点简述
- 核心问题：现有垂直联邦学习标签推断攻击局限于特定场景或需辅助数据，实用性不足
- 方法要点：通过聚类枚举样本-标签映射，基于首轮损失梯度余弦相似度评估模型一致性，实现高效攻击
- 实验或效果：LEA在多种场景下无需辅助数据，计算复杂度从n!降至n^3，并能抵抗梯度噪声和压缩防御

## 摘要（原文）

> A typical Vertical Federated Learning (VFL) scenario involves several participants collaboratively training a machine learning model, where each party has different features for the same samples, with labels held exclusively by one party. Since labels contain sensitive information, VFL must ensure the privacy of labels. However, existing VFL-targeted label inference attacks are either limited to specific scenarios or require auxiliary data, rendering them impractical in real-world applications.
>   We introduce a novel Label Enumeration Attack (LEA) that, for the first time, achieves applicability across multiple VFL scenarios and eschews the need for auxiliary data. Our intuition is that an adversary, employing clustering to enumerate mappings between samples and labels, ascertains the accurate label mappings by evaluating the similarity between the benign model and the simulated models trained under each mapping. To achieve that, the first challenge is how to measure model similarity, as models trained on the same data can have different weights. Drawing from our findings, we propose an efficient approach for assessing congruence based on the cosine similarity of the first-round loss gradients, which offers superior efficiency and precision compared to the comparison of parameter similarities. However, the computational cost may be prohibitive due to the necessity of training and comparing the vast number of simulated models generated through enumeration. To overcome this challenge, we propose Binary-LEA from the perspective of reducing the number of models and eliminating futile training, which lowers the number of enumerations from n! to n^3. Moreover, LEA is resilient against common defense mechanisms such as gradient noise and gradient compression.

