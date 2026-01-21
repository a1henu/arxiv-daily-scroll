---
layout: default
title: Towards Visually Explaining Statistical Tests with Applications in Biomedical Imaging
---

# Towards Visually Explaining Statistical Tests with Applications in Biomedical Imaging
**arXiv**：[2601.13899v1](https://arxiv.org/abs/2601.13899) · [PDF](https://arxiv.org/pdf/2601.13899.pdf)  
**作者**：Masoumeh Javanbakhat, Piotr Komorowski, Dilyara Bareeva, Wei-Chang Lai, Wojciech Samek, Christoph Lippert  

**一句话要点**：提出可解释深度统计测试框架，以增强生物医学成像中无标签群体差异分析的可视化解释。

**关键词**：深度统计测试, 可解释人工智能, 生物医学成像, 双样本测试, 无标签分析, 特征可视化

## 3 点简述
- 核心问题：深度双样本测试缺乏可解释性，现有方法依赖标签，不适用于无标签统计测试场景。
- 方法要点：结合样本级和特征级解释，揭示驱动统计显著差异的样本和输入特征，提供空间和实例级洞察。
- 实验或效果：应用于生物医学成像数据，识别有影响力的样本并突出与疾病相关变异相关的解剖学有意义区域。

## 摘要（原文）

> Deep neural two-sample tests have recently shown strong power for detecting distributional differences between groups, yet their black-box nature limits interpretability and practical adoption in biomedical analysis. Moreover, most existing post-hoc explainability methods rely on class labels, making them unsuitable for label-free statistical testing settings. We propose an explainable deep statistical testing framework that augments deep two-sample tests with sample-level and feature-level explanations, revealing which individual samples and which input features drive statistically significant group differences. Our method highlights which image regions and which individual samples contribute most to the detected group difference, providing spatial and instance-wise insight into the test's decision. Applied to biomedical imaging data, the proposed framework identifies influential samples and highlights anatomically meaningful regions associated with disease-related variation. This work bridges statistical inference and explainable AI, enabling interpretable, label-free population analysis in medical imaging.

