---
layout: default
title: Multi-Cue Anomaly Detection and Localization under Data Contamination
---

# Multi-Cue Anomaly Detection and Localization under Data Contamination
**arXiv**：[2601.22913v1](https://arxiv.org/abs/2601.22913) · [PDF](https://arxiv.org/pdf/2601.22913.pdf)  
**作者**：Anindya Sundar Das, Monowar Bhuyan  

**一句话要点**：提出多线索异常检测框架，结合有限异常监督解决数据污染下的工业视觉异常检测问题

**关键词**：异常检测, 数据污染, 多线索融合, 有限监督, 工业视觉, 可解释性

## 3 点简述
- 核心问题：现有方法假设训练数据纯净且无异常标签，在现实工业数据污染场景下性能受限
- 方法要点：集成偏差学习、不确定性评估和空间分割三线索，通过自适应加权处理污染样本
- 实验效果：在MVTec和VisA基准上超越现有方法，实现强检测定位性能和可解释性

## 摘要（原文）

> Visual anomaly detection in real-world industrial settings faces two major limitations. First, most existing methods are trained on purely normal data or on unlabeled datasets assumed to be predominantly normal, presuming the absence of contamination, an assumption that is rarely satisfied in practice. Second, they assume no access to labeled anomaly samples, limiting the model from learning discriminative characteristics of true anomalies. Therefore, these approaches often struggle to distinguish anomalies from normal instances, resulting in reduced detection and weak localization performance. In real-world applications, where training data are frequently contaminated with anomalies, such methods fail to deliver reliable performance. In this work, we propose a robust anomaly detection framework that integrates limited anomaly supervision into the adaptive deviation learning paradigm. We introduce a composite anomaly score that combines three complementary components: a deviation score capturing statistical irregularity, an entropy-based uncertainty score reflecting predictive inconsistency, and a segmentation-based score highlighting spatial abnormality. This unified scoring mechanism enables accurate detection and supports gradient-based localization, providing intuitive and explainable visual evidence of anomalous regions. Following the few-anomaly paradigm, we incorporate a small set of labeled anomalies during training while simultaneously mitigating the influence of contaminated samples through adaptive instance weighting. Extensive experiments on the MVTec and VisA benchmarks demonstrate that our framework outperforms state-of-the-art baselines and achieves strong detection and localization performance, interpretability, and robustness under various levels of data contamination.

