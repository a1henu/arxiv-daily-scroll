---
layout: default
title: Do LLMs Really Memorize Personally Identifiable Information? Revisiting PII Leakage with a Cue-Controlled Memorization Framework
---

# Do LLMs Really Memorize Personally Identifiable Information? Revisiting PII Leakage with a Cue-Controlled Memorization Framework
**arXiv**：[2601.03791v1](https://arxiv.org/abs/2601.03791) · [PDF](https://arxiv.org/pdf/2601.03791.pdf)  
**作者**：Xiaoyu Luo, Yiyi Chen, Qiongxiu Li, Johannes Bjerva  

**一句话要点**：提出线索控制记忆框架以重新评估大语言模型中的个人身份信息泄露问题

**关键词**：个人身份信息泄露, 线索控制记忆, 大语言模型评估, 隐私量化, 多语言分析

## 3 点简述
- 核心问题：现有PII泄露评估可能高估记忆，因未控制提示中的表面线索。
- 方法要点：定义线索抵抗记忆作为评估框架，强调低词汇线索条件下的必要条件。
- 实验或效果：多语言实验显示，控制线索后重建成功率大幅下降，泄露主要由线索驱动。

## 摘要（原文）

> Large Language Models (LLMs) have been reported to "leak" Personally Identifiable Information (PII), with successful PII reconstruction often interpreted as evidence of memorization. We propose a principled revision of memorization evaluation for LLMs, arguing that PII leakage should be evaluated under low lexical cue conditions, where target PII cannot be reconstructed through prompt-induced generalization or pattern completion. We formalize Cue-Resistant Memorization (CRM) as a cue-controlled evaluation framework and a necessary condition for valid memorization evaluation, explicitly conditioning on prompt-target overlap cues. Using CRM, we conduct a large-scale multilingual re-evaluation of PII leakage across 32 languages and multiple memorization paradigms. Revisiting reconstruction-based settings, including verbatim prefix-suffix completion and associative reconstruction, we find that their apparent effectiveness is driven primarily by direct surface-form cues rather than by true memorization. When such cues are controlled for, reconstruction success diminishes substantially. We further examine cue-free generation and membership inference, both of which exhibit extremely low true positive rates. Overall, our results suggest that previously reported PII leakage is better explained by cue-driven behavior than by genuine memorization, highlighting the importance of cue-controlled evaluation for reliably quantifying privacy-relevant memorization in LLMs.

