---
layout: default
title: EchoTrail-GUI: Building Actionable Memory for GUI Agents via Critic-Guided Self-Exploration
---

# EchoTrail-GUI: Building Actionable Memory for GUI Agents via Critic-Guided Self-Exploration
**arXiv**：[2512.19396v1](https://arxiv.org/abs/2512.19396) · [PDF](https://arxiv.org/pdf/2512.19396.pdf)  
**作者**：Runze Li, Yuwen Zhai, Bo Xu, LiWu Xu, Nian Shi, Wei Zhang, Ran Lin, Liang Wang  

**一句话要点**：提出EchoTrail-GUI框架，通过批评引导的自探索为GUI代理构建可操作记忆以解决任务孤立问题。

**关键词**：GUI代理, 记忆增强, 自探索学习, 轨迹检索, 自动化推理, 视觉语言模型

## 3 点简述
- 核心问题：GUI代理缺乏从过去成功中系统学习的能力，导致性能不佳和重复错误。
- 方法要点：框架包括经验探索、记忆注入和GUI任务推理三阶段，自动化构建和利用任务轨迹记忆。
- 实验或效果：在Android World和AndroidLab基准测试中显著提升任务成功率和操作效率。

## 摘要（原文）

> Contemporary GUI agents, while increasingly capable due to advances in Large Vision-Language Models (VLMs), often operate with a critical limitation: they treat each task in isolation, lacking a mechanism to systematically learn from past successes. This digital ''amnesia'' results in sub-optimal performance, repeated errors, and poor generalization to novel challenges. To bridge this gap, we introduce EchoTrail-GUI, a novel framework designed to mimic human-like experiential learning by equipping agents with a dynamic, accessible memory. Our framework operates in three distinct stages. First, during Experience Exploration, an agent autonomously interacts with GUI environments to build a curated database of successful task trajectories, validated by a reward model. Crucially, the entire knowledge base construction is thus fully automated, requiring no human supervision. Second, in the Memory Injection stage, upon receiving a new task, our system efficiently retrieves the most relevant past trajectories to serve as actionable ''memories''. Finally, during GUI Task Inference, these memories are injected as in-context guidance to inform the agent's reasoning and decision-making process. We demonstrate the efficacy of our approach on benchmarks including Android World and AndroidLab. The results show that EchoTrail-GUI significantly improves the task success rate and operational efficiency of baseline agents, validating the power of structured memory in creating more robust and intelligent GUI automation.

