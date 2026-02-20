---
layout: default
title: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning
---

# Phase-Aware Mixture of Experts for Agentic Reinforcement Learning
**arXiv**：[2602.17038v1](https://arxiv.org/abs/2602.17038) · [PDF](https://arxiv.org/pdf/2602.17038.pdf)  
**作者**：Shengtian Yang, Yu Li, Shuo He, Yewen Li, Qingpeng Cai, Peng Jiang, Lei Feng  

**一句话要点**：提出相位感知专家混合以解决强化学习中简单任务主导参数的问题

**关键词**：强化学习, 专家混合, 相位感知, 策略网络, 任务专业化

## 3 点简述
- 现有强化学习方法使用单一策略网络，导致简单任务占用过多参数，复杂任务能力不足
- 引入相位感知专家混合，通过轻量级相位路由器学习潜在相位边界，分配时间一致的任务给专家
- 实验证明该方法能有效提升专家专业化，增强复杂任务处理能力

## 摘要（原文）

> Reinforcement learning (RL) has equipped LLM agents with a strong ability to solve complex tasks. However, existing RL methods normally use a \emph{single} policy network, causing \emph{simplicity bias} where simple tasks occupy most parameters and dominate gradient updates, leaving insufficient capacity for complex tasks. A plausible remedy could be employing the Mixture-of-Experts (MoE) architecture in the policy network, as MoE allows different parameters (experts) to specialize in different tasks, preventing simple tasks from dominating all parameters. However, a key limitation of traditional MoE is its token-level routing, where the router assigns each token to specialized experts, which fragments phase-consistent patterns into scattered expert assignments and thus undermines expert specialization. In this paper, we propose \textbf{Phase-Aware Mixture of Experts (PA-MoE)}. It first features a lightweight \emph{phase router} that learns latent phase boundaries directly from the RL objective without pre-defining phase categories. Then, the phase router allocates temporally consistent assignments to the same expert, allowing experts to preserve phase-specific expertise. Experimental results demonstrate the effectiveness of our proposed PA-MoE.

