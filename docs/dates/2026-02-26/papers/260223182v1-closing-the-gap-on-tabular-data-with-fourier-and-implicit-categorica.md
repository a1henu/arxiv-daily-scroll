---
layout: default
title: Closing the gap on tabular data with Fourier and Implicit Categorical Features
---

# Closing the gap on tabular data with Fourier and Implicit Categorical Features
**arXiv**：[2602.23182v1](https://arxiv.org/abs/2602.23182) · [PDF](https://arxiv.org/pdf/2602.23182.pdf)  
**作者**：Marius Dragoi, Florin Gogianu, Elena Burceanu  

**一句话要点**：提出基于统计特征处理和傅里叶学习的深度学习方法，以缩小表格数据上神经网络与树模型的性能差距。

**关键词**：表格数据学习, 特征离散化, 傅里叶学习, 深度学习, 树模型对比, 性能提升

## 3 点简述
- 核心问题：深度学习方法在表格数据上表现不如树模型，主要因难以有效建模分类特征的非线性交互。
- 方法要点：使用统计技术识别与目标强相关的离散化特征，并引入傅里叶学习缓解深度模型的过度平滑偏差。
- 实验或效果：在综合基准测试中，该方法显著提升深度学习模型性能，接近或超越XGBoost。

## 摘要（原文）

> While Deep Learning has demonstrated impressive results in applications on various data types, it continues to lag behind tree-based methods when applied to tabular data, often referred to as the last "unconquered castle" for neural networks. We hypothesize that a significant advantage of tree-based methods lies in their intrinsic capability to model and exploit non-linear interactions induced by features with categorical characteristics. In contrast, neural-based methods exhibit biases toward uniform numerical processing of features and smooth solutions, making it challenging for them to effectively leverage such patterns. We address this performance gap by using statistical-based feature processing techniques to identify features that are strongly correlated with the target once discretized. We further mitigate the bias of deep models for overly-smooth solutions, a bias that does not align with the inherent properties of the data, using Learned Fourier. We show that our proposed feature preprocessing significantly boosts the performance of deep learning models and enables them to achieve a performance that closely matches or surpasses XGBoost on a comprehensive tabular data benchmark.

