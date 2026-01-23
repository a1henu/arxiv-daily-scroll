---
layout: default
title: Benchmarking Deep Learning Models for Raman Spectroscopy Across Open-Source Datasets
---

# Benchmarking Deep Learning Models for Raman Spectroscopy Across Open-Source Datasets
**arXiv**：[2601.16107v1](https://arxiv.org/abs/2601.16107) · [PDF](https://arxiv.org/pdf/2601.16107.pdf)  
**作者**：Adithya Sineesh, Akshita Kamsali  

**一句话要点**：提出首个系统基准测试，比较拉曼光谱深度学习模型在开源数据集上的性能

**关键词**：拉曼光谱, 深度学习基准, 开源数据集, 分类模型, 系统评估

## 3 点简述
- 核心问题：现有拉曼光谱深度学习模型缺乏在共享开源数据集上的直接比较，评估常孤立或与传统方法对比。
- 方法要点：在统一训练和超参数调优协议下，评估五个代表性深度学习架构，覆盖三个开源拉曼数据集。
- 实验或效果：报告分类准确率和宏平均F1分数，提供公平可复现的模型比较，支持标准评估、微调和分布偏移测试。

## 摘要（原文）

> Deep learning classifiers for Raman spectroscopy are increasingly reported to outperform classical chemometric approaches. However their evaluations are often conducted in isolation or compared against traditional machine learning methods or trivially adapted vision-based architectures that were not originally proposed for Raman spectroscopy. As a result, direct comparisons between existing deep learning models developed specifically for Raman spectral analysis on shared open-source datasets remain scarce. To the best of our knowledge, this study presents one of the first systematic benchmarks comparing three or more published Raman-specific deep learning classifiers across multiple open-source Raman datasets. We evaluate five representative deep learning architectures under a unified training and hyperparameter tuning protocol across three open-source Raman datasets selected to support standard evaluation, fine-tuning, and explicit distribution-shift testing. We report classification accuracies and macro-averaged F1 scores to provide a fair and reproducible comparison of deep learning models for Raman spectra based classification.

