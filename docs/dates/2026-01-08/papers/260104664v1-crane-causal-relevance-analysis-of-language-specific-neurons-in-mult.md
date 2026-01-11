---
layout: default
title: CRANE: Causal Relevance Analysis of Language-Specific Neurons in Multilingual Large Language Models
---

# CRANE: Causal Relevance Analysis of Language-Specific Neurons in Multilingual Large Language Models
**arXiv**：[2601.04664v1](https://arxiv.org/abs/2601.04664) · [PDF](https://arxiv.org/pdf/2601.04664.pdf)  
**作者**：Yifan Le, Yunliang Li  

**一句话要点**：提出CRANE框架，通过神经元干预重新定义多语言大模型中的语言特异性神经元。

**关键词**：多语言大语言模型, 神经元干预, 语言特异性分析, 因果相关性, 功能必要性, 基准测试

## 3 点简述
- 核心问题：多语言大模型中语言能力在神经元层面的组织机制尚不明确，现有激活启发式方法混淆语言偏好与功能重要性。
- 方法要点：CRANE基于功能必要性，通过针对性神经元干预分析神经元对语言条件预测的贡献，而非激活幅度。
- 实验或效果：在英语、中文和越南语基准测试中，CRANE比激活方法更精确地分离语言特异性组件，揭示非排他性神经元专业化模式。

## 摘要（原文）

> Multilingual large language models (LLMs) achieve strong performance across languages, yet how language capabilities are organized at the neuron level remains poorly understood. Prior work has identified language-related neurons mainly through activation-based heuristics, which conflate language preference with functional importance. Prior work has identified language-related neurons mainly through activation-based heuristics, which conflate language preference with functional importance. We propose CRANE, a relevance-based analysis framework that redefines language specificity in terms of functional necessity, identifying language-specific neurons through targeted neuron-level interventions. CRANE characterizes neuron specialization by their contribution to language-conditioned predictions rather than activation magnitude. Our implementation will be made publicly available. Neuron-level interventions reveal a consistent asymmetric pattern: masking neurons relevant to a target language selectively degrades performance on that language while preserving performance on other languages to a substantial extent, indicating language-selective but non-exclusive neuron specializations. Experiments on English, Chinese, and Vietnamese across multiple benchmarks, together with a dedicated relevance-based metric and base-to-chat model transfer analysis, show that CRANE isolates language-specific components more precisely than activation-based methods.

