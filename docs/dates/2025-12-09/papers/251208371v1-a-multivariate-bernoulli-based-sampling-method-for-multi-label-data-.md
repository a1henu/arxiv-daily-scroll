---
layout: default
title: A Multivariate Bernoulli-Based Sampling Method for Multi-Label Data with Application to Meta-Research
---

# A Multivariate Bernoulli-Based Sampling Method for Multi-Label Data with Application to Meta-Research
**arXiv**：[2512.08371v1](https://arxiv.org/abs/2512.08371) · [PDF](https://arxiv.org/pdf/2512.08371.pdf)  
**作者**：Simon Chung, Colby J. Vorland, Donna L. Maney, Andrew W. Brown  

**一句话要点**：提出基于多元伯努利分布的采样方法，以解决多标签数据中稀有标签样本不足的问题。

**关键词**：多标签采样, 多元伯努利分布, 标签依赖, 加权采样, 数据平衡, 元研究

## 3 点简述
- 核心问题：多标签数据中标签非互斥且频率差异大，导致稀有标签样本不足，影响推断准确性。
- 方法要点：利用多元伯努利分布建模标签依赖，基于观测频率估计参数并计算权重，实现加权采样。
- 实验或效果：应用于Web of Science生物医学文章数据集，平衡了类别频率，提升了少数类别的代表性。

## 摘要（原文）

> Datasets may contain observations with multiple labels. If the labels are not mutually exclusive, and if the labels vary greatly in frequency, obtaining a sample that includes sufficient observations with scarcer labels to make inferences about those labels, and which deviates from the population frequencies in a known manner, creates challenges. In this paper, we consider a multivariate Bernoulli distribution as our underlying distribution of a multi-label problem. We present a novel sampling algorithm that takes label dependencies into account. It uses observed label frequencies to estimate multivariate Bernoulli distribution parameters and calculate weights for each label combination. This approach ensures the weighted sampling acquires target distribution characteristics while accounting for label dependencies. We applied this approach to a sample of research articles from Web of Science labeled with 64 biomedical topic categories. We aimed to preserve category frequency order, reduce frequency differences between most and least common categories, and account for category dependencies. This approach produced a more balanced sub-sample, enhancing the representation of minority categories.

