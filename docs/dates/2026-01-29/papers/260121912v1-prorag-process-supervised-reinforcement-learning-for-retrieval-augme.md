---
layout: default
title: ProRAG: Process-Supervised Reinforcement Learning for Retrieval-Augmented Generation
---

# ProRAG: Process-Supervised Reinforcement Learning for Retrieval-Augmented Generation
**arXiv**：[2601.21912v1](https://arxiv.org/abs/2601.21912) · [PDF](https://arxiv.org/pdf/2601.21912.pdf)  
**作者**：Zhao Wang, Ziliang Zhao, Zhicheng Dou  

**一句话要点**：提出ProRAG框架，通过过程监督强化学习优化检索增强生成中的长程推理任务。

**关键词**：检索增强生成, 强化学习, 过程监督, 多跳推理, 长程任务优化

## 3 点简述
- 传统基于结果的强化学习在检索增强生成中面临奖励稀疏和信用分配低效问题，导致过程幻觉。
- ProRAG集成步骤级监督，包括策略预热、过程奖励模型构建、推理细化和双粒度优势机制。
- 在五个多跳推理基准上验证了ProRAG优于基于结果和过程感知的基线，尤其在复杂长程任务中表现突出。

## 摘要（原文）

> Reinforcement learning (RL) has become a promising paradigm for optimizing Retrieval-Augmented Generation (RAG) in complex reasoning tasks. However, traditional outcome-based RL approaches often suffer from reward sparsity and inefficient credit assignment, as coarse-grained scalar rewards fail to identify specific erroneous steps within long-horizon trajectories. This ambiguity frequently leads to "process hallucinations", where models reach correct answers through flawed logic or redundant retrieval steps. Although recent process-aware approaches attempt to mitigate this via static preference learning or heuristic reward shaping, they often lack the on-policy exploration capabilities required to decouple step-level credit from global outcomes. To address these challenges, we propose ProRAG, a process-supervised reinforcement learning framework designed to integrate learned step-level supervision into the online optimization loop. Our framework consists of four stages: (1) Supervised Policy Warmup to initialize the model with a structured reasoning format; (2) construction of an MCTS-based Process Reward Model (PRM) to quantify intermediate reasoning quality; (3) PRM-Guided Reasoning Refinement to align the policy with fine-grained process preferences; and (4) Process-Supervised Reinforcement Learning with a dual-granularity advantage mechanism. By aggregating step-level process rewards with global outcome signals, ProRAG provides precise feedback for every action. Extensive experiments on five multi-hop reasoning benchmarks demonstrate that ProRAG achieves superior overall performance compared to strong outcome-based and process-aware RL baselines, particularly on complex long-horizon tasks, validating the effectiveness of fine-grained process supervision. The code and model are available at https://github.com/lilinwz/ProRAG.

