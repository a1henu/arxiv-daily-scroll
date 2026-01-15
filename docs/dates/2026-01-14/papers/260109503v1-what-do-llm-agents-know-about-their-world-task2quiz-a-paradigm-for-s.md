---
layout: default
title: What Do LLM Agents Know About Their World? Task2Quiz: A Paradigm for Studying Environment Understanding
---

# What Do LLM Agents Know About Their World? Task2Quiz: A Paradigm for Studying Environment Understanding
**arXiv**：[2601.09503v1](https://arxiv.org/abs/2601.09503) · [PDF](https://arxiv.org/pdf/2601.09503.pdf)  
**作者**：Siyuan Liu, Hongbang Yuan, Xinze Li, Ziyue Zhu, Yixin Cao, Yu-Gang Jiang  

**一句话要点**：提出Task-to-Quiz范式以评估LLM代理的环境理解能力，揭示任务成功与理解脱节。

**关键词**：LLM代理评估, 环境理解, 任务到问答范式, 自动化基准, 记忆机制分析, 可迁移模型

## 3 点简述
- 核心问题：LLM代理在复杂任务中表现出色，但环境理解能力未充分评估，现有指标依赖任务轨迹，缺乏对可迁移环境模型的检验。
- 方法要点：设计Task-to-Quiz（T2Q）范式，自动化评估环境理解，通过T2QBench包含30个环境和1,967个QA对，解耦任务执行与世界状态理解。
- 实验或效果：实验表明任务成功常不能反映环境理解，当前记忆机制无法有效帮助代理获取环境模型，识别主动探索和细粒度状态表示为瓶颈。

## 摘要（原文）

> Large language model (LLM) agents have demonstrated remarkable capabilities in complex decision-making and tool-use tasks, yet their ability to generalize across varying environments remains a under-examined concern. Current evaluation paradigms predominantly rely on trajectory-based metrics that measure task success, while failing to assess whether agents possess a grounded, transferable model of the environment. To address this gap, we propose Task-to-Quiz (T2Q), a deterministic and automated evaluation paradigm designed to decouple task execution from world-state understanding. We instantiate this paradigm in T2QBench, a suite comprising 30 environments and 1,967 grounded QA pairs across multiple difficulty levels. Our extensive experiments reveal that task success is often a poor proxy for environment understanding, and that current memory machanism can not effectively help agents acquire a grounded model of the environment. These findings identify proactive exploration and fine-grained state representation as primary bottlenecks, offering a robust foundation for developing more generalizable autonomous agents.

