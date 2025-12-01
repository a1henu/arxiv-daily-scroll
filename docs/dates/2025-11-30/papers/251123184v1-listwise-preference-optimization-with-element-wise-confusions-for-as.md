---
layout: default
title: Listwise Preference Optimization with Element-wise Confusions for Aspect Sentiment Quad Prediction
---

# Listwise Preference Optimization with Element-wise Confusions for Aspect Sentiment Quad Prediction
**arXiv**：[2511.23184v1](https://arxiv.org/abs/2511.23184) · [PDF](https://arxiv.org/pdf/2511.23184.pdf)  
**作者**：Wenna Lai, Haoran Xie, Guandong Xu, Qing Li, S. Joe Qin  

**一句话要点**：提出基于列表偏好优化与元素混淆的框架，以提升方面情感四元组预测的结构有效性和关系一致性。

**关键词**：方面情感四元组预测, 列表偏好优化, 元素混淆, 推理生成, 自然语言处理, 情感分析

## 3 点简述
- 核心问题：方面情感四元组预测中，基于标记的方法难以建模元素间复杂关系，高阶元素预测性能下降。
- 方法要点：采用基于推理的生成输出四元组和自然语言理由，引入列表偏好优化框架，通过元素混淆候选提升对齐。
- 实验或效果：在四个基准数据集上验证，有效提高四元组预测准确性和解释一致性。

## 摘要（原文）

> Aspect sentiment quad prediction (ASQP) is inherently challenging to predict a structured quadruple with four core sentiment elements, including aspect term (a), aspect category (c), opinion term (o), and sentiment polarity (s). Prior methods relying on marker-based prediction struggle with modeling the intricate relationships among elements and experience sharp performance declines when predicting higher-order elements (e.g., c and s) under standard supervised fine-tuning. To address these limitations, we employ reasoning-based generation to output both the quadruple and a natural language rationale under element prefixes within a unified template, encouraging explicit relational reasoning and interpretability. To further enhance element-wise alignment, we introduce a listwise preference optimization framework for improving structural validity and relational coherence. Specifically, we generate element-wise confusable candidates via syntactic and semantic proximity, then train the model with listwise objectives to prefer the gold candidates over closely competing alternatives. Extensive experiments on four benchmark datasets demonstrate that our framework effectively improves quadruple prediction accuracy and explanation consistency.

