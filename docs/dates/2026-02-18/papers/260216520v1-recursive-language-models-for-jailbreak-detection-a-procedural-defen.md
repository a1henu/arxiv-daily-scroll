---
layout: default
title: Recursive language models for jailbreak detection: a procedural defense for tool-augmented agents
---

# Recursive language models for jailbreak detection: a procedural defense for tool-augmented agents
**arXiv**：[2602.16520v1](https://arxiv.org/abs/2602.16520) · [PDF](https://arxiv.org/pdf/2602.16520.pdf)  
**作者**：Doron Shavit  

**一句话要点**：提出基于递归语言模型的越狱检测框架，以防御工具增强代理中的越狱提示攻击。

**关键词**：越狱检测, 递归语言模型, 工具增强代理, 对抗性输入, 程序化防御

## 3 点简述
- 核心问题：越狱提示通过长上下文隐藏、语义伪装和轻量混淆，威胁大型语言模型在代理系统中的安全性。
- 方法要点：采用递归语言模型，通过根模型协调输入转换、分段查询和证据聚合，实现程序化检测而非单次分类。
- 实验或效果：在AutoDAN风格对抗输入上，检测召回率达92.5-98.0%，精确度98.99-100%，假阳性率0.0-2.0%。

## 摘要（原文）

> Jailbreak prompts are a practical and evolving threat to large language models (LLMs), particularly in agentic systems that execute tools over untrusted content. Many attacks exploit long-context hiding, semantic camouflage, and lightweight obfuscations that can evade single-pass guardrails. We present RLM-JB, an end-to-end jailbreak detection framework built on Recursive Language Models (RLMs), in which a root model orchestrates a bounded analysis program that transforms the input, queries worker models over covered segments, and aggregates evidence into an auditable decision. RLM-JB treats detection as a procedure rather than a one-shot classification: it normalizes and de-obfuscates suspicious inputs, chunks text to reduce context dilution and guarantee coverage, performs parallel chunk screening, and composes cross-chunk signals to recover split-payload attacks. On AutoDAN-style adversarial inputs, RLM-JB achieves high detection effectiveness across three LLM backends (ASR/Recall 92.5-98.0%) while maintaining very high precision (98.99-100%) and low false positive rates (0.0-2.0%), highlighting a practical sensitivity-specificity trade-off as the screening backend changes.

