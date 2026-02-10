---
layout: default
title: M-Loss: Quantifying Model Merging Compatibility with Limited Unlabeled Data
---

# M-Loss: Quantifying Model Merging Compatibility with Limited Unlabeled Data
**arXiv**：[2602.08564v1](https://arxiv.org/abs/2602.08564) · [PDF](https://arxiv.org/pdf/2602.08564.pdf)  
**作者**：Tiantong Wang, Yiyang Duan, Haoyu Chen, Tiantong Wu, Wei Yang Bryan Lim  

**一句话要点**：提出M-Loss以量化模型合并兼容性，使用少量无标签数据评估合并可行性。

**关键词**：模型合并, 模型集成, 无标签数据, 评估指标, 参数平均, 模型剪枝

## 3 点简述
- 核心问题：模型合并常因权重差异导致性能下降，缺乏理论评估指标。
- 方法要点：通过比较参数平均与模型集成差异，量化合并兼容性，指导合并策略。
- 实验或效果：理论分析与实证表明，M-Loss提升合并模型与模型集成的对齐度。

## 摘要（原文）

> Training of large-scale models is both computationally intensive and often constrained by the availability of labeled data. Model merging offers a compelling alternative by directly integrating the weights of multiple source models without requiring additional data or extensive training. However, conventional model merging techniques, such as parameter averaging, often suffer from the unintended combination of non-generalizable features, especially when source models exhibit significant weight disparities. Comparatively, model ensembling generally provides more stable and superior performance that aggregates multiple models by averaging outputs. However, it incurs higher inference costs and increased storage requirements. While previous studies experimentally showed the similarities between model merging and ensembling, theoretical evidence and evaluation metrics remain lacking. To address this gap, we introduce Merging-ensembling loss (M-Loss), a novel evaluation metric that quantifies the compatibility of merging source models using very limited unlabeled data. By measuring the discrepancy between parameter averaging and model ensembling at layer and node levels, M-Loss facilitates more effective merging strategies. Specifically, M-Loss serves both as a quantitative criterion of the theoretical feasibility of model merging, and a guide for parameter significance in model pruning. Our theoretical analysis and empirical evaluations demonstrate that incorporating M-Loss into the merging process significantly improves the alignment between merged models and model ensembling, providing a scalable and efficient framework for accurate model consolidation.

