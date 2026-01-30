---
layout: default
title: Questioning the Coverage-Length Metric in Conformal Prediction: When Shorter Intervals Are Not Better
---

# Questioning the Coverage-Length Metric in Conformal Prediction: When Shorter Intervals Are Not Better
**arXiv**：[2601.21455v1](https://arxiv.org/abs/2601.21455) · [PDF](https://arxiv.org/pdf/2601.21455.pdf)  
**作者**：Yizhou Min, Yizhou Lu, Lanqi Li, Zhen Zhang, Jiaye Teng  

**一句话要点**：质疑共形预测的覆盖长度指标，揭示通过偏见技巧可误导性缩短区间长度

**关键词**：共形预测, 不确定性量化, 覆盖长度指标, 偏见技巧, 区间稳定性

## 3 点简述
- 核心问题：标准覆盖长度指标可能不足，区间长度可通过偏见技巧误导性改进
- 方法要点：提出偏见技巧，概率性返回空或调整置信水平的区间，保持边际覆盖
- 实验或效果：理论推导偏见技巧条件，并在回归和分类任务中提供实证证据

## 摘要（原文）

> Conformal prediction (CP) has become a cornerstone of distribution-free uncertainty quantification, conventionally evaluated by its coverage and interval length. This work critically examines the sufficiency of these standard metrics. We demonstrate that the interval length might be deceptively improved through a counter-intuitive approach termed Prejudicial Trick (PT), while the coverage remains valid. Specifically, for any given test sample, PT probabilistically returns an interval, which is either null or constructed using an adjusted confidence level, thereby preserving marginal coverage. While PT potentially yields a deceptively lower interval length, it introduces practical vulnerabilities: the same input can yield completely different prediction intervals across repeated runs of the algorithm. We formally derive the conditions under which PT achieves these misleading improvements and provides extensive empirical evidence across various regression and classification tasks. Furthermore, we introduce a new metric interval stability which helps detect whether a new CP method implicitly improves the length based on such PT-like techniques.

