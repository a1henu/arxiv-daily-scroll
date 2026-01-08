---
layout: default
title: Evaluating the Pre-Consultation Ability of LLMs using Diagnostic Guidelines
---

# Evaluating the Pre-Consultation Ability of LLMs using Diagnostic Guidelines
**arXiv**：[2601.03627v1](https://arxiv.org/abs/2601.03627) · [PDF](https://arxiv.org/pdf/2601.03627.pdf)  
**作者**：Jean Seo, Gibaeg Kim, Kihun Shin, Seungseop Lim, Hyunkyung Lee, Wooseok Han, Jongwon Lee, Eunho Yang  

**一句话要点**：提出EPAG基准以评估LLMs在临床预咨询中的能力

**关键词**：LLM评估, 临床预咨询, 诊断指南, HPI分析, 开源数据集

## 3 点简述
- 核心问题：评估LLMs在临床预咨询中的能力，基于诊断指南
- 方法要点：通过HPI-指南比较和疾病诊断间接评估LLMs
- 实验或效果：发现小模型在特定数据集微调后可超越前沿LLMs

## 摘要（原文）

> We introduce EPAG, a benchmark dataset and framework designed for Evaluating the Pre-consultation Ability of LLMs using diagnostic Guidelines. LLMs are evaluated directly through HPI-diagnostic guideline comparison and indirectly through disease diagnosis. In our experiments, we observe that small open-source models fine-tuned with a well-curated, task-specific dataset can outperform frontier LLMs in pre-consultation. Additionally, we find that increased amount of HPI (History of Present Illness) does not necessarily lead to improved diagnostic performance. Further experiments reveal that the language of pre-consultation influences the characteristics of the dialogue. By open-sourcing our dataset and evaluation pipeline on https://github.com/seemdog/EPAG, we aim to contribute to the evaluation and further development of LLM applications in real-world clinical settings.

