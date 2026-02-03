---
layout: default
title: Edit Knowledge, Not Just Facts via Multi-Step Reasoning over Background Stories
---

# Edit Knowledge, Not Just Facts via Multi-Step Reasoning over Background Stories
**arXiv**：[2602.02028v1](https://arxiv.org/abs/2602.02028) · [PDF](https://arxiv.org/pdf/2602.02028.pdf)  
**作者**：Ya Gao, Kalle Kujanpää, Pekka Marttinen, Harri Valpola, Alexander Ilin  

**一句话要点**：提出基于背景故事和多步推理的知识编辑训练策略，以增强模型知识整合与应用能力。

**关键词**：知识编辑, 多步推理, 背景故事, 知识蒸馏, 大语言模型, 知识整合

## 3 点简述
- 核心问题：现有知识编辑方法侧重原子事实，难以将新知识整合为跨上下文可用的连贯框架。
- 方法要点：通过背景故事引入新知识，结合自生成多跳问题和知识蒸馏进行训练。
- 实验或效果：模型在需要结合多个新事实的挑战性问题中表现出色，有效利用新知识进行推理。

## 摘要（原文）

> Enabling artificial intelligence systems, particularly large language models, to integrate new knowledge and flexibly apply it during reasoning remains a central challenge. Existing knowledge editing approaches emphasize atomic facts, improving factual recall but often failing to integrate new information into a coherent framework usable across contexts. In this work, we argue that knowledge internalization is fundamentally a reasoning problem rather than a memorization problem. Consequently, a model should be trained in situations where the new information is instrumental to solving a task, combined with pre-existing knowledge, and exercised through multi-step reasoning. Based on this insight, we propose a training strategy based on three principles. First, new knowledge is introduced as a coherent background story that contextualizes novel facts and explains their relation to existing knowledge. Second, models are trained using self-generated multi-hop questions that require multi-step reasoning involving the new information. Third, training is done using knowledge distillation, forcing a student model to internalize the teacher's reasoning behavior without access to the novel information. Experiments show that models trained with this strategy effectively leverage newly acquired knowledge during reasoning and achieve remarkable performance on challenging questions that require combining multiple new facts.

