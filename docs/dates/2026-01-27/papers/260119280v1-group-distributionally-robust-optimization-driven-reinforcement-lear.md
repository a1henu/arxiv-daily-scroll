---
layout: default
title: Group Distributionally Robust Optimization-Driven Reinforcement Learning for LLM Reasoning
---

# Group Distributionally Robust Optimization-Driven Reinforcement Learning for LLM Reasoning
**arXiv**：[2601.19280v1](https://arxiv.org/abs/2601.19280) · [PDF](https://arxiv.org/pdf/2601.19280.pdf)  
**作者**：Kishan Panaganti, Zhenwen Liang, Wenhao Yu, Haitao Mi, Dong Yu  

**一句话要点**：提出多对抗者组分布鲁棒优化框架，以动态适应训练分布解决大语言模型推理中的异构数据效率问题。

**关键词**：大语言模型推理, 分布鲁棒优化, 强化学习, 在线难度分类, 计算效率优化, 异构数据处理

## 3 点简述
- 核心问题：标准强化学习范式在异构、重尾推理数据中因均匀采样和固定rollout数导致计算效率低下，浪费在已解决模式上，而难问题训练不足。
- 方法要点：引入在线难度分类器动态划分提示难度组，并设计Prompt-GDRO和Rollout-GDRO两个独立游戏，分别通过乘性权重采样器和影子价格控制器优化训练分布和rollout分配。
- 实验或效果：在DAPO 14.1k数据集上使用Qwen3-Base模型验证，相比GRPO基线，Prompt-GDRO和Rollout-GDRO在pass@8准确率上平均相对提升10.6%和10.1%，并观察到资源向推理前沿转移的涌现课程。

## 摘要（原文）

> Recent progress in Large Language Model (LLM) reasoning is increasingly driven by the refinement of post-training loss functions and alignment strategies. However, standard Reinforcement Learning (RL) paradigms like Group Relative Policy Optimization (GRPO) remain constrained by static uniformity: uniform prompt sampling and a fixed number of rollouts per prompt. For heterogeneous, heavy-tailed reasoning data, this creates structural inefficiencies that waste compute on already-solved patterns while under-training the long tail of hard problems. To address this, we propose Multi-Adversary Group Distributionally Robust Optimization (GDRO), an optimization-first framework that moves beyond uniform reasoning models by dynamically adapting the training distribution.
>   We introduce an Online Difficulty Classifier that partitions prompts into dynamic pass@k difficulty groups. We then propose two independent GDRO games for post-training: (1) Prompt-GDRO, which employs an EMA-debiased multiplicative-weights bandit sampler to target the intensive difficulty margin and upweight persistently hard groups without frequency bias; and (2) Rollout-GDRO, which uses a shadow-price controller to reallocate rollouts across groups, maximizing gradient variance reduction on hard tasks under a fixed mean budget (compute-neutral). We provide no-regret guarantees for both controllers and additionally a variance-proxy analysis motivating a square-root optimal rollout allocation for Rollout-GDRO. We validate our framework on the DAPO 14.1k dataset using Qwen3-Base models. Prompt-GDRO and Rollout-GDRO achieve average relative gains of +10.6% and +10.1%, respectively, in pass@8 accuracy across 1.7B, 4B, and 8B scales compared to the GRPO baseline. Qualitative analysis shows an emergent curriculum: the adversaries shift resources to the evolving reasoning frontier, enhancing the reasoning model's performance.

