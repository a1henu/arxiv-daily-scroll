---
layout: default
title: Deep Semi-Supervised Survival Analysis for Predicting Cancer Prognosis
---

# Deep Semi-Supervised Survival Analysis for Predicting Cancer Prognosis
**arXiv**：[2601.20729v1](https://arxiv.org/abs/2601.20729) · [PDF](https://arxiv.org/pdf/2601.20729.pdf)  
**作者**：Anchen Sun, Zhibin Chen, Xiaodong Cai  

**一句话要点**：提出基于Mean Teacher的深度半监督Cox模型Cox-MT，以提升癌症预后预测准确性。

**关键词**：生存分析, 半监督学习, 癌症预后预测, Cox比例风险模型, 深度神经网络

## 3 点简述
- 问题：基于神经网络的Cox模型训练需大量标注数据，但标注样本有限制约性能。
- 方法：采用深度半监督学习，结合Mean Teacher框架，利用标注和未标注数据训练单模态和多模态模型。
- 效果：在TCGA数据上，Cox-MT显著优于现有模型，性能随未标注样本增加而提升，多模态模型表现更优。

## 摘要（原文）

> The Cox Proportional Hazards (PH) model is widely used in survival analysis. Recently, artificial neural network (ANN)-based Cox-PH models have been developed. However, training these Cox models with high-dimensional features typically requires a substantial number of labeled samples containing information about time-to-event. The limited availability of labeled data for training often constrains the performance of ANN-based Cox models. To address this issue, we employed a deep semi-supervised learning (DSSL) approach to develop single- and multi-modal ANN-based Cox models based on the Mean Teacher (MT) framework, which utilizes both labeled and unlabeled data for training. We applied our model, named Cox-MT, to predict the prognosis of several types of cancer using data from The Cancer Genome Atlas (TCGA). Our single-modal Cox-MT models, utilizing TCGA RNA-seq data or whole slide images, significantly outperformed the existing ANN-based Cox model, Cox-nnet, using the same data set across four types of cancer considered. As the number of unlabeled samples increased, the performance of Cox-MT significantly improved with a given set of labeled data. Furthermore, our multi-modal Cox-MT model demonstrated considerably better performance than the single-modal model. In summary, the Cox-MT model effectively leverages both labeled and unlabeled data to significantly enhance prediction accuracy compared to existing ANN-based Cox models trained solely on labeled data.

