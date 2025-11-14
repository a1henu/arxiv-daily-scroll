---
layout: default
title: Intrinsic Dimensionality as a Model-Free Measure of Class Imbalance
---

# Intrinsic Dimensionality as a Model-Free Measure of Class Imbalance
**arXiv**：[2511.10475v1](https://arxiv.org/abs/2511.10475) · [PDF](https://arxiv.org/pdf/2511.10475.pdf)  
**作者**：Çağrı Eser, Zeynep Sonat Baltacı, Emre Akbaş, Sinan Kalkan  

**一句话要点**：提出内在维度作为模型无关的类别不平衡度量，以改进分类任务中的不平衡缓解方法。

**关键词**：类别不平衡, 内在维度, 模型无关度量, 分类任务, 不平衡缓解

## 3 点简述
- 核心问题：类别不平衡常用样本数量度量，忽略冗余样本和类别学习难度差异。
- 方法要点：使用内在维度作为易计算、模型无关的不平衡度量，可整合到多种缓解方法中。
- 实验或效果：在五个数据集上，内在维度优于基于数量的重加权和重采样方法。

## 摘要（原文）

> Imbalance in classification tasks is commonly quantified by the cardinalities of examples across classes. This, however, disregards the presence of redundant examples and inherent differences in the learning difficulties of classes. Alternatively, one can use complex measures such as training loss and uncertainty, which, however, depend on training a machine learning model. Our paper proposes using data Intrinsic Dimensionality (ID) as an easy-to-compute, model-free measure of imbalance that can be seamlessly incorporated into various imbalance mitigation methods. Our results across five different datasets with a diverse range of imbalance ratios show that ID consistently outperforms cardinality-based re-weighting and re-sampling techniques used in the literature. Moreover, we show that combining ID with cardinality can further improve performance. Code: https://github.com/cagries/IDIM.

