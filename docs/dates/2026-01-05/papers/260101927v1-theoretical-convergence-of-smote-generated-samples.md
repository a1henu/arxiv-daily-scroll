---
layout: default
title: Theoretical Convergence of SMOTE-Generated Samples
---

# Theoretical Convergence of SMOTE-Generated Samples
**arXiv**：[2601.01927v1](https://arxiv.org/abs/2601.01927) · [PDF](https://arxiv.org/pdf/2601.01927.pdf)  
**作者**：Firuz Kamalov, Hana Sulieman, Witold Pedrycz  

**一句话要点**：证明SMOTE生成样本的概率收敛性，为不平衡数据提供理论支撑

**关键词**：SMOTE, 不平衡数据, 概率收敛, 数据增强, 理论分析

## 3 点简述
- 核心问题：不平衡数据影响机器学习应用，需验证SMOTE的理论基础
- 方法要点：证明合成变量Z依概率收敛于原始变量X，在紧集上更强收敛
- 实验或效果：数值实验支持理论，低近邻秩加速收敛，指导实践

## 摘要（原文）

> Imbalanced data affects a wide range of machine learning applications, from healthcare to network security. As SMOTE is one of the most popular approaches to addressing this issue, it is imperative to validate it not only empirically but also theoretically. In this paper, we provide a rigorous theoretical analysis of SMOTE's convergence properties. Concretely, we prove that the synthetic random variable Z converges in probability to the underlying random variable X. We further prove a stronger convergence in mean when X is compact. Finally, we show that lower values of the nearest neighbor rank lead to faster convergence offering actionable guidance to practitioners. The theoretical results are supported by numerical experiments using both real-life and synthetic data. Our work provides a foundational understanding that enhances data augmentation techniques beyond imbalanced data scenarios.

