---
layout: default
title: FATE: Closed-Loop Feasibility-Aware Task Generation with Active Repair for Physically Grounded Robotic Curricula
---

# FATE: Closed-Loop Feasibility-Aware Task Generation with Active Repair for Physically Grounded Robotic Curricula
**arXiv**：[2603.01505v1](https://arxiv.org/abs/2603.01505) · [PDF](https://arxiv.org/pdf/2603.01505.pdf)  
**作者**：Bingchuan Wei, Bingqi Huang, Jingheng Ma, Zeyu zhang, Sen Cui  

**一句话要点**：提出FATE框架，通过闭环验证与主动修复生成物理可行的机器人任务课程

**关键词**：机器人任务生成, 物理可行性验证, 闭环系统, 主动修复, 具身智能

## 3 点简述
- 核心问题：现有生成方法常产生语言连贯但物理不可行的任务目标
- 方法要点：嵌入具身代理进行迭代验证，并主动修复不可行任务
- 实验或效果：实验显示FATE能生成多样化任务，显著降低执行失败率

## 摘要（原文）

> Recent breakthroughs in generative simulation have harnessed Large Language Models (LLMs) to generate diverse robotic task curricula, yet these open-loop paradigms frequently produce linguistically coherent but physically infeasible goals, stemming from ungrounded task specifications or misaligned objective formulations. To address this critical limitation, we propose FATE (Feasibility-Aware Task gEneration), a closed-loop, self-correcting framework that reimagines task generation as an iterative validation-and-refinement process. Unlike conventional methods that decouple generation and verification into discrete stages, FATE embeds a generalist embodied agent directly into the generation loop to proactively guarantee the physical groundedness of the resulting curriculum. FATE instantiates a sequential auditing pipeline: it first validates static scene attributes (e.g., object affordances, layout compatibility) and subsequently verifies execution feasibility via simulated embodied interaction. Critical to its performance, upon detecting an infeasible task, FATE deploys an active repair module that autonomously adapts scene configurations or policy specifications, converting unworkable proposals into physically valid task instances. Extensive experiments validate that FATE generates semantically diverse, physically grounded task curricula while achieving a substantial reduction in execution failure rates relative to state-of-the-art generative baselines.

