---
layout: default
title: Value Alignment Tax: Measuring Value Trade-offs in LLM Alignment
---

# Value Alignment Tax: Measuring Value Trade-offs in LLM Alignment
**arXiv**：[2602.12134v1](https://arxiv.org/abs/2602.12134) · [PDF](https://arxiv.org/pdf/2602.12134.pdf)  
**作者**：Jiajun Chen, Hua Shen  

**一句话要点**：提出价值对齐税框架以衡量大语言模型对齐中的价值权衡动态

**关键词**：价值对齐, 大语言模型, 价值权衡, 对齐税, 施瓦茨价值理论, 系统性风险

## 3 点简述
- 核心问题：现有价值对齐研究静态描述价值关系，忽略干预措施如何重塑整体价值系统
- 方法要点：引入价值对齐税框架，量化对齐诱导变化在互连价值间的传播与目标增益对比
- 实验或效果：基于施瓦茨价值理论数据集分析，揭示对齐常导致价值间结构化共变，暴露系统性风险

## 摘要（原文）

> Existing work on value alignment typically characterizes value relations statically, ignoring how interventions - such as prompting, fine-tuning, or preference optimization - reshape the broader value system. We introduce the Value Alignment Tax (VAT), a framework that measures how alignment-induced changes propagate across interconnected values relative to achieved on-target gain. VAT captures the dynamics of value expression under alignment pressure. Using a controlled scenario-action dataset grounded in Schwartz value theory, we collect paired pre-post normative judgments and analyze alignment effects across models, values, and alignment strategies. Our results show that alignment often produces uneven, structured co-movement among values. These effects are invisible under conventional target-only evaluation, revealing systemic, process-level alignment risks and offering new insights into the dynamics of value alignment in LLMs.

