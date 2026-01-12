---
layout: default
title: Modular Autonomy with Conversational Interaction: An LLM-driven Framework for Decision Making in Autonomous Driving
---

# Modular Autonomy with Conversational Interaction: An LLM-driven Framework for Decision Making in Autonomous Driving
**arXiv**：[2601.05806v1](https://arxiv.org/abs/2601.05806) · [PDF](https://arxiv.org/pdf/2601.05806.pdf)  
**作者**：Marvin Seegert, Korbinian Moller, Johannes Betz  

**一句话要点**：提出基于LLM的对话交互框架，以解决自动驾驶中自然语言指令到结构化动作的映射问题。

**关键词**：自动驾驶系统, 大型语言模型, 自然语言交互, 模块化软件, 安全验证, 命令翻译

## 3 点简述
- 核心问题：如何将复杂的人类语言映射到模块化自动驾驶软件的结构化动作空间。
- 方法要点：集成LLM交互层与Autoware，采用分类、DSL翻译和安全验证三层架构。
- 实验或效果：评估显示系统时间效率高、翻译鲁棒，仿真验证了五类交互命令的执行。

## 摘要（原文）

> Recent advancements in Large Language Models (LLMs) offer new opportunities to create natural language interfaces for Autonomous Driving Systems (ADSs), moving beyond rigid inputs. This paper addresses the challenge of mapping the complexity of human language to the structured action space of modular ADS software. We propose a framework that integrates an LLM-based interaction layer with Autoware, a widely used open-source software. This system enables passengers to issue high-level commands, from querying status information to modifying driving behavior. Our methodology is grounded in three key components: a taxonomization of interaction categories, an application-centric Domain Specific Language (DSL) for command translation, and a safety-preserving validation layer. A two-stage LLM architecture ensures high transparency by providing feedback based on the definitive execution status. Evaluation confirms the system's timing efficiency and translation robustness. Simulation successfully validated command execution across all five interaction categories. This work provides a foundation for extensible, DSL-assisted interaction in modular and safety-conscious autonomy stacks.

