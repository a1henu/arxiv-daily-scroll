---
layout: default
title: HateXScore: A Metric Suite for Evaluating Reasoning Quality in Hate Speech Explanations
---

# HateXScore: A Metric Suite for Evaluating Reasoning Quality in Hate Speech Explanations
**arXiv**：[2601.13547v1](https://arxiv.org/abs/2601.13547) · [PDF](https://arxiv.org/pdf/2601.13547.pdf)  
**作者**：Yujia Hu, Roy Ka-Wei Lee  

**一句话要点**：提出HateXScore以评估仇恨言论检测中模型解释的推理质量

**关键词**：仇恨言论检测, 模型解释评估, 推理质量度量, 内容审核, 可解释性分析

## 3 点简述
- 核心问题：现有仇恨言论检测评估框架缺乏对模型解释推理质量的系统评估。
- 方法要点：设计四组件度量套件，评估结论明确性、引用忠实性、受保护群体识别和逻辑一致性。
- 实验或效果：在六个数据集上验证，与人类评估高度一致，揭示标准指标未覆盖的失败。

## 摘要（原文）

> Hateful speech detection is a key component of content moderation, yet current evaluation frameworks rarely assess why a text is deemed hateful. We introduce \textsf{HateXScore}, a four-component metric suite designed to evaluate the reasoning quality of model explanations. It assesses (i) conclusion explicitness, (ii) faithfulness and causal grounding of quoted spans, (iii) protected group identification (policy-configurable), and (iv) logical consistency among these elements. Evaluated on six diverse hate speech datasets, \textsf{HateXScore} is intended as a diagnostic complement to reveal interpretability failures and annotation inconsistencies that are invisible to standard metrics like Accuracy or F1. Moreover, human evaluation shows strong agreement with \textsf{HateXScore}, validating it as a practical tool for trustworthy and transparent moderation.
>   \textcolor{red}{Disclaimer: This paper contains sensitive content that may be disturbing to some readers.}

