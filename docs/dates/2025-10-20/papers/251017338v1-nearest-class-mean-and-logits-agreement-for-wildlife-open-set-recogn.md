---
layout: default
title: Nearest-Class Mean and Logits Agreement for Wildlife Open-Set Recognition
---

# Nearest-Class Mean and Logits Agreement for Wildlife Open-Set Recognition
**arXiv**：[2510.17338v1](https://arxiv.org/abs/2510.17338) · [PDF](https://arxiv.org/pdf/2510.17338.pdf)  
**作者**：Jiahao Huo, Mufhumudzi Muthivhi, Terence L. van Zyl, Fredrik Gustafsson  

**一句话要点**：提出基于最近类均值和logits一致性的后处理开放集识别方法，用于野生动物分类。

**关键词**：开放集识别, 野生动物分类, 最近类均值, logits一致性, 后处理方法, 特征距离

## 3 点简述
- 核心问题：现有野生动物分类模型在开放集场景中过度自信，无法拒绝未知类样本。
- 方法要点：通过比较输入特征与最近类均值的距离分布和softmax概率，衡量一致性。
- 实验或效果：在两个数据集上排名前三，AUROC达93.41和95.35，性能稳定。

## 摘要（原文）

> Current state-of-the-art Wildlife classification models are trained under the
> closed world setting. When exposed to unknown classes, they remain
> overconfident in their predictions. Open-set Recognition (OSR) aims to classify
> known classes while rejecting unknown samples. Several OSR methods have been
> proposed to model the closed-set distribution by observing the feature, logit,
> or softmax probability space. A significant drawback of many existing
> approaches is the requirement to retrain the pre-trained classification model
> with the OSR-specific strategy. This study contributes a post-processing OSR
> method that measures the agreement between the models' features and predicted
> logits. We propose a probability distribution based on an input's distance to
> its Nearest Class Mean (NCM). The NCM-based distribution is then compared with
> the softmax probabilities from the logit space to measure agreement between the
> NCM and the classification head. Our proposed strategy ranks within the top
> three on two evaluated datasets, showing consistent performance across the two
> datasets. In contrast, current state-of-the-art methods excel on a single
> dataset. We achieve an AUROC of 93.41 and 95.35 for African and Swedish
> animals. The code can be found
> https://github.com/Applied-Representation-Learning-Lab/OSR.

