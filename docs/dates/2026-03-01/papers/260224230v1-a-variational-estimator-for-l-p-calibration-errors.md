---
layout: default
title: A Variational Estimator for $L_p$ Calibration Errors
---

# A Variational Estimator for $L_p$ Calibration Errors
**arXiv**：[2602.24230v1](https://arxiv.org/abs/2602.24230) · [PDF](https://arxiv.org/pdf/2602.24230.pdf)  
**作者**：Eugène Berta, Sacha Braun, David Holzmüller, Francis Bach, Michael I. Jordan  

**一句话要点**：提出变分估计器以解决多类设置中L_p校准误差的准确估计问题。

**关键词**：校准误差估计, 变分框架, L_p散度, 多类分类, 概率评估

## 3 点简述
- 核心问题：校准误差估计在多类场景中具有挑战性，传统方法易高估。
- 方法要点：扩展变分框架，覆盖L_p散度诱导的校准误差，避免高估并区分过/欠置信。
- 实验或效果：提供广泛实验，代码集成于开源包probmetrics，便于评估校准误差。

## 摘要（原文）

> Calibration$\unicode{x2014}$the problem of ensuring that predicted probabilities align with observed class frequencies$\unicode{x2014}$is a basic desideratum for reliable prediction with machine learning systems. Calibration error is traditionally assessed via a divergence function, using the expected divergence between predictions and empirical frequencies. Accurately estimating this quantity is challenging, especially in the multiclass setting. Here, we show how to extend a recent variational framework for estimating calibration errors beyond divergences induced induced by proper losses, to cover a broad class of calibration errors induced by $L_p$ divergences. Our method can separate over- and under-confidence and, unlike non-variational approaches, avoids overestimation. We provide extensive experiments and integrate our code in the open-source package probmetrics (https://github.com/dholzmueller/probmetrics) for evaluating calibration errors.

