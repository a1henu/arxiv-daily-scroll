---
layout: default
title: ES-MemEval: Benchmarking Conversational Agents on Personalized Long-Term Emotional Support
---

# ES-MemEval: Benchmarking Conversational Agents on Personalized Long-Term Emotional Support
**arXiv**：[2602.01885v1](https://arxiv.org/abs/2602.01885) · [PDF](https://arxiv.org/pdf/2602.01885.pdf)  
**作者**：Tiantian Chen, Jiaqi Lu, Ying Shen, Lin Zhang  

**一句话要点**：提出ES-MemEval基准和EvoEmo数据集，以评估对话代理在个性化长期情感支持中的记忆能力。

**关键词**：情感支持对话, 长期记忆评估, 个性化建模, 检索增强生成, 多会话数据集, 幻觉减少

## 3 点简述
- 现有基准在评估分散、隐含和持续演变的用户信息场景中存在不足。
- ES-MemEval系统评估信息提取、时序推理等五种核心记忆能力。
- 实验表明显式长期记忆对减少幻觉和实现个性化至关重要，但RAG在时序动态方面有局限。

## 摘要（原文）

> Large Language Models (LLMs) have shown strong potential as conversational agents. Yet, their effectiveness remains limited by deficiencies in robust long-term memory, particularly in complex, long-term web-based services such as online emotional support. However, existing long-term dialogue benchmarks primarily focus on static and explicit fact retrieval, failing to evaluate agents in critical scenarios where user information is dispersed, implicit, and continuously evolving. To address this gap, we introduce ES-MemEval, a comprehensive benchmark that systematically evaluates five core memory capabilities: information extraction, temporal reasoning, conflict detection, abstention, and user modeling, in long-term emotional support settings, covering question answering, summarization, and dialogue generation tasks. To support the benchmark, we also propose EvoEmo, a multi-session dataset for personalized long-term emotional support that captures fragmented, implicit user disclosures and evolving user states. Extensive experiments on open-source long-context, commercial, and retrieval-augmented (RAG) LLMs show that explicit long-term memory is essential for reducing hallucinations and enabling effective personalization. At the same time, RAG improves factual consistency but struggles with temporal dynamics and evolving user states. These findings highlight both the potential and limitations of current paradigms and motivate more robust integration of memory and retrieval for long-term personalized dialogue systems.

