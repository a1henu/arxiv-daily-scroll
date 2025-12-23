---
layout: default
title: Multi-Layer Confidence Scoring for Detection of Out-of-Distribution Samples, Adversarial Attacks, and In-Distribution Misclassifications
---

# Multi-Layer Confidence Scoring for Detection of Out-of-Distribution Samples, Adversarial Attacks, and In-Distribution Misclassifications
**arXiv**：[2512.19472v1](https://arxiv.org/abs/2512.19472) · [PDF](https://arxiv.org/pdf/2512.19472.pdf)  
**作者**：Lorenzo Capelli, Leandro de Souza Rosa, Gianluca Setti, Mauro Mangia, Riccardo Rovatti  

**一句话要点**：提出MACS统一后处理框架，通过多层激活分析解决置信度估计、分布外检测和对抗攻击检测问题。

**关键词**：置信度评分, 分布外检测, 对抗攻击检测, 后处理方法, 多层激活分析, 深度学习安全

## 3 点简述
- 核心问题：现有方法难以统一处理置信度估计、分布外检测和对抗攻击检测，且应用受限。
- 方法要点：MACS分析中间激活生成分类图，从中推导统一评分，无需重新训练模型。
- 实验或效果：在VGG16和ViTb16模型上超越现有方法，计算开销较低。

## 摘要（原文）

> The recent explosive growth in Deep Neural Networks applications raises concerns about the black-box usage of such models, with limited trasparency and trustworthiness in high-stakes domains, which have been crystallized as regulatory requirements such as the European Union Artificial Intelligence Act. While models with embedded confidence metrics have been proposed, such approaches cannot be applied to already existing models without retraining, limiting their broad application. On the other hand, post-hoc methods, which evaluate pre-trained models, focus on solving problems related to improving the confidence in the model's predictions, and detecting Out-Of-Distribution or Adversarial Attacks samples as independent applications. To tackle the limited applicability of already existing methods, we introduce Multi-Layer Analysis for Confidence Scoring (MACS), a unified post-hoc framework that analyzes intermediate activations to produce classification-maps. From the classification-maps, we derive a score applicable for confidence estimation, detecting distributional shifts and adversarial attacks, unifying the three problems in a common framework, and achieving performances that surpass the state-of-the-art approaches in our experiments with the VGG16 and ViTb16 models with a fraction of their computational overhead.

