---
layout: default
title: Correcting Human Labels for Rater Effects in AI Evaluation: An Item Response Theory Approach
---

# Correcting Human Labels for Rater Effects in AI Evaluation: An Item Response Theory Approach
**arXiv**：[2602.22585v1](https://arxiv.org/abs/2602.22585) · [PDF](https://arxiv.org/pdf/2602.22585.pdf)  
**作者**：Jodi M. Casabianca, Maggie Beiting-Parrish  

**一句话要点**：提出基于项目反应理论的评分者模型，以校正AI评估中人类标签的系统误差。

**关键词**：AI评估, 评分者效应, 项目反应理论, 多面Rasch模型, 心理测量学, 人类标签校正

## 3 点简述
- 核心问题：人类评估数据存在评分者效应（如严格性和中心性），导致AI模型训练和评估结论不可靠。
- 方法要点：整合心理测量学评分者模型，特别是多面Rasch模型，分离真实输出质量与评分者行为。
- 实验或效果：在OpenAI摘要数据集上应用，校正评分者严格性后获得更准确的摘要质量估计，并提供评分者性能诊断。

## 摘要（原文）

> Human evaluations play a central role in training and assessing AI models, yet these data are rarely treated as measurements subject to systematic error. This paper integrates psychometric rater models into the AI pipeline to improve the reliability and validity of conclusions drawn from human judgments. The paper reviews common rater effects, severity and centrality, that distort observed ratings, and demonstrates how item response theory rater models, particularly the multi-faceted Rasch model, can separate true output quality from rater behavior. Using the OpenAI summarization dataset as an empirical example, we show how adjusting for rater severity produces corrected estimates of summary quality and provides diagnostic insight into rater performance. Incorporating psychometric modeling into human-in-the-loop evaluation offers more principled and transparent use of human data, enabling developers to make decisions based on adjusted scores rather than raw, error-prone ratings. This perspective highlights a path toward more robust, interpretable, and construct-aligned practices for AI development and evaluation.

