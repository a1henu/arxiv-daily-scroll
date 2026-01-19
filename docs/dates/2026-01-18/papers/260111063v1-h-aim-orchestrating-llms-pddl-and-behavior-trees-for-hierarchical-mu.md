---
layout: default
title: H-AIM: Orchestrating LLMs, PDDL, and Behavior Trees for Hierarchical Multi-Robot Planning
---

# H-AIM: Orchestrating LLMs, PDDL, and Behavior Trees for Hierarchical Multi-Robot Planning
**arXiv**：[2601.11063v1](https://arxiv.org/abs/2601.11063) · [PDF](https://arxiv.org/pdf/2601.11063.pdf)  
**作者**：Haishan Zeng, Peng Li  

**一句话要点**：提出H-AIM框架，通过LLM、PDDL和行为树结合，解决异构机器人团队长时任务规划问题。

**关键词**：多机器人规划, LLM应用, PDDL规划, 行为树控制, 异构机器人, 任务规划框架

## 3 点简述
- 核心问题：异构机器人团队执行长时任务时，LLM在推理和协调方面存在局限。
- 方法要点：采用三阶段架构，结合LLM解析指令、经典规划器优化序列、行为树实现反应控制。
- 实验或效果：在MACE-THOR基准上，任务成功率从12%提升至55%，目标条件召回率从32%提升至72%。

## 摘要（原文）

> In embodied artificial intelligence, enabling heterogeneous robot teams to execute long-horizon tasks from high-level instructions remains a critical challenge. While large language models (LLMs) show promise in instruction parsing and preliminary planning, they exhibit limitations in long-term reasoning and dynamic multi-robot coordination. We propose Hierarchical Autonomous Intelligent Multi-Robot Planning(H-AIM), a novel embodied multi-robot task planning framework that addresses these issues through a three-stage cascaded architecture: 1) It leverages an LLM to parse instructions and generate Planning Domain Definition Language (PDDL) problem descriptions, thereby transforming commands into formal planning problems; 2) It combines the semantic reasoning of LLMs with the search capabilities of a classical planner to produce optimized action sequences; 3) It compiles the resulting plan into behavior trees for reactive control. The framework supports dynamically sized heterogeneous robot teams via a shared blackboard mechanism for communication and state synchronization. To validate our approach, we introduce the MACE-THOR benchmark dataset, comprising 42 complex tasks across 8 distinct household layouts. Experimental results demonstrate that H-AIM achieves a remarkable performance improvement, elevating the task success rate from 12% to 55% and boosting the goal condition recall from 32% to 72% against the strongest baseline, LaMMA-P.

