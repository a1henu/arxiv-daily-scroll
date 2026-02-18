---
layout: default
title: Benchmarking Self-Supervised Models for Cardiac Ultrasound View Classification
---

# Benchmarking Self-Supervised Models for Cardiac Ultrasound View Classification
**arXiv**：[2602.15339v1](https://arxiv.org/abs/2602.15339) · [PDF](https://arxiv.org/pdf/2602.15339.pdf)  
**作者**：Youssef Megahed, Salma I. Megahed, Robin Ducharme, Inok Lee, Adrian D. C. Chan, Mark C. Walker, Steven Hawken  

**一句话要点**：评估USF-MAE与MoCo v3在心脏超声视图分类中的自监督学习性能

**关键词**：自监督学习, 心脏超声分类, 视图识别, CACTUS数据集, 性能评估

## 3 点简述
- 核心问题：心脏超声图像可靠解读对临床诊断至关重要，需自动化视图分类。
- 方法要点：在CACTUS数据集上公平比较USF-MAE和MoCo v3，采用5折交叉验证。
- 实验或效果：USF-MAE在AUC、准确率等指标上显著优于MoCo v3，性能提升具有统计显著性。

## 摘要（原文）

> Reliable interpretation of cardiac ultrasound images is essential for accurate clinical diagnosis and assessment. Self-supervised learning has shown promise in medical imaging by leveraging large unlabelled datasets to learn meaningful representations. In this study, we evaluate and compare two self-supervised learning frameworks, USF-MAE, developed by our team, and MoCo v3, on the recently introduced CACTUS dataset (37,736 images) for automated simulated cardiac view (A4C, PL, PSAV, PSMV, Random, and SC) classification. Both models used 5-fold cross-validation, enabling robust assessment of generalization performance across multiple random splits. The CACTUS dataset provides expert-annotated cardiac ultrasound images with diverse views. We adopt an identical training protocol for both models to ensure a fair comparison. Both models are configured with a learning rate of 0.0001 and a weight decay of 0.01. For each fold, we record performance metrics including ROC-AUC, accuracy, F1-score, and recall. Our results indicate that USF-MAE consistently outperforms MoCo v3 across metrics. The average testing AUC for USF-MAE is 99.99% (+/-0.01% 95% CI), compared to 99.97% (+/-0.01%) for MoCo v3. USF-MAE achieves a mean testing accuracy of 99.33% (+/-0.18%), higher than the 98.99% (+/-0.28%) reported for MoCo v3. Similar trends are observed for the F1-score and recall, with improvements statistically significant across folds (paired t-test, p=0.0048 < 0.01). This proof-of-concept analysis suggests that USF-MAE learns more discriminative features for cardiac view classification than MoCo v3 when applied to this dataset. The enhanced performance across multiple metrics highlights the potential of USF-MAE for improving automated cardiac ultrasound classification.

