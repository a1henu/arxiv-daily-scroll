---
layout: default
title: When Actions Teach You to Think: Reasoning-Action Synergy via Reinforcement Learning in Conversational Agents
---

# When Actions Teach You to Think: Reasoning-Action Synergy via Reinforcement Learning in Conversational Agents
**arXiv**：[2512.11277v1](https://arxiv.org/abs/2512.11277) · [PDF](https://arxiv.org/pdf/2512.11277.pdf)  
**作者**：Mrinal Rawat, Arkajyoti Chakraborty, Neha Gupta, Roberto Pieraccini  

**一句话要点**：提出基于强化学习的推理-行动协同方法，以提升对话代理的泛化能力与工具调用精度。

**关键词**：强化学习, 推理增强, 对话代理, 工具调用, 泛化能力, 策略优化

## 3 点简述
- 核心问题：监督微调在数据分布变化时泛化困难，高质量推理标注成本高且难扩展。
- 方法要点：利用强化学习，通过奖励机制（工具准确性和答案正确性）迭代优化推理步骤与工具调用。
- 实验或效果：相比无显式推理的监督微调模型，相对提升1.5%；相比基础模型，增益达40%。

## 摘要（原文）

> Supervised fine-tuning (SFT) has emerged as one of the most effective ways to improve the performance of large language models (LLMs) in downstream tasks. However, SFT can have difficulty generalizing when the underlying data distribution changes, even when the new data does not fall completely outside the training domain. Recent reasoning-focused models such as o1 and R1 have demonstrated consistent gains over their non-reasoning counterparts, highlighting the importance of reasoning for improved generalization and reliability. However, collecting high-quality reasoning traces for SFT remains challenging -- annotations are costly, subjective, and difficult to scale. To address this limitation, we leverage Reinforcement Learning (RL) to enable models to learn reasoning strategies directly from task outcomes. We propose a pipeline in which LLMs generate reasoning steps that guide both the invocation of tools (e.g., function calls) and the final answer generation for conversational agents. Our method employs Group Relative Policy Optimization (GRPO) with rewards designed around tool accuracy and answer correctness, allowing the model to iteratively refine its reasoning and actions. Experimental results demonstrate that our approach improves both the quality of reasoning and the precision of tool invocations, achieving a 1.5% relative improvement over the SFT model (trained without explicit thinking) and a 40% gain compared to the base of the vanilla Qwen3-1.7B model. These findings demonstrate the promise of unifying reasoning and action learning through RL to build more capable and generalizable conversational agents.

