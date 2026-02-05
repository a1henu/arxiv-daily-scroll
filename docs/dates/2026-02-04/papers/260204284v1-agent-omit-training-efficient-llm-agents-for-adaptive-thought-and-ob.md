---
layout: default
title: Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic Reinforcement Learning
---

# Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic Reinforcement Learning
**arXiv**：[2602.04284v1](https://arxiv.org/abs/2602.04284) · [PDF](https://arxiv.org/pdf/2602.04284.pdf)  
**作者**：Yansong Ning, Jun Fang, Naiqiang Tan, Hao Liu  

**一句话要点**：提出Agent-Omit训练框架，通过智能强化学习使LLM代理自适应省略冗余思维和观察以提高效率。

**关键词**：LLM代理, 自适应省略, 智能强化学习, 效率优化, 多轮交互

## 3 点简述
- 核心问题：现有方法忽视多轮交互中思维必要性和观察效用的动态变化，导致效率低下。
- 方法要点：结合冷启动数据微调和省略感知的智能强化学习，包括双采样机制和定制奖励。
- 实验或效果：在五个基准测试中，Agent-Omit-8B性能媲美前沿代理，并在效率-效果权衡上优于七种高效方法。

## 摘要（原文）

> Managing agent thought and observation during multi-turn agent-environment interactions is an emerging strategy to improve agent efficiency. However, existing studies treat the entire interaction trajectories equally, overlooking the thought necessity and observation utility varies across turns. To this end, we first conduct quantitative investigations into how thought and observation affect agent effectiveness and efficiency. Based on our findings, we propose Agent-Omit, a unified training framework that empowers LLM agents to adaptively omit redundant thoughts and observations. Specifically, we first synthesize a small amount of cold-start data, including both single-turn and multi-turn omission scenarios, to fine-tune the agent for omission behaviors. Furthermore, we introduce an omit-aware agentic reinforcement learning approach, incorporating a dual sampling mechanism and a tailored omission reward to incentivize the agent's adaptive omission capability. Theoretically, we prove that the deviation of our omission policy is upper-bounded by KL-divergence. Experimental results on five agent benchmarks show that our constructed Agent-Omit-8B could obtain performance comparable to seven frontier LLM agent, and achieve the best effectiveness-efficiency trade-off than seven efficient LLM agents methods. Our code and data are available at https://github.com/usail-hkust/Agent-Omit.

