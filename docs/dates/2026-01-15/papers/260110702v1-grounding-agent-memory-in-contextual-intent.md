---
layout: default
title: Grounding Agent Memory in Contextual Intent
---

# Grounding Agent Memory in Contextual Intent
**arXiv**：[2601.10702v1](https://arxiv.org/abs/2601.10702) · [PDF](https://arxiv.org/pdf/2601.10702.pdf)  
**作者**：Ruozhen Yang, Yucheng Jiang, Yueqi Jiang, Priyanka Kargupta, Yunyi Zhang, Jiawei Han  

**一句话要点**：提出STITCH代理记忆系统，通过上下文意图索引解决长时目标导向交互中的记忆检索干扰问题。

**关键词**：代理记忆系统, 上下文意图索引, 长时目标导向交互, 结构化检索, 记忆干扰减少, 基准评估

## 3 点简述
- 核心问题：长时目标导向交互中，相似实体和事实在不同潜在目标下重复出现，导致记忆系统检索上下文不匹配的证据。
- 方法要点：STITCH使用结构化检索线索（上下文意图）索引轨迹步骤，包括潜在目标、动作类型和关键实体类型，以匹配当前意图进行历史检索。
- 实验或效果：在CAME-Bench和LongMemEval基准上，STITCH实现最先进性能，比最强基线提升35.6%，尤其在长轨迹中表现更佳。

## 摘要（原文）

> Deploying large language models in long-horizon, goal-oriented interactions remains challenging because similar entities and facts recur under different latent goals and constraints, causing memory systems to retrieve context-mismatched evidence. We propose STITCH (Structured Intent Tracking in Contextual History), an agentic memory system that indexes each trajectory step with a structured retrieval cue, contextual intent, and retrieves history by matching the current step's intent. Contextual intent provides compact signals that disambiguate repeated mentions and reduce interference: (1) the current latent goal defining a thematic segment, (2) the action type, and (3) the salient entity types anchoring which attributes matter. During inference, STITCH filters and prioritizes memory snippets by intent compatibility, suppressing semantically similar but context-incompatible history.
>   For evaluation, we introduce CAME-Bench, a benchmark for context-aware retrieval in realistic, dynamic, goal-oriented trajectories. Across CAME-Bench and LongMemEval, STITCH achieves state-of-the-art performance, outperforming the strongest baseline by 35.6%, with the largest gains as trajectory length increases. Our analysis shows that intent indexing substantially reduces retrieval noise, supporting intent-aware memory for robust long-horizon reasoning.

