---
layout: default
title: Criticality Metrics for Relevance Classification in Safety Evaluation of Object Detection in Automated Driving
---

# Criticality Metrics for Relevance Classification in Safety Evaluation of Object Detection in Automated Driving
**arXiv**：[2512.15181v1](https://arxiv.org/abs/2512.15181) · [PDF](https://arxiv.org/pdf/2512.15181.pdf)  
**作者**：Jörg Gamerdinger, Sven Teufel, Stephan Amann, Oliver Bringmann  

**一句话要点**：提出双向关键性评分与多指标聚合策略，以提升自动驾驶中目标检测系统的安全评估准确性。

**关键词**：自动驾驶安全评估, 目标检测系统, 关键性指标, DeepAccident数据集, 多指标聚合

## 3 点简述
- 核心问题：现有目标检测评估指标缺乏安全特异性，需区分相关与非相关对象以进行安全评估。
- 方法要点：通过文献综述识别关键性指标，并引入双向关键性评分和多指标聚合策略优化评估。
- 实验或效果：在DeepAccident数据集上验证，关键性分类准确率提升高达100%，显著增强安全评估能力。

## 摘要（原文）

> Ensuring safety is the primary objective of automated driving, which necessitates a comprehensive and accurate perception of the environment. While numerous performance evaluation metrics exist for assessing perception capabilities, incorporating safety-specific metrics is essential to reliably evaluate object detection systems. A key component for safety evaluation is the ability to distinguish between relevant and non-relevant objects - a challenge addressed by criticality or relevance metrics. This paper presents the first in-depth analysis of criticality metrics for safety evaluation of object detection systems. Through a comprehensive review of existing literature, we identify and assess a range of applicable metrics. Their effectiveness is empirically validated using the DeepAccident dataset, which features a variety of safety-critical scenarios. To enhance evaluation accuracy, we propose two novel application strategies: bidirectional criticality rating and multi-metric aggregation. Our approach demonstrates up to a 100% improvement in terms of criticality classification accuracy, highlighting its potential to significantly advance the safety evaluation of object detection systems in automated vehicles.

