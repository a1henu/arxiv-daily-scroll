---
layout: default
title: Mitigating Individual Skin Tone Bias in Skin Lesion Classification through Distribution-Aware Reweighting
---

# Mitigating Individual Skin Tone Bias in Skin Lesion Classification through Distribution-Aware Reweighting
**arXiv**：[2512.08733v1](https://arxiv.org/abs/2512.08733) · [PDF](https://arxiv.org/pdf/2512.08733.pdf)  
**作者**：Kuniko Paxton, Zeinab Dehghani, Koorosh Aslansefat, Dhavalkumar Thakker, Yiannis Papadopoulos  

**一句话要点**：提出基于分布感知重加权的框架，以缓解皮肤病变分类中的个体肤色偏差。

**关键词**：皮肤病变分类, 个体公平性, 分布感知重加权, 统计距离度量, 核密度估计, 医学图像分析

## 3 点简述
- 核心问题：传统基于粗粒度子组的公平性方法忽视个体肤色连续变化，可能导致组内异常值偏差被掩盖。
- 方法要点：将肤色视为连续属性，使用核密度估计建模分布，并基于统计距离度量设计重加权损失函数。
- 实验或效果：在CNN和Transformer模型上验证，分布感知重加权优于分类方法，特定距离度量如Fidelity Similarity表现更优。

## 摘要（原文）

> Skin color has historically been a focal point of discrimination, yet fairness research in machine learning for medical imaging often relies on coarse subgroup categories, overlooking individual-level variations. Such group-based approaches risk obscuring biases faced by outliers within subgroups. This study introduces a distribution-based framework for evaluating and mitigating individual fairness in skin lesion classification. We treat skin tone as a continuous attribute rather than a categorical label, and employ kernel density estimation (KDE) to model its distribution. We further compare twelve statistical distance metrics to quantify disparities between skin tone distributions and propose a distance-based reweighting (DRW) loss function to correct underrepresentation in minority tones. Experiments across CNN and Transformer models demonstrate: (i) the limitations of categorical reweighting in capturing individual-level disparities, and (ii) the superior performance of distribution-based reweighting, particularly with Fidelity Similarity (FS), Wasserstein Distance (WD), Hellinger Metric (HM), and Harmonic Mean Similarity (HS). These findings establish a robust methodology for advancing fairness at individual level in dermatological AI systems, and highlight broader implications for sensitive continuous attributes in medical image analysis.

