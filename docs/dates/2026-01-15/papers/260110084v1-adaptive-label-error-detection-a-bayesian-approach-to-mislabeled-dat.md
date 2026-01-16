---
layout: default
title: Adaptive Label Error Detection: A Bayesian Approach to Mislabeled Data Detection
---

# Adaptive Label Error Detection: A Bayesian Approach to Mislabeled Data Detection
**arXiv**：[2601.10084v1](https://arxiv.org/abs/2601.10084) · [PDF](https://arxiv.org/pdf/2601.10084.pdf)  
**作者**：Zan Chaudhry, Noam H. Rotenberg, Brian Caffo, Craig K. Jones, Haris I. Sair  

**一句话要点**：提出自适应标签错误检测方法，以解决医学图像数据中错误标注导致的模型性能下降问题。

**关键词**：标签错误检测, 医学图像分析, 高斯分布建模, 似然比测试, 深度学习特征提取

## 3 点简述
- 核心问题：机器学习分类系统易受错误标注影响，即使专家标注也可能存在误标，需高效检测与纠正。
- 方法要点：从深度卷积神经网络提取特征，去噪后建模为多维高斯分布，通过似然比测试识别误标样本。
- 实验或效果：在多个医学图像数据集上，相比现有方法，ALED显著提高检测灵敏度且保持精度，校正后微调模型可减少33.8%测试错误。

## 摘要（原文）

> Machine learning classification systems are susceptible to poor performance when trained with incorrect ground truth labels, even when data is well-curated by expert annotators. As machine learning becomes more widespread, it is increasingly imperative to identify and correct mislabeling to develop more powerful models. In this work, we motivate and describe Adaptive Label Error Detection (ALED), a novel method of detecting mislabeling. ALED extracts an intermediate feature space from a deep convolutional neural network, denoises the features, models the reduced manifold of each class with a multidimensional Gaussian distribution, and performs a simple likelihood ratio test to identify mislabeled samples. We show that ALED has markedly increased sensitivity, without compromising precision, compared to established label error detection methods, on multiple medical imaging datasets. We demonstrate an example where fine-tuning a neural network on corrected data results in a 33.8% decrease in test set errors, providing strong benefits to end users. The ALED detector is deployed in the Python package statlab.

