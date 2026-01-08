---
layout: default
title: SCRIBE: Structured Mid-Level Supervision for Tool-Using Language Models
---

# SCRIBE: Structured Mid-Level Supervision for Tool-Using Language Models
**arXiv**：[2601.03555v1](https://arxiv.org/abs/2601.03555) · [PDF](https://arxiv.org/pdf/2601.03555.pdf)  
**作者**：Yuxuan Jiang, Francis Ferraro  

**一句话要点**：提出SCRIBE框架，通过结构化中间层监督解决工具增强语言模型中的信用分配难题。

**关键词**：工具增强语言模型, 强化学习, 信用分配, 中间层监督, 技能原型, 结构化奖励

## 3 点简述
- 核心问题：多步推理中信用分配困难，现有LLM评估信号噪声大且不一致。
- 方法要点：基于技能原型库进行中间层抽象，将开放评估转化为约束验证问题。
- 实验效果：在推理和工具使用基准上达到SOTA，显著提升模型准确率和成功率。

## 摘要（原文）

> Training reliable tool-augmented agents remains a significant challenge, largely due to the difficulty of credit assignment in multi-step reasoning. While process-level reward models offer a promising direction, existing LLM-based judges often produce noisy and inconsistent signals because they lack fine-grained, task-specific rubrics to distinguish high-level planning from low-level execution. In this work, we introduce SCRIBE (Skill-Conditioned Reward with Intermediate Behavioral Evaluation), a reinforcement learning framework that intervenes at a novel mid-level abstraction. SCRIBE grounds reward modeling in a curated library of skill prototypes, transforming open-ended LLM evaluation into a constrained verification problem. By routing each subgoal to a corresponding prototype, the reward model is equipped with precise, structured rubrics that substantially reduce reward variance.
>   Experimental results show that SCRIBE achieves state-of-the-art performance across a range of reasoning and tool-use benchmarks. In particular, it improves the AIME25 accuracy of a Qwen3-4B model from 43.3% to 63.3%, and significantly increases success rates in complex multi-turn tool interactions.
>   Further analysis of training dynamics reveals a co-evolution across abstraction levels, where mastery of mid-level skills consistently precedes the emergence of effective high-level planning behaviors. Finally, we demonstrate that SCRIBE is additive to low-level tool optimizations, providing a scalable and complementary pathway toward more autonomous and reliable tool-using agents.

