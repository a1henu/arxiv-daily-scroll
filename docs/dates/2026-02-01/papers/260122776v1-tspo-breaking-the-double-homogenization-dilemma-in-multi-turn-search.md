---
layout: default
title: TSPO: Breaking the Double Homogenization Dilemma in Multi-turn Search Policy Optimization
---

# TSPO: Breaking the Double Homogenization Dilemma in Multi-turn Search Policy Optimization
**arXiv**：[2601.22776v1](https://arxiv.org/abs/2601.22776) · [PDF](https://arxiv.org/pdf/2601.22776.pdf)  
**作者**：Shichao Ma, Zhiyuan Ma, Ming Yang, Xiaofan Li, Xing Wu, Jintao Du, Yu Cheng, Weiqiang Wang, Qiliang Liu, Zhengyang Zhou, Yang Wang  

**一句话要点**：提出TSPO以解决多轮搜索策略优化中的双重同质化困境

**关键词**：多轮工具集成推理, 强化学习优化, 过程级奖励, 大语言模型, 搜索增强推理

## 3 点简述
- 核心问题：现有RL框架依赖稀疏结果奖励，导致过程同质化和组内同质化。
- 方法要点：引入首次出现潜在奖励机制，分配部分奖励到正确答案首次出现的步骤。
- 实验或效果：在Qwen2.5模型上平均性能提升24%和13.6%，优于基线方法。

## 摘要（原文）

> Multi-turn tool-integrated reasoning enables Large Language Models (LLMs) to solve complex tasks through iterative information retrieval. However, current reinforcement learning (RL) frameworks for search-augmented reasoning predominantly rely on sparse outcome-level rewards, leading to a "Double Homogenization Dilemma." This manifests as (1) Process homogenization, where the thinking, reasoning, and tooling involved in generation are ignored. (2) Intra-group homogenization, coarse-grained outcome rewards often lead to inefficiencies in intra-group advantage estimation with methods like Group Relative Policy Optimization (GRPO) during sampling. To address this, we propose Turn-level Stage-aware Policy Optimization (TSPO). TSPO introduces the First-Occurrence Latent Reward (FOLR) mechanism, allocating partial rewards to the step where the ground-truth answer first appears, thereby preserving process-level signals and increasing reward variance within groups without requiring external reward models or any annotations. Extensive experiments demonstrate that TSPO significantly outperforms state-of-the-art baselines, achieving average performance gains of 24% and 13.6% on Qwen2.5-3B and 7B models, respectively.

