---
layout: default
title: Human-Guided Agentic AI for Multimodal Clinical Prediction: Lessons from the AgentDS Healthcare Benchmark
---

# Human-Guided Agentic AI for Multimodal Clinical Prediction: Lessons from the AgentDS Healthcare Benchmark
**arXiv**：[2602.19502v1](https://arxiv.org/abs/2602.19502) · [PDF](https://arxiv.org/pdf/2602.19502.pdf)  
**作者**：Lalitha Pranathi Pulavarthy, Raajitha Muthyala, Aravind V Kuruvikkattil, Zhenan Yin, Rashmita Kudamala, Saptarshi Purkayastha  

**一句话要点**：提出人机协同的智能体AI方法，以提升医疗多模态临床预测的准确性与临床有效性。

**关键词**：智能体AI, 多模态临床预测, 人机协同, 特征工程, 医疗基准测试, 模型选择

## 3 点简述
- 核心问题：自动化AI在临床预测中缺乏领域专业知识，导致性能受限。
- 方法要点：人类专家在关键决策点指导智能体工作流，包括多模态特征工程、模型选择和验证策略。
- 实验或效果：在AgentDS医疗基准测试中排名第5，人机协同带来+0.065 F1的累积增益。

## 摘要（原文）

> Agentic AI systems are increasingly capable of autonomous data science workflows, yet clinical prediction tasks demand domain expertise that purely automated approaches struggle to provide. We investigate how human guidance of agentic AI can improve multimodal clinical prediction, presenting our approach to all three AgentDS Healthcare benchmark challenges: 30-day hospital readmission prediction (Macro-F1 = 0.8986), emergency department cost forecasting (MAE = $465.13), and discharge readiness assessment (Macro-F1 = 0.7939). Across these tasks, human analysts directed the agentic workflow at key decision points, multimodal feature engineering from clinical notes, scanned PDF billing receipts, and time-series vital signs; task-appropriate model selection; and clinically informed validation strategies. Our approach ranked 5th overall in the healthcare domain, with a 3rd-place finish on the discharge readiness task. Ablation studies reveal that human-guided decisions compounded to a cumulative gain of +0.065 F1 over automated baselines, with multimodal feature extraction contributing the largest single improvement (+0.041 F1). We distill three generalizable lessons: (1) domain-informed feature engineering at each pipeline stage yields compounding gains that outperform extensive automated search; (2) multimodal data integration requires task-specific human judgment that no single extraction strategy generalizes across clinical text, PDFs, and time-series; and (3) deliberate ensemble diversity with clinically motivated model configurations outperforms random hyperparameter search. These findings offer practical guidance for teams deploying agentic AI in healthcare settings where interpretability, reproducibility, and clinical validity are essential.

