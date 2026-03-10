---
layout: default
title: Electrocardiogram Classification with Transformers Using Koopman and Wavelet Features
---

# Electrocardiogram Classification with Transformers Using Koopman and Wavelet Features
**arXiv**：[2603.08339v1](https://arxiv.org/abs/2603.08339) · [PDF](https://arxiv.org/pdf/2603.08339.pdf)  
**作者**：Sucheta Ghosh, Zahra Monfared  

**一句话要点**：提出基于Koopman算子与小波特征的Transformer方法，用于心电图分类任务。

**关键词**：心电图分类, Koopman算子, 小波变换, Transformer, 时间序列分析, 动态系统理论

## 3 点简述
- 核心问题：心电图信号复杂多变，自动化分类面临挑战。
- 方法要点：结合Koopman算子（通过EDMD近似）和小波变换提取特征，使用Transformer进行分类。
- 实验或效果：Koopman特征在四类分类中表现优异，优化EDMD字典可提升性能，超越小波基线。

## 摘要（原文）

> Electrocardiogram (ECG) analysis is vital for detecting cardiac abnormalities, yet robust automated classification is challenging due to the complexity and variability of physiological signals. In this work, we investigate transformer-based ECG classification using features derived from the Koopman operator and wavelet transforms. Two tasks are studied: (1) binary classification (Normal vs. Non-normal), and (2) four-class classification (Normal, Atrial Fibrillation, Ventricular Arrhythmia, Block). We use Extended Dynamic Mode Decomposition (EDMD) to approximate the Koopman operator. Our results show that wavelet features excel in binary classification, while Koopman features, when paired with transformers, achieve superior performance in the four-class setting. A simple hybrid of Koopman and wavelet features does not improve accuracy. However, selecting an appropriate EDMD dictionary -- specifically a radial basis function dictionary with tuned parameters -- yields significant gains, surpassing the wavelet-only baseline and the hybrid wavelet-Koopman system. We also present a Koopman-based reconstruction analysis for interpretable insights into the learned dynamics and compare against a recurrent neural network baseline. Overall, our findings demonstrate the effectiveness of Koopman-based feature learning with transformers and highlight promising directions for integrating dynamical systems theory into time-series classification.

