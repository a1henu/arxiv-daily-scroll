---
layout: default
title: Training-Free Test-Time Adaptation with Brownian Distance Covariance in Vision-Language Models
---

# Training-Free Test-Time Adaptation with Brownian Distance Covariance in Vision-Language Models
**arXiv**：[2601.23253v1](https://arxiv.org/abs/2601.23253) · [PDF](https://arxiv.org/pdf/2601.23253.pdf)  
**作者**：Yi Zhang, Chun-Wun Cheng, Angelica I. Aviles-Rivero, Zhihai He, Liang-Jie Zhang  

**一句话要点**：提出TaTa方法，利用布朗距离协方差实现免训练测试时适应，以解决视觉语言模型在域偏移下的性能下降问题。

**关键词**：视觉语言模型, 测试时适应, 布朗距离协方差, 免训练优化, 域泛化, 属性增强提示

## 3 点简述
- 核心问题：视觉语言模型在域偏移下性能下降，现有测试时适应方法计算量大且依赖反向传播。
- 方法要点：使用布朗距离协方差动态适应新域，无需训练或反向传播，结合属性增强提示和动态聚类提升推理。
- 实验或效果：在多个数据集上显著降低计算成本，实现领域和跨数据集泛化的先进性能。

## 摘要（原文）

> Vision-language models suffer performance degradation under domain shift, limiting real-world applicability. Existing test-time adaptation methods are computationally intensive, rely on back-propagation, and often focus on single modalities. To address these issues, we propose Training-free Test-Time Adaptation with Brownian Distance Covariance (TaTa). TaTa leverages Brownian Distance Covariance-a powerful statistical measure that captures both linear and nonlinear dependencies via pairwise distances-to dynamically adapt VLMs to new domains without training or back-propagation. This not only improves efficiency but also enhances stability by avoiding disruptive weight updates. TaTa further integrates attribute-enhanced prompting to improve vision-language inference with descriptive visual cues. Combined with dynamic clustering and pseudo-label refinement, it effectively recalibrates the model for novel visual contexts. Experiments across diverse datasets show that TaTa significantly reduces computational cost while achieving state-of-the-art performance in domain and cross-dataset generalization.

