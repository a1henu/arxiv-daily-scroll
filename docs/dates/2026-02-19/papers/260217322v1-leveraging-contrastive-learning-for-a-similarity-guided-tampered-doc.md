---
layout: default
title: Leveraging Contrastive Learning for a Similarity-Guided Tampered Document Data Generation Pipeline
---

# Leveraging Contrastive Learning for a Similarity-Guided Tampered Document Data Generation Pipeline
**arXiv**：[2602.17322v1](https://arxiv.org/abs/2602.17322) · [PDF](https://arxiv.org/pdf/2602.17322.pdf)  
**作者**：Mohamed Dhouib, Davide Buscaldi, Sonia Vanier, Aymen Shabou  

**一句话要点**：提出基于对比学习的相似性引导篡改文档数据生成方法，以解决数据稀缺问题。

**关键词**：篡改文档检测, 对比学习, 数据生成, 文档图像, 文本裁剪, 视觉质量评估

## 3 点简述
- 核心问题：篡改文档检测因数据稀缺而困难，现有生成方法多样性不足且视觉质量差。
- 方法要点：训练两个辅助网络，分别用于文本裁剪相似性比较和裁剪质量评估，结合生成高质量篡改图像。
- 实验或效果：在相同训练协议下，基于本方法生成的数据训练模型，在多个开源数据集上表现优于现有方法。

## 摘要（原文）

> Detecting tampered text in document images is a challenging task due to data scarcity. To address this, previous work has attempted to generate tampered documents using rule-based methods. However, the resulting documents often suffer from limited variety and poor visual quality, typically leaving highly visible artifacts that are rarely observed in real-world manipulations. This undermines the model's ability to learn robust, generalizable features and results in poor performance on real-world data. Motivated by this discrepancy, we propose a novel method for generating high-quality tampered document images. We first train an auxiliary network to compare text crops, leveraging contrastive learning with a novel strategy for defining positive pairs and their corresponding negatives. We also train a second auxiliary network to evaluate whether a crop tightly encloses the intended characters, without cutting off parts of characters or including parts of adjacent ones. Using a carefully designed generation pipeline that leverages both networks, we introduce a framework capable of producing diverse, high-quality tampered document images. We assess the effectiveness of our data generation pipeline by training multiple models on datasets derived from the same source images, generated using our method and existing approaches, under identical training protocols. Evaluating these models on various open-source datasets shows that our pipeline yields consistent performance improvements across architectures and datasets.

