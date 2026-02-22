---
layout: default
title: Position: Evaluation of ECG Representations Must Be Fixed
---

# Position: Evaluation of ECG Representations Must Be Fixed
**arXiv**：[2602.17531v1](https://arxiv.org/abs/2602.17531) · [PDF](https://arxiv.org/pdf/2602.17531.pdf)  
**作者**：Zachary Berger, Daniel Prakah-Asante, John Guttag, Collin M. Stultz  

**一句话要点**：提出修正心电图表示评估方法，以提升临床相关性与基准可靠性

**关键词**：心电图表示学习, 多标签基准评估, 临床目标对齐, 随机编码器基线, 结构性心脏病预测, 患者级预测

## 3 点简述
- 核心问题：当前12导联心电图表示学习基准局限于心律失常标签，忽略更广泛临床信息如结构性心脏病
- 方法要点：建议扩展下游评估至结构性心脏病和患者预测，并应用多标签不平衡评估最佳实践
- 实验或效果：实证显示随机初始化编码器在线性评估中匹配先进预训练，改变现有性能结论

## 摘要（原文）

> This position paper argues that current benchmarking practice in 12-lead ECG representation learning must be fixed to ensure progress is reliable and aligned with clinically meaningful objectives. The field has largely converged on three public multi-label benchmarks (PTB-XL, CPSC2018, CSN) dominated by arrhythmia and waveform-morphology labels, even though the ECG is known to encode substantially broader clinical information. We argue that downstream evaluation should expand to include an assessment of structural heart disease and patient-level forecasting, in addition to other evolving ECG-related endpoints, as relevant clinical targets. Next, we outline evaluation best practices for multi-label, imbalanced settings, and show that when they are applied, the literature's current conclusion about which representations perform best is altered. Furthermore, we demonstrate the surprising result that a randomly initialized encoder with linear evaluation matches state-of-the-art pre-training on many tasks. This motivates the use of a random encoder as a reasonable baseline model. We substantiate our observations with an empirical evaluation of three representative ECG pre-training approaches across six evaluation settings: the three standard benchmarks, a structural disease dataset, hemodynamic inference, and patient forecasting.

