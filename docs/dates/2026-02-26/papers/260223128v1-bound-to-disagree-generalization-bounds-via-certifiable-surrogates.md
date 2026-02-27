---
layout: default
title: Bound to Disagree: Generalization Bounds via Certifiable Surrogates
---

# Bound to Disagree: Generalization Bounds via Certifiable Surrogates
**arXiv**：[2602.23128v1](https://arxiv.org/abs/2602.23128) · [PDF](https://arxiv.org/pdf/2602.23128.pdf)  
**作者**：Mathieu Bazinet, Valentina Zantedeschi, Pascal Germain  

**一句话要点**：提出基于可认证代理模型的泛化界方法，以解决深度学习泛化界空洞或不可计算问题。

**关键词**：泛化界, 代理模型, 分歧证书, PAC-Bayes理论, 模型压缩, 样本压缩

## 3 点简述
- 核心问题：深度学习泛化界通常空洞、不可计算或限于特定模型类。
- 方法要点：通过代理模型和未标记数据评估分歧界，提供可认证的泛化保证。
- 实验或效果：利用样本压缩、模型压缩和PAC-Bayes理论训练代理模型，实证展示证书紧致性。

## 摘要（原文）

> Generalization bounds for deep learning models are typically vacuous, not computable or restricted to specific model classes. In this paper, we tackle these issues by providing new disagreement-based certificates for the gap between the true risk of any two predictors. We then bound the true risk of the predictor of interest via a surrogate model that enjoys tight generalization guarantees, and evaluating our disagreement bound on an unlabeled dataset. We empirically demonstrate the tightness of the obtained certificates and showcase the versatility of the approach by training surrogate models leveraging three different frameworks: sample compression, model compression and PAC-Bayes theory. Importantly, such guarantees are achieved without modifying the target model, nor adapting the training procedure to the generalization framework.

