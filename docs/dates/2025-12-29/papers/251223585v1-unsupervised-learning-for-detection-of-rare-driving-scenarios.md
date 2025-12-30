---
layout: default
title: Unsupervised Learning for Detection of Rare Driving Scenarios
---

# Unsupervised Learning for Detection of Rare Driving Scenarios
**arXiv**：[2512.23585v1](https://arxiv.org/abs/2512.23585) · [PDF](https://arxiv.org/pdf/2512.23585.pdf)  
**作者**：Dat Le, Thomas Manhardt, Moritz Venator, Johannes Betz  

**一句话要点**：提出基于深度隔离森林的无监督学习框架，以检测自动驾驶中的罕见危险场景

**关键词**：无监督学习, 异常检测, 自动驾驶安全, 深度隔离森林, 自然驾驶数据

## 3 点简述
- 核心问题：自动驾驶中罕见危险场景的检测对系统安全至关重要，但缺乏监督标签。
- 方法要点：利用深度隔离森林结合神经网络特征与隔离森林，从自然驾驶数据中识别非线性异常。
- 实验或效果：通过代理真值和可视化评估，框架有效识别罕见场景，但依赖手动特征和代理真值。

## 摘要（原文）

> The detection of rare and hazardous driving scenarios is a critical challenge for ensuring the safety and reliability of autonomous systems. This research explores an unsupervised learning framework for detecting rare and extreme driving scenarios using naturalistic driving data (NDD). We leverage the recently proposed Deep Isolation Forest (DIF), an anomaly detection algorithm that combines neural network-based feature representations with Isolation Forests (IFs), to identify non-linear and complex anomalies. Data from perception modules, capturing vehicle dynamics and environmental conditions, is preprocessed into structured statistical features extracted from sliding windows. The framework incorporates t-distributed stochastic neighbor embedding (t-SNE) for dimensionality reduction and visualization, enabling better interpretability of detected anomalies. Evaluation is conducted using a proxy ground truth, combining quantitative metrics with qualitative video frame inspection. Our results demonstrate that the proposed approach effectively identifies rare and hazardous driving scenarios, providing a scalable solution for anomaly detection in autonomous driving systems. Given the study's methodology, it was unavoidable to depend on proxy ground truth and manually defined feature combinations, which do not encompass the full range of real-world driving anomalies or their nuanced contextual dependencies.

