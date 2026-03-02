---
layout: default
title: RUMAD: Reinforcement-Unifying Multi-Agent Debate
---

# RUMAD: Reinforcement-Unifying Multi-Agent Debate
**arXiv**：[2602.23864v1](https://arxiv.org/abs/2602.23864) · [PDF](https://arxiv.org/pdf/2602.23864.pdf)  
**作者**：Chao Wang, Han Lin, Huaze Tang, Huijing Lin, Wenbo Ding  

**一句话要点**：提出RUMAD框架，通过强化学习动态控制多智能体辩论的通信拓扑以优化准确性和效率。

**关键词**：多智能体辩论, 强化学习, 动态通信拓扑, 计算效率优化, 零样本泛化

## 3 点简述
- 核心问题：现有多智能体辩论方法难以同时优化准确性、共识形成和计算效率，静态拓扑缺乏适应性，外部协调可能引入偏见。
- 方法要点：使用强化学习训练控制器，基于内容无关的观察动态调整通信图边权重，结合多目标奖励和双阈值机制。
- 实验或效果：在MMLU等基准上，RUMAD减少80%以上token成本，提升推理准确性，并展示零样本泛化能力。

## 摘要（原文）

> Multi-agent debate (MAD) systems leverage collective intelligence to enhance reasoning capabilities, yet existing approaches struggle to simultaneously optimize accuracy, consensus formation, and computational efficiency. Static topology methods lack adaptability to task complexity variations, while external LLM-based coordination risks introducing privileged knowledge that compromises debate neutrality. This work presents RUMAD (Reinforcement-Unifying Multi-Agent Debate), a novel framework that formulates dynamic communication topology control in MAD as a reinforcement learning (RL) problem.
>   RUMAD employs a content-agnostic observation scheme that captures high-level debate dynamics avoiding access to raw agent reasoning content. RUMAD uses a multi-objective reward to model solution quality, cohesion and efficiency. A PPO-trained controller dynamically adjusts edge weights in the communication graph, while a dual-threshold mechanism enables fine-grained control over both agent activation and information visibility.
>   Experimental evaluation across MMLU, GSM8K, and GPQA benchmarks demonstrates that RUMAD achieves substantial efficiency gains, reducing token costs by over 80\%, while still improving reasoning accuracy compared to single LLM model and multiple MAD baselines. Notably, RUMAD trained exclusively on MMLU exhibits robust zero-shot generalization to out-of-domain (OOD) tasks, indicating that the learned communication strategies capture task-independent principles of effective multi-agent coordination. These results establish RUMAD as a efficient and robust approach for deploying multi-agent reasoning application with practical resource constraints.

