---
layout: default
title: FadeMem: Biologically-Inspired Forgetting for Efficient Agent Memory
---

# FadeMem: Biologically-Inspired Forgetting for Efficient Agent Memory
**arXiv**：[2601.18642v1](https://arxiv.org/abs/2601.18642) · [PDF](https://arxiv.org/pdf/2601.18642.pdf)  
**作者**：Lei Wei, Xu Dong, Xiao Peng, Niantao Xie, Bin Wang  

**一句话要点**：提出FadeMem以解决自主代理中记忆效率低下的问题，通过生物启发的遗忘机制优化存储与推理。

**关键词**：自主代理记忆, 生物启发遗忘, 记忆效率优化, 多跳推理, 存储减少

## 3 点简述
- 核心问题：大型语言模型作为自主代理时，缺乏选择性遗忘机制，导致灾难性遗忘或信息过载。
- 方法要点：设计双层级记忆架构，基于语义相关性、访问频率和时间模式，采用自适应指数衰减函数实现差异化解码。
- 实验或效果：在Multi-Session Chat等基准测试中，实现45%存储减少，并提升多跳推理和检索性能。

## 摘要（原文）

> Large language models deployed as autonomous agents face critical memory limitations, lacking selective forgetting mechanisms that lead to either catastrophic forgetting at context boundaries or information overload within them. While human memory naturally balances retention and forgetting through adaptive decay processes, current AI systems employ binary retention strategies that preserve everything or lose it entirely. We propose FadeMem, a biologically-inspired agent memory architecture that incorporates active forgetting mechanisms mirroring human cognitive efficiency. FadeMem implements differential decay rates across a dual-layer memory hierarchy, where retention is governed by adaptive exponential decay functions modulated by semantic relevance, access frequency, and temporal patterns. Through LLM-guided conflict resolution and intelligent memory fusion, our system consolidates related information while allowing irrelevant details to fade. Experiments on Multi-Session Chat, LoCoMo, and LTI-Bench demonstrate superior multi-hop reasoning and retrieval with 45\% storage reduction, validating the effectiveness of biologically-inspired forgetting in agent memory systems.

