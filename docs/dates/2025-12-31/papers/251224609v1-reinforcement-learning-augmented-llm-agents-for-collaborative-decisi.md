---
layout: default
title: Reinforcement Learning-Augmented LLM Agents for Collaborative Decision Making and Performance Optimization
---

# Reinforcement Learning-Augmented LLM Agents for Collaborative Decision Making and Performance Optimization
**arXiv**：[2512.24609v1](https://arxiv.org/abs/2512.24609) · [PDF](https://arxiv.org/pdf/2512.24609.pdf)  
**作者**：Dong Qiu, Duo Xu, Limengxi Yue  

**一句话要点**：提出强化学习增强的LLM智能体框架，以解决多智能体协作决策与性能优化问题。

**关键词**：多智能体协作, 强化学习增强, Dec-POMDP建模, 集中训练分散执行, 协作决策优化

## 3 点简述
- 核心问题：LLM在多智能体环境中缺乏协作意识，难以优化全局性能。
- 方法要点：采用Dec-POMDP建模协作，结合CTDE和GRPO优化策略，平衡任务质量、速度和协调成本。
- 实验或效果：在协作写作和编码基准上，任务处理速度提升3倍，写作一致性达98.7%，编码测试通过率74.6%。

## 摘要（原文）

> Large Language Models (LLMs) perform well in language tasks but often lack collaborative awareness and struggle to optimize global performance in multi-agent settings. We present a reinforcement learning-augmented LLM agent framework that formulates cooperation as a decentralized partially observable Markov decision process (Dec-POMDP) and adopts centralized training with decentralized execution (CTDE). We introduce Group Relative Policy Optimization (GRPO) to jointly optimize agent policies with access to global signals during training, together with a simplified joint reward that balances task quality, speed, and coordination cost. On collaborative writing and coding benchmarks, our framework delivers a 3x increase in task processing speed over single-agent baselines, 98.7% structural/style consistency in writing, and a 74.6% test pass rate in coding. The approach consistently outperforms strong multi-agent LLM baselines and provides a practical path toward reliable collaboration in complex workflows.

