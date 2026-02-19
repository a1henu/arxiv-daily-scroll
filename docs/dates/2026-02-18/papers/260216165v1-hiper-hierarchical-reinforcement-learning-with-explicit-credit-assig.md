---
layout: default
title: HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents
---

# HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents
**arXiv**：[2602.16165v1](https://arxiv.org/abs/2602.16165) · [PDF](https://arxiv.org/pdf/2602.16165.pdf)  
**作者**：Jiangweizhi Peng, Yuanxin Liu, Ruida Zhou, Charles Fleming, Zhaoran Wang, Alfredo Garcia, Mingyi Hong  

**一句话要点**：提出HiPER分层强化学习框架，通过显式信用分配解决大语言模型代理在稀疏奖励长时任务中的训练挑战。

**关键词**：分层强化学习, 信用分配, 大语言模型代理, 长时任务, 稀疏奖励, 多轮决策

## 3 点简述
- 核心问题：稀疏和延迟奖励下，大语言模型代理在长时多轮决策任务中面临信用分配困难，导致优化不稳定。
- 方法要点：HiPER将策略分解为高层规划器和低层执行器，引入分层优势估计技术，显式分配信用以降低方差。
- 实验或效果：在ALFWorld和WebShop基准上达到最先进性能，尤其在依赖多个子任务的长时任务中提升显著。

## 摘要（原文）

> Training LLMs as interactive agents for multi-turn decision-making remains challenging, particularly in long-horizon tasks with sparse and delayed rewards, where agents must execute extended sequences of actions before receiving meaningful feedback. Most existing reinforcement learning (RL) approaches model LLM agents as flat policies operating at a single time scale, selecting one action at each turn. In sparse-reward settings, such flat policies must propagate credit across the entire trajectory without explicit temporal abstraction, which often leads to unstable optimization and inefficient credit assignment.
>   We propose HiPER, a novel Hierarchical Plan-Execute RL framework that explicitly separates high-level planning from low-level execution. HiPER factorizes the policy into a high-level planner that proposes subgoals and a low-level executor that carries them out over multiple action steps. To align optimization with this structure, we introduce a key technique called hierarchical advantage estimation (HAE), which carefully assigns credit at both the planning and execution levels. By aggregating returns over the execution of each subgoal and coordinating updates across the two levels, HAE provides an unbiased gradient estimator and provably reduces variance compared to flat generalized advantage estimation.
>   Empirically, HiPER achieves state-of-the-art performance on challenging interactive benchmarks, reaching 97.4\% success on ALFWorld and 83.3\% on WebShop with Qwen2.5-7B-Instruct (+6.6\% and +8.3\% over the best prior method), with especially large gains on long-horizon tasks requiring multiple dependent subtasks. These results highlight the importance of explicit hierarchical decomposition for scalable RL training of multi-turn LLM agents.

