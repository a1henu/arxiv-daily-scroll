---
layout: default
title: OpenMic: A Multi-Agent-Based Stand-Up Comedy Generation System
---

# OpenMic: A Multi-Agent-Based Stand-Up Comedy Generation System
**arXiv**：[2601.08288v1](https://arxiv.org/abs/2601.08288) · [PDF](https://arxiv.org/pdf/2601.08288.pdf)  
**作者**：Yuyang Wu, Hanzhong Cao, Jianhao Chen, Yufei Li  

**一句话要点**：提出OpenMic多智能体系统，基于AutoGen生成中文脱口秀表演与视频，解决文化幽默与数据集不匹配问题。

**关键词**：多智能体系统, 中文幽默生成, 检索增强生成, 脱口秀表演, 长文本生成, 视频生成

## 3 点简述
- 核心问题：中文脱口秀生成需文化幽默、时机与表演性，现有数据集更适合理解而非长文本生成，导致监督不匹配。
- 方法要点：采用多智能体迭代规划优化幽默与表演，结合检索增强生成和微调JokeWriter以提升结构化和长程回调。
- 实验或效果：系统能将用户话题转化为3-5分钟表演并生成视频，增强生成质量与实用性。

## 摘要（原文）

> Chinese stand-up comedy generation goes beyond plain text generation, requiring culturally grounded humor, precise timing, stage-performance cues, and implicit multi-step reasoning. Moreover, commonly used Chinese humor datasets are often better suited for humor understanding and evaluation than for long-form stand-up generation, making direct supervision misaligned with the target task. To address these challenges, we present OpenMic, an end-to-end multi-agent system built on AutoGen that transforms a user-provided life topic into a 3-5 minute Chinese stand-up performance and further produces a narrated comedy video. OpenMic orchestrates multiple specialized agents in a multi-round iterative loop-planning to jointly optimize humor, timing, and performability. To mitigate the dataset-task mismatch, we augment generation with retrieval-augmented generation (RAG) for material grounding and idea expansion, and we fine-tune a dedicated JokeWriter to better internalize stand-up-specific setup-punchline structures and long-range callbacks.

