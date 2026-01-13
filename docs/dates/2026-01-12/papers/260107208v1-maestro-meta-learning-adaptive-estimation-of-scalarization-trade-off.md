---
layout: default
title: MAESTRO: Meta-learning Adaptive Estimation of Scalarization Trade-offs for Reward Optimization
---

# MAESTRO: Meta-learning Adaptive Estimation of Scalarization Trade-offs for Reward Optimization
**arXiv**：[2601.07208v1](https://arxiv.org/abs/2601.07208) · [PDF](https://arxiv.org/pdf/2601.07208.pdf)  
**作者**：Yang Zhao, Hepeng Wang, Xiao Ding, Yangou Ouyang, Bibo Cai, Kai Xiong, Jinglong Gao, Zhouhao Sun, Li Du, Bing Qin, Ting Liu  

**一句话要点**：提出MAESTRO以解决开放域生成中多目标奖励动态标量化问题

**关键词**：奖励优化, 元学习, 动态标量化, 开放域生成, 上下文赌博机, GRPO扩展

## 3 点简述
- 核心问题：GRPO在开放域中因多目标冲突和静态标量化而受限
- 方法要点：引入元认知层，将标量化建模为动态潜在策略，利用隐藏状态感知任务优先级
- 实验或效果：在七个基准上优于单奖励和静态多目标基线，保持GRPO效率优势

## 摘要（原文）

> Group-Relative Policy Optimization (GRPO) has emerged as an efficient paradigm for aligning Large Language Models (LLMs), yet its efficacy is primarily confined to domains with verifiable ground truths. Extending GRPO to open-domain settings remains a critical challenge, as unconstrained generation entails multi-faceted and often conflicting objectives - such as creativity versus factuality - where rigid, static reward scalarization is inherently suboptimal. To address this, we propose MAESTRO (Meta-learning Adaptive Estimation of Scalarization Trade-offs for Reward Optimization), which introduces a meta-cognitive orchestration layer that treats reward scalarization as a dynamic latent policy, leveraging the model's terminal hidden states as a semantic bottleneck to perceive task-specific priorities. We formulate this as a contextual bandit problem within a bi-level optimization framework, where a lightweight Conductor network co-evolves with the policy by utilizing group-relative advantages as a meta-reward signal. Across seven benchmarks, MAESTRO consistently outperforms single-reward and static multi-objective baselines, while preserving the efficiency advantages of GRPO, and in some settings even reducing redundant generation.

