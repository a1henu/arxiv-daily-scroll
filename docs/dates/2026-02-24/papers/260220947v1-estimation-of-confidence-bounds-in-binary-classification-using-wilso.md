---
layout: default
title: Estimation of Confidence Bounds in Binary Classification using Wilson Score Kernel Density Estimation
---

# Estimation of Confidence Bounds in Binary Classification using Wilson Score Kernel Density Estimation
**arXiv**：[2602.20947v1](https://arxiv.org/abs/2602.20947) · [PDF](https://arxiv.org/pdf/2602.20947.pdf)  
**作者**：Thorbjørn Mosekjær Iversen, Zebin Duan, Frederik Hagelskjær  

**一句话要点**：提出Wilson Score核密度分类方法，用于估计二元分类中的置信边界以支持关键自动化任务。

**关键词**：二元分类, 置信边界估计, 核密度估计, 选择性分类, 自动化检测

## 3 点简述
- 核心问题：在关键自动化应用中，二元分类器需要可靠置信边界以确保统计显著性下的系统性能。
- 方法要点：基于Wilson Score核密度估计器，处理条件变化成功概率的二项实验置信边界估计。
- 实验或效果：在四个数据集上评估选择性分类，性能接近高斯过程分类但计算复杂度更低。

## 摘要（原文）

> The performance and ease of use of deep learning-based binary classifiers have improved significantly in recent years. This has opened up the potential for automating critical inspection tasks, which have traditionally only been trusted to be done manually. However, the application of binary classifiers in critical operations depends on the estimation of reliable confidence bounds such that system performance can be ensured up to a given statistical significance. We present Wilson Score Kernel Density Classification, which is a novel kernel-based method for estimating confidence bounds in binary classification. The core of our method is the Wilson Score Kernel Density Estimator, which is a function estimator for estimating confidence bounds in Binomial experiments with conditionally varying success probabilities. Our method is evaluated in the context of selective classification on four different datasets, illustrating its use as a classification head of any feature extractor, including vision foundation models. Our proposed method shows similar performance to Gaussian Process Classification, but at a lower computational complexity.

