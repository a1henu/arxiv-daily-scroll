---
layout: default
title: Building Reasonable Inference for Vision-Language Models in Blind Image Quality Assessment
---

# Building Reasonable Inference for Vision-Language Models in Blind Image Quality Assessment
**arXiv**：[2512.09555v1](https://arxiv.org/abs/2512.09555) · [PDF](https://arxiv.org/pdf/2512.09555.pdf)  
**作者**：Yuan Li, Zitang Sun, Yen-ju Chen, Shin'ya Nishida  

**一句话要点**：提出两阶段调优方法以解决盲图像质量评估中视觉语言模型的推理矛盾与不稳定性问题

**关键词**：盲图像质量评估, 视觉语言模型, 推理稳定性, 两阶段调优, 视觉特征学习

## 3 点简述
- 分析视觉语言模型在盲图像质量评估中产生矛盾预测和不稳定性的原因，如特征与预测逻辑连接弱
- 引入两阶段调优方法，先学习视觉特征，再基于特征推断质量，以模拟人类推理过程
- 实验表明方法在SPAQ和KONIQ上降低不稳定性至12.39%，并在多个数据集上提升SRCC/PLCC性能

## 摘要（原文）

> Recent progress in BIQA has been driven by VLMs, whose semantic reasoning abilities suggest that they might extract visual features, generate descriptive text, and infer quality in a human-like manner. However, these models often produce textual descriptions that contradict their final quality predictions, and the predicted scores can change unstably during inference - behaviors not aligned with human reasoning. To understand these issues, we analyze the factors that cause contradictory assessments and instability. We first estimate the relationship between the final quality predictions and the generated visual features, finding that the predictions are not fully grounded in the features and that the logical connection between them is weak. Moreover, decoding intermediate VLM layers shows that the model frequently relies on a limited set of candidate tokens, which contributes to prediction instability. To encourage more human-like reasoning, we introduce a two-stage tuning method that explicitly separates visual perception from quality inference. In the first stage, the model learns visual features; in the second, it infers quality solely from these features. Experiments on SPAQ and KONIQ demonstrate that our approach reduces prediction instability from 22.00% to 12.39% and achieves average gains of 0.3124/0.3507 in SRCC/PLCC across LIVE, CSIQ, SPAQ, and KONIQ compared to the baseline. Further analyses show that our method improves both stability and the reliability of the inference process.

