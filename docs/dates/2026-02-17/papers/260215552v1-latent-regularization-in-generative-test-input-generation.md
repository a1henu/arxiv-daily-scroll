---
layout: default
title: Latent Regularization in Generative Test Input Generation
---

# Latent Regularization in Generative Test Input Generation
**arXiv**：[2602.15552v1](https://arxiv.org/abs/2602.15552) · [PDF](https://arxiv.org/pdf/2602.15552.pdf)  
**作者**：Giorgi Merabishvili, Oliver Weißl, Andrea Stocco  

**一句话要点**：研究潜在空间截断正则化对基于风格GAN的深度学习分类器测试输入生成质量的影响

**关键词**：潜在空间正则化, 生成测试输入, 风格GAN, 故障检测, 深度学习分类器, 图像数据集

## 3 点简述
- 核心问题：潜在空间正则化（截断）如何影响生成测试输入的质量，包括有效性、多样性和故障检测能力
- 方法要点：采用风格GAN，比较两种截断策略：潜在代码混合与二分搜索优化、随机潜在截断
- 实验或效果：在MNIST、Fashion MNIST和CIFAR-10数据集上评估，潜在代码混合方法在故障检测率、多样性和有效性上优于随机截断

## 摘要（原文）

> This study investigates the impact of regularization of latent spaces through truncation on the quality of generated test inputs for deep learning classifiers. We evaluate this effect using style-based GANs, a state-of-the-art generative approach, and assess quality along three dimensions: validity, diversity, and fault detection. We evaluate our approach on the boundary testing of deep learning image classifiers across three datasets, MNIST, Fashion MNIST, and CIFAR-10. We compare two truncation strategies: latent code mixing with binary search optimization and random latent truncation for generative exploration. Our experiments show that the latent code-mixing approach yields a higher fault detection rate than random truncation, while also improving both diversity and validity.

