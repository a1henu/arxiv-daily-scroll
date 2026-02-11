---
layout: default
title: Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning
---

# Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning
**arXiv**：[2602.10090v1](https://arxiv.org/abs/2602.10090) · [PDF](https://arxiv.org/pdf/2602.10090.pdf)  
**作者**：Zhaoyang Wang, Canwen Xu, Boyi Liu, Yite Wang, Siwei Han, Zhewei Yao, Huaxiu Yao, Yuxiong He  

**一句话要点**：提出Agent World Model以解决智能体强化学习中环境多样性与可靠性不足的问题。

**关键词**：智能体强化学习, 合成环境生成, 工具使用, 泛化能力, 代码驱动环境

## 3 点简述
- 核心问题：智能体训练受限于缺乏多样且可靠的环境，难以扩展。
- 方法要点：构建完全合成的代码驱动环境生成管道，支持大规模工具交互和数据库状态。
- 实验或效果：在合成环境中训练智能体，实现强泛化能力，优于基准特定环境。

## 摘要（原文）

> Recent advances in large language model (LLM) have empowered autonomous agents to perform complex tasks that require multi-turn interactions with tools and environments. However, scaling such agent training is limited by the lack of diverse and reliable environments. In this paper, we propose Agent World Model (AWM), a fully synthetic environment generation pipeline. Using this pipeline, we scale to 1,000 environments covering everyday scenarios, in which agents can interact with rich toolsets (35 tools per environment on average) and obtain high-quality observations. Notably, these environments are code-driven and backed by databases, providing more reliable and consistent state transitions than environments simulated by LLMs. Moreover, they enable more efficient agent interaction compared with collecting trajectories from realistic environments. To demonstrate the effectiveness of this resource, we perform large-scale reinforcement learning for multi-turn tool-use agents. Thanks to the fully executable environments and accessible database states, we can also design reliable reward functions. Experiments on three benchmarks show that training exclusively in synthetic environments, rather than benchmark-specific ones, yields strong out-of-distribution generalization. The code is available at https://github.com/Snowflake-Labs/agent-world-model.

