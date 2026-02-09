---
layout: default
title: Reinforcement Learning-Based Dynamic Management of Structured Parallel Farm Skeletons on Serverless Platforms
---

# Reinforcement Learning-Based Dynamic Management of Structured Parallel Farm Skeletons on Serverless Platforms
**arXiv**：[2602.06555v1](https://arxiv.org/abs/2602.06555) · [PDF](https://arxiv.org/pdf/2602.06555.pdf)  
**作者**：Lanpei Li, Massimo Coppola, Malio Li, Valerio Besozzi, Jack Bell, Vincenzo Lomonaco  

**一句话要点**：提出基于强化学习的无服务器平台结构化并行Farm骨架动态管理框架，以提升性能与弹性。

**关键词**：无服务器计算, 并行处理骨架, 强化学习, 自动扩缩容, 性能管理, OpenFaaS平台

## 3 点简述
- 核心问题：在无服务器平台上动态管理Farm并行骨架，实现高性能与弹性，同时保持可编程性。
- 方法要点：结合可重用Farm模板与基于Gymnasium的监控控制层，利用强化学习策略进行QoS感知的自动扩缩容。
- 实验或效果：在OpenFaaS上评估强化学习策略，相比基于模型的反应式管理，能更好适应平台限制，提升QoS并保持资源效率。

## 摘要（原文）

> We present a framework for dynamic management of structured parallel processing skeletons on serverless platforms. Our goal is to bring HPC-like performance and resilience to serverless and continuum environments while preserving the programmability benefits of skeletons. As a first step, we focus on the well known Farm pattern and its implementation on the open-source OpenFaaS platform, treating autoscaling of the worker pool as a QoS-aware resource management problem. The framework couples a reusable farm template with a Gymnasium-based monitoring and control layer that exposes queue, timing, and QoS metrics to both reactive and learning-based controllers. We investigate the effectiveness of AI-driven dynamic scaling for managing the farm's degree of parallelism via the scalability of serverless functions on OpenFaaS. In particular, we discuss the autoscaling model and its training, and evaluate two reinforcement learning (RL) policies against a baseline of reactive management derived from a simple farm performance model. Our results show that AI-based management can better accommodate platform-specific limitations than purely model-based performance steering, improving QoS while maintaining efficient resource usage and stable scaling behaviour.

