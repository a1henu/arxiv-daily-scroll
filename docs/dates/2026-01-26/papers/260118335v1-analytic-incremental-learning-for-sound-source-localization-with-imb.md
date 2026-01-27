---
layout: default
title: Analytic Incremental Learning For Sound Source Localization With Imbalance Rectification
---

# Analytic Incremental Learning For Sound Source Localization With Imbalance Rectification
**arXiv**：[2601.18335v1](https://arxiv.org/abs/2601.18335) · [PDF](https://arxiv.org/pdf/2601.18335.pdf)  
**作者**：Zexia Fan, Yu Chen, Qiquan Zhang, Kainan Chen, Xinyuan Qian  

**一句话要点**：提出统一框架以解决声源定位中的双重不平衡问题，提升实际部署性能。

**关键词**：声源定位, 不平衡学习, 灾难性遗忘, 数据增强, 动态校正, 任务适应

## 3 点简述
- 核心问题：声源定位面临长尾分布和跨任务不平衡，导致灾难性遗忘和精度下降。
- 方法要点：设计GCC-PHAT数据增强缓解任务内不平衡，提出分析动态不平衡校正器适应任务间动态。
- 实验或效果：在SSLR基准上实现89.0%准确率，平均绝对误差5.3°，展示无需样本存储的鲁棒性。

## 摘要（原文）

> Sound source localization (SSL) demonstrates remarkable results in controlled settings but struggles in real-world deployment due to dual imbalance challenges: intra-task imbalance arising from long-tailed direction-of-arrival (DoA) distributions, and inter-task imbalance induced by cross-task skews and overlaps. These often lead to catastrophic forgetting, significantly degrading the localization accuracy. To mitigate these issues, we propose a unified framework with two key innovations. Specifically, we design a GCC-PHAT-based data augmentation (GDA) method that leverages peak characteristics to alleviate intra-task distribution skews. We also propose an Analytic dynamic imbalance rectifier (ADIR) with task-adaption regularization, which enables analytic updates that adapt to inter-task dynamics. On the SSLR benchmark, our proposal achieves state-of-the-art (SoTA) results of 89.0% accuracy, 5.3° mean absolute error, and 1.6 backward transfer, demonstrating robustness to evolving imbalances without exemplar storage.

