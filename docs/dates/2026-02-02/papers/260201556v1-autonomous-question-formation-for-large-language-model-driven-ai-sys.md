---
layout: default
title: Autonomous Question Formation for Large Language Model-Driven AI Systems
---

# Autonomous Question Formation for Large Language Model-Driven AI Systems
**arXiv**：[2602.01556v1](https://arxiv.org/abs/2602.01556) · [PDF](https://arxiv.org/pdf/2602.01556.pdf)  
**作者**：Hong Su  

**一句话要点**：提出基于人类模拟的框架，使AI系统在动态环境中自主形成问题以提升决策能力。

**关键词**：自主问题形成, 大语言模型驱动系统, 多智能体模拟, 环境感知提示, 决策过程优化

## 3 点简述
- 核心问题：现有LLM驱动系统依赖预定义任务，难以在环境变化时自主识别应解决的问题。
- 方法要点：将问题形成作为首要决策过程，整合内部驱动、环境感知和智能体间感知的提示范围。
- 实验或效果：多智能体模拟中，环境感知提示减少无进食事件，智能体间感知提示进一步降低超60%。

## 摘要（原文）

> Large language model (LLM)-driven AI systems are increasingly important for autonomous decision-making in dynamic and open environments. However, most existing systems rely on predefined tasks and fixed prompts, limiting their ability to autonomously identify what problems should be solved when environmental conditions change. In this paper, we propose a human-simulation-based framework that enables AI systems to autonomously form questions and set tasks by reasoning over their internal states, environmental observations, and interactions with other AI systems. The proposed method treats question formation as a first-class decision process preceding task selection and execution, and integrates internal-driven, environment-aware, and inter-agent-aware prompting scopes to progressively expand cognitive coverage. In addition, the framework supports learning the question-formation process from experience, allowing the system to improve its adaptability and decision quality over time. xperimental results in a multi-agent simulation environment show that environment-aware prompting significantly reduces no-eat events compared with the internal-driven baseline, and inter-agent-aware prompting further reduces cumulative no-eat events by more than 60% over a 20-day simulation, with statistically significant improvements (p < 0.05).

