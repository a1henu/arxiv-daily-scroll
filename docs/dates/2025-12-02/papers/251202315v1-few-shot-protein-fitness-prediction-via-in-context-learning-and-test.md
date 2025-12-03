---
layout: default
title: Few-shot Protein Fitness Prediction via In-context Learning and Test-time Training
---

# Few-shot Protein Fitness Prediction via In-context Learning and Test-time Training
**arXiv**：[2512.02315v1](https://arxiv.org/abs/2512.02315) · [PDF](https://arxiv.org/pdf/2512.02315.pdf)  
**作者**：Felix Teufel, Aaron W. Kollasch, Yining Huang, Ole Winther, Kevin K. Yang, Pascal Notin, Debora S. Marks  

**一句话要点**：提出PRIMO框架，结合上下文学习与测试时训练，以解决蛋白质适应度预测中数据稀缺问题。

**关键词**：蛋白质适应度预测, 上下文学习, 测试时训练, Transformer, 掩码语言建模, 偏好损失

## 3 点简述
- 核心问题：蛋白质工程中，实验数据有限时准确预测适应度是持续挑战。
- 方法要点：基于Transformer，通过预训练掩码语言建模统一编码序列、零射预测和稀疏标签，使用偏好损失函数。
- 实验或效果：在多种蛋白质家族和突变类型中，优于零射和全监督基线方法。

## 摘要（原文）

> Accurately predicting protein fitness with minimal experimental data is a persistent challenge in protein engineering. We introduce PRIMO (PRotein In-context Mutation Oracle), a transformer-based framework that leverages in-context learning and test-time training to adapt rapidly to new proteins and assays without large task-specific datasets. By encoding sequence information, auxiliary zero-shot predictions, and sparse experimental labels from many assays as a unified token set in a pre-training masked-language modeling paradigm, PRIMO learns to prioritize promising variants through a preference-based loss function. Across diverse protein families and properties-including both substitution and indel mutations-PRIMO outperforms zero-shot and fully supervised baselines. This work underscores the power of combining large-scale pre-training with efficient test-time adaptation to tackle challenging protein design tasks where data collection is expensive and label availability is limited.

