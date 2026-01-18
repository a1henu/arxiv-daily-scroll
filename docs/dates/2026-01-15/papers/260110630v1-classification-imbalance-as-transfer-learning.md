---
layout: default
title: Classification Imbalance as Transfer Learning
---

# Classification Imbalance as Transfer Learning
**arXiv**：[2601.10630v1](https://arxiv.org/abs/2601.10630) · [PDF](https://arxiv.org/pdf/2601.10630.pdf)  
**作者**：Eric Xia, Jason M. Klusowski  

**一句话要点**：将分类不平衡视为迁移学习，分析过采样方法的转移成本以指导策略选择。

**关键词**：分类不平衡, 迁移学习, 过采样, SMOTE, 转移成本, 自助法

## 3 点简述
- 核心问题：分类不平衡时，少数类样本稀少，影响模型性能评估。
- 方法要点：将不平衡数据视为源分布，平衡分布为目标，通过过采样估计少数类分布，量化转移成本。
- 实验或效果：理论分析表明，在高维中，SMOTE的转移成本高于自助法，实验支持自助法通常更优。

## 摘要（原文）

> Classification imbalance arises when one class is much rarer than the other. We frame this setting as transfer learning under label (prior) shift between an imbalanced source distribution induced by the observed data and a balanced target distribution under which performance is evaluated. Within this framework, we study a family of oversampling procedures that augment the training data by generating synthetic samples from an estimated minority-class distribution to roughly balance the classes, among which the celebrated SMOTE algorithm is a canonical example. We show that the excess risk decomposes into the rate achievable under balanced training (as if the data had been drawn from the balanced target distribution) and an additional term, the cost of transfer, which quantifies the discrepancy between the estimated and true minority-class distributions. In particular, we show that the cost of transfer for SMOTE dominates that of bootstrapping (random oversampling) in moderately high dimensions, suggesting that we should expect bootstrapping to have better performance than SMOTE in general. We corroborate these findings with experimental evidence. More broadly, our results provide guidance for choosing among augmentation strategies for imbalanced classification.

