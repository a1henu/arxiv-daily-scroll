---
layout: default
title: PFed-Signal: An ADR Prediction Model based on Federated Learning
---

# PFed-Signal: An ADR Prediction Model based on Federated Learning
**arXiv**：[2512.23262v1](https://arxiv.org/abs/2512.23262) · [PDF](https://arxiv.org/pdf/2512.23262.pdf)  
**作者**：Tao Li, Peilin Li, Kui Lu, Yilei Wang, Junliang Shang, Guangshun Li, Huiyu Zhou  

**一句话要点**：提出PFed-Signal，基于联邦学习消除FAERS数据偏差以提升ADR预测准确性

**关键词**：药物不良反应预测, 联邦学习, 数据偏差消除, Transformer模型, 信号预测

## 3 点简述
- 核心问题：FAERS数据偏差导致ADR预测不准确，传统统计方法无法消除偏差
- 方法要点：使用联邦学习结合欧氏距离识别并删除偏差数据，基于Transformer训练预测模型
- 实验或效果：在清洁数据集上ROR和PRR优于传统方法，预测指标如准确率达0.887

## 摘要（原文）

> The adverse drug reactions (ADRs) predicted based on the biased records in FAERS (U.S. Food and Drug Administration Adverse Event Reporting System) may mislead diagnosis online. Generally, such problems are solved by optimizing reporting odds ratio (ROR) or proportional reporting ratio (PRR). However, these methods that rely on statistical methods cannot eliminate the biased data, leading to inaccurate signal prediction. In this paper, we propose PFed-signal, a federated learning-based signal prediction model of ADR, which utilizes the Euclidean distance to eliminate the biased data from FAERS, thereby improving the accuracy of ADR prediction. Specifically, we first propose Pfed-Split, a method to split the original dataset into a split dataset based on ADR. Then we propose ADR-signal, an ADR prediction model, including a biased data identification method based on federated learning and an ADR prediction model based on Transformer. The former identifies the biased data according to the Euclidean distance and generates a clean dataset by deleting the biased data. The latter is an ADR prediction model based on Transformer trained on the clean data set. The results show that the ROR and PRR on the clean dataset are better than those of the traditional methods. Furthermore, the accuracy rate, F1 score, recall rate and AUC of PFed-Signal are 0.887, 0.890, 0.913 and 0.957 respectively, which are higher than the baselines.

