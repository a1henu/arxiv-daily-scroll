---
layout: default
title: milearn: A Python Package for Multi-Instance Machine Learning
---

# milearn: A Python Package for Multi-Instance Machine Learning
**arXiv**：[2512.01287v1](https://arxiv.org/abs/2512.01287) · [PDF](https://arxiv.org/pdf/2512.01287.pdf)  
**作者**：Dmitry Zankov, Pavlo Polishchuk, Michal Sobieraj, Mario Barbatti  

**一句话要点**：提出milearn包以统一多示例学习算法，支持小数据集超参数优化。

**关键词**：多示例学习, Python包, 超参数优化, 小数据集, 关键实例检测, 分子性质预测

## 3 点简述
- 核心问题：多示例学习在回归和分类任务中缺乏统一框架，小数据集模型选择困难。
- 方法要点：提供scikit-learn接口，集成经典和神经网络算法，内置超参数优化。
- 实验或效果：在合成基准数据集上验证，包括数字分类、分子性质预测和蛋白质互作预测。

## 摘要（原文）

> We introduce milearn, a Python package for multi-instance learning (MIL) that follows the familiar scikit-learn fit/predict interface while providing a unified framework for both classical and neural-network-based MIL algorithms for regression and classification. The package also includes built-in hyperparameter optimization designed specifically for small MIL datasets, enabling robust model selection in data-scarce scenarios. We demonstrate the versatility of milearn across a broad range of synthetic MIL benchmark datasets, including digit classification and regression, molecular property prediction, and protein-protein interaction (PPI) prediction. Special emphasis is placed on the key instance detection (KID) problem, for which the package provides dedicated support.

