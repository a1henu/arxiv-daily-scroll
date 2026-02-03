---
layout: default
title: FlowSteer: Interactive Agentic Workflow Orchestration via End-to-End Reinforcement Learning
---

# FlowSteer: Interactive Agentic Workflow Orchestration via End-to-End Reinforcement Learning
**arXiv**：[2602.01664v1](https://arxiv.org/abs/2602.01664) · [PDF](https://arxiv.org/pdf/2602.01664.pdf)  
**作者**：Mingda Zhang, Haoran Luo, Tiesunlong Shen, Qika Lin, Xiaoying Tang, Rui Mao, Erik Cambria  

**一句话要点**：提出FlowSteer框架，通过端到端强化学习解决智能体工作流编排的自动化挑战。

**关键词**：智能体工作流编排, 端到端强化学习, 交互式自动化, 策略优化, 插件化框架

## 3 点简述
- 核心问题：现有工作流编排依赖人工、特定算子或大模型，奖励信号稀疏，成本高。
- 方法要点：采用轻量策略模型与可执行画布环境，通过多轮交互自动化编排，支持插件化算子库和可替换大模型后端。
- 实验或效果：在12个数据集上显著优于基线，验证了Canvas Workflow Relative Policy Optimization的有效性。

## 摘要（原文）

> In recent years, a variety of powerful agentic workflows have been applied to solve a wide range of human problems. However, existing workflow orchestration still faces key challenges, including high manual cost, reliance on specific operators/large language models (LLMs), and sparse reward signals. To address these challenges, we propose FlowSteer, an end-to-end reinforcement learning framework that takes a lightweight policy model as the agent and an executable canvas environment, automating workflow orchestration through multi-turn interaction. In this process, the policy model analyzes execution states and selects editing actions, while the canvas executes operators and returns feedback for iterative refinement. Moreover, FlowSteer provides a plug-and-play framework that supports diverse operator libraries and interchangeable LLM backends. To effectively train this interaction paradigm, we propose Canvas Workflow Relative Policy Optimization (CWRPO), which introduces diversity-constrained rewards with conditional release to stabilize learning and suppress shortcut behaviors. Experimental results on twelve datasets show that FlowSteer significantly outperforms baselines across various tasks.

