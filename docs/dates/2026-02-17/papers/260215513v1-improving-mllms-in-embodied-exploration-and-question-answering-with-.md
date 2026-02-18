---
layout: default
title: Improving MLLMs in Embodied Exploration and Question Answering with Human-Inspired Memory Modeling
---

# Improving MLLMs in Embodied Exploration and Question Answering with Human-Inspired Memory Modeling
**arXiv**：[2602.15513v1](https://arxiv.org/abs/2602.15513) · [PDF](https://arxiv.org/pdf/2602.15513.pdf)  
**作者**：Ji Li, Jing Xia, Mingyi Li, Shiyan Hu  

**一句话要点**：提出非参数记忆框架以提升具身代理在探索和问答中的性能

**关键词**：具身智能, 多模态大语言模型, 记忆建模, 情景记忆, 语义记忆, 探索问答

## 3 点简述
- 核心问题：现有基于文本摘要的记忆方法在长时观察和有限上下文下丢弃视觉空间细节，导致非平稳环境中脆弱。
- 方法要点：通过解耦情景和语义记忆，采用检索优先、推理辅助范式，结合程序式规则提取机制。
- 实验或效果：在A-EQA和GOAT-Bench基准上实现SOTA，提升LLM-Match 7.3%和成功率7.7%。

## 摘要（原文）

> Deploying Multimodal Large Language Models as the brain of embodied agents remains challenging, particularly under long-horizon observations and limited context budgets. Existing memory assisted methods often rely on textual summaries, which discard rich visual and spatial details and remain brittle in non-stationary environments. In this work, we propose a non-parametric memory framework that explicitly disentangles episodic and semantic memory for embodied exploration and question answering. Our retrieval-first, reasoning-assisted paradigm recalls episodic experiences via semantic similarity and verifies them through visual reasoning, enabling robust reuse of past observations without rigid geometric alignment. In parallel, we introduce a program-style rule extraction mechanism that converts experiences into structured, reusable semantic memory, facilitating cross-environment generalization. Extensive experiments demonstrate state-of-the-art performance on embodied question answering and exploration benchmarks, yielding a 7.3% gain in LLM-Match and an 11.4% gain in LLM MatchXSPL on A-EQA, as well as +7.7% success rate and +6.8% SPL on GOAT-Bench. Analyses reveal that our episodic memory primarily improves exploration efficiency, while semantic memory strengthens complex reasoning of embodied agents.

