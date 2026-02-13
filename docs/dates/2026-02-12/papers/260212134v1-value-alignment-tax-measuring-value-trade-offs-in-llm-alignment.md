---
layout: default
title: Value Alignment Tax: Measuring Value Trade-offs in LLM Alignment
---

# Value Alignment Tax: Measuring Value Trade-offs in LLM Alignment
**arXiv**：[2602.12134v1](https://arxiv.org/abs/2602.12134) · [PDF](https://arxiv.org/pdf/2602.12134.pdf)  
**作者**：Jiajun Chen, Hua Shen  

**一句话要点**：提出价值对齐税框架，测量大语言模型对齐中价值权衡的动态效应

**关键词**：价值对齐, 大语言模型, 价值权衡, 对齐评估, 施瓦茨价值理论, 动态效应

## 3 点简述
- 现有研究静态描述价值关系，忽略干预措施如何重塑整体价值系统
- 引入价值对齐税框架，量化对齐变化在互连价值间的传播与目标增益比
- 基于施瓦茨价值理论构建数据集，分析模型、价值和策略的对齐效应

## 摘要（原文）

> Existing work on value alignment typically characterizes value relations statically, ignoring how interventions - such as prompting, fine-tuning, or preference optimization - reshape the broader value system. We introduce the Value Alignment Tax (VAT), a framework that measures how alignment-induced changes propagate across interconnected values relative to achieved on-target gain. VAT captures the dynamics of value expression under alignment pressure. Using a controlled scenario-action dataset grounded in Schwartz value theory, we collect paired pre-post normative judgments and analyze alignment effects across models, values, and alignment strategies. Our results show that alignment often produces uneven, structured co-movement among values. These effects are invisible under conventional target-only evaluation, revealing systemic, process-level alignment risks and offering new insights into the dynamics of value alignment in LLMs.

