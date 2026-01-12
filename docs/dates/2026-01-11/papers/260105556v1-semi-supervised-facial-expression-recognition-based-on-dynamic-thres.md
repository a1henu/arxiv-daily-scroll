---
layout: default
title: Semi-Supervised Facial Expression Recognition based on Dynamic Threshold and Negative Learning
---

# Semi-Supervised Facial Expression Recognition based on Dynamic Threshold and Negative Learning
**arXiv**：[2601.05556v1](https://arxiv.org/abs/2601.05556) · [PDF](https://arxiv.org/pdf/2601.05556.pdf)  
**作者**：Zhongpeng Cai, Jun Yu, Wei Xu, Tianyu Liu, Jianqing Sun, Jiaen Liang  

**一句话要点**：提出基于动态阈值调整和选择性负学习的半监督面部表情识别算法，以解决标注数据稀缺问题。

**关键词**：半监督学习, 面部表情识别, 动态阈值调整, 选择性负学习, 特征增强

## 3 点简述
- 核心问题：面部表情识别中标注数据获取成本高，需有效利用未标注数据。
- 方法要点：结合动态阈值调整适应半监督框架，通过选择性负学习挖掘低置信度样本的互补标签信息。
- 实验或效果：在RAF-DB和AffectNet数据集上达到先进性能，超越全监督方法，证明有效性。

## 摘要（原文）

> Facial expression recognition is a key task in human-computer interaction and affective computing. However, acquiring a large amount of labeled facial expression data is often costly. Therefore, it is particularly important to design a semi-supervised facial expression recognition algorithm that makes full use of both labeled and unlabeled data. In this paper, we propose a semi-supervised facial expression recognition algorithm based on Dynamic Threshold Adjustment (DTA) and Selective Negative Learning (SNL). Initially, we designed strategies for local attention enhancement and random dropout of feature maps during feature extraction, which strengthen the representation of local features while ensuring the model does not overfit to any specific local area. Furthermore, this study introduces a dynamic thresholding method to adapt to the requirements of the semi-supervised learning framework for facial expression recognition tasks, and through a selective negative learning strategy, it fully utilizes unlabeled samples with low confidence by mining useful expression information from complementary labels, achieving impressive results. We have achieved state-of-the-art performance on the RAF-DB and AffectNet datasets. Our method surpasses fully supervised methods even without using the entire dataset, which proves the effectiveness of our approach.

