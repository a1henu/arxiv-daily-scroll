---
layout: default
title: LFQA-HP-1M: A Large-Scale Human Preference Dataset for Long-Form Question Answering
---

# LFQA-HP-1M: A Large-Scale Human Preference Dataset for Long-Form Question Answering
**arXiv**：[2602.23603v1](https://arxiv.org/abs/2602.23603) · [PDF](https://arxiv.org/pdf/2602.23603.pdf)  
**作者**：Rafid Ishrak Jahan, Fahmid Shahriar Iqbal, Sagnik Ray Choudhury  

**一句话要点**：提出LFQA-HP-1M大规模数据集和基于规则的评估框架，以解决长问答中人类偏好评估的不足。

**关键词**：长问答评估, 人类偏好数据集, 规则驱动框架, LLM评估器偏差, 对抗性扰动

## 3 点简述
- 核心问题：长问答评估中现有指标常无法反映人类判断，缺乏大规模偏好数据。
- 方法要点：构建包含130万人类成对偏好标注的数据集，并设计九个答案质量评估规则。
- 实验或效果：基于规则的线性模型性能媲美先进LLM评估器，并揭示了LLM评估器的偏差和脆弱性。

## 摘要（原文）

> Long-form question answering (LFQA) demands nuanced evaluation of multi-sentence explanatory responses, yet existing metrics often fail to reflect human judgment. We present LFQA-HP-1M, a large-scale dataset comprising 1.3M human pairwise preference annotations for LFQA. We propose nine rubrics for answer quality evaluation, and show that simple linear models based on these features perform comparably to state-of-the-art LLM evaluators. We further examine transitivity consistency, positional bias, and verbosity biases in LLM evaluators and demonstrate their vulnerability to adversarial perturbations. Overall, this work provides one of the largest public LFQA preference datasets and a rubric-driven framework for transparent and reliable evaluation.

