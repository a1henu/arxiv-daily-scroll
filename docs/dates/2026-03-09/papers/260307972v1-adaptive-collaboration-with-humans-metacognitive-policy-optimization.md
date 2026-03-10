---
layout: default
title: Adaptive Collaboration with Humans: Metacognitive Policy Optimization for Multi-Agent LLMs with Continual Learning
---

# Adaptive Collaboration with Humans: Metacognitive Policy Optimization for Multi-Agent LLMs with Continual Learning
**arXiv**：[2603.07972v1](https://arxiv.org/abs/2603.07972) · [PDF](https://arxiv.org/pdf/2603.07972.pdf)  
**作者**：Wei Yang, Defu Cao, Jiacheng Pang, Muyan Weng, Yan Liu  

**一句话要点**：提出人机协同多智能体框架HILA，通过元认知策略优化解决静态知识限制问题。

**关键词**：人机协同, 多智能体系统, 元认知策略, 持续学习, 策略优化

## 3 点简述
- 核心问题：多智能体系统受限于预训练模型的静态知识，在未知任务中易集体失败。
- 方法要点：引入双循环策略优化，内循环优化延迟决策，外循环通过持续学习增强推理能力。
- 实验效果：在数学和问题解决基准测试中，HILA持续优于先进多智能体系统。

## 摘要（原文）

> While scaling individual Large Language Models (LLMs) has delivered remarkable progress, the next frontier lies in scaling collaboration through multi-agent systems (MAS). However, purely autonomous MAS remain ''closed-world'' systems, constrained by the static knowledge horizon of pre-trained models. This limitation makes them brittle on tasks requiring knowledge beyond training data, often leading to collective failure under novel challenges. To address this, we propose the Human-In-the-Loop Multi-Agent Collaboration (HILA) framework, a principled paradigm for human--agent collaboration. HILA trains agents to learn a metacognitive policy that governs when to solve problems autonomously and when to defer to a human expert. To operationalize this policy, we introduce Dual-Loop Policy Optimization, which disentangles immediate decision-making from long-term capability growth. The inner loop applies Group Relative Policy Optimization (GRPO) with a cost-aware reward to optimize deferral decisions, while the outer loop implements continual learning, transforming expert feedback into high-quality supervised signals that strengthen the agent's reasoning ability. Experiments on challenging mathematical and problem-solving benchmarks show that HILA, equipped with Dual-Loop Policy Optimization, consistently outperforms advanced MAS, establishing a principled foundation for collaborative and continually improving agentic systems.

