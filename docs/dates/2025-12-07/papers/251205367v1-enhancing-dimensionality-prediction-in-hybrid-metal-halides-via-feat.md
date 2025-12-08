---
layout: default
title: Enhancing Dimensionality Prediction in Hybrid Metal Halides via Feature Engineering and Class-Imbalance Mitigation
---

# Enhancing Dimensionality Prediction in Hybrid Metal Halides via Feature Engineering and Class-Imbalance Mitigation
**arXiv**：[2512.05367v1](https://arxiv.org/abs/2512.05367) · [PDF](https://arxiv.org/pdf/2512.05367.pdf)  
**作者**：Mariia Karabin, Isaac Armstrong, Leo Beck, Paulina Apanel, Markus Eisenbach, David B. Mitzi, Hanna Terletska, Hendrik Heinz  

**一句话要点**：提出基于特征工程和类别不平衡处理的机器学习框架，以预测杂化金属卤化物的结构维度。

**关键词**：杂化金属卤化物, 结构维度预测, 特征工程, 类别不平衡处理, 机器学习框架, SMOTE

## 3 点简述
- 核心问题：杂化金属卤化物数据集类别不平衡，影响维度预测准确性。
- 方法要点：结合化学特征工程、SMOTE过采样和多阶段工作流优化模型。
- 实验或效果：显著提升少数类F1分数，实现稳健的交叉验证性能。

## 摘要（原文）

> We present a machine learning framework for predicting the structural dimensionality of hybrid metal halides (HMHs), including organic-inorganic perovskites, using a combination of chemically-informed feature engineering and advanced class-imbalance handling techniques. The dataset, consisting of 494 HMH structures, is highly imbalanced across dimensionality classes (0D, 1D, 2D, 3D), posing significant challenges to predictive modeling. This dataset was later augmented to 1336 via the Synthetic Minority Oversampling Technique (SMOTE) to mitigate the effects of the class imbalance. We developed interaction-based descriptors and integrated them into a multi-stage workflow that combines feature selection, model stacking, and performance optimization to improve dimensionality prediction accuracy. Our approach significantly improves F1-scores for underrepresented classes, achieving robust cross-validation performance across all dimensionalities.

