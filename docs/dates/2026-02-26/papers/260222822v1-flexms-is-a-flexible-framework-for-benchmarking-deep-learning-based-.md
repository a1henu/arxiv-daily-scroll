---
layout: default
title: FlexMS is a flexible framework for benchmarking deep learning-based mass spectrum prediction tools in metabolomics
---

# FlexMS is a flexible framework for benchmarking deep learning-based mass spectrum prediction tools in metabolomics
**arXiv**：[2602.22822v1](https://arxiv.org/abs/2602.22822) · [PDF](https://arxiv.org/pdf/2602.22822.pdf)  
**作者**：Yunhua Zhong, Yixuan Tang, Yifan Li, Jie Yang, Pan Liu, Jun Xia  

**一句话要点**：提出FlexMS框架以解决代谢组学中深度学习质谱预测工具缺乏统一基准的问题

**关键词**：质谱预测, 深度学习基准, 代谢组学, 模型评估, 检索基准

## 3 点简述
- 核心问题：深度学习质谱预测模型评估困难，源于方法异质性和基准缺失。
- 方法要点：FlexMS支持动态构建多种模型架构，并在预处理公共数据集上评估性能。
- 实验或效果：分析数据集多样性、超参数、预训练等影响因素，提供模型选择指导。

## 摘要（原文）

> The identification and property prediction of chemical molecules is of central importance in the advancement of drug discovery and material science, where the tandem mass spectrometry technology gives valuable fragmentation cues in the form of mass-to-charge ratio peaks. However, the lack of experimental spectra hinders the attachment of each molecular identification, and thus urges the establishment of prediction approaches for computational models. Deep learning models appear promising for predicting molecular structure spectra, but overall assessment remains challenging as a result of the heterogeneity in methods and the lack of well-defined benchmarks. To address this, our contribution is the creation of benchmark framework FlexMS for constructing and evaluating diverse model architectures in mass spectrum prediction. With its easy-to-use flexibility, FlexMS supports the dynamic construction of numerous distinct combinations of model architectures, while assessing their performance on preprocessed public datasets using different metrics. In this paper, we provide insights into factors influencing performance, including the structural diversity of datasets, hyperparameters like learning rate and data sparsity, pretraining effects, metadata ablation settings and cross-domain transfer learning analysis. This provides practical guidance in choosing suitable models. Moreover, retrieval benchmarks simulate practical identification scenarios and score potential matches based on predicted spectra.

