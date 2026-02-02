---
layout: default
title: Causal Characterization of Measurement and Mechanistic Anomalies
---

# Causal Characterization of Measurement and Mechanistic Anomalies
**arXiv**：[2601.23026v1](https://arxiv.org/abs/2601.23026) · [PDF](https://arxiv.org/pdf/2601.23026.pdf)  
**作者**：Hendrik Suhr, David Kaltenpoth, Jilles Vreeken  

**一句话要点**：提出因果模型以区分测量误差与机制偏移的异常根因分析

**关键词**：异常根因分析, 因果模型, 测量误差, 机制偏移, 最大似然估计, 潜在干预

## 3 点简述
- 核心问题：异常根因分析忽略测量误差与机制偏移的根本差异，影响处理策略
- 方法要点：定义包含潜在干预的因果模型，通过最大似然估计实现可识别性与分类
- 实验或效果：匹配根因定位性能，准确分类异常类型，在未知因果DAG时保持稳健

## 摘要（原文）

> Root cause analysis of anomalies aims to identify those features that cause the deviation from the normal process. Existing methods ignore, however, that anomalies can arise through two fundamentally different processes: measurement errors, where data was generated normally but one or more values were recorded incorrectly, and mechanism shifts, where the causal process generating the data changed. While measurement errors can often be safely corrected, mechanistic anomalies require careful consideration. We define a causal model that explicitly captures both types by treating outliers as latent interventions on latent ("true") and observed ("measured") variables. We show that they are identifiable, and propose a maximum likelihood estimation approach to put this to practice. Experiments show that our method matches state-of-the-art performance in root cause localization, while it additionally enables accurate classification of anomaly types, and remains robust even when the causal DAG is unknown.

