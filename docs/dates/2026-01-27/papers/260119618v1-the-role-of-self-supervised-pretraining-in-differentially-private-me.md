---
layout: default
title: The role of self-supervised pretraining in differentially private medical image analysis
---

# The role of self-supervised pretraining in differentially private medical image analysis
**arXiv**：[2601.19618v1](https://arxiv.org/abs/2601.19618) · [PDF](https://arxiv.org/pdf/2601.19618.pdf)  
**作者**：Soroosh Tayebi Arasteh, Mina Farajiamiri, Mahshad Lotfinia, Behrus Hinrichs-Puladi, Jonas Bienzeisler, Mohamed Alhaskir, Mirabela Rusu, Christiane Kuhl, Sven Nebelung, Daniel Truhn  

**一句话要点**：评估自监督预训练在差分隐私医学图像分析中的作用，提升诊断效用与公平性

**关键词**：差分隐私, 医学图像分析, 自监督学习, 模型初始化, 诊断性能, 公平性评估

## 3 点简述
- 核心问题：差分隐私保护导致医学图像分析性能下降，模型初始化策略影响未知
- 方法要点：大规模评估ImageNet、DINOv3和MIMIC-CXR初始化在DP-SGD训练下的效果
- 实验或效果：DINOv3优于ImageNet但不及领域特定监督预训练，初始化影响公平性与泛化

## 摘要（原文）

> Differential privacy (DP) provides formal protection for sensitive data but typically incurs substantial losses in diagnostic performance. Model initialization has emerged as a critical factor in mitigating this degradation, yet the role of modern self-supervised learning under full-model DP remains poorly understood. Here, we present a large-scale evaluation of initialization strategies for differentially private medical image analysis, using chest radiograph classification as a representative benchmark with more than 800,000 images. Using state-of-the-art ConvNeXt models trained with DP-SGD across realistic privacy regimes, we compare non-domain-specific supervised ImageNet initialization, non-domain-specific self-supervised DINOv3 initialization, and domain-specific supervised pretraining on MIMIC-CXR, the largest publicly available chest radiograph dataset. Evaluations are conducted across five external datasets spanning diverse institutions and acquisition settings. We show that DINOv3 initialization consistently improves diagnostic utility relative to ImageNet initialization under DP, but remains inferior to domain-specific supervised pretraining, which achieves performance closest to non-private baselines. We further demonstrate that initialization choice strongly influences demographic fairness, cross-dataset generalization, and robustness to data scale and model capacity under privacy constraints. The results establish initialization strategy as a central determinant of utility, fairness, and generalization in differentially private medical imaging.

