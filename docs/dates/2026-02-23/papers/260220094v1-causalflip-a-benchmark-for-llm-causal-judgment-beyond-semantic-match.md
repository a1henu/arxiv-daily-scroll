---
layout: default
title: CausalFlip: A Benchmark for LLM Causal Judgment Beyond Semantic Matching
---

# CausalFlip: A Benchmark for LLM Causal Judgment Beyond Semantic Matching
**arXiv**：[2602.20094v1](https://arxiv.org/abs/2602.20094) · [PDF](https://arxiv.org/pdf/2602.20094.pdf)  
**作者**：Yuzhe Wang, Yaochen Zhu, Jundong Li  

**一句话要点**：提出CausalFlip基准以评估LLM在因果推理中超越语义匹配的能力

**关键词**：因果推理基准, 语义匹配偏差, 大语言模型评估, 噪声前缀评估, 内部化推理

## 3 点简述
- 核心问题：LLMs在复杂决策中依赖语义模式而非真实因果结构，导致推理偏差
- 方法要点：构建语义相似但因果答案相反的问题对，并引入噪声前缀评估
- 实验或效果：内部化因果推理方法显著提升因果基础，优于显式思维链监督

## 摘要（原文）

> As large language models (LLMs) witness increasing deployment in complex, high-stakes decision-making scenarios, it becomes imperative to ground their reasoning in causality rather than spurious correlations. However, strong performance on traditional reasoning benchmarks does not guarantee true causal reasoning ability of LLMs, as high accuracy may still arise from memorizing semantic patterns instead of analyzing the underlying true causal structures. To bridge this critical gap, we propose a new causal reasoning benchmark, CausalFlip, designed to encourage the development of new LLM paradigm or training algorithms that ground LLM reasoning in causality rather than semantic correlation. CausalFlip consists of causal judgment questions built over event triples that could form different confounder, chain, and collider relations. Based on this, for each event triple, we construct pairs of semantically similar questions that reuse the same events but yield opposite causal answers, where models that rely heavily on semantic matching are systematically driven toward incorrect predictions. To further probe models' reliance on semantic patterns, we introduce a noisy-prefix evaluation that prepends causally irrelevant text before intermediate causal reasoning steps without altering the underlying causal relations or the logic of the reasoning process. We evaluate LLMs under multiple training paradigms, including answer-only training, explicit Chain-of-Thought (CoT) supervision, and a proposed internalized causal reasoning approach that aims to mitigate explicit reliance on correlation in the reasoning process. Our results show that explicit CoT can still be misled by spurious semantic correlations, where internalizing reasoning steps yields substantially improved causal grounding, suggesting that it is promising to better elicit the latent causal reasoning capabilities of base LLMs.

