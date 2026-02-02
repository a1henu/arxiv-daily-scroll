---
layout: default
title: High-quality generation of dynamic game content via small language models: A proof of concept
---

# High-quality generation of dynamic game content via small language models: A proof of concept
**arXiv**：[2601.23206v1](https://arxiv.org/abs/2601.23206) · [PDF](https://arxiv.org/pdf/2601.23206.pdf)  
**作者**：Morten I. K. Munk, Arturo Valdivia, Paolo Burelli  

**一句话要点**：提出基于小语言模型的高质量动态游戏内容生成方法，通过针对性微调解决叙事不连贯与高成本问题。

**关键词**：小语言模型, 动态游戏内容生成, 针对性微调, 合成数据生成, 实时生成, 游戏引擎约束

## 3 点简述
- 核心问题：大语言模型在动态游戏内容生成中面临叙事不连贯、高运营成本及离线应用限制。
- 方法要点：采用小语言模型，通过基于DAG的合成数据生成和针对性微调，实现窄上下文或约束结构的高质量生成。
- 实验或效果：在最小RPG循环中验证，通过重试策略达到实时生成质量，适合游戏引擎约束。

## 摘要（原文）

> Large language models (LLMs) offer promise for dynamic game content generation, but they face critical barriers, including narrative incoherence and high operational costs. Due to their large size, they are often accessed in the cloud, limiting their application in offline games. Many of these practical issues are solved by pivoting to small language models (SLMs), but existing studies using SLMs have resulted in poor output quality. We propose a strategy of achieving high-quality SLM generation through aggressive fine-tuning on deliberately scoped tasks with narrow context, constrained structure, or both. In short, more difficult tasks require narrower scope and higher specialization to the training corpus. Training data is synthetically generated via a DAG-based approach, grounding models in the specific game world. Such models can form the basis for agentic networks designed around the narratological framework at hand, representing a more practical and robust solution than cloud-dependent LLMs. To validate this approach, we present a proof-of-concept focusing on a single specialized SLM as the fundamental building block. We introduce a minimal RPG loop revolving around rhetorical battles of reputations, powered by this model. We demonstrate that a simple retry-until-success strategy reaches adequate quality (as defined by an LLM-as-a-judge scheme) with predictable latency suitable for real-time generation. While local quality assessment remains an open question, our results demonstrate feasibility for real-time generation under typical game engine constraints.

