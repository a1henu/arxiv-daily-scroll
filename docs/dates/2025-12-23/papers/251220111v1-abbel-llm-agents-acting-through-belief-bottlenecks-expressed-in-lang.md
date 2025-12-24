---
layout: default
title: ABBEL: LLM Agents Acting through Belief Bottlenecks Expressed in Language
---

# ABBEL: LLM Agents Acting through Belief Bottlenecks Expressed in Language
**arXiv**：[2512.20111v1](https://arxiv.org/abs/2512.20111) · [PDF](https://arxiv.org/pdf/2512.20111.pdf)  
**作者**：Aly Lidayan, Jakob Bjorner, Satvik Golechha, Kartik Goyal, Alane Suhr  

**一句话要点**：提出ABBEL框架，通过语言表达的信念瓶颈来维持LLM代理在长序列决策任务中的简洁上下文。

**关键词**：LLM代理, 信念瓶颈, 序列决策, 强化学习, 上下文压缩, 可解释AI

## 3 点简述
- 核心问题：长序列决策任务中，完整交互历史在计算上不切实际，需减少内存使用。
- 方法要点：用自然语言信念状态替代历史，通过信念更新和动作选择，支持可解释性并保持近恒定内存。
- 实验或效果：在六个多步环境中评估，RL后训练能提升性能，超越完整上下文设置，同时减少内存。

## 摘要（原文）

> As the length of sequential decision-making tasks increases, it becomes computationally impractical to keep full interaction histories in context. We introduce a general framework for LLM agents to maintain concise contexts through multi-step interaction: Acting through Belief Bottlenecks Expressed in Language (ABBEL), and methods to further improve ABBEL agents with RL post-training. ABBEL replaces long multi-step interaction history by a belief state, i.e., a natural language summary of what has been discovered about task-relevant unknowns. Under ABBEL, at each step the agent first updates a prior belief with the most recent observation from the environment to form a posterior belief, then uses only the posterior to select an action. We systematically evaluate frontier models under ABBEL across six diverse multi-step environments, finding that ABBEL supports generating interpretable beliefs while maintaining near-constant memory use over interaction steps. However, bottleneck approaches are generally prone to error propagation, which we observe causing inferior performance when compared to the full context setting due to errors in belief updating. Therefore, we train LLMs to generate and act on beliefs within the ABBEL framework via reinforcement learning (RL). We experiment with belief grading, to reward higher quality beliefs, as well as belief length penalties to reward more compressed beliefs. Our experiments demonstrate the ability of RL to improve ABBEL's performance beyond the full context setting, while using less memory than contemporaneous approaches.

