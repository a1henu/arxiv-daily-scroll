---
layout: default
title: LLM-based Argument Mining meets Argumentation and Description Logics: a Unified Framework for Reasoning about Debates
---

# LLM-based Argument Mining meets Argumentation and Description Logics: a Unified Framework for Reasoning about Debates
**arXiv**：[2603.02858v1](https://arxiv.org/abs/2603.02858) · [PDF](https://arxiv.org/pdf/2603.02858.pdf)  
**作者**：Gianvincenzo Alfano, Sergio Greco, Lucio La Cava, Stefano Francesco Monea, Irina Trubitsyna  

**一句话要点**：提出集成论证挖掘与模糊描述逻辑的框架，以增强大语言模型在辩论分析中的可解释推理能力。

**关键词**：论证挖掘, 模糊描述逻辑, 大语言模型, 辩论分析, 可解释推理

## 3 点简述
- 核心问题：大语言模型在辩论文本中缺乏透明、可验证的结构化推理机制。
- 方法要点：从原始文本提取模糊论证知识库，应用定量论证语义计算强度，并嵌入模糊描述逻辑进行查询。
- 实验或效果：提供透明、可解释且形式化基础的方法，克服纯统计分析的限制。

## 摘要（原文）

> Large Language Models (LLMs) achieve strong performance in analyzing and generating text, yet they struggle with explicit, transparent, and verifiable reasoning over complex texts such as those containing debates. In particular, they lack structured representations that capture how arguments support or attack each other and how their relative strengths determine overall acceptability. We encompass these limitations by proposing a framework that integrates learning-based argument mining with quantitative reasoning and ontology-based querying. Starting from a raw debate text, the framework extracts a fuzzy argumentative knowledge base, where arguments are explicitly represented as entities, linked by attack and support relations, and annotated with initial fuzzy strengths reflecting plausibility w.r.t. the debate's context. Quantitative argumentation semantics are then applied to compute final argument strengths by propagating the effects of supports and attacks. These results are then embedded into a fuzzy description logic setting, enabling expressive query answering through efficient rewriting techniques. The proposed approach provides a transparent, explainable, and formally grounded method for analyzing debates, overcoming purely statistical LLM-based analyses.

