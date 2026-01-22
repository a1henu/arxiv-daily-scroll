---
layout: default
title: MAS-Orchestra: Understanding and Improving Multi-Agent Reasoning Through Holistic Orchestration and Controlled Benchmarks
---

# MAS-Orchestra: Understanding and Improving Multi-Agent Reasoning Through Holistic Orchestration and Controlled Benchmarks
**arXiv**：[2601.14652v1](https://arxiv.org/abs/2601.14652) · [PDF](https://arxiv.org/pdf/2601.14652.pdf)  
**作者**：Zixuan Ke, Yifei Ming, Austin Xu, Ryan Chin, Xuan-Phi Nguyen, Prathyusha Jwalapuram, Semih Yavuz, Caiming Xiong, Shafiq Joty  

**一句话要点**：提出MAS-Orchestra框架与MASBENCH基准，以提升多智能体系统推理能力与理解其适用性

**关键词**：多智能体系统, 智能体编排, 强化学习, 基准测试, 全局推理, 任务分析

## 3 点简述
- 核心问题：现有自动多智能体系统设计方法因顺序执行和缺乏全局推理而效果不佳，且效益不确定
- 方法要点：将多智能体编排建模为函数调用强化学习问题，通过整体编排一次性生成系统，并引入MASBENCH基准分析任务结构
- 实验或效果：在数学推理、多跳问答等公开基准上实现一致改进，揭示多智能体效益取决于任务结构和智能体能力

## 摘要（原文）

> While multi-agent systems (MAS) promise elevated intelligence through coordination of agents, current approaches to automatic MAS design under-deliver. Such shortcomings stem from two key factors: (1) methodological complexity - agent orchestration is performed using sequential, code-level execution that limits global system-level holistic reasoning and scales poorly with agent complexity - and (2) efficacy uncertainty - MAS are deployed without understanding if there are tangible benefits compared to single-agent systems (SAS). We propose MAS-Orchestra, a training-time framework that formulates MAS orchestration as a function-calling reinforcement learning problem with holistic orchestration, generating an entire MAS at once. In MAS-Orchestra, complex, goal-oriented sub-agents are abstracted as callable functions, enabling global reasoning over system structure while hiding internal execution details. To rigorously study when and why MAS are beneficial, we introduce MASBENCH, a controlled benchmark that characterizes tasks along five axes: Depth, Horizon, Breadth, Parallel, and Robustness. Our analysis reveals that MAS gains depend critically on task structure, verification protocols, and the capabilities of both orchestrator and sub-agents, rather than holding universally. Guided by these insights, MAS-Orchestra achieves consistent improvements on public benchmarks including mathematical reasoning, multi-hop QA, and search-based QA. Together, MAS-Orchestra and MASBENCH enable better training and understanding of MAS in the pursuit of multi-agent intelligence.

