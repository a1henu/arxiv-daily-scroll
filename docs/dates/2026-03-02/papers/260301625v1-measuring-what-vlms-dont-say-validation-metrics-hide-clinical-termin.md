---
layout: default
title: Measuring What VLMs Don't Say: Validation Metrics Hide Clinical Terminology Erasure in Radiology Report Generation
---

# Measuring What VLMs Don't Say: Validation Metrics Hide Clinical Terminology Erasure in Radiology Report Generation
**arXiv**：[2603.01625v1](https://arxiv.org/abs/2603.01625) · [PDF](https://arxiv.org/pdf/2603.01625.pdf)  
**作者**：Aditya Parikh, Aasa Feragen, Sneha Das, Stella Frank  

**一句话要点**：提出词汇多样性指标与临床关联位移框架，以解决放射学报告生成中临床术语缺失的评估盲点。

**关键词**：放射学报告生成, 视觉语言模型评估, 临床术语缺失, 词汇多样性指标, 人口统计偏差, 解码策略分析

## 3 点简述
- 核心问题：当前评估指标因解码策略导致模板崩溃，模型生成通用文本而忽略临床术语，隐藏临床信号损失。
- 方法要点：引入词汇多样性检查临床特异性，并提出临床关联位移框架量化基于人口统计的词关联变化。
- 实验或效果：确定性解码导致高语义擦除，随机采样增加多样性但可能引入新偏见，需重新定义最优报告标准。

## 摘要（原文）

> Reliable deployment of Vision-Language Models (VLMs) in radiology requires validation metrics that go beyond surface-level text similarity to ensure clinical fidelity and demographic fairness. This paper investigates a critical blind spot in current model evaluation: the use of decoding strategies that lead to high aggregate token-overlap scores despite succumbing to template collapse, in which models generate only repetitive, safe generic text and omit clinical terminology. Unaddressed, this blind spot can lead to metric gaming, where models that perform well on benchmarks prove clinically uninformative. Instead, we advocate for lexical diversity measures to check model generations for clinical specificity. We introduce Clinical Association Displacement (CAD), a vocabulary-level framework that quantifies shifts in demographic-based word associations in generated reports. Weighted Association Erasure (WAE) aggregates these shifts to measure the clinical signal loss across demographic groups. We show that deterministic decoding produces high levels of semantic erasure, while stochastic sampling generates diverse outputs but risks introducing new bias, motivating a fundamental rethink of how "optimal" reporting is defined.

