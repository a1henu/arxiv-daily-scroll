---
layout: default
title: CRIMSON: A Clinically-Grounded LLM-Based Metric for Generative Radiology Report Evaluation
---

# CRIMSON: A Clinically-Grounded LLM-Based Metric for Generative Radiology Report Evaluation
**arXiv**：[2603.06183v1](https://arxiv.org/abs/2603.06183) · [PDF](https://arxiv.org/pdf/2603.06183.pdf)  
**作者**：Mohammed Baharoon, Thibault Heintz, Siavash Raissi, Mahmoud Alabbad, Mona Alhammad, Hassan AlOmaish, Sung Eun Kim, Oishi Banerjee, Pranav Rajpurkar  

**一句话要点**：提出CRIMSON框架，基于临床背景评估胸部X光报告生成，强调诊断正确性和患者安全。

**关键词**：胸部X光报告生成, 临床评估指标, 错误分类, 严重性加权, 放射学基准

## 3 点简述
- 核心问题：现有评估指标缺乏临床上下文，可能过度关注非重要发现，忽略诊断错误。
- 方法要点：结合患者年龄、指征和指南，分类错误并加权临床重要性，优先处理紧急或可操作错误。
- 实验或效果：在ReXVal、RadJudge和RadPref基准上验证，与放射科医生判断和偏好高度一致。

## 摘要（原文）

> We introduce CRIMSON, a clinically grounded evaluation framework for chest X-ray report generation that assesses reports based on diagnostic correctness, contextual relevance, and patient safety. Unlike prior metrics, CRIMSON incorporates full clinical context, including patient age, indication, and guideline-based decision rules, and prevents normal or clinically insignificant findings from exerting disproportionate influence on the overall score. The framework categorizes errors into a comprehensive taxonomy covering false findings, missing findings, and eight attribute-level errors (e.g., location, severity, measurement, and diagnostic overinterpretation). Each finding is assigned a clinical significance level (urgent, actionable non-urgent, non-actionable, or expected/benign), based on a guideline developed in collaboration with attending cardiothoracic radiologists, enabling severity-aware weighting that prioritizes clinically consequential mistakes over benign discrepancies. CRIMSON is validated through strong alignment with clinically significant error counts annotated by six board-certified radiologists in ReXVal (Kendalls tau = 0.61-0.71; Pearsons r = 0.71-0.84), and through two additional benchmarks that we introduce. In RadJudge, a targeted suite of clinically challenging pass-fail scenarios, CRIMSON shows consistent agreement with expert judgment. In RadPref, a larger radiologist preference benchmark of over 100 pairwise cases with structured error categorization, severity modeling, and 1-5 overall quality ratings from three cardiothoracic radiologists, CRIMSON achieves the strongest alignment with radiologist preferences. We release the metric, the evaluation benchmarks, RadJudge and RadPref, and a fine-tuned MedGemma model to enable reproducible evaluation of report generation, all available at https://github.com/rajpurkarlab/CRIMSON.

