---
layout: default
title: Muon is Provably Faster with Momentum Variance Reduction
---

# Muon is Provably Faster with Momentum Variance Reduction
**arXiv**：[2512.16598v1](https://arxiv.org/abs/2512.16598) · [PDF](https://arxiv.org/pdf/2512.16598.pdf)  
**作者**：Xun Qian, Hussein Rammal, Dmitry Kovalev, Peter Richtárik  

**一句话要点**：提出动量方差缩减以改进基于非欧几里得LMO的优化器，提升大语言模型训练效率

**关键词**：动量方差缩减, 非欧几里得优化, 大语言模型训练, Gluon框架, 收敛率分析, 非凸优化

## 3 点简述
- 核心问题：基于非欧几里得LMO的优化器如Muon和Scion在训练大语言模型时收敛速度有限
- 方法要点：将动量方差缩减融入Gluon框架，改进动量机制，适用于更一般的平滑性假设
- 实验或效果：在非凸情况下，收敛率从O(1/K^{1/4})提升至O(1/K^{1/3})，数值实验验证迭代复杂度优势

## 摘要（原文）

> Recent empirical research has demonstrated that deep learning optimizers based on the linear minimization oracle (LMO) over specifically chosen Non-Euclidean norm balls, such as Muon and Scion, outperform Adam-type methods in the training of large language models. In this work, we show that such optimizers can be provably improved by replacing their vanilla momentum by momentum variance reduction (MVR). Instead of proposing and analyzing MVR variants of Muon and Scion separately, we incorporate MVR into the recently proposed Gluon framework, which captures Muon, Scion and other specific Non-Euclidean LMO-based methods as special cases, and at the same time works with a more general smoothness assumption which better captures the layer-wise structure of neural networks. In the non-convex case, we incorporate MVR into Gluon in three different ways. All of them improve the convergence rate from ${\cal O} (\frac{1}{K^{1/4}})$ to ${\cal O} (\frac{1}{K^{1/3}})$. Additionally, we provide improved rates in the star-convex case. Finally, we conduct several numerical experiments that verify the superior performance of our proposed algorithms in terms of iteration complexity.

