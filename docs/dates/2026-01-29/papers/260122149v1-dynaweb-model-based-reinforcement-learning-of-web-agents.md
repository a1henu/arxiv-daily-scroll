---
layout: default
title: DynaWeb: Model-Based Reinforcement Learning of Web Agents
---

# DynaWeb: Model-Based Reinforcement Learning of Web Agents
**arXiv**：[2601.22149v1](https://arxiv.org/abs/2601.22149) · [PDF](https://arxiv.org/pdf/2601.22149.pdf)  
**作者**：Hang Ding, Peidong Liu, Junqiao Wang, Ziwei Ji, Meng Cao, Rongzhao Zhang, Lynn Ai, Eric Yang, Tianyu Shi, Lei Yu  

**一句话要点**：提出DynaWeb框架，通过基于模型的强化学习训练网络代理，以解决在线交互效率低和风险高的问题。

**关键词**：网络代理, 基于模型的强化学习, 世界模型, 模拟交互, 样本效率

## 3 点简述
- 核心问题：训练网络代理时，与实时互联网交互效率低、成本高且风险大。
- 方法要点：学习网络世界模型预测网页表示，用于模拟交互和策略生成，结合专家轨迹提升稳定性。
- 实验或效果：在WebArena和WebVoyager基准测试中显著提升开源网络代理模型的性能。

## 摘要（原文）

> The development of autonomous web agents, powered by Large Language Models (LLMs) and reinforcement learning (RL), represents a significant step towards general-purpose AI assistants. However, training these agents is severely hampered by the challenges of interacting with the live internet, which is inefficient, costly, and fraught with risks. Model-based reinforcement learning (MBRL) offers a promising solution by learning a world model of the environment to enable simulated interaction. This paper introduces DynaWeb, a novel MBRL framework that trains web agents through interacting with a web world model trained to predict naturalistic web page representations given agent actions. This model serves as a synthetic web environment where an agent policy can dream by generating vast quantities of rollout action trajectories for efficient online reinforcement learning. Beyond free policy rollouts, DynaWeb incorporates real expert trajectories from training data, which are randomly interleaved with on-policy rollouts during training to improve stability and sample efficiency. Experiments conducted on the challenging WebArena and WebVoyager benchmarks demonstrate that DynaWeb consistently and significantly improves the performance of state-of-the-art open-source web agent models. Our findings establish the viability of training web agents through imagination, offering a scalable and efficient way to scale up online agentic RL.

