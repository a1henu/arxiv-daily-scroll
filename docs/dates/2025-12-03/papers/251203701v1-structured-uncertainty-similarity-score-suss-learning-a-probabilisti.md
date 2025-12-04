---
layout: default
title: Structured Uncertainty Similarity Score (SUSS): Learning a Probabilistic, Interpretable, Perceptual Metric Between Images
---

# Structured Uncertainty Similarity Score (SUSS): Learning a Probabilistic, Interpretable, Perceptual Metric Between Images
**arXiv**：[2512.03701v1](https://arxiv.org/abs/2512.03701) · [PDF](https://arxiv.org/pdf/2512.03701.pdf)  
**作者**：Paula Seidler, Neill D. F. Campbell, Ivor J A Simpson  

**一句话要点**：提出结构化不确定性相似度评分以解决图像感知相似度评估中的可解释性与对齐问题

**关键词**：感知相似度评分, 结构化不确定性建模, 可解释性评估, 生成式自监督学习, 图像感知损失

## 3 点简述
- 核心问题：现有感知相似度评分如LPIPS缺乏可解释性，而SSIM等手工方法缺失关键感知属性。
- 方法要点：通过结构化多元正态分布建模图像感知组件，以生成式自监督训练学习人类不可察觉的增强。
- 实验或效果：SUSS在人类感知判断对齐、感知校准和可解释性方面表现优异，并作为感知损失在下游任务中具有竞争力。

## 摘要（原文）

> Perceptual similarity scores that align with human vision are critical for both training and evaluating computer vision models. Deep perceptual losses, such as LPIPS, achieve good alignment but rely on complex, highly non-linear discriminative features with unknown invariances, while hand-crafted measures like SSIM are interpretable but miss key perceptual properties.
>   We introduce the Structured Uncertainty Similarity Score (SUSS); it models each image through a set of perceptual components, each represented by a structured multivariate Normal distribution. These are trained in a generative, self-supervised manner to assign high likelihood to human-imperceptible augmentations. The final score is a weighted sum of component log-probabilities with weights learned from human perceptual datasets. Unlike feature-based methods, SUSS learns image-specific linear transformations of residuals in pixel space, enabling transparent inspection through decorrelated residuals and sampling.
>   SUSS aligns closely with human perceptual judgments, shows strong perceptual calibration across diverse distortion types, and provides localized, interpretable explanations of its similarity assessments. We further demonstrate stable optimization behavior and competitive performance when using SUSS as a perceptual loss for downstream imaging tasks.

