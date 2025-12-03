---
layout: default
title: AuditCopilot: Leveraging LLMs for Fraud Detection in Double-Entry Bookkeeping
---

# AuditCopilot: Leveraging LLMs for Fraud Detection in Double-Entry Bookkeeping
**arXiv**：[2512.02726v1](https://arxiv.org/abs/2512.02726) · [PDF](https://arxiv.org/pdf/2512.02726.pdf)  
**作者**：Md Abdul Kadir, Sai Suresh Macharla Vasu, Sidharth S. Nair, Daniel Sonntag  

**一句话要点**：提出AuditCopilot，利用大语言模型检测复式记账中的欺诈，以提升审计效率和可解释性。

**关键词**：大语言模型, 欺诈检测, 复式记账, 审计增强, 异常检测, 可解释性

## 3 点简述
- 核心问题：传统基于规则的日记账测试在税务相关账本异常检测中产生大量误报，难以处理细微异常。
- 方法要点：研究大语言模型作为异常检测器，在合成和真实匿名账本上基准测试LLaMA和Gemma等模型。
- 实验或效果：大语言模型在性能上优于传统规则方法和机器学习基线，并提供自然语言解释增强可解释性。

## 摘要（原文）

> Auditors rely on Journal Entry Tests (JETs) to detect anomalies in tax-related ledger records, but rule-based methods generate overwhelming false positives and struggle with subtle irregularities. We investigate whether large language models (LLMs) can serve as anomaly detectors in double-entry bookkeeping. Benchmarking SoTA LLMs such as LLaMA and Gemma on both synthetic and real-world anonymized ledgers, we compare them against JETs and machine learning baselines. Our results show that LLMs consistently outperform traditional rule-based JETs and classical ML baselines, while also providing natural-language explanations that enhance interpretability. These results highlight the potential of \textbf{AI-augmented auditing}, where human auditors collaborate with foundation models to strengthen financial integrity.

