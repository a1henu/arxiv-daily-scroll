---
layout: default
title: Scalable Delphi: Large Language Models for Structured Risk Estimation
---

# Scalable Delphi: Large Language Models for Structured Risk Estimation
**arXiv**：[2602.08889v1](https://arxiv.org/abs/2602.08889) · [PDF](https://arxiv.org/pdf/2602.08889.pdf)  
**作者**：Tobias Lorenz, Mario Fritz  

**一句话要点**：提出Scalable Delphi方法，利用大语言模型作为结构化专家评估的可扩展代理，以解决高风险领域量化风险评估耗时过长的问题。

**关键词**：结构化专家评估, 大语言模型, 风险评估, 可扩展代理, 网络安全, 校准评估

## 3 点简述
- 核心问题：传统Delphi方法进行结构化专家评估需数月协调，难以广泛应用。
- 方法要点：基于大语言模型设计Scalable Delphi，引入专家角色、迭代优化和理由共享。
- 实验或效果：在AI增强网络安全风险领域评估，LLM面板与基准真相强相关，时间从数月缩短至分钟。

## 摘要（原文）

> Quantitative risk assessment in high-stakes domains relies on structured expert elicitation to estimate unobservable properties. The gold standard - the Delphi method - produces calibrated, auditable judgments but requires months of coordination and specialist time, placing rigorous risk assessment out of reach for most applications. We investigate whether Large Language Models (LLMs) can serve as scalable proxies for structured expert elicitation. We propose Scalable Delphi, adapting the classical protocol for LLMs with diverse expert personas, iterative refinement, and rationale sharing. Because target quantities are typically unobservable, we develop an evaluation framework based on necessary conditions: calibration against verifiable proxies, sensitivity to evidence, and alignment with human expert judgment. We evaluate in the domain of AI-augmented cybersecurity risk, using three capability benchmarks and independent human elicitation studies. LLM panels achieve strong correlations with benchmark ground truth (Pearson r=0.87-0.95), improve systematically as evidence is added, and align with human expert panels - in one comparison, closer to a human panel than the two human panels are to each other. This demonstrates that LLM-based elicitation can extend structured expert judgment to settings where traditional methods are infeasible, reducing elicitation time from months to minutes.

