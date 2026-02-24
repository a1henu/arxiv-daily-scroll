---
layout: default
title: Drift Localization using Conformal Predictions
---

# Drift Localization using Conformal Predictions
**arXiv**：[2602.19790v1](https://arxiv.org/abs/2602.19790) · [PDF](https://arxiv.org/pdf/2602.19790.pdf)  
**作者**：Fabian Hinder, Valerie Vaquet, Johannes Brinkrolf, Barbara Hammer  

**一句话要点**：提出基于共形预测的漂移定位方法，以解决高维低信号场景下的概念漂移问题。

**关键词**：概念漂移, 漂移定位, 共形预测, 高维数据, 机器学习监控

## 3 点简述
- 核心问题：概念漂移导致学习系统性能下降，现有局部测试方法在高维低信号场景中易失效。
- 方法要点：采用共形预测框架，通过统计置信度来定位受漂移影响的样本，避免依赖局部假设。
- 实验或效果：在先进图像数据集上验证了方法的性能，展示了其优于常见方法的潜力。

## 摘要（原文）

> Concept drift -- the change of the distribution over time -- poses significant challenges for learning systems and is of central interest for monitoring. Understanding drift is thus paramount, and drift localization -- determining which samples are affected by the drift -- is essential. While several approaches exist, most rely on local testing schemes, which tend to fail in high-dimensional, low-signal settings. In this work, we consider a fundamentally different approach based on conformal predictions. We discuss and show the shortcomings of common approaches and demonstrate the performance of our approach on state-of-the-art image datasets.

