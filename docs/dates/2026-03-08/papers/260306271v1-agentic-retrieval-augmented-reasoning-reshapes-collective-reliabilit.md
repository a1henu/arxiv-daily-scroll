---
layout: default
title: Agentic retrieval-augmented reasoning reshapes collective reliability under model variability in radiology question answering
---

# Agentic retrieval-augmented reasoning reshapes collective reliability under model variability in radiology question answering
**arXiv**：[2603.06271v1](https://arxiv.org/abs/2603.06271) · [PDF](https://arxiv.org/pdf/2603.06271.pdf)  
**作者**：Mina Farajiamiri, Jeta Sopa, Saba Afza, Lisa Adams, Felix Barajas Ordonez, Tri-Thien Nguyen, Mahshad Lotfinia, Sebastian Wind, Keno Bressem, Sven Nebelung, Daniel Truhn, Soroosh Tayebi Arasteh  

**一句话要点**：提出代理检索增强推理以提升放射学问答中模型变异性下的集体可靠性

**关键词**：代理检索增强推理, 模型变异性, 放射学问答, 集体可靠性, 临床决策支持, 大语言模型

## 3 点简述
- 研究代理检索增强推理在临床决策支持中如何影响模型变异性下的可靠性，而非仅关注准确性
- 通过多步骤代理检索条件，使用34个LLM在169个放射学问题上比较零样本推理，生成结构化证据报告
- 代理推理减少模型间决策分散，增强跨模型正确性稳健性，但高一致性不保证正确性，需补充稳定性分析

## 摘要（原文）

> Agentic retrieval-augmented reasoning pipelines are increasingly used to structure how large language models (LLMs) incorporate external evidence in clinical decision support. These systems iteratively retrieve curated domain knowledge and synthesize it into structured reports before answer selection. Although such pipelines can improve performance, their impact on reliability under model variability remains unclear. In real-world deployment, heterogeneous models may align, diverge, or synchronize errors in ways not captured by accuracy. We evaluated 34 LLMs on 169 expert-curated publicly available radiology questions, comparing zero-shot inference with a radiology-specific multi-step agentic retrieval condition in which all models received identical structured evidence reports derived from curated radiology knowledge. Agentic inference reduced inter-model decision dispersion (median entropy 0.48 vs. 0.13) and increased robustness of correctness across models (mean 0.74 vs. 0.81). Majority consensus also increased overall (P<0.001). Consensus strength and robust correctness remained correlated under both strategies (\r{ho}=0.88 for zero-shot; \r{ho}=0.87 for agentic), although high agreement did not guarantee correctness. Response verbosity showed no meaningful association with correctness. Among 572 incorrect outputs, 72% were associated with moderate or high clinically assessed severity, although inter-rater agreement was low (\k{appa}=0.02). Agentic retrieval therefore was associated with more concentrated decision distributions, stronger consensus, and higher cross-model robustness of correctness. These findings suggest that evaluating agentic systems through accuracy or agreement alone may not always be sufficient, and that complementary analyses of stability, cross-model robustness, and potential clinical impact are needed to characterize reliability under model variability.

