---
layout: default
title: How Implicit Bias Accumulates and Propagates in LLM Long-term Memory
---

# How Implicit Bias Accumulates and Propagates in LLM Long-term Memory
**arXiv**：[2602.01558v1](https://arxiv.org/abs/2602.01558) · [PDF](https://arxiv.org/pdf/2602.01558.pdf)  
**作者**：Yiming Ma, Lixu Wang, Lionel Z. Wang, Hongkun Yang, Haoming Sun, Xin Xu, Jiaqi Wu, Bin Chen, Wei Dong  

**一句话要点**：提出动态记忆标记以缓解大语言模型长期记忆中的隐式偏见累积与传播

**关键词**：大语言模型, 长期记忆, 隐式偏见, 公平性评估, 动态干预, 决策基准

## 3 点简述
- 研究大语言模型长期记忆机制中隐式偏见的动态累积与跨域传播风险
- 引入决策隐式偏见基准与长时模拟框架，评估六种模型在九大社会领域的偏见表现
- 提出动态记忆标记方法，在记忆写入时施加公平约束，有效减少偏见积累与传播

## 摘要（原文）

> Long-term memory mechanisms enable Large Language Models (LLMs) to maintain continuity and personalization across extended interaction lifecycles, but they also introduce new and underexplored risks related to fairness. In this work, we study how implicit bias, defined as subtle statistical prejudice, accumulates and propagates within LLMs equipped with long-term memory. To support systematic analysis, we introduce the Decision-based Implicit Bias (DIB) Benchmark, a large-scale dataset comprising 3,776 decision-making scenarios across nine social domains, designed to quantify implicit bias in long-term decision processes. Using a realistic long-horizon simulation framework, we evaluate six state-of-the-art LLMs integrated with three representative memory architectures on DIB and demonstrate that LLMs' implicit bias does not remain static but intensifies over time and propagates across unrelated domains. We further analyze mitigation strategies and show that a static system-level prompting baseline provides limited and short-lived debiasing effects. To address this limitation, we propose Dynamic Memory Tagging (DMT), an agentic intervention that enforces fairness constraints at memory write time. Extensive experimental results show that DMT substantially reduces bias accumulation and effectively curtails cross-domain bias propagation.

