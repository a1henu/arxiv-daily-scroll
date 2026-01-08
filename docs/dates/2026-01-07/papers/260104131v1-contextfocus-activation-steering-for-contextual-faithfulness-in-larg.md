---
layout: default
title: ContextFocus: Activation Steering for Contextual Faithfulness in Large Language Models
---

# ContextFocus: Activation Steering for Contextual Faithfulness in Large Language Models
**arXiv**：[2601.04131v1](https://arxiv.org/abs/2601.04131) · [PDF](https://arxiv.org/pdf/2601.04131.pdf)  
**作者**：Nikhil Anand, Shwetha Somasundaram, Anirudh Phukan, Apoorv Saxena, Koyel Mukherjee  

**一句话要点**：提出ContextFocus激活引导方法，以提升大语言模型在知识冲突场景下的上下文忠实性。

**关键词**：激活引导, 上下文忠实性, 知识冲突, 轻量级方法, 推理效率

## 3 点简述
- 核心问题：大语言模型在外部检索上下文与内部知识冲突时，常默认记忆事实，导致输出不忠实。
- 方法要点：采用轻量级激活引导，无需微调模型，推理开销小，保持流畅性和效率。
- 实验或效果：在ConFiQA基准上显著提升上下文忠实性，对提示策略互补，适用于更大模型。

## 摘要（原文）

> Large Language Models (LLMs) encode vast amounts of parametric knowledge during pre-training. As world knowledge evolves, effective deployment increasingly depends on their ability to faithfully follow externally retrieved context. When such evidence conflicts with the model's internal knowledge, LLMs often default to memorized facts, producing unfaithful outputs. In this work, we introduce ContextFocus, a lightweight activation steering approach that improves context faithfulness in such knowledge-conflict settings while preserving fluency and efficiency. Unlike prior approaches, our solution requires no model finetuning and incurs minimal inference-time overhead, making it highly efficient. We evaluate ContextFocus on the ConFiQA benchmark, comparing it against strong baselines including ContextDPO, COIECD, and prompting-based methods. Furthermore, we show that our method is complementary to prompting strategies and remains effective on larger models. Extensive experiments show that ContextFocus significantly improves contextual-faithfulness. Our results highlight the effectiveness, robustness, and efficiency of ContextFocus in improving contextual-faithfulness of LLM outputs.

