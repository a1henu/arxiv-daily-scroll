---
layout: default
title: AdaCap: An Adaptive Contrastive Approach for Small-Data Neural Networks
---

# AdaCap: An Adaptive Contrastive Approach for Small-Data Neural Networks
**arXiv**：[2511.20170v1](https://arxiv.org/abs/2511.20170) · [PDF](https://arxiv.org/pdf/2511.20170.pdf)  
**作者**：Bruno Belucci, Karim Lounici, Katia Meziani  

**一句话要点**：提出AdaCap自适应对比方法，增强小样本表格数据上神经网络的性能。

**关键词**：小样本学习, 对比学习, 表格数据, 神经网络正则化, 回归任务

## 3 点简述
- 神经网络在小样本表格数据集上表现不佳，树模型仍占主导。
- 结合置换对比损失和Tikhonov闭式输出映射，实现自适应正则化。
- 在85个真实回归数据集上显著提升性能，尤其适用于残差模型。

## 摘要（原文）

> Neural networks struggle on small tabular datasets, where tree-based models remain dominant. We introduce Adaptive Contrastive Approach (AdaCap), a training scheme that combines a permutation-based contrastive loss with a Tikhonov-based closed-form output mapping. Across 85 real-world regression datasets and multiple architectures, AdaCap yields consistent and statistically significant improvements in the small-sample regime, particularly for residual models. A meta-predictor trained on dataset characteristics (size, skewness, noise) accurately anticipates when AdaCap is beneficial. These results show that AdaCap acts as a targeted regularization mechanism, strengthening neural networks precisely where they are most fragile. All results and code are publicly available at https://github.com/BrunoBelucci/adacap.

