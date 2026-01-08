---
layout: default
title: Membox: Weaving Topic Continuity into Long-Range Memory for LLM Agents
---

# Membox: Weaving Topic Continuity into Long-Range Memory for LLM Agents
**arXiv**：[2601.03785v1](https://arxiv.org/abs/2601.03785) · [PDF](https://arxiv.org/pdf/2601.03785.pdf)  
**作者**：Dehao Tao, Guoliang Ma, Yongfeng Huang, Minghu Jiang  

**一句话要点**：提出Membox以解决LLM代理在长对话中主题连续性丢失的问题

**关键词**：LLM代理, 主题连续性, 记忆系统, 时序推理, 对话建模

## 3 点简述
- 核心问题：现有LLM代理记忆系统因存储时对话流碎片化，破坏主题连续性和因果流
- 方法要点：引入Topic Loom和Trace Weaver，通过滑动窗口分组同主题对话为记忆盒，并链接成长期事件时间线
- 实验或效果：在LoCoMo上，Membox在时序推理任务中F1提升达68%，且上下文令牌使用量显著减少

## 摘要（原文）

> Human-agent dialogues often exhibit topic continuity-a stable thematic frame that evolves through temporally adjacent exchanges-yet most large language model (LLM) agent memory systems fail to preserve it. Existing designs follow a fragmentation-compensation paradigm: they first break dialogue streams into isolated utterances for storage, then attempt to restore coherence via embedding-based retrieval. This process irreversibly damages narrative and causal flow, while biasing retrieval towards lexical similarity. We introduce membox, a hierarchical memory architecture centered on a Topic Loom that continuously monitors dialogue in a sliding-window fashion, grouping consecutive same-topic turns into coherent "memory boxes" at storage time. Sealed boxes are then linked by a Trace Weaver into long-range event-timeline traces, recovering macro-topic recurrences across discontinuities. Experiments on LoCoMo demonstrate that Membox achieves up to 68% F1 improvement on temporal reasoning tasks, outperforming competitive baselines (e.g., Mem0, A-MEM). Notably, Membox attains these gains while using only a fraction of the context tokens required by existing methods, highlighting a superior balance between efficiency and effectiveness. By explicitly modeling topic continuity, Membox offers a cognitively motivated mechanism for enhancing both coherence and efficiency in LLM agents.

