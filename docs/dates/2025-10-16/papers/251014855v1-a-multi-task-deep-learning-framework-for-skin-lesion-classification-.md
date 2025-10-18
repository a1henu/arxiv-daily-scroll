---
layout: default
title: A Multi-Task Deep Learning Framework for Skin Lesion Classification, ABCDE Feature Quantification, and Evolution Simulation
---

# A Multi-Task Deep Learning Framework for Skin Lesion Classification, ABCDE Feature Quantification, and Evolution Simulation
**arXiv**：[2510.14855v1](https://arxiv.org/abs/2510.14855) · [PDF](https://arxiv.org/pdf/2510.14855.pdf)  
**作者**：Harsha Kotla, Arun Kumar Rajasekaran, Hannah Rana  

**一句话要点**：提出多任务深度学习框架，用于皮肤病变分类、ABCDE特征量化与演化模拟。

**关键词**：皮肤病变分类, 多任务学习, 特征量化, 演化模拟, 医学图像分析

## 3 点简述
- 核心问题：皮肤病变自动分析挑战大，ABCDE特征在深度学习中缺乏可解释性。
- 方法要点：框架同时分类病变并量化ABCD特征，模拟E特征演化。
- 实验或效果：在HAM10000数据集上，分类准确率约89%，AUC达0.96。

## 摘要（原文）

> Early detection of melanoma has grown to be essential because it
> significantly improves survival rates, but automated analysis of skin lesions
> still remains challenging. ABCDE, which stands for Asymmetry, Border
> irregularity, Color variation, Diameter, and Evolving, is a well-known
> classification method for skin lesions, but most deep learning mechanisms treat
> it as a black box, as most of the human interpretable features are not
> explained. In this work, we propose a deep learning framework that both
> classifies skin lesions into categories and also quantifies scores for each
> ABCD feature. It simulates the evolution of these features over time in order
> to represent the E aspect, opening more windows for future exploration. The A,
> B, C, and D values are quantified particularly within this work. Moreover, this
> framework also visualizes ABCD feature trajectories in latent space as skin
> lesions evolve from benign nevuses to malignant melanoma. The experiments are
> conducted using the HAM10000 dataset that contains around ten thousand images
> of skin lesions of varying stages. In summary, the classification worked with
> an accuracy of around 89 percent, with melanoma AUC being 0.96, while the
> feature evaluation performed well in predicting asymmetry, color variation, and
> diameter, though border irregularity remains more difficult to model. Overall,
> this work provides a deep learning framework that will allow doctors to link ML
> diagnoses to clinically relevant criteria, thus improving our understanding of
> skin cancer progression.

