---
layout: default
title: Learning Deep Hybrid Models with Sharpness-Aware Minimization
---

# Learning Deep Hybrid Models with Sharpness-Aware Minimization
**arXiv**：[2602.06837v1](https://arxiv.org/abs/2602.06837) · [PDF](https://arxiv.org/pdf/2602.06837.pdf)  
**作者**：Naoya Takeishi  

**一句话要点**：提出基于锐度感知最小化的深度混合模型学习方法，以提升模型简单性。

**关键词**：混合建模, 锐度感知最小化, 深度学习, 模型正则化, 损失平坦性

## 3 点简述
- 混合建模中机器学习模型可能忽略科学模型，导致预测失效。
- 采用锐度感知最小化思想，聚焦损失最小值的平坦性以简化模型。
- 数值实验表明该方法在不同模型和数据集上表现良好。

## 摘要（原文）

> Hybrid modeling, the combination of machine learning models and scientific mathematical models, enables flexible and robust data-driven prediction with partial interpretability. However, effectively the scientific models may be ignored in prediction due to the flexibility of the machine learning model, making the idea of hybrid modeling pointless. Typically some regularization is applied to hybrid model learning to avoid such a failure case, but the formulation of the regularizer strongly depends on model architectures and domain knowledge. In this paper, we propose to focus on the flatness of loss minima in learning hybrid models, aiming to make the model as simple as possible. We employ the idea of sharpness-aware minimization and adapt it to the hybrid modeling setting. Numerical experiments show that the SAM-based method works well across different choices of models and datasets.

