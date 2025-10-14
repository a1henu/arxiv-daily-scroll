---
layout: default
title: Comparative Evaluation of Neural Network Architectures for Generalizable Human Spatial Preference Prediction in Unseen Built Environments
---

# Comparative Evaluation of Neural Network Architectures for Generalizable Human Spatial Preference Prediction in Unseen Built Environments
**arXiv**：[2510.10954v1](https://arxiv.org/abs/2510.10954) · [PDF](https://arxiv.org/pdf/2510.10954.pdf)  
**作者**：Maral Doctorarastoo, Katherine A. Flanigan, Mario Bergés, Christopher McComb  

**一句话要点**：比较图神经网络、卷积神经网络和前馈神经网络在未见建筑环境中预测人类空间偏好的泛化能力

**关键词**：空间偏好预测, 神经网络架构比较, 泛化能力评估, 建筑环境建模, 图神经网络, 卷积神经网络

## 3 点简述
- 核心问题：预测人类空间偏好的模型在未见环境布局中泛化能力不足。
- 方法要点：使用合成口袋公园数据比较不同神经网络架构的泛化性能。
- 实验或效果：基于精确率-召回率曲线下面积评估模型在可见和未见布局中的泛化得分。

## 摘要（原文）

> The capacity to predict human spatial preferences within built environments
> is instrumental for developing Cyber-Physical-Social Infrastructure Systems
> (CPSIS). A significant challenge in this domain is the generalizability of
> preference models, particularly their efficacy in predicting preferences within
> environmental configurations not encountered during training. While deep
> learning models have shown promise in learning complex spatial and contextual
> dependencies, it remains unclear which neural network architectures are most
> effective at generalizing to unseen layouts. To address this, we conduct a
> comparative study of Graph Neural Networks, Convolutional Neural Networks, and
> standard feedforward Neural Networks using synthetic data generated from a
> simplified and synthetic pocket park environment. Beginning with this
> illustrative case study, allows for controlled analysis of each model's ability
> to transfer learned preference patterns to unseen spatial scenarios. The models
> are evaluated based on their capacity to predict preferences influenced by
> heterogeneous physical, environmental, and social features. Generalizability
> score is calculated using the area under the precision-recall curve for the
> seen and unseen layouts. This generalizability score is appropriate for
> imbalanced data, providing insights into the suitability of each neural network
> architecture for preference-aware human behavior modeling in unseen built
> environments.

