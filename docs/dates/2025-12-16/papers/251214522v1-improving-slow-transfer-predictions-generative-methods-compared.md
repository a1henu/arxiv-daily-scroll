---
layout: default
title: Improving Slow Transfer Predictions: Generative Methods Compared
---

# Improving Slow Transfer Predictions: Generative Methods Compared
**arXiv**：[2512.14522v1](https://arxiv.org/abs/2512.14522) · [PDF](https://arxiv.org/pdf/2512.14522.pdf)  
**作者**：Jacob Taegon Kim, Alex Sim, Kesheng Wu, Jinoh Kim  

**一句话要点**：比较生成方法以解决科学计算网络中数据转移预测的类别不平衡问题

**关键词**：数据转移预测, 类别不平衡, 生成方法, 过采样, CTGAN, 科学计算网络

## 3 点简述
- 核心问题：机器学习模型在数据转移性能预测中面临类别不平衡，影响预测准确性。
- 方法要点：分析并比较传统过采样与生成技术（如CTGAN）等增强策略，调整训练数据集的不平衡比例。
- 实验或效果：增强策略可能提升性能，但随着不平衡比例增加，性能改善不显著，CTGAN未明显优于简单分层采样。

## 摘要（原文）

> Monitoring data transfer performance is a crucial task in scientific computing networks. By predicting performance early in the communication phase, potentially sluggish transfers can be identified and selectively monitored, optimizing network usage and overall performance. A key bottleneck to improving the predictive power of machine learning (ML) models in this context is the issue of class imbalance. This project focuses on addressing the class imbalance problem to enhance the accuracy of performance predictions. In this study, we analyze and compare various augmentation strategies, including traditional oversampling methods and generative techniques. Additionally, we adjust the class imbalance ratios in training datasets to evaluate their impact on model performance. While augmentation may improve performance, as the imbalance ratio increases, the performance does not significantly improve. We conclude that even the most advanced technique, such as CTGAN, does not significantly improve over simple stratified sampling.

