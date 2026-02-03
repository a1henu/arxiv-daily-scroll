---
layout: default
title: TIDE: Trajectory-based Diagnostic Evaluation of Test-Time Improvement in LLM Agents
---

# TIDE: Trajectory-based Diagnostic Evaluation of Test-Time Improvement in LLM Agents
**arXiv**：[2602.02196v1](https://arxiv.org/abs/2602.02196) · [PDF](https://arxiv.org/pdf/2602.02196.pdf)  
**作者**：Hang Yan, Xinyu Che, Fangzhi Xu, Qiushi Sun, Zichen Ding, Kanzhi Cheng, Jian Zhang, Tao Qin, Jun Liu, Qika Lin  

**一句话要点**：提出TIDE框架以诊断LLM代理在测试时改进中的轨迹动态与约束机制

**关键词**：LLM代理, 测试时改进, 轨迹诊断, 评估框架, 交互动态, 工作记忆

## 3 点简述
- 核心问题：现有评估指标无法捕捉LLM代理测试时改进的任务优化效率、行为适应和工作记忆效用
- 方法要点：TIDE将测试时改进分解为三个维度，测量任务完成动态、递归循环行为和累积记忆负担
- 实验或效果：通过多代理和环境实验，TIDE揭示性能提升需优化代理与环境交互动态，而非仅扩展内部推理

## 摘要（原文）

> Recent advances in autonomous LLM agents demonstrate their ability to improve performance through iterative interaction with the environment. We define this paradigm as Test-Time Improvement (TTI). However, the mechanisms under how and why TTI succeed or fail remain poorly understood, and existing evaluation metrics fail to capture their task optimization efficiency, behavior adaptation after erroneous actions, and the specific utility of working memory for task completion. To address these gaps, we propose Test-time Improvement Diagnostic Evaluation (TIDE), an agent-agnostic and environment-agnostic framework that decomposes TTI into three comprehensive and interconnected dimensions. The framework measures (1) the overall temporal dynamics of task completion and (2) identifies whether performance is primarily constrained by recursive looping behaviors or (3) by burdensome accumulated memory. Through extensive experiments across diverse agents and environments, TIDE highlights that improving agent performance requires more than scaling internal reasoning, calling for explicitly optimizing the interaction dynamics between the agent and the environment.

