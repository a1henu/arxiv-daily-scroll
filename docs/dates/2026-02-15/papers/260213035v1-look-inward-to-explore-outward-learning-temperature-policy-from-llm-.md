---
layout: default
title: Look Inward to Explore Outward: Learning Temperature Policy from LLM Internal States via Hierarchical RL
---

# Look Inward to Explore Outward: Learning Temperature Policy from LLM Internal States via Hierarchical RL
**arXiv**：[2602.13035v1](https://arxiv.org/abs/2602.13035) · [PDF](https://arxiv.org/pdf/2602.13035.pdf)  
**作者**：Yixiao Zhou, Yang Li, Dongzhou Cheng, Hehe Fan, Yu Cheng  

**一句话要点**：提出Introspective LLM框架，通过分层强化学习从LLM内部状态学习温度策略以优化解码探索。

**关键词**：强化学习, 大语言模型, 温度策略, 分层强化学习, 解码策略, 数学推理

## 3 点简述
- 核心问题：现有方法依赖静态或启发式温度，与任务奖励解耦，影响探索-利用平衡。
- 方法要点：基于分层强化学习，模型根据隐藏状态选择温度，并与令牌策略联合优化。
- 实验或效果：在数学推理基准上，学习到的温度策略优于固定和启发式基线，展现可解释探索行为。

## 摘要（原文）

> Reinforcement Learning from Verifiable Rewards (RLVR) trains large language models (LLMs) from sampled trajectories, making decoding strategy a core component of learning rather than a purely inference-time choice. Sampling temperature directly controls the exploration--exploitation trade-off by modulating policy entropy, yet existing methods rely on static values or heuristic adaptations that are decoupled from task-level rewards. We propose Introspective LLM, a hierarchical reinforcement learning framework that learns to control sampling temperature during generation. At each decoding step, the model selects a temperature based on its hidden state and samples the next token from the resulting distribution. Temperature and token policies are jointly optimized from downstream rewards using a coordinate ascent scheme. Experiments on mathematical reasoning benchmarks show that learned temperature policies outperform fixed and heuristic baselines, while exhibiting interpretable exploration behaviors aligned with reasoning uncertainty.

