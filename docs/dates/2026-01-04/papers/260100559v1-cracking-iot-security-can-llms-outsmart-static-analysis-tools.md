---
layout: default
title: Cracking IoT Security: Can LLMs Outsmart Static Analysis Tools?
---

# Cracking IoT Security: Can LLMs Outsmart Static Analysis Tools?
**arXiv**：[2601.00559v1](https://arxiv.org/abs/2601.00559) · [PDF](https://arxiv.org/pdf/2601.00559.pdf)  
**作者**：Jason Quantrill, Noura Khajehnouri, Zihan Guo, Manar H. Alalfi  

**一句话要点**：评估LLMs在IoT规则交互威胁检测中的性能，对比符号分析基线。

**关键词**：物联网安全, 大语言模型评估, 规则交互威胁, 静态分析, 符号推理, 混合架构

## 3 点简述
- 核心问题：IoT平台规则交互威胁检测需语义理解和结构推理，传统依赖符号静态分析。
- 方法要点：首次全面评估LLMs在多类别威胁分类上的表现，使用原始和突变数据集。
- 实验或效果：LLMs在语义理解上表现良好，但结构推理准确性下降，符号基线更稳定。

## 摘要（原文）

> Smart home IoT platforms such as openHAB rely on Trigger Action Condition (TAC) rules to automate device behavior, but the interplay among these rules can give rise to interaction threats, unintended or unsafe behaviors emerging from implicit dependencies, conflicting triggers, or overlapping conditions. Identifying these threats requires semantic understanding and structural reasoning that traditionally depend on symbolic, constraint-driven static analysis. This work presents the first comprehensive evaluation of Large Language Models (LLMs) across a multi-category interaction threat taxonomy, assessing their performance on both the original openHAB (oHC/IoTB) dataset and a structurally challenging Mutation dataset designed to test robustness under rule transformations. We benchmark Llama 3.1 8B, Llama 70B, GPT-4o, Gemini-2.5-Pro, and DeepSeek-R1 across zero-, one-, and two-shot settings, comparing their results against oHIT's manually validated ground truth. Our findings show that while LLMs exhibit promising semantic understanding, particularly on action- and condition-related threats, their accuracy degrades significantly for threats requiring cross-rule structural reasoning, especially under mutated rule forms. Model performance varies widely across threat categories and prompt settings, with no model providing consistent reliability. In contrast, the symbolic reasoning baseline maintains stable detection across both datasets, unaffected by rule rewrites or structural perturbations. These results underscore that LLMs alone are not yet dependable for safety critical interaction-threat detection in IoT environments. We discuss the implications for tool design and highlight the potential of hybrid architectures that combine symbolic analysis with LLM-based semantic interpretation to reduce false positives while maintaining structural rigor.

