---
layout: default
title: Practical Deep Heteroskedastic Regression
---

# Practical Deep Heteroskedastic Regression
**arXiv**：[2603.01750v1](https://arxiv.org/abs/2603.01750) · [PDF](https://arxiv.org/pdf/2603.01750.pdf)  
**作者**：Mikkel Jordahn, Jonas Vestergaard Jensen, James Harrison, Michael Riis Andersen, Mikkel N. Schmidt  

**一句话要点**：提出后验方差拟合方法以解决深度异方差回归中的优化与过拟合问题

**关键词**：异方差回归, 不确定性量化, 深度学习, 后验拟合, 分子图数据集, 方差模型

## 3 点简述
- 核心问题：深度异方差回归在不确定性量化与均值预测间存在优化困难、表示崩溃和方差过拟合等挑战
- 方法要点：在预训练网络中间层上，使用保留数据集后验拟合方差模型，简单高效
- 实验或效果：在多个分子图数据集上实现与先进方法相当或更优的不确定性量化，不损害均值预测精度且预测成本低

## 摘要（原文）

> Uncertainty quantification (UQ) in deep learning regression is of wide interest, as it supports critical applications including sequential decision making and risk-sensitive tasks. In heteroskedastic regression, where the uncertainty of the target depends on the input, a common approach is to train a neural network that parameterizes the mean and the variance of the predictive distribution. Still, training deep heteroskedastic regression models poses practical challenges in the trade-off between uncertainty quantification and mean prediction, such as optimization difficulties, representation collapse, and variance overfitting. In this work we identify previously undiscussed fallacies and propose a simple and efficient procedure that addresses these challenges jointly by post-hoc fitting a variance model across the intermediate layers of a pretrained network on a hold-out dataset. We demonstrate that our method achieves on-par or state-of-the-art uncertainty quantification on several molecular graph datasets, without compromising mean prediction accuracy and remaining cheap to use at prediction time.

