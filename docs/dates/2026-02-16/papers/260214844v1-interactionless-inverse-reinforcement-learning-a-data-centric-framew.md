---
layout: default
title: Interactionless Inverse Reinforcement Learning: A Data-Centric Framework for Durable Alignment
---

# Interactionless Inverse Reinforcement Learning: A Data-Centric Framework for Durable Alignment
**arXiv**：[2602.14844v1](https://arxiv.org/abs/2602.14844) · [PDF](https://arxiv.org/pdf/2602.14844.pdf)  
**作者**：Elias Malomgré, Pieter Simoens  

**一句话要点**：提出Interactionless Inverse Reinforcement Learning以解决AI对齐中的Alignment Waste问题，实现可检查、可编辑的奖励模型。

**关键词**：AI对齐, 逆强化学习, 奖励模型, Alignment Flywheel, 模型无关性, 可验证安全

## 3 点简述
- 核心问题：现有AI对齐方法如RLHF和DPO产生不透明、单次使用的对齐工件，导致Alignment Waste。
- 方法要点：通过Interactionless Inverse Reinforcement Learning解耦对齐工件学习和策略优化，生成模型无关的奖励模型。
- 实验或效果：引入Alignment Flywheel生命周期，通过自动化审计和精炼迭代强化奖励模型，提升安全性的耐久性和可验证性。

## 摘要（原文）

> AI alignment is growing in importance, yet current approaches suffer from a critical structural flaw that entangles the safety objectives with the agent's policy. Methods such as Reinforcement Learning from Human Feedback and Direct Preference Optimization create opaque, single-use alignment artifacts, which we term Alignment Waste. We propose Interactionless Inverse Reinforcement Learning to decouple alignment artifact learning from policy optimization, producing an inspectable, editable, and model-agnostic reward model. Additionally, we introduce the Alignment Flywheel, a human-in-the-loop lifecycle that iteratively hardens the reward model through automated audits and refinement. This architecture transforms safety from a disposable expense into a durable, verifiable engineering asset.

