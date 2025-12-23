---
layout: default
title: KerJEPA: Kernel Discrepancies for Euclidean Self-Supervised Learning
---

# KerJEPA: Kernel Discrepancies for Euclidean Self-Supervised Learning
**arXiv**：[2512.19605v1](https://arxiv.org/abs/2512.19605) · [PDF](https://arxiv.org/pdf/2512.19605.pdf)  
**作者**：Eric Zimmermann, Harley Wiltzer, Justin Szeto, David Alvarez-Melis, Lester Mackey  

**一句话要点**：提出KerJEPA，一种基于核正则化的自监督学习算法家族，以增强训练稳定性和设计灵活性。

**关键词**：自监督学习, 联合嵌入预测架构, 核正则化, 最大均值差异, 训练稳定性, 高斯先验

## 3 点简述
- 核心问题：自监督联合嵌入预测架构（JEPA）中，正则化表示向各向同性高斯先验可提升训练稳定性和下游泛化，但现有方法在核和先验选择上受限。
- 方法要点：扩展核和先验类别，计算切片最大均值差异（MMD）的闭式高维极限，开发新的KerJEPA算法，提供更灵活的核正则化设计。
- 实验或效果：KerJEPA展现出改进的训练稳定性和设计灵活性，具体性能增益未知，但基于理论推导和算法扩展。

## 摘要（原文）

> Recent breakthroughs in self-supervised Joint-Embedding Predictive Architectures (JEPAs) have established that regularizing Euclidean representations toward isotropic Gaussian priors yields provable gains in training stability and downstream generalization. We introduce a new, flexible family of KerJEPAs, self-supervised learning algorithms with kernel-based regularizers. One instance of this family corresponds to the recently-introduced LeJEPA Epps-Pulley regularizer which approximates a sliced maximum mean discrepancy (MMD) with a Gaussian prior and Gaussian kernel. By expanding the class of viable kernels and priors and computing the closed-form high-dimensional limit of sliced MMDs, we develop alternative KerJEPAs with a number of favorable properties including improved training stability and design flexibility.

