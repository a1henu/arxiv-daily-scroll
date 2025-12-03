---
layout: default
title: Flexible Gravitational-Wave Parameter Estimation with Transformers
---

# Flexible Gravitational-Wave Parameter Estimation with Transformers
**arXiv**：[2512.02968v1](https://arxiv.org/abs/2512.02968) · [PDF](https://arxiv.org/pdf/2512.02968.pdf)  
**作者**：Annalena Kofler, Maximilian Dax, Stephen R. Green, Jonas Wildberger, Nihar Gupte, Jakob H. Macke, Jonathan Gair, Alessandra Buonanno, Bernhard Schölkopf  

**一句话要点**：提出基于Transformer的灵活架构以解决引力波参数估计中数据分析设置多变的问题。

**关键词**：引力波参数估计, Transformer架构, 灵活推理, 深度学习, 数据分析设置, 样本效率提升

## 3 点简述
- 核心问题：引力波数据分析需处理噪声信号，但观测率增加和复杂性提升带来挑战，现有深度学习方法缺乏灵活性以适应不同分析设置。
- 方法要点：引入基于Transformer的灵活架构和训练策略，使模型能在推理时适应多种分析配置，如探测器设置或频率范围变化。
- 实验或效果：Dingo-T1模型分析48个引力波事件，支持系统研究探测器影响，进行广义相对论测试，并将样本效率中位数从1.4%提升至4.2%。

## 摘要（原文）

> Gravitational-wave data analysis relies on accurate and efficient methods to extract physical information from noisy detector signals, yet the increasing rate and complexity of observations represent a growing challenge. Deep learning provides a powerful alternative to traditional inference, but existing neural models typically lack the flexibility to handle variations in data analysis settings. Such variations accommodate imperfect observations or are required for specialized tests, and could include changes in detector configurations, overall frequency ranges, or localized cuts. We introduce a flexible transformer-based architecture paired with a training strategy that enables adaptation to diverse analysis settings at inference time. Applied to parameter estimation, we demonstrate that a single flexible model -- called Dingo-T1 -- can (i) analyze 48 gravitational-wave events from the third LIGO-Virgo-KAGRA Observing Run under a wide range of analysis configurations, (ii) enable systematic studies of how detector and frequency configurations impact inferred posteriors, and (iii) perform inspiral-merger-ringdown consistency tests probing general relativity. Dingo-T1 also improves median sample efficiency on real events from a baseline of 1.4% to 4.2%. Our approach thus demonstrates flexible and scalable inference with a principled framework for handling missing or incomplete data -- key capabilities for current and next-generation observatories.

