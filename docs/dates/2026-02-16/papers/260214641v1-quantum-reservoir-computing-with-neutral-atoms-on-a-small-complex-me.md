---
layout: default
title: Quantum Reservoir Computing with Neutral Atoms on a Small, Complex, Medical Dataset
---

# Quantum Reservoir Computing with Neutral Atoms on a Small, Complex, Medical Dataset
**arXiv**：[2602.14641v1](https://arxiv.org/abs/2602.14641) · [PDF](https://arxiv.org/pdf/2602.14641.pdf)  
**作者**：Luke Antoncich, Yuben Moodley, Ugo Varetto, Jingbo Wang, Jonathan Wurtz, Jing Chen, Pascal Jahan Elahi, Casey R. Myers  

**一句话要点**：提出量子储层计算用于小规模复杂医疗数据集，通过硬件执行提升模型准确性和稳定性。

**关键词**：量子储层计算, 医疗数据集, 中性原子处理器, 正则化效应, 特征分布分析

## 3 点简述
- 核心问题：医疗数据非线性关系、特征相关性和规模小，经典机器学习方法面临挑战。
- 方法要点：使用中性原子Rydberg处理器Aquila进行量子储层计算，对比无噪声仿真和硬件执行。
- 实验或效果：硬件执行模型在测试准确率上显著提升，并表现出正则化效应，减少过拟合。

## 摘要（原文）

> Biomarker-based prediction of clinical outcomes is challenging due to nonlinear relationships, correlated features, and the limited size of many medical datasets. Classical machine-learning methods can struggle under these conditions, motivating the search for alternatives. In this work, we investigate quantum reservoir computing (QRC), using both noiseless emulation and hardware execution on the neutral-atom Rydberg processor \textit{Aquila}. We evaluate performance with six classical machine-learning models and use SHAP to generate feature subsets. We find that models trained on emulated quantum features achieve mean test accuracies comparable to those trained on classical features, but have higher training accuracies and greater variability over data splits, consistent with overfitting. When comparing hardware execution of QRC to noiseless emulation, the models are more robust over different data splits and often exhibit statistically significant improvements in mean test accuracy. This combination of improved accuracy and increased stability is suggestive of a regularising effect induced by hardware execution. To investigate the origin of this behaviour, we examine the statistical differences between hardware and emulated quantum feature distributions. We find that hardware execution applies a structured, time-dependent transformation characterised by compression toward the mean and a progressive reduction in mutual information relative to emulation.

