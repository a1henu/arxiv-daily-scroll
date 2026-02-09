---
layout: default
title: The Window Dilemma: Why Concept Drift Detection is Ill-Posed
---

# The Window Dilemma: Why Concept Drift Detection is Ill-Posed
**arXiv**：[2602.06456v1](https://arxiv.org/abs/2602.06456) · [PDF](https://arxiv.org/pdf/2602.06456.pdf)  
**作者**：Brandon Gower-Winter, Misja Groen, Georg Krempl  

**一句话要点**：提出窗口困境，指出概念漂移检测是病态问题，质疑检测器在流分类中的必要性。

**关键词**：概念漂移检测, 窗口困境, 流分类, 病态问题, 数据流分析

## 3 点简述
- 核心问题：概念漂移检测因窗口选择而呈现漂移，实际验证困难，导致问题病态。
- 方法要点：通过示例和实验比较，展示传统批处理技术常优于漂移感知方法。
- 实验或效果：实证分析表明，漂移检测器在流分类中可能不如简单适应策略有效。

## 摘要（原文）

> Non-stationarity of an underlying data generating process that leads to distributional changes over time is a key characteristic of Data Streams. This phenomenon, commonly referred to as Concept Drift, has been intensively studied, and Concept Drift Detectors have been established as a class of methods for detecting such changes (drifts). For the most part, Drift Detectors compare regions (windows) of the data stream and detect drift if those windows are sufficiently dissimilar.
>   In this work, we introduce the Window Dilemma, an observation that perceived drift is a product of windowing and not necessarily the underlying data generating process. Additionally, we highlight that drift detection is ill-posed, primarily because verification of drift events are implausible in practice. We demonstrate these contributions first by an illustrative example, followed by empirical comparisons of drift detectors against a variety of alternative adaptation strategies. Our main finding is that traditional batch learning techniques often perform better than their drift-aware counterparts further bringing into question the purpose of detectors in Stream Classification.

