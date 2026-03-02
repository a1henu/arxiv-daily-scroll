---
layout: default
title: SafeGen-LLM: Enhancing Safety Generalization in Task Planning for Robotic Systems
---

# SafeGen-LLM: Enhancing Safety Generalization in Task Planning for Robotic Systems
**arXiv**：[2602.24235v1](https://arxiv.org/abs/2602.24235) · [PDF](https://arxiv.org/pdf/2602.24235.pdf)  
**作者**：Jialiang Fan, Weizhe Xu, Mengyu Liu, Oleg Sokolsky, Insup Lee, Fangxin Kong  

**一句话要点**：提出SafeGen-LLM以增强机器人任务规划中的安全泛化能力

**关键词**：安全泛化, 任务规划, 大型语言模型, PDDL3基准, 策略优化, 机器人系统

## 3 点简述
- 核心问题：机器人安全关键任务规划中，传统方法可扩展性差，RL泛化不佳，基础LLM无法保证安全。
- 方法要点：构建多域PDDL3基准，采用两阶段后训练框架，包括监督微调和基于奖励机器的策略优化。
- 实验或效果：在跨域任务和多种输入格式中，SafeGen-LLM实现强安全泛化，优于前沿基线。

## 摘要（原文）

> Safety-critical task planning in robotic systems remains challenging: classical planners suffer from poor scalability, Reinforcement Learning (RL)-based methods generalize poorly, and base Large Language Models (LLMs) cannot guarantee safety. To address this gap, we propose safety-generalizable large language models, named SafeGen-LLM. SafeGen-LLM can not only enhance the safety satisfaction of task plans but also generalize well to novel safety properties in various domains. We first construct a multi-domain Planning Domain Definition Language 3 (PDDL3) benchmark with explicit safety constraints. Then, we introduce a two-stage post-training framework: Supervised Fine-Tuning (SFT) on a constraint-compliant planning dataset to learn planning syntax and semantics, and Group Relative Policy Optimization (GRPO) guided by fine-grained reward machines derived from formal verification to enforce safety alignment and by curriculum learning to better handle complex tasks. Extensive experiments show that SafeGen-LLM achieves strong safety generalization and outperforms frontier proprietary baselines across multi-domain planning tasks and multiple input formats (e.g., PDDLs and natural language).

