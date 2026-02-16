---
layout: default
title: Agentic AI for Robot Control: Flexible but still Fragile
---

# Agentic AI for Robot Control: Flexible but still Fragile
**arXiv**：[2602.13081v1](https://arxiv.org/abs/2602.13081) · [PDF](https://arxiv.org/pdf/2602.13081.pdf)  
**作者**：Oscar Lima, Marc Vinci, Martin Günther, Marian Renz, Alexander Sung, Sebastian Stock, Johannes Brust, Lennart Niecksch, Zongyao Yi, Felix Igelbrink, Benjamin Kisliuk, Martin Atzmueller, Joachim Hertzberg  

**一句话要点**：提出基于语言模型的智能体控制系统，用于机器人任务规划与执行，但存在脆弱性问题。

**关键词**：机器人控制, 语言模型, 任务规划, 智能体系统, 不确定性处理

## 3 点简述
- 核心问题：机器人控制中不确定性、部分可观测性和自然语言指令模糊性带来的挑战。
- 方法要点：利用推理能力语言模型在迭代规划-执行循环中选择和调用机器人技能。
- 实验或效果：在移动操作和农业导航平台上验证系统灵活性，但表现出非确定性行为和高提示敏感性。

## 摘要（原文）

> Recent work leverages the capabilities and commonsense priors of generative models for robot control. In this paper, we present an agentic control system in which a reasoning-capable language model plans and executes tasks by selecting and invoking robot skills within an iterative planner and executor loop. We deploy the system on two physical robot platforms in two settings: (i) tabletop grasping, placement, and box insertion in indoor mobile manipulation (Mobipick) and (ii) autonomous agricultural navigation and sensing (Valdemar). Both settings involve uncertainty, partial observability, sensor noise, and ambiguous natural-language commands. The system exposes structured introspection of its planning and decision process, reacts to exogenous events via explicit event checks, and supports operator interventions that modify or redirect ongoing execution. Across both platforms, our proof-of-concept experiments reveal substantial fragility, including non-deterministic suboptimal behavior, instruction-following errors, and high sensitivity to prompt specification. At the same time, the architecture is flexible: transfer to a different robot and task domain largely required updating the system prompt (domain model, affordances, and action catalogue) and re-binding the same tool interface to the platform-specific skill API.

