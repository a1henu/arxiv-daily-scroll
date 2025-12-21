---
layout: default
title: TimeSeries2Report prompting enables adaptive large language model management of lithium-ion batteries
---

# TimeSeries2Report prompting enables adaptive large language model management of lithium-ion batteries
**arXiv**：[2512.16453v1](https://arxiv.org/abs/2512.16453) · [PDF](https://arxiv.org/pdf/2512.16453.pdf)  
**作者**：Jiayang Yang, Chunhui Zhao, Martin Guay, Zhixing Cao  

**一句话要点**：提出TimeSeries2Report提示框架，将锂离子电池时间序列转换为结构化报告，以增强大语言模型在电池储能系统管理中的自适应能力。

**关键词**：时间序列分析, 大语言模型提示, 电池储能系统管理, 自适应决策, 异常检测, 状态预测

## 3 点简述
- 核心问题：大语言模型在电池储能系统运维中应用不足，难以直接处理原始时间序列数据。
- 方法要点：通过分割、语义抽象和规则解释，将短期动态编码为自然语言报告，连接低层信号与高层洞察。
- 实验或效果：在实验室和真实数据集上评估，报告提示优于基线，提升准确性、鲁棒性和可解释性，实现专家级决策。

## 摘要（原文）

> Large language models (LLMs) offer promising capabilities for interpreting multivariate time-series data, yet their application to real-world battery energy storage system (BESS) operation and maintenance remains largely unexplored. Here, we present TimeSeries2Report (TS2R), a prompting framework that converts raw lithium-ion battery operational time-series into structured, semantically enriched reports, enabling LLMs to reason, predict, and make decisions in BESS management scenarios. TS2R encodes short-term temporal dynamics into natural language through a combination of segmentation, semantic abstraction, and rule-based interpretation, effectively bridging low-level sensor signals with high-level contextual insights. We benchmark TS2R across both lab-scale and real-world datasets, evaluating report quality and downstream task performance in anomaly detection, state-of-charge prediction, and charging/discharging management. Compared with vision-, embedding-, and text-based prompting baselines, report-based prompting via TS2R consistently improves LLM performance in terms of across accuracy, robustness, and explainability metrics. Notably, TS2R-integrated LLMs achieve expert-level decision quality and predictive consistency without retraining or architecture modification, establishing a practical path for adaptive, LLM-driven battery intelligence.

