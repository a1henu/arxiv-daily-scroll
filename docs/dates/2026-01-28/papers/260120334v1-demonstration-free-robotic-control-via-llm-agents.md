---
layout: default
title: Demonstration-Free Robotic Control via LLM Agents
---

# Demonstration-Free Robotic Control via LLM Agents
**arXiv**：[2601.20334v1](https://arxiv.org/abs/2601.20334) · [PDF](https://arxiv.org/pdf/2601.20334.pdf)  
**作者**：Brian Y. Tsui, Alan Y. Fang, Tiffany J. Hwu  

**一句话要点**：提出FAEA框架，将LLM智能体直接应用于机器人操作，无需演示或微调。

**关键词**：机器人操作, 大语言模型智能体, 无演示控制, 任务规划, 仿真训练

## 3 点简述
- 核心问题：现有视觉-语言-动作模型需任务特定演示和微调，泛化能力差。
- 方法要点：应用未修改的LLM智能体框架，通过迭代推理规划操作策略。
- 实验或效果：在多个基准测试中，成功率接近需演示的模型，并可增强训练数据。

## 摘要（原文）

> Robotic manipulation has increasingly adopted vision-language-action (VLA) models, which achieve strong performance but typically require task-specific demonstrations and fine-tuning, and often generalize poorly under domain shift. We investigate whether general-purpose large language model (LLM) agent frameworks, originally developed for software engineering, can serve as an alternative control paradigm for embodied manipulation. We introduce FAEA (Frontier Agent as Embodied Agent), which applies an LLM agent framework directly to embodied manipulation without modification. Using the same iterative reasoning that enables software agents to debug code, FAEA enables embodied agents to reason through manipulation strategies. We evaluate an unmodified frontier agent, Claude Agent SDK, across the LIBERO, ManiSkill3, and MetaWorld benchmarks. With privileged environment state access, FAEA achieves success rates of 84.9%, 85.7%, and 96%, respectively. This level of task success approaches that of VLA models trained with less than 100 demonstrations per task, without requiring demonstrations or fine-tuning. With one round of human feedback as an optional optimization, performance increases to 88.2% on LIBERO. This demonstration-free capability has immediate practical value: FAEA can autonomously explore novel scenarios in simulation and generate successful trajectories for training data augmentation in embodied learning. Our results indicate that general-purpose agents are sufficient for a class of manipulation tasks dominated by deliberative, task-level planning. This opens a path for robotics systems to leverage actively maintained agent infrastructure and benefit directly from ongoing advances in frontier models. Code is available at https://github.com/robiemusketeer/faea-sim

