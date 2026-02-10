---
layout: default
title: When Do Multi-Agent Systems Outperform? Analysing the Learning Efficiency of Agentic Systems
---

# When Do Multi-Agent Systems Outperform? Analysing the Learning Efficiency of Agentic Systems
**arXiv**：[2602.08272v1](https://arxiv.org/abs/2602.08272) · [PDF](https://arxiv.org/pdf/2602.08272.pdf)  
**作者**：Junwei Su, Chuan Wu  

**一句话要点**：分析多智能体强化学习在大型语言模型中的样本效率，基于PAC框架推导理论边界

**关键词**：多智能体强化学习, 样本复杂度, 任务分解, 大型语言模型, PAC框架, 理论分析

## 3 点简述
- 核心问题：多智能体强化学习何时优于单智能体强化学习，理论依据不足
- 方法要点：使用PAC框架定义SARL和MARL，推导样本复杂度边界，分析任务分解与对齐
- 实验或效果：MARL在独立子任务中提升样本效率，依赖子任务削弱优势，量化任务对齐权衡

## 摘要（原文）

> Reinforcement Learning (RL) has emerged as a crucial method for training or fine-tuning large language models (LLMs), enabling adaptive, task-specific optimizations through interactive feedback. Multi-Agent Reinforcement Learning (MARL), in particular, offers a promising avenue by decomposing complex tasks into specialized subtasks learned by distinct interacting agents, potentially enhancing the ability and efficiency of LLM systems. However, theoretical insights regarding when and why MARL outperforms Single-Agent RL (SARL) remain limited, creating uncertainty in selecting the appropriate RL framework. In this paper, we address this critical gap by rigorously analyzing the comparative sample efficiency of MARL and SARL within the context of LLM. Leveraging the Probably Approximately Correct (PAC) framework, we formally define SARL and MARL setups for LLMs, derive explicit sample complexity bounds, and systematically characterize how task decomposition and alignment influence learning efficiency. Our results demonstrate that MARL improves sample complexity when tasks naturally decompose into independent subtasks, whereas dependent subtasks diminish MARL's comparative advantage. Additionally, we introduce and analyze the concept of task alignment, quantifying the trade-offs when enforcing independent task decomposition despite potential misalignments. These theoretical insights clarify empirical inconsistencies and provide practical criteria for deploying MARL strategies effectively in complex LLM scenarios.

