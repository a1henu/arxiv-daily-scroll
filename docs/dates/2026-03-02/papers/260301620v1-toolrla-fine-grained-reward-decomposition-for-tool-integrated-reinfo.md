---
layout: default
title: ToolRLA: Fine-Grained Reward Decomposition for Tool-Integrated Reinforcement Learning Alignment in Domain-Specific Agents
---

# ToolRLA: Fine-Grained Reward Decomposition for Tool-Integrated Reinforcement Learning Alignment in Domain-Specific Agents
**arXiv**：[2603.01620v1](https://arxiv.org/abs/2603.01620) · [PDF](https://arxiv.org/pdf/2603.01620.pdf)  
**作者**：Pengbo Liu  

**一句话要点**：提出ToolRLA，通过细粒度奖励分解解决领域特定工具集成智能体对齐问题

**关键词**：工具集成智能体, 强化学习对齐, 细粒度奖励分解, 领域特定部署, 后训练流程

## 3 点简述
- 核心问题：现有强化学习使用粗粒度二元奖励，难以指导领域特定任务中工具调用的细微操作
- 方法要点：采用三阶段后训练流程，核心为基于乘法分解的细粒度奖励函数，评估工具调用的四个维度
- 实验或效果：在金融顾问助手部署中，任务完成率提升47%，工具调用错误降低63%，违规率降低93%

## 摘要（原文）

> Tool-integrated reasoning agents interleaving natural language deliberation with external API calls show promise for complex multi-step tasks. However, aligning such agents for high-stakes domain-specific deployment is challenging, as existing reinforcement learning uses coarse binary rewards (success/failure) that insufficiently guide nuanced tool invocation in production. We present ToolRLA, a three-stage post-training pipeline (Supervised Fine-Tuning, Group Relative Policy Optimization, Direct Preference Optimization) for domain-specific tool-integrated agents. Its core is a fine-grained reward function with multiplicative correctness decomposition, evaluating tool invocation across four dimensions: format validity, tool selection correctness, invocation efficiency, and domain constraint compliance. Multiplicative composition prioritizes correct tool selection (a prerequisite for meaningful parameter evaluation), while a large negative compliance penalty (λ=10) ensures regulatory adherence. Deployed on a real-world financial advisory copilot (80+ advisors, 1,200+ daily queries, 15+ heterogeneous APIs), ToolRLA achieves 47% higher end-to-end task completion (62% to 91%), 63% lower tool invocation error (38% to 14%), 93% lower regulatory violation (12% to 0.8%), and sub-2-second latency after three months. Ablation studies confirm fine-grained reward decomposition contributes 7 percentage points over coarse additive rewards; generalizability is validated on ToolBench and API-Bank.

