---
layout: default
title: Latent-DARM: Bridging Discrete Diffusion And Autoregressive Models For Reasoning
---

# Latent-DARM: Bridging Discrete Diffusion And Autoregressive Models For Reasoning
**arXiv**：[2603.09184v1](https://arxiv.org/abs/2603.09184) · [PDF](https://arxiv.org/pdf/2603.09184.pdf)  
**作者**：Lina Berrayana, Ahmed Heakl, Abdullah Sohail, Thomas Hofmann, Salman Khan, Wei Chen  

**一句话要点**：提出Latent-DARM框架，通过潜在空间通信桥接离散扩散与自回归模型以增强多智能体推理能力。

**关键词**：多智能体系统, 离散扩散模型, 自回归模型, 潜在空间通信, 推理能力, 异构模型协作

## 3 点简述
- 核心问题：自回归模型限制全局推理与计划修订，离散扩散模型文本流畅性不足，阻碍异构模型协作。
- 方法要点：设计潜在空间通信框架，使离散扩散模型作为规划器、自回归模型作为执行器协同工作。
- 实验或效果：在数学、科学和常识推理基准上提升准确性，如DART-5从27.0%到36.0%，AIME2024从0.0%到14.0%。

## 摘要（原文）

> Most multi-agent systems rely exclusively on autoregressive language models (ARMs) that are based on sequential generation. Although effective for fluent text, ARMs limit global reasoning and plan revision. On the other hand, Discrete Diffusion Language Models (DDLMs) enable non-sequential, globally revisable generation and have shown strong planning capabilities, but their limited text fluency hinders direct collaboration with ARMs. We introduce Latent-DARM, a latent-space communication framework bridging DDLM (planners) and ARM (executors), maximizing collaborative benefits. Across mathematical, scientific, and commonsense reasoning benchmarks, Latent-DARM outperforms text-based interfaces on average, improving accuracy from 27.0% to 36.0% on DART-5 and from 0.0% to 14.0% on AIME2024. Latent-DARM approaches the results of state-of-the-art reasoning models while using less than 2.2% of its token budget. This work advances multi-agent collaboration among agents with heterogeneous models.

