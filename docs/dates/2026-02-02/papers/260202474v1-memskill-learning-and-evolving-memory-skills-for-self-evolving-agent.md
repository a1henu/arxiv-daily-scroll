---
layout: default
title: MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents
---

# MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents
**arXiv**：[2602.02474v1](https://arxiv.org/abs/2602.02474) · [PDF](https://arxiv.org/pdf/2602.02474.pdf)  
**作者**：Haozhen Zhang, Quanyu Long, Jianzhu Bao, Tao Feng, Weizhi Zhang, Haodong Yue, Wenya Wang  

**一句话要点**：提出MemSkill以解决LLM代理内存系统操作静态、适应性差的问题。

**关键词**：LLM代理, 内存管理, 技能学习, 自适应系统, 长历史处理

## 3 点简述
- 核心问题：现有LLM代理内存系统依赖静态手工操作，导致在多样交互模式和长历史中效率低下。
- 方法要点：将内存操作重构为可学习、可演化的技能，通过控制器选择技能，执行器生成记忆，设计器演化技能集。
- 实验或效果：在多个基准测试中提升任务性能，并展示技能演化过程，增强适应性。

## 摘要（原文）

> Most Large Language Model (LLM) agent memory systems rely on a small set of static, hand-designed operations for extracting memory. These fixed procedures hard-code human priors about what to store and how to revise memory, making them rigid under diverse interaction patterns and inefficient on long histories. To this end, we present \textbf{MemSkill}, which reframes these operations as learnable and evolvable memory skills, structured and reusable routines for extracting, consolidating, and pruning information from interaction traces. Inspired by the design philosophy of agent skills, MemSkill employs a \emph{controller} that learns to select a small set of relevant skills, paired with an LLM-based \emph{executor} that produces skill-guided memories. Beyond learning skill selection, MemSkill introduces a \emph{designer} that periodically reviews hard cases where selected skills yield incorrect or incomplete memories, and evolves the skill set by proposing refinements and new skills. Together, MemSkill forms a closed-loop procedure that improves both the skill-selection policy and the skill set itself. Experiments on LoCoMo, LongMemEval, HotpotQA, and ALFWorld demonstrate that MemSkill improves task performance over strong baselines and generalizes well across settings. Further analyses shed light on how skills evolve, offering insights toward more adaptive, self-evolving memory management for LLM agents.

